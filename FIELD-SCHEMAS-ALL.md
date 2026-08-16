# Field schemas — all 28 policies (auto-extracted, verified against source)

Generated from the starter documents. Each field: clean label, category (VALUE / DECISION / CLAUSE / NOTE), type, default, source line. `NOTE` = reviewer-only, never shown to the clinic. `clinic_name` de-duplicated to one field.

Machine-readable version: `fields.json`.


## BCP — 33 fields (32 value · 1 decision · 0 clause)

| line | label | category | type | default |
|---|---|---|---|---|
| 3 | Clinic name | VALUE | clinic-name |  |
| 15 | Named responsible person | VALUE | role |  |
| 16 | Authorised by | VALUE | text |  |
| 17 | Issue Date | VALUE | date |  |
| 37 | All locations | VALUE | text |  |
| 43 | Printed copy at the premises | VALUE | text |  |
| 44 | Printed copy held off-site by a named person | VALUE | role |  |
| 45 | Electronic copy accessible without the clinic network | VALUE | role |  |
| 47 | Who checks quarterly that the contact numbers still work | VALUE | role |  |
| 59 | List this clinic's business critical processes, in priority order | VALUE | list |  |
| 85 | Every figure below | VALUE | duration |  |
| 93 | % | VALUE | text |  |
| 94 | Hours | VALUE | text |  |
| 95 | Days | VALUE | duration |  |
| 102 | Where the clinic uses a cloud-hosted clinical system rather than its own server, replace the server assumptions with the supplier's published availability and recovery commitments | VALUE | text |  |
| 132 | Who has authority to invoke the plan, and who does so in their absence | VALUE | role |  |
| 138 | How, and who holds the list if the system is down | VALUE | role |  |
| 151 | Named alternative provider(s) who have agreed in advance to see patients on a temporary basis | VALUE | role |  |
| 153 | Is there an actual agreement in place, in writing, with a named provider? v01 refers to "other independent doctors that have previously agreed" without naming any | DECISION | yes/no |  |
| 155 | How the clinic identifies those patients quickly when the system is unavailable | VALUE | text |  |
| 161 | This section in full | VALUE | text |  |
| 165 | Who decides | VALUE | role |  |
| 166 | Who authorises any decision | VALUE | role |  |
| 167 | IT support provider, and their out-of-hours contact | VALUE | text |  |
| 169 | Cyber insurer, and the policy number | VALUE | text |  |
| 174 | Paper contingency | VALUE | text |  |
| 176 | Backup arrangements | VALUE | duration |  |
| 182 | Clinic's critical suppliers and the alternative for each | VALUE | text |  |
| 201 | Contact-details check frequency | VALUE | duration | quarterly |
| 202 | Desktop exercise frequency | VALUE | duration | annually |
| 206 | Governance meeting | VALUE | text |  |
| 208 | Who is trained on the plan, and how new staff learn about it | VALUE | role |  |
| 214 | Audit owner | VALUE | role | Registered Manager, annually |

## C01 — 11 fields (9 value · 1 decision · 1 clause)

| line | label | category | type | default |
|---|---|---|---|---|
| 3 | Clinic name | VALUE | clinic-name |  |
| 11 | Named responsible person | VALUE | role |  |
| 12 | Authorised by | VALUE | text |  |
| 13 | Issue Date | VALUE | date |  |
| 59 | What happens instead | CLAUSE | text | the appointment is rescheduled, or the patient is referred, and the reason is recorded. Proceeding without a chaperone because none was available is not an acce |
| 77 | Who at this clinic is trained to act as a chaperone | VALUE | role |  |
| 104 | Clinic's position | VALUE | text |  |
| 118 | What the training covers and who delivers it | VALUE | role |  |
| 127 | Chaperones require a DBS check | DECISION | yes/no |  |
| 129 | Chaperone training refresh interval | VALUE | duration | every 3 years |
| 141 | Audit owner and frequency | VALUE | role | clinical lead, annually |

## C010 — 20 fields (16 value · 1 decision · 3 clause)

| line | label | category | type | default |
|---|---|---|---|---|
| 3 | Clinic name | VALUE | clinic-name |  |
| 11 | Named responsible person | VALUE | role |  |
| 12 | Authorised by | VALUE | text |  |
| 13 | Issue Date | VALUE | date |  |
| 50 | What happens where mandatory training lapses | CLAUSE | text | the individual is removed from the relevant duties until it is completed |
| 58 | Who holds and maintains the matrix | VALUE | role |  |
| 66 | Clinic's mandatory list and frequencies | VALUE | list |  |
| 70 | Safeguarding-adults training frequency | VALUE | duration | 3 years, with annual updates for Level 3 |
| 71 | Safeguarding-children training frequency | VALUE | duration | 3 years |
| 74 | IPC training frequency | VALUE | duration | annually |
| 78 | Health & safety / fire training frequency | VALUE | duration | annually for fire |
| 94 | Service-specific training | VALUE | text |  |
| 100 | Who delivers it and over what period | VALUE | role |  |
| 108 | How competence is assessed for each clinical role before independent practice, and who signs it off | VALUE | role |  |
| 112 | Supervision arrangements | CLAUSE | duration | clinical supervision for all clinical staff at least quarterly, recorded; line management supervision at least quarterly |
| 122 | Who appraises whom, including who appraises the Registered Manager | VALUE | role |  |
| 124 | Audit results feed individual appraisal | DECISION | yes/no |  |
| 137 | How the clinic satisfies itself that revalidation is on track | VALUE | role |  |
| 138 | Who checks | VALUE | role |  |
| 144 | Audit owner and frequency | CLAUSE | role | Registered Manager, quarterly for the matrix, annually for the full audit |

## C015 — 30 fields (29 value · 1 decision · 0 clause)

