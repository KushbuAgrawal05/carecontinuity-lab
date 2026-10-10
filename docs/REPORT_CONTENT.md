# When the EHR Goes Dark
A Case Study of the 2026 University of Mississippi Medical Center Ransomware Incident and a Healthcare Disruption Risk Estimator

**Course:** Cyber Security, Unit 4, Continuous Assessment 2, Part 2  
**Institution:** Symbiosis Institute of Technology, Pune  
**B.Tech Project Group No.:** [Insert the B.Tech project group number]  
**Student:** Kushbu Agrawa, PRN 23070122267  
**Submission date:** 10 October 2026

## Abstract

On February 19, 2026, the University of Mississippi Medical Center (UMMC) detected unusual activity that led to a ransomware incident and disruption of systems used to support care. UMMC later said its electronic health record and phone services were unavailable, clinics and some procedures were cancelled, and hospital teams used paper records while care continued. Most systems used in regular operations were back online by February 28, but the forensic review was still under way in April. This report examines what public sources establish, what remains unknown, and how healthcare cybersecurity guidance applies. It introduces CareContinuity Lab, a Streamlit application that estimates healthcare service-disruption risk from selected cybersecurity indicators and continuity controls. The transparent rule-based score supports scenario assessment; it is not a measured probability or clinical decision. The case connects Unit 4 topics such as intrusion detection, ransomware analysis, incident response, and digital forensics to the practical problem of keeping care going during an outage.

**Keywords:** healthcare cybersecurity, ransomware, electronic health record, downtime procedures, incident response, digital forensics, business continuity

## 1. Introduction

### 1.1 Cybersecurity in healthcare

Hospitals depend on electronic health records (EHRs), laboratory systems, appointment services, staff accounts, and communication tools to coordinate care. A cyber incident can therefore affect clinical work as well as information security. The February 2026 UMMC incident is a useful real case because the public record shows how a technology outage led staff to use downtime procedures while technical teams investigated and restored services [1-5,31].

### 1.2 Ransomware and healthcare service outages

Ransomware can make systems unavailable and may involve attempts to steal information. In healthcare, an outage can interrupt access to patient records, appointment schedules, phone systems, billing, and laboratory results. The scale and effects depend on which services are affected and how well the organization can switch to approved alternatives [12-18].

### 1.3 Why clinical downtime planning matters

When digital systems are unavailable, care teams need safe ways to identify patients, document care, place orders, communicate results, and reconnect records after restoration. Paper procedures can help, but staff need to know where forms are kept, who is responsible for them, and how information will be reconciled later [17-19].

### 1.4 The UMMC case and its relevance

The disruption began on February 19, 2026, when UMMC later said its systems detected unusual activity and users reported problems. UMMC publicly confirmed a ransomware attack in a statement dated February 20. At that point, its EHR and phone systems were unavailable. Clinics statewide and elective procedures were cancelled for Thursday and Friday, while hospitals and emergency departments remained open using downtime procedures [1,4,5,31]. The February 27 update described continued paper-based hospital care and a gradual restart of urgent clinic visits [2]. In April, UMMC said operations had largely returned to normal by February 28, while forensic analysis continued [4].

### 1.5 Objectives

This report has six objectives:

1. Set out a dated timeline and distinguish when events happened from when they were publicly described.
2. Separate confirmed public statements, independent reporting, guidance, and analysis.
3. Relate the case to Unit 4 topics in intrusion detection, malware analysis, incident response, and digital forensics.
4. Discuss how the outage affected care and continuity procedures.
5. Implement CareContinuity Lab, a rule-based healthcare disruption risk estimator inspired by the documented case.
6. Provide a section for the GitHub repository, Streamlit deployment, and screenshots of the user's final output.

CareContinuity Lab combines the sourced case timeline with an adjustable risk-estimation interface. It is separate from UMMC systems and uses no patient data.

## 2. Literature Review

### Malware and ransomware in healthcare

Ransomware can lock organizations out of their systems, and some incidents also involve attempts to steal data. CISA advises organizations to prepare in advance, isolate affected systems, restore carefully from protected backups, and record lessons after an incident [23]. HHS's healthcare cybersecurity goals also emphasize incident planning, preparedness, and supplier security [12]. A 2023 review of hospital cyber resilience points to risks such as ransomware and gaps in device protection, account security, network management, software updates, and incident response [14]. Together, these sources show why hospitals need to plan for keeping services available as well as protecting information.

