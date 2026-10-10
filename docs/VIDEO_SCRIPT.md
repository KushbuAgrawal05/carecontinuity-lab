# CareContinuity Lab Full Report and App Walkthrough

**Target duration:** approximately 7 to 8 minutes at a clear pace, including the app demonstration  
**Course:** Cyber Security, Unit 4, CA-2 Part 2  
**Presenter:** Kushbu Agrawa, PRN 23070122267  
**Group:** [Insert project group number]  
**Topic:** When the EHR Goes Dark: the UMMC ransomware case and CareContinuity Lab

## 0:00 to 0:35 | Title, abstract, and keywords

“Good morning. I’m Kushbu Agrawa, PRN 23070122267, from B.Tech project group [number]. My report is titled *When the EHR Goes Dark*. It studies the February 2026 ransomware incident at the University of Mississippi Medical Center, or UMMC, and presents CareContinuity Lab, a healthcare disruption risk estimator.

The abstract summarizes the case, its operational effects, the evidence limits, and the project. The keywords are healthcare cybersecurity, ransomware, electronic health records, downtime procedures, incident response, digital forensics, and business continuity.”

## 0:35 to 1:20 | Introduction and objectives

“The introduction explains that hospitals rely on electronic records, laboratory and appointment systems, staff accounts, and communication tools. If these fail, care teams still need ways to identify patients, document care, communicate, and reconcile records after systems return.

The six objectives are to build an event-dated timeline; separate facts, reporting, guidance, and analysis; connect the incident to Unit 4; explain care continuity; build the estimator; and document GitHub, Streamlit, and actual output. The central question is how a healthcare service can compare cyber exposure with its readiness to continue care.”

## 1:20 to 2:05 | Literature review

“The literature review covers ransomware preparation, containment, backups, recovery, downtime workflows, alternate communication, and digital forensics. It draws on NIST, CISA, HHS, ASPR TRACIE, ONC, healthcare research, and the Unit 4 materials on intrusion detection and malware analysis. The gap is that general guidance can feel abstract, so this project pairs a real case with a transparent estimator. Public sources do not establish UMMC’s access route or malware family, and the report leaves those unknown.”

## 2:05 to 3:30 | Methodology and scoring method

“The methodology is a qualitative public-source case study. UMMC updates are the main evidence, supported by contemporary news, healthcare guidance, research, and Unit 4 materials. No patient data, leaked material, interviews, or internal records were used. Evidence is labelled as a public fact, corroborating report, guidance, analysis, or unknown. The timeline separates event dates from publication dates. Unit 4 mapping is only made where supported; unknown technical details are not inferred.

For the estimator, ten aggregate indicators were grouped into four domains and assigned ranges and maximum points. Risk-increasing values scale to their maximum; protective controls are scored by their gaps. Readiness and redundancy use a zero-to-five scale; backup states contribute zero, 7.5, or 15 points. Inputs are bounded before calculation. The four domains each have a 25-point maximum. Fixed bands and rule-based thresholds produce labels and recommendations. The code was compiled and the default example manually checked. That verifies calculation consistency, not predictive accuracy. There is no labelled incident dataset, calibration, or independent validation.”

## 3:30 to 4:20 | Implementation and app demonstration

“The implementation uses a sourced UMMC timeline, a Streamlit interface, and a separate risk calculation module. The app has three tabs: Case timeline, Risk estimator, and About the project.

[Show Case timeline.] The dates run from February 19, when UMMC later said unusual activity was detected and affected systems were shut down, to its February 20 ransomware announcement. The February 27 update described paper care and clinic restart planning; the April update looked back to recovery by February 28. March and April updates said forensic work continued. Each card has an evidence label and source link, and the expanded section lists unresolved facts, including the access route and data exposure scope.

[Show Risk estimator.] The ten inputs cover suspicious sign-ins, high-severity alerts, critical vulnerabilities, patch age, supplier dependence, endpoint coverage, backup state, downtime readiness, service redundancy, and clinical-service criticality. I’ll change one value at a time. The result updates with an overall score and band, a chart for all four domains, leading contributors, and suggested priorities. The JSON button downloads the submitted inputs and calculated output.”

## 4:20 to 5:15 | Results and discussion

“With the displayed default scenario, the index is 26.9 out of 100, Moderate. The domain results are 5.5 for threat signals, 4.4 for exposure, 1.0 for recovery resilience, and 16.0 for care continuity impact. Clinical-service criticality is the largest individual contributor. This is a demonstration scenario, not UMMC’s measured score.

Reported effects include unavailable EHR and phones, clinic and elective procedure cancellations, continued hospital and emergency care, and paper documentation. The report does not claim measured patient harm. Its recommendations are to practice downtime, prepare alternate communications, protect logs, define containment and recovery roles, keep an offline decision log, and preserve evidence. These are planning suggestions, not claims that UMMC lacked controls.

The comparison with Change Healthcare shows two disruption paths: local clinical systems versus a shared billing and transaction service. Future work includes department-specific scenarios, timed exercises, an after-action worksheet, and expert review.”

## 5:15 to 6:00 | Output, conclusion, and references

“The Output section records the GitHub repository, branch, and app file, with spaces for the live URL, deployment date, commit ID, and screenshots of actual output. I will fill these in after confirming deployment.

The conclusion is that hospitals need both technical response and plans to continue care during outages. The 33 references include UMMC, AP and Mississippi Today, NIST, CISA, HHS, CMS, ASPR TRACIE, ONC, healthcare research, MITRE ATT&CK, and the Unit 4 materials.”

## 6:00 to 7:00 | About tab, scope, and closing

“[Show About the project.] This tab explains the assessment flow and limits. The app does not connect to a hospital, use patient data, detect attacks, analyze malware, or make care decisions. The score is not a probability. Its weights need suitable data, expert review, calibration, and independent validation before operational use.

My work brings together case evidence, Unit 4 concepts, and an interactive way to compare security and continuity. Hospitals need plans to organize care while digital systems are unavailable, alongside plans to contain and recover from cyber incidents. Thank you.”

## Recording checklist

- Replace the group-number placeholder.
- Show each of the app’s three tabs and demonstrate at least one input change.
- Say that 26.9 is the default scenario result, not UMMC’s actual risk score.
- Add the live URL, commit ID, and screenshots to the Output section only after deployment.
- Keep the reference list visible briefly at the end; do not read all 33 citations aloud.
