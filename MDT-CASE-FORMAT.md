# MDT case format — structured clerking proforma

**P0. Replaces the free-text case submission.** 21 Jul 2026.
**Companion to [MDT-CASE-SUBMISSION-SPEC.md](MDT-CASE-SUBMISSION-SPEC.md).**

---

## Why

Two problems have one solution.

**The cases are unusable.** Live examples: a case whose entire summary is *"dddd"*; a question reading *"please advise on xxxxx"*; a case titled *"Rash photo case"* whose whole content is *"Age 30-39 rash. Question: Is this rosacea?"*

**And the boundary is unenforced.** *"Is this rosacea?"* was submitted and answered because nothing in the form required the clinician to have thought first.

> **A blank box invites a blank thought.** A clerking proforma forces clinical reasoning — and a clinician who has already reasoned is not asking the panel to reason for them.

This **supersedes** the *"what did you think it was / what did you do"* fields in the submission spec. Those two questions are now answered by **Differentials**, **Working diagnosis**, **Rationale** and **Management**, in clinically native language.

---

## Structure

**A core spine, always shown. Specialty blocks, shown conditionally.**

Progressive disclosure — one section at a time, not a wall of twenty fields. Every optional field has a one-click **Not applicable**.

---

## PART 1 — CORE (always)

| Field | Required | Notes |
|---|---|---|
| **Age band** | ✅ | Band only — never a precise age. See anonymisation below |
| **Sex** | ✅ | Clinically relevant; drives conditional blocks |
| **PC** — presenting complaint | ✅ | One line, patient's own words where useful |
| **HPC** — history of presenting complaint | ✅ | Onset, duration, course, associated features, what they have tried |
| **PMH** — past medical history | ✅ | Or explicit *nil significant* |
| **DH** — drug history | ✅ | Including OTC and herbal. **Allergies mandatory** — or explicit *no known drug allergies*. A blank allergy field is not the same as none |
| **FH** — family history | ✅ | Or *not relevant* |
| **SH** — social history | ✅ | ⚠️ See anonymisation warning below |
| **Surgical history** | Conditional | |
| **Review of systems** | ✅ | Relevant positives **and negatives** |
| **Vitals / observations** | ✅ | Or explicit *not recorded* — and if not recorded, that is itself a discussion point |
| **Examination findings** | ✅ | |
| **Investigations** | Conditional | Requested, results, and **whether they were acted on** |

---

## PART 2 — THE REASONING (always, all mandatory)

> **This is the part that makes it teaching rather than a referral.**

| Field | Required | Notes |
|---|---|---|
| **Differentials** | ✅ **Minimum 2** | Free-text list. **Plural is enforced.** This is the single most valuable field in the form |
| **Working diagnosis** | ✅ | What the clinician concluded |
| **Rationale** | ✅ | **Why** — what pointed toward it, and what pointed away from the alternatives |
| **Management** | ✅ | What was actually done. Prescribed, referred, safety-netted, reviewed |
| **Outcome, if known** | Optional | |
| **Learning question** | ✅ | Constrained — see submission spec §3 |

**Why minimum two differentials:** a clinician who has generated a differential has done the reasoning. A clinician who has not is asking the panel to do it. The field is the boundary.

**Rationale is where the teaching happens.** The panel's most useful contribution is rarely *"you were right"* — it is *"your reasoning was sound but you under-weighted X"*.

---

## PART 3 — SPECIALTY BLOCKS (conditional)

Shown only where the selected specialty or sex makes them relevant.

### Dermatology

> The most common failure in dermatology cases is *"rash"*. **Description, not a label.**

| Field | Required |
|---|---|
| **Primary lesion** | ✅ macule · patch · papule · plaque · nodule · vesicle · bulla · pustule · wheal · cyst |
| **Secondary change** | ✅ scale · crust · excoriation · lichenification · erosion · ulcer · fissure · atrophy · scarring |
| **Distribution** | ✅ localised · generalised · flexural · extensor · photodistributed · dermatomal · acral · truncal |
| **Configuration** | ✅ discrete · confluent · annular · linear · grouped · target · serpiginous |
| **Colour** | ✅ Including whether it blanches |
| **Size and number** | ✅ |
| **Border** | ✅ well-defined · ill-defined |
| **Surface and texture** | ✅ |
| **Symptoms** | ✅ itch · pain · burning · asymptomatic |
| **Nails, hair, mucosae** | ✅ Examined? Findings, or explicit *not examined* |
| **Image** | Optional — see submission spec §6 |