In healthcare, a technology outage can become a patient-care problem. HHS describes cyber resilience as part of keeping essential services and patient safety in view [25]. Hospital downtime checklists from ASPR TRACIE recommend preparing paper workflows, backup ways to communicate, and practice for longer outages [17,18]. ONC's 2025 SAFER Guide also covers what to do when an EHR is unavailable [19]. UMMC's public updates give a real example to compare with this advice [1,2].

### Incident response and recovery

NIST's incident-response guide connects preparation, detection, response, and recovery with an organization's wider security planning [6]. Its contingency-planning guide covers restoring systems and using manual alternatives during an outage [8]. CISA also provides a ransomware response guide for healthcare organizations that can be adapted and kept available offline [16]. The shared message is that technical teams and care teams need to plan and respond together.

UMMC's updates say that affected systems were shut down, specialists and federal agencies helped with the response, staff used existing downtime procedures, and systems were brought back in stages [1-3]. In April, UMMC said its monitoring had detected the unusual activity and that the incident was not caused by one user clicking a malicious email [4]. The public updates do not say how the attackers first got in, so this report does not guess.

### Digital forensics and evidence limits

Digital forensics is the careful collection and examination of evidence so that other people can review how conclusions were reached [9]. Good log management helps by keeping useful records, consistent timestamps, and protected copies of logs [10]. Response guidance also recommends preserving relevant files and recording important decisions [6]. This report is based on public statements and news coverage, not on UMMC's computers or investigation files. It therefore cannot show system images, detailed logs, malware samples, or a complete evidence-handling record. The report labels public facts, outside reporting, and its own analysis separately.

In March, UMMC said that building a full forensic picture could take months or longer [3]. In April, it said investigators were still checking what information might have been accessed or taken [4]. This means the public material does not support firm conclusions about the cause or the amount of data involved. CareContinuity Lab keeps links and evidence labels with its timeline, but it does not reproduce UMMC's forensic investigation.

### Intrusion detection, malware analysis, and safe interpretation

Unit 4 covers intrusion detection, malware analysis, and digital forensics. An intrusion-detection system can flag activity that looks suspicious, but responders need to compare an alert with other evidence before deciding what happened [27]. Malware analysis studies malicious programs in a controlled setting. Knowing that an organization called an incident ransomware does not tell us which malware was used, how the attackers got in, or everything they did. MITRE ATT&CK describes data encryption as a behavior used in some ransomware incidents, but that general description is not proof that a specific technique was used at UMMC [26].

The supplied Unit 4 presentations give course background for IDS, malware analysis, and digital forensics [28-30]. CareContinuity Lab applies those ideas through its sourced timeline and risk estimator. It does not run malware, scan networks, or claim to detect attacks automatically. The public sources describe service disruption and recovery, but provide little technical detail about the investigation.

### Continuity planning and the project's contribution

The NIST Cybersecurity Framework groups security work under six functions: Govern, Identify, Protect, Detect, Respond, and Recover [7]. HHS's healthcare cybersecurity goals and HICP guide adapt related practices for hospitals and other care organizations [12,13]. NIST's security controls and ONC's SAFER Guides offer additional ways to plan for risk and EHR outages [11,19]. CareContinuity Lab turns these ideas into an adjustable risk estimate: users select observed security indicators and continuity controls, then see a transparent score, risk band, and recommended response priorities.

The project addresses the gap between high-level guidance and a practical, explainable scenario assessment. Its rule-based estimate surfaces how security signals and continuity controls combine. It is not calibrated against incident frequency data and must not be interpreted as a probability of attack or patient harm.

### Literature gap

Healthcare guidance discusses ransomware response and downtime planning, but the public UMMC material offers a current case through which analysts can examine how those ideas connect. This report contributes an evidence-graded timeline and an explainable disruption risk estimator. It does not claim access to internal records or add technical details that UMMC has not publicly shared.

## 3. Methodology

### 3.1 Research design

This is a qualitative case study using material available to the public. The main sources are UMMC statements from February, March, and April 2026 [1-4]. An Associated Press report adds independent coverage from the time, including information about clinic closures, cancelled services, EHR disruption, and FBI involvement [5]. Healthcare and cybersecurity guidance informs the discussion and recommendations [6-25]. I did not use UMMC internal records, patient information, interviews, or leaked material.

### 3.2 Data collection and source selection

The main sources are UMMC statements published on February 20 and 27, March 13, and April 10, 2026 [1-4]. The Associated Press and Mississippi Today provide reporting from February 19 and 20 that helps establish the early chronology and immediate disruption [5,31]. Government and healthcare guidance, standards, and the supplied Unit 4 presentations provide context for the discussion [6-30]. Sources were selected for authority, relevance, date, technical specificity, and whether important facts could be corroborated. No patient records, leaked material, or internal UMMC systems were used.