| line | label | category | type | default |
|---|---|---|---|---|
| 3 | Clinic name | VALUE | clinic-name |  |
| 13 | Named responsible person | VALUE | role |  |
| 14 | Authorised by | VALUE | text |  |
| 15 | Issue Date | VALUE | date |  |
| 47 | This section in full | VALUE | text |  |
| 51 | Registered provider | VALUE | text |  |
| 52 | Registered manager | VALUE | role |  |
| 53 | Registered address(es) | VALUE | address |  |
| 54 | Regulated activities registered for | VALUE | text |  |
| 55 | E.g | VALUE | text |  |
| 59 | List every service actually offered | VALUE | duration |  |
| 67 | And make this consistent with C032, which contradicted itself on whether under-18s are seen | VALUE | text |  |
| 73 | Days and hours for each service | VALUE | duration |  |
| 75 | NHS 111 / their GP / A&E as appropriate | VALUE | text |  |
| 75 | What the answerphone and website say, and whether they are consistent with each other | VALUE | text |  |
| 77 | The clinic provides any out-of-hours cover for patients under active treatment | DECISION | yes/no |  |
| 85 | Complete against the organisational chart | VALUE | role |  |
| 90 | Clinical Lead | VALUE | role |  |
| 91 | Safeguarding Lead | VALUE | role |  |
| 92 | IPC Lead | VALUE | role |  |
| 93 | Medicines Lead | VALUE | role |  |
| 94 | Risk Management Lead | VALUE | role |  |
| 95 | Complaints Manager | VALUE | role |  |
| 96 | Information Governance / Caldicott Lead | VALUE | role |  |
| 98 | Where one person holds several of these roles | VALUE | role |  |
| 108 | What meetings exist, who attends, how often, and who takes minutes | VALUE | role |  |
| 114 | Where governance minutes are held | VALUE | text |  |
| 120 | How this is recorded and who checks it | VALUE | role |  |
| 130 | Who makes the suitability decision for each service, and against what criteria | VALUE | role |  |
| 138 | Audit owner and frequency | VALUE | role | Registered Manager, annually |

## C017 — 21 fields (18 value · 1 decision · 2 clause)

| line | label | category | type | default |
|---|---|---|---|---|
| 3 | Clinic name | VALUE | clinic-name |  |
| 11 | Named responsible person | VALUE | role |  |
| 12 | Authorised by | VALUE | text |  |
| 13 | Issue Date | VALUE | date |  |
| 26 | Current version | VALUE | text |  |
| 73 | NAMED individual | VALUE | role |  |
| 80 | Who receives an incident report concerning the Risk Management Lead or Registered Manager | VALUE | role |  |
| 91 | Role | VALUE | role |  |
| 130 | RIDDOR reporting timescales | VALUE | role |  |
| 130 | RIDDOR reporting timescales | CLAUSE | duration | timescales — specified injuries and dangerous occurrences within 10 days; over-seven-day injuries within 15 days |
| 141 | Who is responsible for Yellow Card reporting, and how the clinic satisfies itself it is happening | VALUE | role |  |
| 145 | Named person, and their deputy | VALUE | role |  |
| 147 | The clinic reports patient safety events to the national patient safety system | DECISION | yes/no |  |
| 159 | Who reviews aggregate incident data, and how often | VALUE | role | Risk Management Lead, monthly |
| 161 | Investigation timescales | CLAUSE | duration | low — 10 working days; moderate — 20 working days; severe — 40 working days, with the patient kept updated throughout under C021 |
| 169 | How completed actions are verified as effective, not merely marked done | VALUE | duration |  |
| 173 | This section | VALUE | text |  |
| 177 | Who holds the register and how often it is reviewed | VALUE | role | Risk Management Lead, reviewed at every governance meeting |
| 192 | What support is available | VALUE | text |  |
| 238 | Incident-reporting training frequency | VALUE | duration | annually |
| 244 | Audit owner and frequency | VALUE | role | Risk Management Lead, annually |

## C02 — 35 fields (33 value · 1 decision · 1 clause)

| line | label | category | type | default |
|---|---|---|---|---|
| 3 | Clinic name | VALUE | clinic-name |  |
| 11 | Named responsible person | VALUE | role |  |
| 12 | Authorised by | VALUE | text |  |
| 13 | Issue Date | VALUE | date |  |
| 22 | Cite the current edition | VALUE | text |  |
| 27 | Relevant only where reusable instruments are decontaminated on site | VALUE | text |  |
| 28 | Current title and version | VALUE | text |  |
| 59 | NAMED individual | VALUE | role |  |
| 62 | Governance meeting | VALUE | text |  |
| 75 | See the assurance requirements below | VALUE | text |  |
| 85 | Hand-hygiene training frequency | VALUE | duration | annually |
| 98 | Bare below the elbows policy in clinical areas | VALUE | text |  |
| 109 | What is held, and when it is used | VALUE | text |  |
| 113 | Who checks PPE stock levels and how often | CLAUSE | role | IPC Lead, monthly — a policy requiring PPE that is not in the cupboard is not a control |
| 119 | Clinic's approach | VALUE | text |  |
| 124 | What | VALUE | text |  |
| 126 | Exclusion periods | VALUE | text |  |
| 127 | Ventilation arrangements in clinical rooms | VALUE | text |  |
| 150 | Role | VALUE | role |  |
| 152 | Named route and out-of-hours arrangement | VALUE | role |  |
| 154 | Who makes RIDDOR reports | VALUE | role |  |
| 161 | Who holds immunisation records and how the clinic satisfies itself they are current | VALUE | role |  |
| 163 | Other immunisations required by role, against the Green Book | VALUE | role |  |
| 165 | Which roles have clinical contact with patients | VALUE | role |  |
| 172 | Waste contractor, collection frequency, and where consignment notes are held | VALUE | duration |  |
| 178 | Where the spillage kit is kept and who checks it | VALUE | role |  |
| 182 | Applicable only where the clinic uses reusable linen | VALUE | duration |  |
| 188 | Who tracks this and where it is recorded | VALUE | role |  |
| 196 | Any reusable instruments are decontaminated on the premises | DECISION | yes/no | NO. Where YES, a full decontamination procedure, validated equipment, and HTM-compliant records are required, and that is a substantially larger undertaking tha |
| 205 | Who cleans | VALUE | role |  |
| 217 | Named contact at the landlord/contractor, and the frequency of joint review | VALUE | role | quarterly, recorded |
| 219 | Water safety | VALUE | role |  |
| 245 | Audit owner | VALUE | role | IPC Lead |
| 249 | Hand-hygiene audit frequency | VALUE | duration | six-monthly |
| 250 | Environment / cleanliness audit frequency | VALUE | duration | quarterly |

## C021 — 12 fields (11 value · 0 decision · 1 clause) · 1 note

