# CareContinuity Lab

**Healthcare cyber disruption risk estimator and incident evidence viewer**

CareContinuity Lab is a healthcare cyber disruption risk estimator informed by the February 2026 ransomware incident at the University of Mississippi Medical Center (UMMC). It presents sourced incident facts and estimates scenario risk from selected security indicators and continuity controls. It includes a local dashboard and a Streamlit deployment.

`data/ummc_public_timeline.json` contains statements documented by UMMC or AP. Risk-estimator inputs are scenario assumptions, not UMMC telemetry, an attacker reconstruction, or clinical decision support.

## What the project does

- Displays a sourced public timeline of the UMMC event and labels unresolved facts.
- Accepts selectable indicators for unusual network activity, privileged-account anomalies, critical service exposure, endpoint detection coverage, isolated backups, and service redundancy.
- Maps selected conditions to a transparent risk index, risk band, leading factors, and response priorities.
- Downloads a JSON copy of the risk assessment. The command-line assessment also records a SHA-256 digest of its input file.
- Keeps all incident facts in local JSON files. The local dashboard uses Python's standard library; the Streamlit version adds the dependency listed in `requirements.txt`.

It does not diagnose patients, rank individual patients, recommend treatment, attribute an attack, execute malware, or connect to hospital systems.

## Run it

Requirements: Python 3.10 or later.

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Streamlit opens the dashboard in your browser. The original standard-library dashboard is also available with:

```bash
python3 -m carecontinuity --open
```

That version opens at `http://127.0.0.1:8765` and can be stopped with `Ctrl+C`.

## Deploy with GitHub and Streamlit Community Cloud

1. Create a GitHub repository named `carecontinuity-lab` and upload the unzipped contents of this folder to its `main` branch. Keep `streamlit_app.py`, `requirements.txt`, `carecontinuity/`, and `data/` at the repository's top level.
2. Open [share.streamlit.io](https://share.streamlit.io) and sign in with the GitHub account that owns the repository.
3. Choose **Create app**, then **Yup, I have an app**.
4. Select the repository, the `main` branch, and `streamlit_app.py` as the app file.
5. Choose an app address if you like, then deploy. Streamlit installs the packages listed in `requirements.txt` and gives you a shareable `streamlit.app` link.
6. To publish later changes, commit them to the selected GitHub branch. Streamlit Community Cloud updates the app from that repository.

The Streamlit deployment is publicly reachable, so use only the included scenario configuration. Do not enter patient or other confidential information. For the official deployment instructions, see the [Streamlit Community Cloud guide](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy).

## Use the command line

```bash
python3 -m carecontinuity assess data/risk_scenario.json --output reports/demo-assessment.json
```

The command prints a concise summary and writes the assessment as JSON. Output folders are created when needed. The hash records which scenario file was assessed; it does not prove the source, time, or integrity of external evidence.

## Project structure

```text
streamlit_app.py     Streamlit dashboard entry point
requirements.txt     Streamlit dependency for deployment
carecontinuity/       Assessment logic and local web server
data/                 sourced incident timeline and tabletop scenario
docs/                 editable report source and 7 to 8 minute video script
reports/              example output
web/                  original local dashboard interface
```

## Evidence and ethical boundaries

Each timeline fact has a source, a date, and an evidence label. Unknowns remain unknown. UMMC's April 2026 account says it was still conducting forensic analysis into what data was accessed or exfiltrated. The project does not fill that gap with speculation. The estimator is rule-based and uses transparent, configurable weights. It is not calibrated against incident frequency data and its score is not an attack probability.

## Report and video

- `docs/REPORT_CONTENT.md` is the editable report source.
- `docs/VIDEO_SCRIPT.md` is a timed script designed for a 7 to 8 minute presentation.
- The formatted Word report and submission PDF are `Report_CareContinuity_UMMC.docx` and `Report_CareContinuity_UMMC.pdf` in this project root.

## References

The report includes 30 references, including primary incident statements from UMMC, healthcare cyber resilience guidance, NIST and CISA materials, and the supplied Unit 4 course presentations. See `docs/REPORT_CONTENT.md` for the complete list.