### 3.3 Data verification and evidence grading

Claims are classified as follows:

| Label | Meaning | Example in this report |
|---|---|---|
| Primary public fact | Direct statement published by UMMC | UMMC said the EHR and phone systems were unavailable [1]. |
| Corroborating report | Independent contemporaneous reporting | AP reported clinic closures and the impact on outpatient services [5]. |
| Guidance | Recommended practice, not a description of what UMMC did | ASPR TRACIE downtime planning checklists [17,18]. |
| Analysis | Interpretation or proposed control based on evidence | A manual reconciliation queue can reduce omissions during restoration. |
| Unknown | Not established in cited public material | The specific initial access vector and complete exfiltration scope. |

Attribution, infection path, malware family, and patient-level harm are not inferred. UMMC's April account explicitly says the incident was not caused by a single user clicking a malicious email; it does not disclose a replacement initial-access explanation [4].

### 3.4 Timeline reconstruction, framework mapping, risk analysis, and limitations

I arranged the events by the date they happened and included the publication date or source with each item where it differs. In particular, UMMC's April statement looks back to unusual activity and system shutdown on February 19; the ransomware confirmation was published the following day [1,4,5,31]. A return to regular operations is not treated as the end of the investigation: UMMC said services were largely back to normal by February 28, while its forensic review continued in March and April [3,4].

The public facts are mapped to incident-response stages and relevant Unit 4 ideas only where the evidence supports the connection. Since no malware sample, detailed logs, or initial access path is public, those items are marked unknown rather than inferred. The main limitations are the small number of public incident updates and the absence of internal UMMC evidence.

CareContinuity Lab has two parts. The first shows sourced facts and questions the public record has not answered. The second estimates disruption risk from user-selected security signals and continuity controls, then displays the score, factors, and response prompts. Inputs are scenario assumptions, not UMMC telemetry or internal records.

The predictor takes ten aggregate inputs: suspicious sign-in rate, high-severity alerts, exposed critical vulnerabilities, age of the oldest critical patch, endpoint monitoring coverage, backup verification state, downtime readiness, tested redundancy, clinical-service criticality, and critical supplier dependence. Each input is normalized to its stated range and scaled to a fixed maximum contribution. The four domains contribute up to 25 points each, for a total index from 0 to 100. Risk bands are Low (0-24), Moderate (25-49), High (50-74), and Critical (75-100). The model is deterministic and explainable; its weights are expert-assigned design choices, not statistically fitted coefficients. It is not a security review of UMMC or a clinical decision tool.

### 3.5 Predictor design and calculation procedure

The predictor was designed as a transparent weighted index so a user can trace each result back to an input. The design process was: (1) identify operational indicators that can represent threat activity, technical exposure, recovery readiness, and potential care disruption; (2) group them into four domains; (3) define a bounded range and maximum point contribution for each indicator; (4) normalize each value to that range; (5) sum the contributions into a 0-100 index; and (6) use fixed score bands and rule-based prompts to present the result. The indicators are aggregate scenario values. They do not require patient identifiers, clinical records, or UMMC system access.

For a risk-increasing indicator, the calculation is `contribution = min(max(value, 0), cap) / cap × maximum points`. For a protective control, the model scores the gap: `contribution = (100 - min(max(coverage, 0), 100)) / 100 × maximum points`. Downtime readiness and redundancy use a 0-5 scale, so their gaps are `(5 - bounded rating) / 5 × maximum points`. Backup verification uses three ordered states with fixed contributions: a verified, isolated, tested copy adds 0 points; an isolated copy not recently tested adds 7.5; and no isolated verified copy adds 15. The implementation clamps out-of-range numeric entries to the stated bounds before calculating contributions.

**Table 1. Predictor inputs, bounds, domains, and maximum contributions**

| Domain | Input | Accepted range or options | Maximum points |
|---|---|---:|---:|
| Threat signals | Suspicious sign-in rate | 0-20 percent | 12 |
| Threat signals | High-severity alerts in 24 hours | 0-20 alerts | 13 |
| Exposure | Exposed critical vulnerabilities | 0-10 findings | 12 |
| Exposure | Age of oldest critical patch | 0-90 days | 8 |
| Exposure | Critical supplier dependency | 0-100 percent | 5 |
| Recovery resilience | Endpoint detection coverage gap | 0-100 percent coverage, scored inversely | 10 |
| Recovery resilience | Backup verification state | Three defined states, 0, 7.5, or 15 points | 15 |
| Care continuity impact | Downtime readiness | 0-5, scored as a gap | 8 |
| Care continuity impact | Tested service redundancy | 0-5, scored as a gap | 7 |
| Care continuity impact | Clinical-service criticality | 0-5 | 10 |