| line | label | category | type | default |
|---|---|---|---|---|
| 3 | Clinic name | VALUE | clinic-name |  |
| 11 | Named responsible person | VALUE | role |  |
| 12 | Authorised by | VALUE | text |  |
| 13 | Issue Date | VALUE | date |  |
| 93 | [reviewer note] | NOTE | note | verify against the current text of Regulation 20(9) and CQC's guidance before adopting. |
| 119 | Who decides who apologises, and the default apologiser | VALUE | role |  |
| 123 | What support is available | VALUE | text |  |
| 141 | Role | VALUE | role |  |
| 166 | Written follow-up timescale | VALUE | duration | within 10 working days of the notification |
| 176 | Near-miss disclosure position | CLAUSE | text | — near misses the patient did not notice are not routinely disclosed, but are always recorded and reviewed |
| 195 | Governance meeting | VALUE | text |  |
| 215 | Duty-of-candour training frequency | VALUE | duration | annually |
| 221 | Audit owner and frequency | VALUE | role | Clinical Lead, six-monthly |

## C024 — 16 fields (15 value · 1 decision · 0 clause)

| line | label | category | type | default |
|---|---|---|---|---|
| 3 | Clinic name | VALUE | clinic-name |  |
| 11 | Named responsible person | VALUE | role |  |
| 12 | Authorised by | VALUE | text |  |
| 13 | Issue Date | VALUE | date |  |
| 74 | This whole section | VALUE | duration |  |
| 78 | E.g | VALUE | text |  |
| 79 | Named individual | VALUE | role |  |
| 80 | Who attends | VALUE | role |  |
| 81 | Governance meeting frequency | VALUE | duration | quarterly, minimum |
| 82 | Minimum attendance for decisions to be valid | VALUE | text |  |
| 83 | Minutes taken by | VALUE | text |  |
| 84 | Where governance minutes are held, and for how long | VALUE | text |  |
| 117 | Adjust to the clinic's own year | VALUE | duration |  |
| 125 | Who owns the governance calendar and ensures each item happens | VALUE | role |  |
| 141 | The clinic maintains an assurance framework or dashboard bringing these together | DECISION | yes/no |  |
| 158 | Audit owner and frequency | VALUE | role | Registered Manager, annually |

## C025 — 21 fields (19 value · 2 decision · 0 clause)

| line | label | category | type | default |
|---|---|---|---|---|
| 3 | Clinic name | VALUE | clinic-name |  |
| 13 | Named responsible person | VALUE | role |  |
| 14 | Authorised by | VALUE | text |  |
| 15 | Issue Date | VALUE | date |  |
| 66 | Any conditional start is permitted while a DBS check is outstanding, and if so with what supervision | DECISION | yes/no | no unsupervised patient contact until DBS is returned and satisfactory |
| 83 | Which method | VALUE | text |  |
| 84 | Level for each role | VALUE | role |  |
| 86 | Minimum level required | VALUE | text |  |
| 90 | Arrangements | VALUE | text |  |
| 93 | Who is responsible for completing the checklists (Appendices 1 and 2), and who countersigns to confirm all checks are complete before a start date is agreed | VALUE | role |  |
| 108 | Standard channels | VALUE | text |  |
| 114 | Role | VALUE | role |  |
| 118 | Minimum 6 months | VALUE | duration |  |
| 126 | How | VALUE | role |  |
| 131 | The clinic holds a sponsor licence, and who manages sponsor duties | DECISION | yes/no |  |
| 139 | Registration re-verification interval | VALUE | duration | annually |
| 141 | DBS renewal interval | VALUE | duration | every 3 years, or subscription to the DBS Update Service |
| 142 | This duty must be in the contract and the staff handbook, not only in this policy | VALUE | text |  |
| 149 | Audit owner and frequency | VALUE | role | Registered Manager, annually |
| 188 | Has any appointment decision been made in reliance on this paragraph? If so, take employment law advice | VALUE | text |  |
| 189 | Has this policy been shared with anyone else | VALUE | text |  |

## C029 — 15 fields (14 value · 0 decision · 1 clause) · 2 note

| line | label | category | type | default |
|---|---|---|---|---|
| 3 | Clinic name | VALUE | clinic-name |  |
| 11 | Named responsible person | VALUE | role |  |
| 12 | Authorised by | VALUE | text |  |
| 13 | Issue Date | VALUE | date |  |
| 24 | Current edition | VALUE | text |  |
| 52 | This whole section | VALUE | role |  |
| 70 | Who maintains the policy register and where it is held | VALUE | role |  |
| 78 | Who runs the review schedule and how overdue reviews are escalated | CLAUSE | role | reviews due in the next quarter are a standing item at the governance meeting |
| 84 | Role | VALUE | role |  |
| 92 | Who holds the signature record and checks completeness | VALUE | role |  |
| 93 | [reviewer note] | NOTE | note | where the current policy set is held so staff can find it — one location only. Multiple copies in multiple places is how superseded versions |
| 99 | [reviewer note] | NOTE | note | where the archive is and who has access. An archived copy must be clearly marked SUPERSEDED and dated. |
| 101 | Governance meeting | VALUE | text |  |
| 134 | Retention periods | VALUE | text |  |
| 136 | Who reviews records reaching the end of their retention period, and how often | VALUE | role |  |
| 142 | Who places and lifts a legal hold, and how it is recorded | VALUE | role |  |
| 156 | Audit owner and frequency | VALUE | role | Registered Manager, annually |

## C03 — 16 fields (12 value · 2 decision · 2 clause)

| line | label | category | type | default |
|---|---|---|---|---|
| 3 | Clinic name | VALUE | clinic-name |  |
| 11 | Named responsible person | VALUE | role |  |
| 12 | Authorised by | VALUE | text |  |
| 13 | Issue Date | VALUE | date |  |
| 69 | How patient preferences about who may be told what are recorded at registration | VALUE | role |  |
| 90 | Confidentiality / IG training frequency | VALUE | duration | annually |
| 101 | The clinical system logs access and who reviews the log | DECISION | yes/no |  |
| 117 | Approved text templates | VALUE | text |  |
| 118 | Route | CLAUSE | text | NHSmail to NHSmail, or password-protected attachment. Standard unencrypted email is not acceptable for identifiable clinical information |
| 129 | Who decides | CLAUSE | role | the Registered Manager or clinical lead, never the person who took the call |
| 133 | Role | VALUE | role |  |
| 134 | Who handles these | VALUE | role |  |
| 141 | Automatic screen lock timeout | VALUE | text | 5 minutes |
| 145 | Staff may access clinical systems remotely or on personal devices, and under what controls | DECISION | yes/no | NO personal devices; remote access only on clinic-managed equipment |
| 163 | Governance meeting | VALUE | text |  |
| 173 | Audit owner and frequency | VALUE | role | Registered Manager, annually |

