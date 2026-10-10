"""CareContinuity healthcare disruption risk estimator."""
from __future__ import annotations

import json
from pathlib import Path

import streamlit as st



ROOT = Path(__file__).resolve().parent
TIMELINE_PATH = ROOT / "data" / "ummc_public_timeline.json"

st.set_page_config(page_title="CareContinuity Lab", page_icon="🩺", layout="wide")
st.markdown(
    """
    <style>
    .block-container {max-width: 1120px; padding-top: 2rem; padding-bottom: 3rem;}
    .hero {padding: 1.5rem 1.7rem; border-radius: 18px; background: linear-gradient(120deg,#102b46,#176b72); color: white; margin-bottom: 1.25rem;}
    .hero h1 {color: white; margin-bottom: .25rem;}
    .hero p {color: #e4f3f3; font-size: 1.05rem; margin-bottom: 0;}
    .muted {color: #607080;}
    [data-testid="stMetric"] {background: #f3f7fa; border: 1px solid #dce6ee; padding: 1rem; border-radius: 14px;}
    </style>
    """,
    unsafe_allow_html=True,
)

timeline = json.loads(TIMELINE_PATH.read_text(encoding="utf-8"))

st.markdown(
    """
    <div class="hero">
      <h1>CareContinuity Lab</h1>
      <p>Explore a real healthcare cyber incident, then practise planning for a systems outage.</p>
    </div>
    """,
    unsafe_allow_html=True,
)
st.caption("A scenario-based healthcare cyber disruption risk estimator informed by the public UMMC incident timeline.")

tab_case, tab_lab, tab_about = st.tabs(["Case timeline", "Risk estimator", "About the project"])

with tab_case:
    st.subheader(timeline["case_title"])
    st.info(timeline["scope_note"])
    for event in timeline["events"]:
        with st.container(border=True):
            date_col, detail_col = st.columns([1, 5])
            with date_col:
                st.markdown(f"**{event['date']}**")
                st.caption(event["evidence_type"].title())
            with detail_col:
                st.markdown(f"#### {event['label']}")
                st.write(event["detail"])
                st.link_button("Open source statement", event["source_url"])
    with st.expander("What the public sources still do not establish"):
        for item in timeline["unresolved_public_facts"]:
            st.write(f"• {item}")

with tab_lab:
    st.subheader("Estimate healthcare service-disruption risk")
    st.write("Choose the conditions that describe a scenario. The transparent score updates with each selection.")
    st.info("This scenario index uses explicit rules and weights. It is not a statistically calibrated probability of an attack or patient harm. Do not enter patient or confidential information.")
    st.markdown("#### Security and recovery indicators")
    i1, i2 = st.columns(2)
    with i1:
        network = st.toggle("Unusual network activity observed", value=True)
        privilege = st.toggle("Privileged-account anomaly observed", value=False)
        exposed = st.toggle("Critical service has an exposed weakness", value=True)
    with i2:
        edr_down = st.toggle("Endpoint detection coverage unavailable", value=False)
        backups_missing = st.toggle("Isolated backups unavailable", value=False)
        redundancy_missing = st.toggle("No tested alternative for critical services", value=True)
    isolation_ready = st.toggle("Documented isolation and response process is ready", value=True)
    points = {"Unusual network activity": 3 if network else 0, "Privileged-account anomaly": 3 if privilege else 0, "Exposed critical service": 2 if exposed else 0, "Detection coverage gap": 2 if edr_down else 0, "Isolated backup gap": 3 if backups_missing else 0, "Service redundancy gap": 2 if redundancy_missing else 0}
    raw = sum(points.values())
    adjustment = 2 if isolation_ready else 0
    score = max(0, raw - adjustment)
    band = "High" if score >= 9 else "Moderate" if score >= 4 else "Low"
    drivers = [name for name, value in points.items() if value]
    m1, m2, m3 = st.columns(3)
    m1.metric("Scenario risk index", f"{score} / 15")
    m2.metric("Risk band", band)
    m3.metric("Active risk factors", str(len(drivers)))
    st.caption(f"Rule-based estimate. Raw indicator points: {raw}; response readiness adjustment: {adjustment}.")
    st.markdown("#### Main contributors")
    st.write(" · ".join(drivers) if drivers else "No elevated indicators selected.")
    st.markdown("#### Suggested priorities")
    actions = []
    if network or privilege: actions.append("Preserve relevant logs, validate alerts, and review affected identities.")
    if exposed or edr_down: actions.append("Review exposed services and restore endpoint visibility where safe.")
    if backups_missing: actions.append("Verify isolated, recoverable backups and restoration ownership.")
    if redundancy_missing: actions.append("Confirm approved downtime workflows and alternate communications.")
    if isolation_ready: actions.append("Keep response roles and isolation steps current and tested.")
    for action in actions: st.markdown(f"- {action}")
    result = {"tool":"CareContinuity Lab", "scenario_risk_index":score, "risk_band":band, "raw_indicator_points":raw, "response_readiness_adjustment":adjustment, "contributors":drivers, "selected_indicators":{"unusual_network_activity":network,"privileged_account_anomaly":privilege,"exposed_critical_service":exposed,"endpoint_detection_unavailable":edr_down,"isolated_backups_unavailable":backups_missing,"no_tested_service_redundancy":redundancy_missing,"isolation_process_ready":isolation_ready}, "response_priorities":actions, "model_note":"Transparent rule-based scenario index, not an empirically calibrated probability."}
    st.download_button("Download assessment as JSON", data=json.dumps(result, indent=2), file_name="carecontinuity-risk-assessment.json", mime="application/json")

with tab_about:
    st.subheader("About CareContinuity Lab")
    st.write("CareContinuity Lab connects the publicly documented UMMC ransomware incident to intrusion detection, malware analysis, incident response, digital forensics, and healthcare continuity. The estimator makes its scenario inputs and scoring rules visible.")
    st.markdown("**What it does**")
    st.markdown("- Shows a sourced timeline and unresolved incident facts.\n- Lets users select security indicators and continuity controls.\n- Displays an explainable risk index, leading factors, and response priorities.\n- Downloads an assessment as JSON.")
    st.markdown("**Scope**")
    st.write("The app is not connected to UMMC or a hospital and does not provide medical advice, detect attacks, investigate malware, or make patient-care decisions. Its score is a scenario index, not a measured probability.")