The model sums the first two contributions as Threat signals, the next three as Exposure, the next two as Recovery resilience, and the final three as Care continuity impact. Each domain can contribute at most 25 points. The overall score is the sum of the domain scores, bounded to 0-100 and rounded to one decimal place. The bands are Low (0-24.9), Moderate (25-49.9), High (50-74.9), and Critical (75-100). The band is assigned using the displayed one-decimal score.

### 3.6 Recommendation rules and output generation

Recommendations are triggered by contribution thresholds rather than by a language model. The application checks the relevant contribution values and displays an action prompt when a condition is met: sign-in or alert contribution of at least 5; vulnerability contribution of at least 6 or patch-age contribution of at least 5; endpoint detection gap of at least 4; backup gap of at least 5; downtime gap of at least 4 or redundancy gap of at least 3; supplier dependency contribution of at least 2; or clinical criticality contribution of at least 8. If no threshold is met, the application suggests maintaining monitoring and repeating the assessment when conditions change. The interface then shows the total score and band, domain scores, leading factor contributions, recommended actions, and a downloadable JSON record containing the submitted inputs and calculated outputs.

### 3.7 Verification and methodological limitations

Verification for this version consisted of compiling the Python source and manually cross-checking the displayed default scenario against its weighted contributions. That check produced 26.9/100, Moderate, with domain values of 5.5 for Threat signals, 4.4 for Exposure, 1.0 for Recovery resilience, and 16.0 for Care continuity impact. This checks that the documented example agrees with the implementation; it does not establish predictive accuracy. The model has no labelled hospital incident dataset, statistical calibration, independent validation, clinical review, or operational evaluation. Its weights and thresholds are design choices intended to make scenario comparisons explainable. Before any operational use, the model would need suitable de-identified data, documented governance, expert review, calibration, and independent validation. Until then, its output is a comparative scenario index, not the probability of an incident or patient harm.

## 4. Implementation Details

### 4.1 Healthcare systems and workflow context

Hospitals depend on connected services to document care, order tests, coordinate medications, schedule appointments, and contact staff and patients. CareContinuity Lab accepts ten aggregate indicators across four domains: threat signals, exposure, recovery resilience, and care continuity impact. Numeric sliders capture sign-in rates, high-severity alert counts, vulnerability counts, patch age, endpoint coverage, readiness, redundancy, clinical criticality, and supplier dependence. A selector captures backup verification state. Each input contributes a bounded number of points to the 0-100 index. The interface presents the overall band, domain chart, leading factors, recommended priorities, and a downloadable JSON assessment. Inputs do not map UMMC's technical environment.

### 4.2 Incident evidence and attack surface

Public sources establish that UMMC's EHR and phone systems were unavailable and that affected systems were taken offline to contain the threat [1,4]. They do not identify the first access route, a malware family, or the detailed affected network components. The evidence available for this case is therefore operational and institutional, not a set of forensic artifacts. No specific phishing route, exploit, or attacker technique is assigned in this report.

### 4.3 Attack timeline

The table separates the date of the event from the date of the later statement. February 19 is the reported start of the disruption; February 20 is the date of UMMC's public ransomware update. The April update provides the clearest retrospective account of early detection and recovery timing [1,4,5,31].

**Table 2. Timeline of publicly documented events**

| Event date | Event or later update | What the source establishes | Source |
|---|---|---|---|
| 19 Feb 2026 | Early activity and system outage | UMMC later said monitoring detected irregular activity in the early hours, users reported issues, and affected systems were shut down. Contemporary reporting described statewide clinic closures and interrupted care. | UMMC retrospective [4]; Mississippi Today [31] |
| 20 Feb 2026 | UMMC ransomware statement | UMMC publicly identified the incident as ransomware. EHR and phone services were unavailable; inpatient care continued with paper procedures; clinics and elective procedures were cancelled for Thursday and Friday; emergency departments remained open. | UMMC [1]; AP [5] |
| 27 Feb 2026 | Downtime care and clinic restart planning | UMMC said hospitals and emergency departments continued care using paper charts. It had begun seeing some urgent clinic patients and aimed for at least a partial return to normal appointments on Monday. | UMMC [2] |
| 28 Feb 2026 | Recovery milestone, reported later | UMMC's April account said it was largely back to normal by this date. This is a retrospective recovery milestone, not the date of the April statement. | UMMC [4] |
| 13 Mar 2026 | Recovery and forensic work | UMMC said most systems used for regular operations were back online; a full forensic picture could take months or longer. | UMMC [3] |
| 10 Apr 2026 | Retrospective status | UMMC said monitoring detected the unusual activity, the incident was not caused by one user clicking a malicious email, and forensic analysis of possible data access or exfiltration continued. | UMMC [4] |

