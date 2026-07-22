# Training catalogue — MEDLRN CPD Diplomas

**Decision (Faheem, 21 Jul 2026): MEDLRN content goes in as-is.** No separate governance re-review before publication. Faheem is the author and clinical lead; the content is already sold and delivered under MEDLRN.

**Replaces the six placeholder modules currently on the Training page.**

---

## The catalogue

Six specialist programmes. **Level 7 benchmark. Built for prescribers.**
*Self-paced eLearning · Live Q&A · Certified on completion.*

| # | Diploma | Covers | Tag |
|---|---|---|---|
| **01** | **ADHD** | Assessment, prescribing, and lifelong management | SPECIALTY |
| **02** | **Mental Health** | Anxiety, depression, and complex presentations | SPECIALTY |
| **03** | **Women's Health** | Hormones, contraception, and perimenopause | SPECIALTY |
| **04** | **TRT** | Diagnosis, prescribing, and patient pathways | SPECIALTY |
| **05** | **Minor Illness** | Acute presentations in primary care | SPECIALTY |
| **06** | **Weight Management** | GLP-1 prescribing and lifestyle interventions | SPECIALTY |

**Provider:** MEDLRN by The Pharmacy Guy · medlrn.com

---

## ⚠️ A diploma is not a module

The current Training page treats everything as a flat list of 30–45 minute modules. **These are Level 7 diplomas — multi-unit programmes ending in certification.** Modelling one as a single "module" breaks two things:

1. **CPD recording.** A clinician who completes Unit 3 of the ADHD diploma has done something worth a CPD record *now*. Waiting until the whole diploma completes to log one record wastes most of the learning and misrepresents when it happened.
2. **Progress.** "Not started / Completed" is useless for a programme with eight units. The clinician needs to see where they are.

### Required structure

```
DIPLOMA  (programme — ADHD, Level 7)
   └── UNIT  (the trainable, completable thing)
          └── completion → CPD record (planned learning) + reflection prompt
   └── UNIT
   └── ...
   └── ALL UNITS COMPLETE → certificate issued
```

| Level | Behaviour |
|---|---|
| **Diploma** | Has a title, description, level, unit count, overall progress (`3 of 8 units`), and a certificate on completion |
| **Unit** | Has content (video + text + optional quiz), a duration, and **generates its own CPD record on completion** |

**Each unit completion = one planned learning record.** Q1/Q2 pre-fill from the unit outline; Q3 (benefit to service users, with an example) is the clinician's own reflection. See `CPD-LOG-FIX-SPEC.md` §3.

`[CONFIRM: unit list for each diploma. Faheem to supply — the ADHD diploma has units already defined; the others need their unit breakdown before they can be loaded.]`

---

## Access and pricing

> `[CONFIRM: this is a commercial decision and it blocks the build.]`

These are **paid programmes sold by MEDLRN**. Putting them inside Clinickly's Training tab needs a model:

| Option | |
|---|---|
| **(a) Included** | Diplomas bundled into the Clinickly subscription. Simplest experience; gives away existing MEDLRN revenue |
| **(b) Separate purchase** | Diplomas visible in Clinickly, purchased separately. Training tab shows locked/unlocked state and a route to buy |
| **(c) Tiered** | A sample unit free to all Clinickly users; full diploma paid. Strongest conversion path |
| **(d) Cross-credit** | Existing MEDLRN diploma holders get their completions recognised in Clinickly's CPD log |

**Recommendation: (c), with (d).** A free first unit turns the Training tab into a shop window for MEDLRN rather than a list of things the user cannot open — and existing MEDLRN customers should not lose credit for work already done.

`[CONFIRM: how a Clinickly account is matched to an existing MEDLRN account for (d).]`

---

## Delivery

**Embed, do not link out.** Video hosted on **Bunny**, embedded in the unit. Text and optional quiz alongside.

A module that links out to MEDLRN or YouTube loses completion tracking, which loses the reflection prompt, which loses the CPD record — the entire reason the page exists.

`[CONFIRM: are the MEDLRN videos already on Bunny, or do they need migrating from their current host?]`

**Live Q&A** is part of the MEDLRN offer and has no equivalent in Clinickly today. `[CONFIRM: is live Q&A in scope for the Clinickly delivery, or does it stay on MEDLRN? If in scope, attendance should generate an **unplanned learning** or **peer discussion** record — see CPD-LOG-FIX-SPEC.md §4.]`

---

## Retain alongside the diplomas

The placeholder modules currently shown include some that are **not** MEDLRN diplomas but are still needed:

| Module | Keep? |
|---|---|
| Documentation that stands up to inspection | **Keep** — CORE. Directly supports the policy library and the governance product |
| Recognising the deteriorating patient | **Keep** — SAFETY |
| Reflective practice & revalidation | **Keep** — PROFESSIONAL. Needed to make the CPD hub usable |
| Foundations of independent prescribing | **Keep** — CORE |
| Rosacea & common facial dermatoses | `[CONFIRM: is this MEDLRN content or a placeholder? Not in the diploma catalogue]` |
| ADHD in pharmacist-led clinics | **Replace** — superseded by the ADHD diploma |

`[CONFIRM: the CORE / SAFETY / PROFESSIONAL modules above have no content behind them either. Are these to be built, or removed until they exist? A visible module that opens to nothing is worse than an absent one.]`

---

## Governance note

Per the decision above, MEDLRN content is published as-is.

**Two things still apply:**

1. **Version and date every unit.** Clinical content ages — the corpus review found guidance up to twelve years out of date. Each unit carries an issue date and a review date, and the Training page flags overdue ones to the admin. `[CONFIRM: review cycle. Recommend annual for prescribing content.]`
2. **The CPD record belongs to the clinician, not to us.** A record documents *their* learning and reflection. That is true regardless of who authored the content, so the as-is decision does not weaken the CPD side.

Where a unit is later found to be wrong, it is withdrawn under the same rule as a policy — removed from circulation, and anyone who completed it is told. See `C029 Document Control` Part One.