## C032 — 23 fields (22 value · 0 decision · 1 clause) · 2 note

| line | label | category | type | default |
|---|---|---|---|---|
| 3 | Clinic name | VALUE | clinic-name |  |
| 15 | Named responsible person | VALUE | role |  |
| 16 | Authorised by | VALUE | text |  |
| 17 | Issue Date | VALUE | date |  |
| 29 | [reviewer note] | NOTE | note | cite the current edition. The 2010 edition cited in v01 has been superseded several times; check the current version before adopting. |
| 30 | [reviewer note] | NOTE | note | cite the edition the clinic holds. The 2014 edition cited in v01 has been superseded. |
| 131 | How the clinic verifies parental responsibility before treating a child or releasing records | CLAUSE | role | sight of the birth certificate or court order; recorded in the clinical record. "The person who brought them in" is not evidence of PR |
| 139 | NAMED individual | VALUE | role |  |
| 139 | 3 minimum | VALUE | text |  |
| 144 | Where the Safeguarding Lead and Registered Manager are the same person, name an external safeguarding contact for concerns involving that person | VALUE | role |  |
| 179 | Referral-confirmation timescale | VALUE | duration | 5 working days |
| 186 | Name of local authority | VALUE | text |  |
| 186 | Daytime phone | VALUE | text |  |
| 186 | Out-of-hours / emergency duty team | VALUE | text |  |
| 188 | Local Safeguarding Children Partnership | VALUE | text |  |
| 189 | Prevent / Channel | VALUE | text |  |
| 193 | Local multi-agency safeguarding arrangements and their published thresholds document | VALUE | text |  |
| 206 | Which staff at this clinic hold the personal duty | VALUE | role |  |
| 218 | Complete this section only where the service sees under-18s | VALUE | text |  |
| 296 | Level definitions against the current edition of the Intercollegiate Document | VALUE | text |  |
| 298 | Who holds it and reviews completion | VALUE | role |  |
| 304 | Governance meeting | VALUE | text |  |
| 310 | Audit owner and frequency | VALUE | role | Safeguarding Lead, annually |
| 342 | Name | VALUE | text |  |
| 342 | Contact | VALUE | text |  |

## C033 — 14 fields (13 value · 0 decision · 1 clause)

| line | label | category | type | default |
|---|---|---|---|---|
| 3 | Clinic name | VALUE | clinic-name |  |
| 11 | Named responsible person | VALUE | role |  |
| 12 | Authorised by | VALUE | text |  |
| 13 | Issue Date | VALUE | date |  |
| 55 | Caldicott Guardian or information governance lead | VALUE | role |  |
| 65 | Role | VALUE | role |  |
| 65 | Governance meeting | VALUE | text |  |
| 73 | Other regulators | VALUE | text |  |
| 78 | Minimum annual audit set | VALUE | text |  |
| 89 | And to GPhC standards where the clinic is dual-regulated | VALUE | text |  |
| 104 | Re-audit interval | CLAUSE | duration | re-audit interval — 6 months, or 3 months where the finding was significant |
| 117 | Retention period for audit data | VALUE | text |  |
| 125 | How patient feedback is gathered and how it feeds the audit programme | VALUE | text |  |
| 131 | Audit owner and frequency | VALUE | role | clinical lead, annually |

## C034 — 35 fields (29 value · 5 decision · 1 clause)

| line | label | category | type | default |
|---|---|---|---|---|
| 3 | Clinic name | VALUE | clinic-name |  |
| 13 | Named responsible person | VALUE | role |  |
| 14 | Authorised by | VALUE | text |  |
| 15 | Issue Date | VALUE | date |  |
| 24 | Cite the current edition of each | VALUE | duration |  |
| 30 | The clinic uses ReSPECT forms or recognises them | DECISION | yes/no |  |
| 65 | Location, and the internal emergency call procedure | VALUE | text |  |
| 71 | Emergency equipment & medicines check frequency | VALUE | duration | weekly — see C07 |
| 73 | Governance meeting | VALUE | text |  |
| 81 | Clinic's own emergency call procedure | VALUE | role |  |
| 91 | Compression rate, depth and ratio against the current Resuscitation Council UK guidelines rather than reproducing figures from a template | VALUE | text |  |
| 108 | Adrenaline dose table by age, verified against current Resuscitation Council UK guidance | VALUE | text |  |
| 110 | What the clinic does about refractory anaphylaxis | VALUE | duration |  |
| 116 | Which of these the clinic holds a procedure for, based on the services it provides and the medicines it uses | VALUE | text |  |
| 123 | Relevant where the clinic treats diabetes or uses medicines affecting glucose | VALUE | text |  |
| 124 | The clinic holds any, and under what direction | DECISION | yes/no |  |
| 125 | Relevant where the clinic prescribes opioids | VALUE | text |  |
| 126 | Severe asthma exacerbation | VALUE | text |  |
| 130 | What is held, and where | VALUE | duration |  |
| 134 | Location, pad expiry, battery status, and who checks | VALUE | role |  |
| 135 | Required if under-18s attend | VALUE | text |  |
| 136 | Cylinder contents checked, and by whom | VALUE | text |  |
| 137 | Adult and, where relevant, paediatric | VALUE | text |  |
| 138 | Held or not | VALUE | text |  |
| 139 | And that staff are trained to use anything held | VALUE | text |  |
| 147 | Emergency medicines list, against the clinic's actual risk profile and age range | VALUE | list |  |
| 150 | Paediatric strengths | VALUE | text |  |
| 152 | Emergency medicines check frequency | VALUE | duration | weekly |
| 156 | Clinic's position | VALUE | text |  |
| 162 | Does the clinic make DNACPR decisions itself, or only recognise decisions made elsewhere? For most outpatient clinics the answer is only to recognise them, and saying so is clearer than implying a capability the service does not have | DECISION | yes/no |  |
| 170 | Who leads it and when | CLAUSE | role | the same day, and separately from the incident investigation — a debrief is for the people, not for the paperwork |
| 184 | Emergency-recognition training frequency | VALUE | duration | annually |
| 186 | Training is practical, with a manikin and the clinic's own AED | DECISION | yes/no |  |
| 188 | The clinic runs a simulated emergency drill | DECISION | yes/no |  |
| 194 | Audit owner and frequency | VALUE | role | clinical lead, six-monthly |