### 4.4 Incident lifecycle and framework mapping

The map below links only the public evidence to broad response stages. It does not claim that a particular malware family or ATT&CK technique was used.

**Table 3. Evidence-based incident lifecycle discussion**

| Stage or topic | Public evidence | Evidence status | Relevant lesson |
|---|---|---|---|
| Detection | UMMC later said monitoring detected irregular activity and users reported issues [4]. | Confirmed institutional statement | Correlate alerts and reports; preserve timestamps and logs [6,10]. |
| Containment | UMMC said affected systems were shut down to contain the threat [2,4]. | Confirmed institutional statement | Plan isolation steps with technical and clinical teams [6,23]. |
| Downtime operations | Inpatient care continued using paper procedures; emergency departments stayed open [1,2]. | Confirmed institutional statement | Rehearse approved paper workflows and communication alternatives [17,18]. |
| Recovery | UMMC said most systems used for regular operations were online by Feb 28 [3,4]. | Retrospective institutional statement | Restore in stages and validate services before use [6,8]. |
| Forensic investigation | UMMC said a full forensic picture could take months and review of possible data access continued [3,4]. | Confirmed institutional statement | Preserve evidence and avoid premature conclusions [9,10]. |
| Initial access and malware family | Not specified in the cited UMMC updates. | Unknown | Do not assign an attack technique without supporting evidence. |

### 4.5 Ransomware role and what remains unknown

UMMC publicly identified the event as ransomware [1]. The cited sources do not name a malware family or provide a sample for analysis. The incident should therefore not be mapped to a named ransomware strain or a specific technical attack path. The April statement also rules out the oversimplified explanation that a single user clicking a malicious email caused the event, but it does not disclose an alternative entry method [4].

### 4.6 Clinical disruption and downtime workflow

UMMC reported that outpatient clinics and elective procedures were cancelled while inpatient teams used paper documentation and orders. Hospitals and emergency departments remained open, and time-sensitive care was prioritized for rescheduling [1,2]. CareContinuity Lab uses those service categories to inform its scenario inputs. It does not reproduce actual UMMC workflows or patient-level decisions.

### 4.7 Forensics, containment, and recovery

UMMC's updates describe system shutdown, support from cybersecurity specialists and federal agencies, continued care under downtime procedures, and recovery over time [1-4]. They also make clear that operational recovery and forensic closure were separate: most routine systems were back by February 28, while the review of possible data access was still under way in April [3,4]. The public record does not support a more detailed reconstruction.

## 5. Results & Discussions

### 5.1 Incident timeline and operational impact

The dated timeline shows an important distinction: system problems began on February 19, UMMC's ransomware statement was published on February 20, the public goal for restarting some clinic schedules was stated on February 27, and the later April account placed the broad return to normal by February 28 [1-5]. The dates describe different stages and should not be collapsed into a single “recovery date.”

The immediate operational effects documented by UMMC were unavailable EHR and phone services, statewide clinic closures, cancelled elective procedures, paper records and orders in hospitals, and continued emergency and inpatient care [1,2]. UMMC's April account says that delayed procedures, rescheduled visits, and operational challenges continued as consequences of the incident [4]. The public sources do not quantify patient harm, so this report does not make a patient-outcome claim.

**Table 4. Publicly reported effects and continuity response**

| Area | Publicly reported effect | Continuity response described by UMMC | Evidence |
|---|---|---|---|
| EHR and phones | Not operational during the initial response | Affected systems taken offline; downtime procedures used | UMMC [1,2,4] |
| Inpatient and emergency care | Services continued during the outage | Paper documentation and orders; emergency departments remained open | UMMC [1,2] |
| Clinics and elective procedures | Clinics statewide and elective procedures cancelled, later restarted in stages | Urgent clinic visits prioritized; schedules gradually resumed | UMMC [1,2,4] |
| Possible data exposure | Scope remained under investigation in April | Forensic review continued; regulatory and reporting work planned | UMMC [4] |

### 5.2 CareContinuity Lab risk-estimator results

