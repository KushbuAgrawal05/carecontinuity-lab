"""Transparent healthcare service downtime impact model for tabletop training."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

SERVICES = {
    "ehr": {"title": "Electronic health record", "weight": 5},
    "communications": {"title": "Staff and patient communications", "weight": 4},
    "scheduling": {"title": "Scheduling and registration", "weight": 3},
    "laboratory": {"title": "Laboratory information", "weight": 4},
    "identity": {"title": "Identity and access services", "weight": 3},
}

WORKFLOWS = [
    {
        "name": "Clinical documentation and orders",
        "depends_on": ["ehr", "identity"],
        "impact": 5,
        "actions": [
            "Activate the approved paper chart and order workflow.",
            "Use approved patient identity checks and downtime identifiers.",
            "Assign a unique downtime record number and reconcile entries after restoration."
        ]
    },
    {
        "name": "Laboratory requests and result delivery",
        "depends_on": ["ehr", "laboratory", "communications"],
        "impact": 5,
        "actions": [
            "Use approved paper requisitions and documented read-back for critical results.",
            "Record who received a result, when it was received, and how it was acknowledged."
        ]
    },
    {
        "name": "Appointment access and rescheduling",
        "depends_on": ["scheduling", "communications", "ehr"],
        "impact": 4,
        "actions": [
            "Use a controlled, access-restricted downtime queue with a clear owner.",
            "Use approved alternate communication channels and reconcile every queued request."
        ]
    },
    {
        "name": "Medication workflow coordination",
        "depends_on": ["ehr", "identity", "communications"],
        "impact": 5,
        "actions": [
            "Follow the facility's approved medication downtime procedure and independent checks.",
            "Keep downtime records secure and reconcile them to the authoritative record after recovery."
        ]
    },
    {
        "name": "Incident command and status coordination",
        "depends_on": ["communications", "identity"],
        "impact": 3,
        "actions": [
            "Use a pre-approved alternate incident command channel and paper decision log.",
            "Confirm staff identity and record decision owner, timestamp, and next review point."
        ]
    }
]

VALID_STATES = {"available", "degraded", "down"}
STATE_FACTOR = {"available": 0.0, "degraded": 0.5, "down": 1.0}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_scenario(path: Path) -> dict:
    scenario = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(scenario, dict) or not isinstance(scenario.get("services"), dict):
        raise ValueError("scenario must be a JSON object with a services object")
    validate_services(scenario["services"])
    return scenario


def validate_services(values: dict) -> None:
    unknown = set(values) - set(SERVICES)
    missing = set(SERVICES) - set(values)
    if unknown or missing:
        raise ValueError(f"service keys mismatch; missing={sorted(missing)}, unknown={sorted(unknown)}")
    invalid = {name: state for name, state in values.items() if state not in VALID_STATES}
    if invalid:
        raise ValueError(f"invalid service states: {invalid}")


def assess(scenario: dict, scenario_digest: str | None = None) -> dict:
    states = scenario["services"]
    validate_services(states)
    items = []
    for workflow in WORKFLOWS:
        affected = [name for name in workflow["depends_on"] if states[name] != "available"]
        if not affected:
            status = "available"
            score = 0
        else:
            severity = max(STATE_FACTOR[states[name]] for name in affected)
            score = round(workflow["impact"] * severity)
            status = "at risk" if score >= 4 else "degraded"
        items.append({
            "workflow": workflow["name"],
            "status": status,
            "impact_score": score,
            "affected_services": [SERVICES[name]["title"] for name in affected],
            "continuity_actions": workflow["actions"]
        })
    total = sum(item["impact_score"] for item in items)
    max_score = sum(workflow["impact"] for workflow in WORKFLOWS)
    return {
        "tool": "CareContinuity Lab",
        "version": "1.0.0",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "scenario_name": scenario.get("scenario_name", "Untitled tabletop"),
        "scenario_type": scenario.get("scenario_type", "user-supplied tabletop scenario"),
        "scenario_sha256": scenario_digest,
        "services": [{"service": SERVICES[name]["title"], "state": states[name]} for name in SERVICES],
        "workflows": items,
        "aggregate_exercise_score": total,
        "aggregate_maximum": max_score,
        "interpretation": "Operational tabletop signal only. This score is not a clinical risk score and must not be used to prioritize individual patients or determine treatment.",
        "exercise_note": scenario.get("exercise_note", "Training output only; validate local procedures with clinical and emergency-management leadership.")
    }


def assess_file(path: Path) -> dict:
    return assess(load_scenario(path), sha256_file(path))
