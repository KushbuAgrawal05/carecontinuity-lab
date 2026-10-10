"""Explainable healthcare cyber disruption scenario risk model.

This is a transparent, expert-weighted index. It is not trained on patient data
or calibrated as an incident probability.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class RiskInputs:
    suspicious_login_rate_pct: float
    high_severity_alerts_24h: int
    exposed_critical_vulnerabilities: int
    oldest_critical_patch_age_days: int
    endpoint_detection_coverage_pct: float
    backup_state: str
    downtime_readiness: int
    service_redundancy: int
    clinical_service_criticality: int
    critical_vendor_dependency_pct: float


BACKUP_GAP = {"Verified isolated and tested": 0.0, "Isolated but not recently tested": 7.5, "No isolated verified copy": 15.0}


def _bounded(value: float, maximum: float) -> float:
    return max(0.0, min(float(value), maximum))


def predict_risk(inputs: RiskInputs) -> dict:
    """Return a 0-100 scenario risk index, domain breakdown and response actions."""
    login = _bounded(inputs.suspicious_login_rate_pct, 20) / 20 * 12
    alerts = _bounded(inputs.high_severity_alerts_24h, 20) / 20 * 13
    vulns = _bounded(inputs.exposed_critical_vulnerabilities, 10) / 10 * 12
    patch = _bounded(inputs.oldest_critical_patch_age_days, 90) / 90 * 8
    vendor = _bounded(inputs.critical_vendor_dependency_pct, 100) / 100 * 5
    edr_gap = (100 - _bounded(inputs.endpoint_detection_coverage_pct, 100)) / 100 * 10
    backup_gap = BACKUP_GAP.get(inputs.backup_state, 15.0)
    downtime_gap = (5 - _bounded(inputs.downtime_readiness, 5)) / 5 * 8
    redundancy_gap = (5 - _bounded(inputs.service_redundancy, 5)) / 5 * 7
    clinical_criticality = _bounded(inputs.clinical_service_criticality, 5) / 5 * 10

    components = {
        "Suspicious sign-in rate": round(login, 1),
        "High-severity alerts": round(alerts, 1),
        "Exposed critical vulnerabilities": round(vulns, 1),
        "Critical patch age": round(patch, 1),
        "Critical vendor dependency": round(vendor, 1),
        "Endpoint detection gap": round(edr_gap, 1),
        "Backup recovery gap": round(backup_gap, 1),
        "Downtime readiness gap": round(downtime_gap, 1),
        "Service redundancy gap": round(redundancy_gap, 1),
        "Clinical service criticality": round(clinical_criticality, 1),
    }
    domains = {
        "Threat signals": round(login + alerts, 1),
        "Exposure": round(vulns + patch + vendor, 1),
        "Recovery resilience": round(edr_gap + backup_gap, 1),
        "Care continuity impact": round(downtime_gap + redundancy_gap + clinical_criticality, 1),
    }
    score = round(min(100.0, max(0.0, sum(domains.values()))), 1)
    band = "Critical" if score >= 75 else "High" if score >= 50 else "Moderate" if score >= 25 else "Low"

    recommendations = []
    if login >= 5 or alerts >= 5:
        recommendations.append("Validate high-confidence alerts, review affected accounts, and preserve relevant logs.")
    if vulns >= 6 or patch >= 5:
        recommendations.append("Prioritize exposed critical systems for mitigation or patching under change control.")
    if edr_gap >= 4:
        recommendations.append("Restore endpoint monitoring coverage and check that critical assets report to monitoring.")
    if backup_gap >= 5:
        recommendations.append("Verify offline or immutable backups and confirm restoration with a documented test.")
    if downtime_gap >= 4 or redundancy_gap >= 3:
        recommendations.append("Review approved clinical downtime procedures, alternate communications, and recovery ownership.")
    if vendor >= 2:
        recommendations.append("Review critical supplier dependencies, outage contacts, and tested fallback arrangements.")
    if clinical_criticality >= 8:
        recommendations.append("Escalate continuity review for the affected high-criticality care service with clinical operations.")
    if not recommendations:
        recommendations.append("Maintain monitoring and repeat the assessment when indicators or service conditions change.")

    return {
        "model": "CareContinuity weighted scenario risk index v2.0",
        "score": score,
        "risk_band": band,
        "domain_scores": domains,
        "factor_contributions": components,
        "leading_factors": sorted(components.items(), key=lambda item: item[1], reverse=True)[:5],
        "recommendations": recommendations,
        "inputs": asdict(inputs),
        "interpretation": "A transparent scenario index for comparing conditions. Not a calibrated probability, clinical risk score, or substitute for incident response judgment.",
    }