`[CONFIRM: whether to offer a picker for these. Recommended — it teaches the vocabulary to clinicians who do not have it, which is a large part of the audience.]`

### Women's health

Menstrual history · LMP · cycle regularity and length · contraception · obstetric history (gravidity, parity) · menopausal status · HRT history · cervical screening status

### Sexual health

Shown only where the presentation indicates it. Sexual history · risk assessment · partner notification considered · testing offered

### Mental health

Mental state examination · **risk assessment — self, others, safeguarding** · previous psychiatric history · substance use · current support and services

### ADHD

Developmental and school history · symptom onset before 12 · impairment across ≥2 settings · screening tool used and score (DIVA, ASRS, Conners) · comorbidity screen · cardiovascular history and baseline observations before stimulant

### Weight management

Weight, height, **BMI** · weight history and previous attempts · comorbidities · eating pattern · physical activity · contraindications to pharmacotherapy · thyroid and diabetes status

### TRT

Symptom score · **two morning testosterone levels** · LH, FSH, prolactin, SHBG · haematocrit · PSA where indicated · fertility discussion · cardiovascular risk

### General and acute

Red flag screen for the presentation · safety-netting given · follow-up arranged

---

## ⚠️ Anonymisation — richer detail means more identifiable

**More clinical detail increases identifiability, and this format asks for a lot more detail.** The controls have to be stronger, not the same.

| Risk | Control |
|---|---|
| **Precise ages in prose** — currently present: *"15-year-old male"*, *"30-year-old"* | Age band field only. **Strip and flag precise ages found in any free-text field** |
| **Occupation in social history** — "airline pilot with epilepsy" is identifiable | Occupation as a **category** (manual / office-based / healthcare / driving or safety-critical / not relevant), never free text |
| **Rare conditions** | A rare diagnosis plus a location is identifiable regardless of banding. Flag at submission |
| **Ethnicity** | Include **only where clinically relevant** — and it genuinely is in dermatology. Prompt the clinician to confirm relevance |
| **Dates** | Relative only — *"2-day history"*, never *"seen on 14 July"* |
| **Initials** — currently present: *"J.M."* | Blocked at field level, not just warned |
| **Free-text leakage** | Run the anonymiser over **every** field, not just the summary |

---

## What this changes

**Fewer cases, better cases.** This raises the submission bar, and some clinicians will not bother. That is the correct trade — five well-clerked cases teach more than fifty one-liners, and *"dddd"* would not survive the first field.

**Cases become reusable.** A structured case can go into the Session library as teaching material, be searched by presentation or diagnosis, and support pattern-based learning. A free-text blob cannot.

**The panel can answer properly.** A panel member given a full clerking can teach. Given *"Age 30-39 rash, is this rosacea?"* their only options are to guess or to diagnose — and diagnosing is what happened.

**And it does the boundary work.** A completed clerking with differentials, a working diagnosis, a rationale and a management plan is, on its face, a **closed case being reviewed**. There is no version of that form which reads as a request for a decision on a live patient.

---

## Build notes

- **Progressive disclosure.** One section at a time with a progress indicator. Twenty fields at once will lose people
- **Save as draft.** Clerking takes time and should survive a closed tab
- **Pre-fill from the consultation** where the case arises from one already in Clinickly — presentation, medications, allergies, observations. `[CONFIRM: how much can be carried across, and re-anonymised on the way]`
- **"Not applicable" is one click** on every optional field, and it is recorded — a deliberate N/A is information; a blank is not
- **Do not let a clinician skip Part 2.** Everything else can be light; the reasoning cannot

**Acceptance test:** *"dddd"* cannot be submitted. *"Age 30-39 rash. Is this rosacea?"* cannot be submitted. A clinician who completes the form has produced something a panel member can teach from — and has already done the thinking the panel would otherwise have done for them.