## C038 — 37 fields (34 value · 2 decision · 1 clause)

| line | label | category | type | default |
|---|---|---|---|---|
| 3 | Clinic name | VALUE | clinic-name |  |
| 13 | Named responsible person | VALUE | role |  |
| 14 | Authorised by | VALUE | text |  |
| 15 | Issue Date | VALUE | date |  |
| 54 | Role | VALUE | role |  |
| 66 | Location | VALUE | text |  |
| 74 | Every row | VALUE | role |  |
| 78 | Overall responsibility for health and safety | VALUE | text |  |
| 79 | Fire warden | VALUE | text |  |
| 80 | First aider | VALUE | text |  |
| 81 | This was left as `<INSERT NAME>` in v01 | VALUE | text |  |
| 82 | Who makes RIDDOR reports | VALUE | role |  |
| 84 | Where the clinic is genuinely too small to have separate people, state what happens when the single post-holder is absent | VALUE | role |  |
| 92 | Who carries out risk assessments, where they are held, and how often they are reviewed | CLAUSE | role | reviewed annually, and after any incident, change of premises, change of equipment or change of process |
| 99 | Who carried it out, when, and whether the clinic or the landlord holds it | VALUE | role |  |
| 100 | Who holds the COSHH register and the safety data sheets | VALUE | role |  |
| 103 | Does anyone work alone | DECISION | yes/no |  |
| 104 | Absent from v01 | VALUE | text |  |
| 112 | Arrangements, and who is responsible for each | VALUE | role |  |
| 116 | Fire risk assessment review frequency | VALUE | duration | annually |
| 117 | Fire alarm test frequency | VALUE | duration | weekly, recorded |
| 120 | Fire drill frequency | VALUE | duration | annually, recorded |
| 122 | Escape-route check frequency | VALUE | duration | weekly |
| 124 | Evacuation arrangements for patients with limited mobility | VALUE | role |  |
| 130 | Complete following a first aid needs assessment | VALUE | text |  |
| 133 | Where the first aid kit is, who checks it and how often | VALUE | role | monthly, recorded |
| 134 | Where the accident book is kept | VALUE | text |  |
| 135 | The clinic's clinical emergency equipment is separate from its workplace first aid kit | DECISION | yes/no |  |
| 148 | Named person and deputy | VALUE | role |  |
| 155 | Portable appliance testing | VALUE | role |  |
| 156 | Servicing and calibration of clinical equipment | VALUE | text |  |
| 157 | Water safety and legionella | VALUE | role |  |
| 164 | This section | VALUE | text |  |
| 171 | Who decides whether the clinic continues to treat that patient, and how the decision is communicated | VALUE | role |  |
| 184 | Typically 3 years with annual refresher | VALUE | duration |  |
| 185 | Manual-handling training frequency | VALUE | duration | 3 years |
| 193 | Audit owner and frequency | VALUE | role | Registered Manager, annually |

## C039 — 14 fields (12 value · 0 decision · 2 clause)

| line | label | category | type | default |
|---|---|---|---|---|
| 3 | Clinic name | VALUE | clinic-name |  |
| 11 | Named responsible person | VALUE | role |  |
| 12 | Authorised by | VALUE | text |  |
| 13 | Issue Date | VALUE | date |  |
| 25 | Who receives them | VALUE | role |  |
| 75 | Which treatments require verified photographic ID before they may be provided | CLAUSE | list | any controlled drug, any long-term or high-risk medicine, and any treatment requiring monitoring. Where identity cannot be verified, those are not provided |
| 95 | How parental responsibility is established | VALUE | text |  |
| 115 | This section in full | VALUE | text |  |
| 121 | Method | VALUE | text |  |
| 126 | How the clinic detects the same person registering more than once under different details, and how it detects one person obtaining supplies from multiple services | VALUE | role |  |
| 130 | Clinic's approach where there are indicators of misuse | CLAUSE | role | escalate to the clinical lead, record, and consider whether a safeguarding referral is required |
| 137 | Which treatments are withheld where identity is unverified | VALUE | list |  |
| 143 | Audit owner and frequency | VALUE | role | Registered Manager, annually |
| 146 | Checked by observation | VALUE | text |  |

## C04 — 24 fields (22 value · 2 decision · 0 clause)

| line | label | category | type | default |
|---|---|---|---|---|
| 3 | Clinic name | VALUE | clinic-name |  |
| 13 | Named responsible person | VALUE | role |  |
| 14 | Authorised by | VALUE | text |  |
| 15 | Issue Date | VALUE | date |  |
| 28 | Independent adjudication scheme the clinic subscribes to | VALUE | text |  |
| 63 | Check the clinic's indemnity terms | VALUE | text |  |
| 73 | These are the figures the clinic commits to | VALUE | text |  |
| 81 | Maximum extension before escalation is offered | VALUE | duration | 40 working days |
| 98 | Role | VALUE | role |  |
| 104 | Named complaints manager | VALUE | role |  |
| 109 | Who investigates where the complaint concerns the Registered Manager | VALUE | role |  |
| 119 | Clinical lead | VALUE | role |  |
| 119 | MDU / MPS / MDDUS / other | VALUE | text |  |
| 121 | Named alternative clinician | VALUE | role |  |
| 160 | Actual escalation route offered | VALUE | text |  |
| 164 | Are we a member? If NO, this cannot be offered | DECISION | yes/no |  |
| 168 | Offered, and who pays | DECISION | yes/no |  |
| 171 | Where the clinic subscribes to no independent scheme, decide and record what is offered instead | VALUE | text |  |
| 184 | Named decision-maker | VALUE | role |  |
| 187 | Persistent-contact restriction review interval | VALUE | duration | 6 months |
| 189 | Governance meeting | VALUE | text |  |
| 205 | Complaints training frequency | VALUE | duration | annually |
| 210 | Accessible formats and languages available | VALUE | text |  |
| 217 | Audit owner and frequency | VALUE | role | Registered Manager, annually |

