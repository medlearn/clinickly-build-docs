# Completeness Check — build spec

**For the developer. New feature, P1.**

The governed library now has **28 policies** in `/starters/`. This spec defines the check that runs against them before anything is published to a clinic.

Every rule below comes from a real defect found in a real 119-document policy corpus that had **passed a CQC inspection**. None of it is hypothetical.

---

## Why this matters commercially

A clinic cannot run these checks on itself. It needs the whole corpus, the requirement-theme map and a maintained reference list to spot any of it. That is what Clinickly has and a clinic does not.

This is the feature that makes the library a product rather than a folder of documents.

---

## Rule 1 — Unfilled placeholders block publication

**Severity: BLOCK. Cannot publish.**

Detect any of:

```
Xxxx          XXXX          XXXXX
<INSERT NAME> [INSERT ...]  INSERT LOCAL
[CONFIRM: ...]              X hours / X days / X %
```

**Real examples found:**

| Document | Placeholder |
|---|---|
| C05 Consent | `XXXXX procedure` — **on a form a patient signs** |
| C08 Safeguarding Adults | `Xxxx` ×4, `INSERT LOCAL S/S` ×2 |
| C032 Safeguarding Children | `[INSERT Social Services Safeguarding Protocols]` — the referral framework itself |
| C017 Risk Management | `<INSERT NAME>` — who handles media during a serious incident |
| C038 Health & Safety | `<INSERT NAME>` — who to report blocked fire exits to |
| Business Continuity | `X hours`, `X days`, `X %` ×4 — the IT recovery assumptions |

**Design note:** the reason these survived is that `Xxxx` is *camouflaged* — it looks like text. Our `[CONFIRM: …]` convention is deliberately ugly so an unfinished field is visible. Keep it that way.

**Patient-facing documents get a louder warning.** The C05 defect is the worst in the corpus not because the law is wrong but because it reached a patient.

---

## Rule 2 — Statutes that do not exist

**Severity: BLOCK.**

Maintain a list of valid UK statute titles. Flag any citation that does not match.

**Real examples found:**

| Cited | Actual |
|---|---|
| "Children and Young Persons Act 1989" ×8 | **Children Act 1989** |
| "Adoption and Children and Young Persons Act 2002" | **Adoption and Children Act 2002** |
| "Data Protection Act 1989" | No such Act |
| "Data Protection Act 2004" | No such Act |

The first two were caused by a global find-and-replace of *child* → *young person* that was never proofread. It also produced: *"'Children and children and young persons' therefore means 'children and young persons and young people'"*.

**Also flag suspicious bulk-edit artefacts** — repeated phrases, sentences that no longer parse.

---

## Rule 3 — Superseded references

**Severity: WARN, with the replacement named.**

Maintain a reference table of `superseded → current`. Seed it with:

| Superseded | Current | Found in |
|---|---|---|
| Data Protection Act 1998 | **DPA 2018 + UK GDPR** | **8 docs** |
| National Patient Safety Agency | Abolished 2012 → NHS England / LFPSE; alerts via CAS | **9 docs** |
| GMC *Good Medical Practice* 2013 | 2024 edition | Many |
| GMC *Consent: Patients and Doctors…* 2008 | *Decision making and consent* (2020) | C05 |
| **Resuscitation Council (UK) 2015** | **RC UK Guidelines 2021**; body renamed 2020 | **C034 ×11** |
| RIDDOR 1995 | **RIDDOR 2013** | C017 |
| Working Together 2010 (DCSF) | Current edition; DCSF abolished 2010 | C032 |
| Intercollegiate Document 2014 / 2018 | Current editions | C08, C032 |
| CQC *Essential Standards of Quality and Safety* | Fundamental Standards (2015) | S01 |
| GMC *Equality and Diversity 2011 to 2014* | **Expired scheme** | S01 |
| Caldicott Principles 1997 (6) | **2020 (8 principles)** | C033, C029 |
| NHS Choices | NHS.uk (2018) | C09 |
| Department of Health | DHSC | Several |

**Tier by risk.** A stale complaints reference is untidy. **A stale resuscitation guideline could change what someone does during a cardiac arrest** — C034 must be treated as high severity and gets an annual review cycle, not two-yearly.

