"""Streamlit version of the CareContinuity Lab classroom tabletop."""
from __future__ import annotations

import json
from pathlib import Path

import streamlit as st

from carecontinuity.engine import SERVICES, assess


ROOT = Path(__file__).resolve().parent
TIMELINE_PATH = ROOT / "data" / "ummc_public_timeline.json"
SCENARIO_PATH = ROOT / "data" / "training_scenario.json"
STATE_LABELS = {"available": "Available", "degraded": "Degraded", "down": "Down"}

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
scenario = json.loads(SCENARIO_PATH.read_text(encoding="utf-8"))

st.markdown(
    """
    <div class="hero">
      <h1>CareContinuity Lab</h1>
      <p>Explore a real healthcare cyber incident, then practise planning for a systems outage.</p>
    </div>
    """,
    unsafe_allow_html=True,
)
st.caption("A classroom learning project based on public information about the 2026 UMMC ransomware incident.")

tab_case, tab_lab, tab_about = st.tabs(["Case timeline", "Tabletop lab", "About the project"])

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
    st.subheader("Try a downtime scenario")
    st.write("Change the service states and see which sample workflows may need continuity planning.")
    st.warning(
        "Training exercise only. The sample scenario is synthetic and is not UMMC system data. "
        "The score is not a clinical risk measure. Do not enter patient or confidential information.",
        icon="⚠️",
    )
    states: dict[str, str] = {}
    default_states = scenario["services"]
    service_keys = list(SERVICES)
    cols = st.columns(2)
    for i, key in enumerate(service_keys):
        with cols[i % 2]:
            states[key] = st.selectbox(
                SERVICES[key]["title"],
                options=list(STATE_LABELS),
                format_func=lambda value: STATE_LABELS[value],
                index=list(STATE_LABELS).index(default_states[key]),
                key=f"service_{key}",
            )

    result = assess({
        "scenario_name": "Streamlit classroom tabletop",
        "scenario_type": "synthetic training exercise",
        "services": states,
        "exercise_note": "Synthetic training output only. It does not describe UMMC systems or patient care.",
    })

    st.divider()
    score_col, summary_col = st.columns([1, 2])
    with score_col:
        st.metric("Exercise impact", f"{result['aggregate_exercise_score']} / {result['aggregate_maximum']}")
    with summary_col:
        flagged = sum(item["status"] != "available" for item in result["workflows"])
        st.markdown(f"**{flagged} of {len(result['workflows'])} workflows** have at least one disrupted dependency.")
        st.caption(result["interpretation"])

    st.markdown("### Workflow details")
    for item in result["workflows"]:
        with st.container(border=True):
            title_col, status_col = st.columns([4, 1])
            title_col.markdown(f"**{item['workflow']}**")
            status_col.markdown(f"**{item['status'].title()}** · {item['impact_score']}/5")
            st.caption("Affected services: " + (", ".join(item["affected_services"]) or "None"))
            if item["continuity_actions"]:
                for action in item["continuity_actions"]:
                    st.markdown(f"- {action}")

    st.download_button(
        "Download this exercise as JSON",
        data=json.dumps(result, indent=2),
        file_name="carecontinuity-tabletop.json",
        mime="application/json",
        use_container_width=False,
    )

with tab_about:
    st.subheader("Why this project was built")
    st.write(
        "CareContinuity Lab connects a publicly documented healthcare ransomware incident "
        "to Unit 4 topics in intrusion detection, malware analysis, incident response, and digital forensics. "
        "The tabletop helps students discuss how outages can affect everyday hospital workflows."
    )
    st.markdown("**What it does**")
    st.markdown(
        "- Shows a timeline with links to public statements.\n"
        "- Lets learners change the availability of five example services.\n"
        "- Shows affected workflows and general continuity prompts.\n"
        "- Downloads a JSON copy of the synthetic exercise."
    )
    st.markdown("**What it does not do**")
    st.markdown(
        "It is not connected to UMMC or any hospital. It does not provide medical advice, "
        "detect attacks, investigate malware, or make patient-care decisions."
    )