## C040 — 17 fields (11 value · 2 decision · 4 clause)

| line | label | category | type | default |
|---|---|---|---|---|
| 3 | Clinic name | VALUE | clinic-name |  |
| 11 | Named responsible person | VALUE | role |  |
| 12 | Authorised by | VALUE | text |  |
| 13 | Issue Date | VALUE | date |  |
| 62 | Verified, not assumed | VALUE | text |  |
| 72 | Which services and conditions may be delivered remotely, and which may not | CLAUSE | text | exclusions: any consultation requiring physical examination; first prescription of a controlled drug; anything requiring an intimate examination |
| 80 | Approved platform(s) | VALUE | role |  |
| 87 | A DPIA has been completed for the platform | DECISION | yes/no |  |
| 91 | What to do when the connection is inadequate | CLAUSE | text | stop, and either restart, switch to telephone, or convert to a face-to-face appointment — and record that this happened |
| 97 | Clinician must be alone and unable to be overheard | VALUE | text |  |
| 111 | Acceptable documents | VALUE | text |  |
| 117 | Where identity cannot be verified, which treatments are not provided | VALUE | list |  |
| 133 | How a patient can signal they are not safe to speak | CLAUSE | role | the clinician offers a closed-question route — "is it convenient to talk about this now?" — and a named way to make contact later |
| 155 | Consultations are recorded | DECISION | yes/no | NO. Where YES: separate explicit consent is required (C05), the patient is told who will have access and for how long it is kept, the recording is stored secure |
| 166 | Medicines not prescribed remotely | CLAUSE | text | controlled drugs on first prescription; any medicine requiring physical examination or baseline observations that have not been obtained |
| 174 | Who delivers training and how often | VALUE | role |  |
| 180 | Audit owner and frequency | VALUE | role | clinical lead, six-monthly |

## C05 — 20 fields (16 value · 3 decision · 1 clause) · 1 note

| line | label | category | type | default |
|---|---|---|---|---|
| 3 | Clinic name | VALUE | clinic-name |  |
| 13 | Named responsible person | VALUE | role |  |
| 14 | Authorised by | VALUE | text |  |
| 15 | Issue Date | VALUE | date |  |
| 30 | [reviewer note] | NOTE | note | check current status — this is an archived DH publication; the GMC 2020 guidance is the operative source |
| 119 | The service offers any treatment warranting a formal cooling-off period between decision and procedure | DECISION | yes/no | yes for any elective cosmetic or non-surgical aesthetic treatment — minimum 14 days between consultation and treatment, and never treat at the first appointment |
| 125 | Maximum interval after which written consent is re-taken rather than reconfirmed | VALUE | duration | 3 months |
| 135 | List of procedures at this clinic requiring written consent | VALUE | list |  |
| 156 | Any consent is delegated at this clinic | DECISION | yes/no | for a small clinic: NO — the treating clinician takes their own consent. Only complete the section below if delegation genuinely happens |
| 158 | Role | VALUE | role |  |
| 166 | Interpreting service and how to book it | VALUE | text |  |
| 167 | Arrangements | VALUE | text |  |
| 169 | Route | VALUE | text |  |
| 235 | Local IMCA service and how to instruct | VALUE | text |  |
| 246 | Complete this section only where the clinic sees under-18s | VALUE | text |  |
| 252 | Clinic's position | CLAUSE | role | any refusal by a competent young person of a treatment considered necessary is escalated to the clinical lead and, where the matter is serious, legal advice is  |
| 266 | Any recordings are used for marketing, including before-and-after images | DECISION | yes/no |  |
| 302 | Consent training refresh interval | VALUE | duration | every 3 years |
| 306 | Who holds it | VALUE | role |  |
| 312 | Audit owner and frequency | VALUE | role | Clinical Lead, annually |
| 323 | Governance meeting | VALUE | text |  |

## C07 — 24 fields (19 value · 4 decision · 1 clause)

| line | label | category | type | default |
|---|---|---|---|---|
| 3 | Clinic name | VALUE | clinic-name |  |
| 11 | Named responsible person | VALUE | role |  |
| 12 | Authorised by | VALUE | text |  |
| 13 | Issue Date | VALUE | date |  |
| 26 | Applicable where the clinic operates from GPhC-registered premises | VALUE | text |  |
| 46 | The clinic holds and supplies stock medicines, or prescribes only | DECISION | yes/no | for a prescribing-only service: sections on stock, storage and disposal are marked not applicable, and that is stated explicitly rather than left ambiguous |
| 68 | NAMED individual | VALUE | role |  |
| 81 | Where emergency medicines, oxygen and the defibrillator are held | VALUE | duration |  |
| 84 | Emergency medicines & equipment check frequency | VALUE | duration | weekly |
| 87 | Emergency medicines held, against the clinic's actual risk profile and the age range seen | VALUE | text |  |
| 116 | Which of these routes the clinic actually uses | VALUE | text |  |
| 121 | Where PSD templates are held | VALUE | text |  |
| 122 | The clinic uses PGDs at all | DECISION | yes/no | NO |
| 125 | PGD authorisation — signatories & authorised practitioners | VALUE | role |  |
| 135 | How licence status is verified | VALUE | text |  |
| 137 | Role | VALUE | role |  |
| 141 | The clinic verifies pack authenticity on receipt, and how | DECISION | yes/no |  |
| 149 | Excursion procedure | VALUE | text |  |
| 151 | Who checks storage conditions, and how often | VALUE | role |  |
| 160 | Waste contractor and where consignment notes are held | VALUE | text |  |
| 164 | The clinic accepts medicines returned by patients | DECISION | yes/no | NO — patients are directed to a community pharmacy. Where YES: returned medicines are never returned to stock or reissued to another patient under any circumsta |
| 177 | Who is responsible for Yellow Card reporting | VALUE | role |  |
| 181 | Who receives National Patient Safety Alerts and MHRA Drug Safety Update, how they are actioned, and where the record of action is kept | CLAUSE | role | medicines lead, checked monthly, actions recorded and reported to the governance meeting |
| 187 | Audit owner and frequency | VALUE | role | medicines lead, six-monthly |

## C07F — 12 fields (4 value · 7 decision · 1 clause)