The implementation was run with its displayed default inputs. The resulting scenario index was **26.9/100 (Moderate)**. Care continuity impact contributed 16.0 of 25 points, threat signals 5.5, exposure 4.4, and recovery resilience 1.0. Clinical-service criticality was the largest individual contributor at 10 points, followed by the suspicious sign-in rate at 3.6 points. These values demonstrate how the inputs change the assessment; they are not a measured UMMC risk score.

**Table 5. Predictor domain output for the included default scenario**

| Risk domain | Maximum points | Default result | Main interpretation |
|---|---:|---:|---|
| Threat signals | 25 | 5.5 | Aggregate sign-in anomaly rate and high-severity alerts |
| Exposure | 25 | 4.4 | Exposed critical vulnerabilities, patch delay, supplier dependence |
| Recovery resilience | 25 | 1.0 | Endpoint monitoring gap and backup verification state |
| Care continuity impact | 25 | 16.0 | Downtime readiness, tested redundancy, clinical criticality |
| Total | 100 | 26.9, Moderate | Highest weighted concern is continuity for a high-criticality service |

The score uses linear normalization within declared input ranges and caps values at those ranges. Risk bands are Low (0-24), Moderate (25-49), High (50-74), and Critical (75-100). Users can inspect the domain chart and factor contributions, then download the full inputs and outputs as JSON. Recommendations are triggered by elevated domain factors. A change in any input immediately recalculates the result.

This prototype has no labelled hospital incident dataset and has not been calibrated or externally validated. Consequently, the score supports structured scenario comparison, not the probability that an attack will occur. Real deployment would require suitable de-identified operational data, subject-matter review, calibration, and validation before operational use.

### 5.3 Detection and response

UMMC's April account says its monitoring systems detected irregular activity and that the response included a decision to shut down affected systems [4]. The February updates describe support from specialists and federal agencies, paper-based continuity procedures, and continuing efforts to restore services [1,2]. The public statements do not describe specific alerts, log findings, or the initial access route. The report therefore does not claim that a particular IDS rule or malware analysis result detected the incident.

### 5.4 Weaknesses highlighted by the case and recommended controls

The following are planning areas suggested by the outage and healthcare guidance. They are not claims that UMMC lacked these controls.

**Table 6. Planning areas and potential controls**

| Area | Risk to consider | Recommended preparation | Guidance |
|---|---|---|---|
| EHR downtime | Clinical records and orders may be unavailable | Practice paper documentation, patient identity checks, and post-recovery reconciliation | ASPR TRACIE; ONC [17-19] |
| Communications | Staff may not reach patients or one another through normal channels | Prepare approved alternate channels, call trees, and message ownership | HHS; ASPR TRACIE [17,18,25] |
| Detection and logging | A developing incident may be hard to understand quickly | Protect logs, synchronize time, and rehearse alert escalation | NIST [6,10,27] |
| Containment and recovery | Restoring too quickly can reintroduce risk | Define isolation roles, backup validation, and staged restoration checks | NIST; CISA [6,8,23] |
| Incident command | Decisions may be spread across technical and care teams | Keep an offline decision log and include clinical, privacy, and IT leads | NIST; HHS [6,12,13] |
| Data exposure | Early public information may not establish what was accessed | Preserve evidence and communicate uncertainty until review is complete | NIST; HHS [9,20-22] |

### 5.5 Comparative analysis

The 2024 Change Healthcare incident provides a useful comparison because it disrupted healthcare operations through a different part of the care system. HHS described nationwide disruption to healthcare and billing information systems, while CMS issued flexibilities to help prevent interruptions to Medicaid services and provider solvency [32,33]. UMMC's public account emphasizes local clinical-system downtime and paper-based hospital care; Change Healthcare illustrates how disruption at a shared transaction and billing provider can affect care organizations beyond the directly attacked company.

**Table 7. UMMC and Change Healthcare: different paths to healthcare disruption**

| Comparison point | UMMC, 2026 | Change Healthcare, 2024 |
|---|---|---|
| Disrupted service | EHR, phone, clinic and hospital support systems [1,2] | Claims, billing, eligibility, and healthcare transaction services [32,33] |
| Reported operational response | Paper procedures for hospital care; outpatient clinics and elective procedures cancelled [1,2] | Federal guidance and temporary payment flexibilities aimed to reduce disruption to care and providers [33] |
| Shared lesson | Healthcare continuity depends on prepared downtime processes | Dependencies on a shared external service can spread disruption across many providers |
| Evidence boundary | Initial access route and full data exposure scope remained under forensic review [4] | The cited HHS sources describe service and policy impacts, not a full technical reconstruction [32,33] |

### 5.6 Future directions