---

## Rule 4 — Contradictions within one document

**Severity: BLOCK.**

Two statements of fact that cannot both be true.

**Real examples:**

- **C032:** *"under 18s are not seen at the clinic"* and *"At Ahmeys Clinic under 18s are seen"* — **same section, four lines apart.** This determines the mandatory safeguarding training level for every clinical member of staff.
- **C04:** response due in *"21 days"* / *"28 working days"* / *"21 working days"* — three figures for one deadline.
- **C04:** tells complainants to escalate to CQC, then states CQC will not arbitrate.

**Start with the tractable subset:** numeric values for the same named quantity (deadlines, intervals, ages, frequencies) stated differently within one document. That catches C04 mechanically.

---

## Rule 5 — Contradictions across documents

**Severity: WARN.** Harder, and the highest-value rule we have.

**Real example:** C039 lists a utility bill as acceptable ID. C040 states *"Bills will not meet this criteria."* Neither document is wrong on its own face. A member of staff following clinic policy correctly could reach either answer.

**Approach:** extract typed assertions against the requirement-theme layer — acceptable ID documents, retention periods, response deadlines, training frequencies — and compare across documents sharing a theme.

---

## Rule 6 — Duplicate policies

**Severity: BLOCK on publish, WARN on library.**

**Real example:** C025 and S07 are both live recruitment policies with near-identical text. **Both contained the same unlawful clause.** Correcting one would have left the other in force.

Detect high text similarity across documents, and any two documents mapped to the same requirement theme with the same scope.

---

## Rule 7 — Suspiciously thin for the theme

**Severity: WARN.**

Compare word count against other documents on the same theme.

**Real examples:**

| Policy | Length | Carries |
|---|---|---|
| **C09 Record Keeping** | **898 words** | CQC Reg 17; a personal standard under GMC *and* GPhC |
| **C03 Confidentiality** | **1,211 words** | UK GDPR, Caldicott, common law duty |
| **C010 Training** | **349 words** | **CQC Reg 18 — the staffing regulation** |
| **C015 Operational** | **388 words** | Describes what the clinic *is* |

Every one of these was missing something structural — C03 had no data breach procedure and no mention of the **72-hour ICO duty**; C010 had no mandatory training list, no induction, no supervision, no appraisal.

**Length is a proxy, not a verdict.** Flag for review; never auto-fail.

---

## Rule 8 — Unverifiable sources

**Severity: WARN.**

A reference must be a citable, checkable document.

**Real examples:**

| Cited as a reference | Problem |
|---|---|
| **"Prof. Sparrow Surgery CQC no. 15"**, "CQC: Prof Sparrow mythbusters", "CQC: Prof Sparrow No4" | **11 documents.** Presented as CQC material; it is not |
| "Bredon Hill Surgery" | Another practice's document |
| "York University HR Dept." | Another organisation's internal function |
| "Rosalie Thompson – infection control nurse" | A person, not a document |
| "Heart of England NHS Foundation" | Trust **dissolved 2018** |
| "University Hospitals Bristol NHS Foundation Trust" | Trust **dissolved 2020** |
| "British Medical Association", "NHS England", "BMA" | Organisation names, no document title |

**Also flag organisations that no longer exist** — NPSA, DCSF, dissolved NHS trusts.

---

## Rule 9 — Regulator coverage

**Severity: WARN.**

Every published policy declares the regulators it evidences. Flag where a theme's expected regulator is missing.

**Real finding — and the most commercially important one:**

| Regulator | Documents mentioning it |
|---|---|
| **GMC** | **41 of 119** |
| **GPhC** | **0 of 119** |

Not one document in a corpus owned and operated by a **pharmacist prescriber who is the registered manager** references the pharmacy regulator. C07 Medicines Management cited the GMC, the NMC and *Dale and Appelbe* — and not the GPhC.

Clinickly's core market is **pharmacist prescribers working from GPhC-registered premises**. Shipping GMC-framed policies to that audience is the exact failure the product exists to prevent. Every starter now maps GPhC alongside CQC.

---

## Rule 10 — Named-role integrity

**Severity: WARN.**

Flag role references with no name, and single points of failure.

