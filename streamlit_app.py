"""CareContinuity healthcare disruption risk estimator."""
from __future__ import annotations

import json
from pathlib import Path

import streamlit as st
import pandas as pd

from carecontinuity.risk_model import RiskInputs, predict_risk



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
    st.subheader("Healthcare Cyber Disruption Risk Predictor")
    st.write("Enter current security and continuity indicators to estimate how exposed a healthcare service may be to a disruptive cyber incident.")
    st.info("The 0-100 index uses transparent expert-assigned weights. It supports scenario comparison, not a calibrated probability of attack or patient harm. Do not enter patient or confidential information.")

    st.markdown("#### 1. Threat signals")
    c1, c2 = st.columns(2)
    with c1:
        login_rate = st.slider("Suspicious sign-ins (% of sign-ins)", 0, 20, 6, help="Use an aggregate percentage from security monitoring, not account or patient identifiers.")
    with c2:
        alert_count = st.slider("High-severity security alerts in the last 24 hours", 0, 20, 3)

    st.markdown("#### 2. Exposure and supplier dependency")
    c1, c2, c3 = st.columns(3)
    with c1:
        vuln_count = st.slider("Exposed critical vulnerabilities", 0, 10, 1)
    with c2:
        patch_age = st.slider("Age of oldest exposed critical patch (days)", 0, 90, 14)
    with c3:
        vendor_share = st.slider("Critical service dependence on one supplier (%)", 0, 100, 40)

    st.markdown("#### 3. Detection and recovery readiness")
    c1, c2 = st.columns(2)
    with c1:
        edr_coverage = st.slider("Endpoint detection coverage (%)", 0, 100, 90)
        backup_state = st.selectbox("Backup recovery state", ["Verified isolated and tested", "Isolated but not recently tested", "No isolated verified copy"])
    with c2:
        downtime_readiness = st.slider("Clinical downtime readiness", 0, 5, 3, help="0 means no documented or practiced process. 5 means documented and recently exercised.")
        redundancy = st.slider("Tested service redundancy", 0, 5, 3, help="0 means no usable alternative. 5 means a tested alternative is available.")
    clinical_criticality = st.slider("Criticality of affected clinical service", 1, 5, 5, help="1 means limited care impact; 5 means the service supports time-critical care.")

    inputs = RiskInputs(login_rate, alert_count, vuln_count, patch_age, edr_coverage, backup_state, downtime_readiness, redundancy, clinical_criticality, vendor_share)
    result = predict_risk(inputs)

    st.divider()
    st.markdown("#### Predictor output")
    m1, m2, m3 = st.columns(3)
    m1.metric("Disruption risk index", f"{result['score']} / 100")
    m2.metric("Risk band", result["risk_band"])
    m3.metric("Assessment", "Updated from current inputs")
    st.caption(result["interpretation"])

    left, right = st.columns([1, 1])
    with left:
        st.markdown("##### Risk by domain")
        chart = pd.DataFrame({"Domain": list(result["domain_scores"].keys()), "Risk points": list(result["domain_scores"].values())})
        st.bar_chart(chart, x="Risk points", y="Domain", horizontal=True)
        st.caption("Maximum domain scores: threat 25, exposure 25, recovery 25, care continuity 25.")
    with right:
        st.markdown("##### Main risk contributors")
        for factor, points in result["leading_factors"]:
            st.write(f"**{factor}** · {points} points")
        st.markdown("##### Recommended priorities")
        for action in result["recommendations"]:
            st.markdown(f"- {action}")

    st.download_button("Download full assessment (JSON)", data=json.dumps(result, indent=2), file_name="carecontinuity-risk-assessment.json", mime="application/json")

with tab_about:
    st.subheader("About CareContinuity Lab")
    st.write("CareContinuity Lab connects the publicly documented UMMC ransomware incident to intrusion detection, malware analysis, incident response, digital forensics, and healthcare continuity. Its estimator makes scenario inputs, score contributions, and response priorities visible.")
    st.markdown("**Assessment flow**")
    st.markdown("1. Enter aggregate threat and exposure indicators.\n2. Rate detection, backup, downtime, and redundancy readiness.\n3. Review the total score, risk band, domain chart, leading factors, and suggested priorities.\n4. Download the assessment to JSON.")
    st.markdown("**Scope**")
    st.write("The app is not connected to UMMC or a hospital and does not provide medical advice, detect attacks, investigate malware, or make patient-care decisions. The score is a scenario index, not a measured probability.")