Future work could add department-specific synthetic scenarios, timed exercise events, an after-action worksheet, and a clearer output page for screenshots and deployment results. The project could also be reviewed by healthcare operations or emergency-management staff before being used in a real exercise. Such review would be necessary before adapting any prompt to local procedures.

## 6. Output

This section records the GitHub implementation and provides fields for deployment evidence and observed output. Update the live link and screenshots after deployment.

### 6.1 GitHub repository and deployment details

| Output item | Details to record |
|---|---|
| GitHub repository | https://github.com/KushbuAgrawal05/carecontinuity-lab |
| Branch | main |
| Streamlit app file | streamlit_app.py |
| Deployed Streamlit URL | [Paste the public streamlit.app link after deployment] |
| Deployment date and status | [Add date and successful deployment status] |
| Commit used for deployment | [Add the short GitHub commit ID shown by Streamlit] |

### 6.2 Screenshots and observed output

Insert screenshots captured from the deployed app. Keep each caption with the screenshot and record observed results.

| Figure | Screenshot to insert | Caption or observed result |
|---|---|---|
| Figure 1 | [Insert screenshot of the deployed case timeline] | Public UMMC timeline with source links is displayed. |
| Figure 2 | [Insert screenshot of selected selected risk indicator states] | The interface shows the selected risk indicators and continuity controls. |
| Figure 3 | [Insert screenshot of risk band, score, and contributing factors] | Add the risk band, score, and leading factors shown by your deployment. |
| Figure 4 | [Optional: insert screenshot of downloaded JSON or Streamlit deployment status] | Record the file name or deployment status you observed. |

## 7. Conclusion

The February 2026 UMMC incident shows how a ransomware outage can interrupt the digital systems hospitals use to organize care. The disruption began on February 19, was publicly identified as ransomware in UMMC's February 20 update, and affected EHR and phone access, clinics, elective procedures, and hospital workflows. UMMC reported that hospitals continued care using paper procedures and later said most operations were largely restored by February 28. Its forensic review of possible data access continued afterward [1-4]. Keeping event dates separate from publication dates and later recovery summaries gives a more accurate account.

CareContinuity Lab links the documented case to a separate scenario estimator. It does not recreate UMMC's systems or assess clinical risk. The main practical lesson is to prepare for system outages alongside technical incident response: practise downtime procedures, plan alternate communications, preserve evidence, and report only what the available evidence supports.

## References

[1] University of Mississippi Medical Center, “We Press On,” Vice Chancellor Notes, February 20, 2026. https://www.umc.edu/news/VCNotes/2026/02/20.html

[2] University of Mississippi Medical Center, “#UMMCStrong, Always,” Vice Chancellor Notes, February 27, 2026. https://www.umc.edu/news/VCNotes/2026/02/27.html

[3] University of Mississippi Medical Center, “Multi-topic,” Vice Chancellor Notes, March 13, 2026. https://www.umc.edu/news/VCNotes/2026/03/13.html

[4] University of Mississippi Medical Center, “Spring Update,” Vice Chancellor Notes, April 10, 2026. https://www.umc.edu/news/VCNotes/2026/04/10.html

[5] S. Bates, “Mississippi hospital system closes all clinics after ransomware attack,” Associated Press, February 20, 2026. https://apnews.com/article/cyberattack-university-mississippi-clinics-hospital-4b27a578a5e095c5a7d25c90768a5312

[6] A. Nelson, S. Rekhi, M. Souppaya, and K. Scarfone, *Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile*, NIST SP 800-61 Rev. 3, April 2025. https://doi.org/10.6028/NIST.SP.800-61r3

[7] NIST, *The NIST Cybersecurity Framework (CSF) 2.0*, NIST CSWP 29, February 2024. https://doi.org/10.6028/NIST.CSWP.29

[8] M. Swanson et al., *Contingency Planning Guide for Federal Information Systems*, NIST SP 800-34 Rev. 1, May 2010. https://doi.org/10.6028/NIST.SP.800-34r1

[9] K. Kent, S. Chevalier, T. Grance, and H. Dang, *Guide to Integrating Forensic Techniques into Incident Response*, NIST SP 800-86, August 2006. https://doi.org/10.6028/NIST.SP.800-86

[10] K. Kent and M. Souppaya, *Guide to Computer Security Log Management*, NIST SP 800-92, September 2006. https://doi.org/10.6028/NIST.SP.800-92

[11] NIST, *Security and Privacy Controls for Information Systems and Organizations*, NIST SP 800-53 Rev. 5, Update 1, December 2020. https://doi.org/10.6028/NIST.SP.800-53r5