**Real examples:**

- **C08:** "the Adult Safeguarding Lead" throughout, **never named**. A worried receptionist cannot use a job title at 4pm on a Friday.
- **C038:** the same individual named as H&S lead, **both** fire wardens (listed twice), **and** the first aider. When they are on leave the clinic has no fire warden and no first aider.
- Several policies have no alternative route where the concern is *about* the named person.

**Rules:** every named role has a real name · every critical role has a deputy · every escalation route has an alternative when the concern involves the post-holder.

---

## Rule 11 — Review-date integrity

**Severity: WARN at 90 days, BLOCK past due for high-risk themes.**

Requires a **policy register** — the single source of truth for which version is current.

The corpus had no register, no version convention, no approval workflow, and no process for withdrawing a superseded version. **That absence is why every defect above survived: nothing was responsible for noticing.**

C029 — the *Document Control* policy — had none of this, and its own header block says **C027**.

---

## Implementation order

1. **Rule 1** (placeholders) — trivially detectable, catches the worst real defect
2. **Rule 3** (superseded refs) — needs the reference table; highest ongoing value
3. **Rule 11** (register + review dates) — the control that prevents recurrence
4. **Rule 2** (invalid statutes) — needs a statute list
5. **Rule 6** (duplicates), **Rule 7** (thin), **Rule 8** (bad sources) — cheap heuristics
6. **Rule 10** (named roles), **Rule 9** (regulator coverage)
7. **Rule 4**, then **Rule 5** (contradictions) — hardest, most valuable

**Output:** a per-document report with severity, the exact location, the rule, and the suggested fix. **BLOCK-severity findings prevent publication.** Every check result is audit-logged with the version it ran against.

---

## What this is not

The check does **not** assess whether clinical content is correct, and it must never claim to. It checks completeness, currency, consistency and provenance.

**Clinical correctness comes from the governance pipeline** — MDT review, clinical-lead sign-off — not from software. Keep the language on this precise: it is a **completeness check**, not an approval, and not a compliance guarantee. See `RED-LINES.md`.

---

## Appendix — why the AI must retrieve, never recall

**Evidence, not assertion.** The requirement-theme mapping in `REGULATOR-MAPPING.md` was originally written from model memory. It read fluently and confidently. When it was later checked against the published source texts, **four of the mappings were wrong**:

| Error | Effect if shipped |
|---|---|
| GPhC Pharmacy Principles **1 and 5 swapped** (governance is 1, not 5) | 8 policies citing the wrong principle |
| Professional Standard 7 labelled *"work in partnership"* (that is Standard 2; 7 is confidentiality) | The confidentiality policy citing the wrong standard, and omitting the right one |
| **Duty of candour thresholds taken from Reg 20(8) — the NHS definition** | Every clinic applying the wrong notifiable-incident test. Reg 20(9) applies to non-NHS providers and uses **28-day duration** tests, not "moderate harm" — and catches incidents where harm was **prevented** by treatment |
| Reg 20A | Correct — verified |

**Nothing in the drafted text signalled which of the twenty-four mappings were the wrong ones.** The errors were indistinguishable from the correct entries by reading. They were only found by opening [legislation.gov.uk](https://www.legislation.gov.uk/uksi/2014/2936/part/3/made) and the GPhC standards and checking line by line.

### What this means for the build

- **Ask Clinickly must answer only from retrieved source text, with a citation per statement.** An uncited answer is not a lower-quality answer — it is an answer whose error rate is unknowable, which is worse.
- **A confident tone carries no information about accuracy.** Any UI that renders model output as authoritative without a source link is misleading by construction.
- **Where nothing relevant is retrieved, the honest output is "not in the library" plus a route to request it** — never a generated answer.
- **Regulatory citations are the highest-risk content in the product.** They look verifiable, so nobody checks them. Reference data — statute names, standard numbers, guideline editions — should be a maintained table the system reads from, not something a model produces.

This is already the decision in `CLINICKLY-MASTER.md` ("our AI = grounded, not fine-tuned") and is a P0 in `DEVELOPER-FIX-LIST.md`. This appendix records the measured evidence for it: **a 4-in-24 error rate on exactly the kind of content the tool will be asked to produce.**