| line | label | category | type | default |
|---|---|---|---|---|
| 3 | Clinic name | VALUE | clinic-name |  |
| 12 | Named responsible person | VALUE | role |  |
| 14 | Who signs this off | VALUE | role |  |
| 44 | Does your clinic prescribe controlled drugs, and if so which schedules? | DECISION | yes/no | NO — this clinic does not prescribe controlled drugs of any schedule |
| 45 | Does your clinic restrict prescribing to a defined formulary or exclude particular drug classes | DECISION | yes/no | NO formal formulary — prescribing follows BNF/NICE and local antimicrobial guidance |
| 47 | Does your clinic issue any prescription without a same-day consultation? | DECISION | yes/no | NO |
| 59 | Does your clinic provide written medicine information | DECISION | yes/no | verbal plus the manufacturer's patient information leaflet |
| 63 | Is GP notification the default (with patient consent)? | DECISION | yes/no | YES — offered at every prescribing encounter and the decision recorded |
| 70 | Does your clinic prescribe medicines requiring ongoing monitoring or a risk-management programme | DECISION | yes/no | NO |
| 73 | Does your clinic initiate or continue medicines for long-term conditions? | DECISION | yes/no | NO — acute and episodic care only; long-term-condition management remains with the patient's own GP |
| 80 | What is your clinic's disposal route? | CLAUSE | text | returned to a registered pharmacy for destruction; the return is recorded |
| 95 | Disposal route | VALUE | text |  |

## C08 — 25 fields (24 value · 0 decision · 1 clause) · 1 note

| line | label | category | type | default |
|---|---|---|---|---|
| 3 | Clinic name | VALUE | clinic-name |  |
| 13 | Named responsible person | VALUE | role |  |
| 14 | Authorised by | VALUE | text |  |
| 15 | Issue Date | VALUE | date |  |
| 31 | [reviewer note] | NOTE | note | cite the edition the clinic holds. The 2018 first edition was superseded in 2024 — check for the current edition before adopting. |
| 143 | NAMED individual | VALUE | role |  |
| 143 | 3 or above | VALUE | text |  |
| 148 | Where the Safeguarding Lead and Registered Manager are the same person | VALUE | role |  |
| 164 | Refresher frequency | CLAUSE | duration | Level 1 every 3 years; Levels 2 and 3 every 3 years with annual updates, per the Intercollegiate Document |
| 166 | Who holds the matrix and reviews completion | VALUE | role |  |
| 203 | Referral-decision timescale | VALUE | text | 1 working day |
| 207 | Referral follow-up timescale | VALUE | duration | 5 working days |
| 235 | Who makes CQC statutory notifications | VALUE | role |  |
| 277 | Decision-not-to-refer review interval | VALUE | duration | every 3 months, or sooner on any change |
| 289 | Local MARAC referral route | VALUE | text |  |
| 294 | Local Prevent/Channel referral contact | VALUE | text |  |
| 322 | Role | VALUE | role |  |
| 332 | Access to occupational health or an employee assistance programme | VALUE | text |  |
| 342 | Governance meeting | VALUE | text |  |
| 347 | Audit owner and frequency | VALUE | role | Safeguarding Lead, annually |
| 354 | Checked annually | VALUE | duration |  |
| 378 | Name | VALUE | text |  |
| 378 | Contact | VALUE | text |  |
| 381 | Name of authority | VALUE | text |  |
| 381 | Phone | VALUE | text |  |
| 381 | Out of hours | VALUE | text |  |

## C09 — 18 fields (15 value · 1 decision · 2 clause) · 1 note

| line | label | category | type | default |
|---|---|---|---|---|
| 3 | Clinic name | VALUE | clinic-name |  |
| 13 | Named responsible person | VALUE | role |  |
| 14 | Authorised by | VALUE | text |  |
| 15 | Issue Date | VALUE | date |  |
| 25 | Cite the current edition | VALUE | text |  |
| 58 | Who maintains the approved abbreviation list | VALUE | role |  |
| 112 | Role | VALUE | role |  |
| 114 | Who may amend a record, and who may not | CLAUSE | role | a clinician may add an addendum to their own entry at any time; nobody may amend another person's entry — they add their own, cross-referenced |
| 129 | Where paper records are held, and what protects them | VALUE | text |  |
| 130 | Electronic system, where data is hosted, and whether it is UK/EEA hosted | VALUE | text |  |
| 131 | Backup arrangements and how restoration is tested | CLAUSE | duration | daily backup, restoration tested at least annually — an untested backup is an assumption, not a control |
| 138 | [reviewer note] | NOTE | note | verify every period below against the current **Records Management Code of Practice** before adopting. The schedule in v01 was drawn from a  |
| 147 | Against the current Code | VALUE | text |  |
| 149 | Who places and lifts a retention hold | VALUE | role |  |
| 151 | Destruction schedule | VALUE | role | annual review by the Registered Manager |
| 158 | Who holds the destruction log | VALUE | role |  |
| 164 | Audit owner and frequency | VALUE | role | Clinical Lead, six-monthly |
| 178 | Governance meeting | VALUE | text |  |
| 178 | Record keeping audit results feed individual appraisal | DECISION | yes/no |  |

## C41 — 13 fields (11 value · 0 decision · 2 clause)

| line | label | category | type | default |
|---|---|---|---|---|
| 3 | Clinic name | VALUE | clinic-name |  |
| 11 | Named responsible person | VALUE | role |  |
| 12 | Authorised by | VALUE | text |  |
| 13 | Issue Date | VALUE | date |  |
| 60 | Additional service-specific trigger | VALUE | text |  |
| 69 | Services where GP notification is a non-negotiable condition of treatment | CLAUSE | text | controlled drugs, any long-term or high-risk medicine, and any treatment requiring blood monitoring. For these, "no GP letter" means "no treatment." |
| 73 | Route used | CLAUSE | address | NHSmail (@nhs.net) to the practice's shared clinical inbox where both parties hold NHSmail; otherwise password-protected attachment or postal letter marked priv |
| 75 | Who reviews incoming clinical correspondence and within what timescale | VALUE | role | the treating clinician, within 3 working days |
| 105 | GP-letter timescale — new long-term / high-risk prescription | VALUE | duration | 2 working days |
| 106 | GP-letter timescale — routine | VALUE | duration | 5 working days |
| 114 | Services that require a registered GP | VALUE | text | any treatment requiring monitoring or repeat prescribing |
| 132 | Audit owner and frequency | VALUE | role | Clinical Lead, six-monthly |
| 140 | Governance meeting | VALUE | text |  |