[12] U.S. Department of Health and Human Services, “Healthcare and Public Health Sector-Specific Cybersecurity Performance Goals,” HHS Cyber Gateway, 2024. https://hhscyber.hhs.gov/cybersecurity-performance-goals.html

[13] U.S. Department of Health and Human Services, *Health Industry Cybersecurity Practices: Managing Threats and Protecting Patients*, 2023 Edition, 405(d) Program. https://405d.hhs.gov/Documents/HICP-Main-508.pdf

[14] HHS, Health Sector Coordinating Council, and Centers for Medicare & Medicaid Services, *Hospital Cyber Resiliency Initiative: Landscape Analysis*, 2023. https://hhscyber.hhs.gov/landscape-analysis.html

[15] Health Sector Coordinating Council Cybersecurity Working Group, *Health Industry Cybersecurity Strategic Plan 2024-2029*, 2024. https://asprtracie.hhs.gov/technical-resources/resource/12199/health-industry-cybersecurity-strategic-plan-2024-2029

[16] Cybersecurity and Infrastructure Security Agency, *Responding to Ransomware: A Guide for Healthcare Organizations*, 2021. https://www.cisa.gov/sites/default/files/21-601_HDO-RansomwareGuide_09072021_508c.pdf

[17] ASPR TRACIE, *Hospital Downtime Preparedness Checklist*, U.S. Department of Health and Human Services. https://files.asprtracie.hhs.gov/documents/healthcare-system-cybersecurity-incident-considerations-hospital-downtime-preparedness-checklist.pdf

[18] ASPR TRACIE, *Hospital Downtime Operations Checklist*, U.S. Department of Health and Human Services. https://files.asprtracie.hhs.gov/documents/healthcare-system-cybersecurity-incident-considerations-hospital-downtime-operations-checklist.pdf

[19] Office of the National Coordinator for Health Information Technology, “2025 SAFER Guide: Contingency Planning,” 2025. https://healthit.gov/resources/2025-safer-guide-contingency-planning/

[20] U.S. Department of Health and Human Services, “The Security Rule,” HIPAA for Professionals. https://www.hhs.gov/hipaa/for-professionals/security/index.html

[21] U.S. Department of Health and Human Services, “Breach Notification Rule,” HIPAA for Professionals. https://www.hhs.gov/hipaa/for-professionals/breach-notification/index.html

[22] U.S. Department of Health and Human Services, Office for Civil Rights, “Guidance on Ransomware and HIPAA,” 2016. https://www.hhs.gov/hipaa/for-professionals/special-topics/ransomware/index.html

[23] Cybersecurity and Infrastructure Security Agency, *#StopRansomware Guide*, updated 2023. https://www.cisa.gov/stopransomware/ransomware-guide

[24] Cybersecurity and Infrastructure Security Agency, “Tabletop Exercise Packages,” CISA Services. https://www.cisa.gov/resources-tools/services/cisa-tabletop-exercise-packages

[25] U.S. Department of Health and Human Services, “HHS Cyber Gateway,” Healthcare and Public Health Sector resources. https://hhscyber.hhs.gov/

[26] MITRE, “Data Encrypted for Impact: T1486,” *MITRE ATT&CK Enterprise*. https://attack.mitre.org/techniques/T1486/

[27] NIST, *Guide to Intrusion Detection and Prevention Systems (IDPS)*, NIST SP 800-94, February 2007. https://doi.org/10.6028/NIST.SP.800-94

[28] Symbiosis Institute of Technology, “Intrusion Detection System,” supplied Unit 4 course presentation, PowerPoint, 2026.

[29] Symbiosis Institute of Technology, “Malware Analysis,” supplied Unit 4 course presentation, PowerPoint, 2026.

[30] Symbiosis Institute of Technology, “Digital Forensics,” supplied Unit 4 course presentation, PowerPoint, 2026.


[31] Mississippi Today, “Cyberattack shuts down University of Mississippi Medical Center systems,” February 19, 2026. https://mississippitoday.org/2026/02/19/ummc-cyberattack/

[32] U.S. Department of Health and Human Services, “Change Healthcare Cybersecurity Incident Frequently Asked Questions,” Office for Civil Rights. https://www.hhs.gov/hipaa/for-professionals/special-topics/change-healthcare-cybersecurity-incident-frequently-asked-questions/index.html

[33] Centers for Medicare & Medicaid Services, “Change Healthcare Cybersecurity Incident: CMS Response and State Flexibilities.” https://www.hhs.gov/guidance/document/change-healthcare-cybersecurity-incident-cms-response-and-state-flexibilities
