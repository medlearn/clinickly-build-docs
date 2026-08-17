# Proportionate credentialing — panel members

**The current Credentialing screen is built for the wrong risk level.** It applies a locum-deployment capability framework (population scope, risk scope, qualification route, coded licence status) to people who **comment on anonymised, already-concluded teaching cases.** They are not treating patients, prescribing, or accessing identifiable records. The vetting should be proportionate to that.

**Principle:** a panel member needs to be a *real, registered, insured, safe clinician in their field, who has agreed to keep cases confidential.* That is the whole risk. Everything beyond it is machinery.

---

## Keep — the required core set (8)

A member becomes **active only when all 8 are verified and none expired.**

| Check | Confirms | Evidence | Expiry |
|---|---|---|---|
| **Identity** | Who they are | Photo ID sighted | — |
| **Professional registration** | On the live GMC/GPhC/NMC register, in good standing | Live register check (below) | ✔ follows registration |
| **Professional indemnity** | Insurance covering advisory/MDT work | Certificate | ✔ |
| **Fitness to practise** | No relevant restrictions or open FtP concerns | Register check + self-declaration | ✔ annual |
| **Qualifications** | Qualified in their stated specialty | Certificate(s) sighted | — |
| **Two references** | Professional standing | Confirmed with referees | — |
| **Confidentiality + data-processing agreement** | They'll keep cases confidential (GDPR) | Signed | ✔ on terms change |
| **Right to work** | Legally allowed (if paid) | Standard check | ✔ |

Each item records only: **verified (yes/no) · date seen · expiry (where it applies).** Nothing else.

---

## Optional / risk-based (offer, don't require)

| Check | When |
|---|---|
| **Basic DBS** | Optional probity check. No enhanced DBS — panel members have no patient contact and no regulated activity, so enhanced is not warranted |
| **CV** | A supporting attachment, not a formal credential — it's covered by qualifications + references |

---

## Drop for panel members (these are employee-grade)

Justify against the actual role, not a generic HR template:

| Currently required | Why it doesn't apply to a panel member |
|---|---|
| **Complete employment history + gap review** | Employee onboarding. Registration + references already establish accountability |
| **Induction before independent work** | Replace with a lightweight one-time **onboarding acknowledgement** — they've read the anonymisation rules and the "teaching, not advice" boundary. Not a tracked credential |
| **Role and service competence assessed** | Their registration + specialty qualification *is* the competence signal. A separate assessment is for employees delivering a service |
| **Annual appraisal + revalidation (as a tracked item)** | The clinician's own duty. Capture "revalidation in good standing" inside the register check, not as a separate credential to chase |
| **Contract (as distinct from the confidentiality agreement)** | Fold into the one confidentiality + data-processing + terms agreement |

This takes ~14 tracked credentials down to **8 required + 2 optional.**

---

## Replace the coded register block with a plain-language one

The "Direct register checks" block is right in intent (verify against the live register) but drowns in jargon. Reduce to:

| Field | |
|---|---|
| Register | GMC / GPhC / NMC |
| Registration number | |
| Checked on | date |
| Status | **Current** / not current |
| Restrictions | **None** / present → describe |
| Next check due | auto = 12 months, or before expiry |

**Remove:** licence status code · scope code · "evidence issuer route" · "qualification route" · a supplied certificate as a substitute for the live check. Keep the attestation *"I checked the live register on this date."*

---

## Remove entirely — the capability-claims framework

The whole **"Controlled capability claims"** section:

`capability · qualification route · exact clean evidence version · evidence issuer route · issuer safe name · reference suffix · population scope · risk scope · restriction · valid until · dual next-check`

**Delete it.** It scopes a clinician for **live-patient deployment across populations and risk tiers** — a problem this product does not have. A panel member has **one specialty**, confirmed by their qualification, used for routing. Nothing more.

**This also fixes PM-R5** (identity split / no single source of truth): the member's **specialty = their credentialed specialty, one field**, and routing derives from it. No separate "display specialty" that can drift from a "capability."

---

## Keep the good governance already built

- **Expiry dates + renewal reminders** (the PM7 fix).
- **Activation gated on the required set** (the PM8 fix): member is active only when all 8 required are verified and unexpired; **auto-suspend if any required item expires.**
- **Audit log** of who verified what, when — as a simple log, not a prominent "immutable timeline" panel.
- **Privacy:** sensitive evidence and health detail not exposed; suspension messages don't leak DBS/health.

---

## The one-line target for the developer

**8 required checks, each = verified + date + expiry; one plain-language register check; one specialty field that drives routing; activation auto-gated on the required set.** Delete the capability-scoping framework and the coded register fields — they solve a live-deployment risk this teaching-CPD product doesn't carry.