## S01 — 11 fields (9 value · 1 decision · 1 clause)

| line | label | category | type | default |
|---|---|---|---|---|
| 3 | Clinic name | VALUE | clinic-name |  |
| 11 | Named responsible person | VALUE | role |  |
| 12 | Authorised by | VALUE | text |  |
| 13 | Issue Date | VALUE | date |  |
| 24 | Applicability | VALUE | text |  |
| 84 | What adjustments the clinic can make and what it cannot | VALUE | date |  |
| 86 | What is available | VALUE | duration |  |
| 117 | What the clinic does where a patient harasses a member of staff | CLAUSE | text | the member of staff may withdraw from the situation immediately without needing permission; the incident is reported under C017; and the clinic decides whether  |
| 148 | EDI training | VALUE | role | all staff at induction, then every 3 years |
| 149 | The clinic monitors the diversity of its workforce and of the patients it sees, and what it does with that information | DECISION | yes/no |  |
| 159 | Audit owner and frequency | VALUE | role | Registered Manager, annually |

## S03 — 20 fields (17 value · 1 decision · 2 clause)

| line | label | category | type | default |
|---|---|---|---|---|
| 3 | Clinic name | VALUE | clinic-name |  |
| 11 | Named responsible person | VALUE | role |  |
| 12 | Authorised by | VALUE | text |  |
| 13 | Issue Date | VALUE | date |  |
| 58 | Role | VALUE | role |  |
| 95 | Governance meeting | VALUE | text |  |
| 106 | Named Registered Manager | VALUE | role |  |
| 107 | Named Clinical Lead | VALUE | role |  |
| 108 | Named Safeguarding Lead | VALUE | role |  |
| 109 | Named Speaking Up Guardian, or an independent named person such as a non-executive director or external adviser | CLAUSE | role | for a small clinic: a named person outside the direct management line — this must be a real named individual, not a role that does not exist |
| 111 | An anonymous route exists | DECISION | yes/no | a monitored email address checked by two named people |
| 123 | Concern acknowledgement timescale | VALUE | duration | 2 working days |
| 124 | Concern initial-assessment timescale | VALUE | duration | 5 working days |
| 126 | Investigation timescale | CLAUSE | role | 20 working days; where longer, the person is told why and given a revised date |
| 152 | Local contact | VALUE | text |  |
| 158 | Occupational health / EAP arrangements, if any | VALUE | text |  |
| 167 | Speaking-up training frequency | VALUE | text | annual |
| 168 | Where speaking-up routes are displayed | VALUE | text | staff room and staff intranet |
| 170 | Speaking-up governance-report frequency | VALUE | duration | six-monthly |
| 174 | Audit owner and frequency | VALUE | role | Registered Manager, annually |

## S12 — 23 fields (19 value · 1 decision · 3 clause)

| line | label | category | type | default |
|---|---|---|---|---|
| 3 | Clinic name | VALUE | clinic-name |  |
| 11 | Named responsible person | VALUE | role |  |
| 12 | Authorised by | VALUE | text |  |
| 13 | Issue Date | VALUE | date |  |
| 51 | Where the price list is displayed | VALUE | text | on the website, in the waiting area, and provided on request |
| 63 | An assessment fee is refundable where no treatment is offered | DECISION | yes/no | the assessment fee is retained, because the assessment was delivered — but this must be stated before the appointment, not after |
| 65 | Mechanism | CLAUSE | text | the patient confirms the quoted fee in writing (booking confirmation, signed consent form, or e-form) and a copy is retained |
| 75 | Known financial interests to be declared as standard | VALUE | text |  |
| 79 | Charges for non-routine administrative work | VALUE | list |  |
| 102 | Cancellation notice period (full refund) | VALUE | text | 48 hours |
| 102 | Cancellation notice period (full refund) | VALUE | text | — full refund or free reschedule |
| 103 | Cancellation fee position (under 48h notice) | CLAUSE | text | — fee retained, discretion applied for illness, bereavement or emergency |
| 104 | Did-not-attend fee position | VALUE | text | — fee retained |
| 107 | Part-course cancellation refund position | CLAUSE | text | — refund of unused sessions less any non-recoverable costs already incurred, itemised |
| 114 | Named role | VALUE | role |  |
| 115 | Refund acknowledgement timescale | VALUE | duration | 3 working days |
| 116 | Refund decision timescale | VALUE | duration | 20 working days |
| 117 | E.g | VALUE | text |  |
| 118 | Governance meeting | VALUE | text |  |
| 126 | Fee-list review frequency | VALUE | duration | annually |
| 126 | Fee-list review frequency | VALUE | role |  |
| 129 | New-price effective delay | VALUE | duration | 30 days |
| 133 | Audit owner and frequency | VALUE | role | Registered Manager, annually |

## S13 — 18 fields (17 value · 0 decision · 1 clause)

| line | label | category | type | default |
|---|---|---|---|---|
| 3 | Clinic name | VALUE | clinic-name |  |
| 11 | Named responsible person | VALUE | role |  |
| 12 | Authorised by | VALUE | text |  |
| 13 | Issue Date | VALUE | date |  |
| 53 | Rating-display update deadline | CLAUSE | duration | 21 calendar days of publication — CQC's guidance expects display "as soon as reasonably practicable"; 21 days is the outside limit, not the target |
| 64 | Where the service operates from GPhC-registered pharmacy premises | VALUE | text |  |
| 65 | Registration numbers of the professionals providing care, if displayed | VALUE | text |  |
| 69 | Display-accuracy check frequency | VALUE | duration | — checked quarterly and recorded |
| 85 | GPhC premises registration number, if applicable | VALUE | text |  |
| 86 | Responsible Pharmacist notice, if applicable | VALUE | text |  |
| 87 | Professional registration numbers of clinicians | VALUE | text |  |
| 90 | Additional premises | VALUE | duration |  |
| 94 | Role | VALUE | role |  |
| 95 | Rating-update timescale after publication | VALUE | duration | 5 working days |
| 100 | Governance meeting | VALUE | text |  |
| 119 | Others | VALUE | text |  |
| 125 | Display check frequency | VALUE | duration | quarterly |
| 138 | Audit owner and frequency | VALUE | role | Registered Manager, annually |