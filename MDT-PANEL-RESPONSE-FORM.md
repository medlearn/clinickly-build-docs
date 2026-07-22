# MDT panel response form — build spec

**P0. Replaces the free-text response box.** 21 Jul 2026.
**Companion to [MDT-CASE-FORMAT.md](MDT-CASE-FORMAT.md) and [MDT-CASE-SUBMISSION-SPEC.md](MDT-CASE-SUBMISSION-SPEC.md).**

---

## Why

**This is the side where the breach happened.** Case C-241: a dermatologist typed *"Consistent with rosacea."* into a free box, and nothing stopped her.

**And the other responses are not much better:**

| Live response | Problem |
|---|---|
| *"Consistent with rosacea."* | **Diagnosis on a live patient** |
| *"Agree with the documented triage & plan"* ×2 | **Agreement is not teaching.** Teaches nothing, evidences nothing |
| *"Chair oversight note."* | Not a clinical response at all |
| *"djdjdjjsddjfhdfhndhdjdjdjjssjssjssjsdsss"* ×2 | Test data attributed to named panel members |

**Two design rules follow:**

> **1. Answer the clinician's reasoning, not the patient's problem.**
> **2. Agreement alone is not a response.** If the reasoning was sound, say what was sound and why — that is still teaching.

---

## The form

**The response mirrors the submission.** The clinician gave differentials with reasoning, a working diagnosis, a rationale and a management plan. The panel responds to each. That structure alone prevents *"consistent with rosacea"* — there is nowhere to type it.

**Field names matter.** No field on this form is called *diagnosis*, *assessment*, *plan* or *recommendation*. Field names shape what people write.

---

### 1 · The differential

| Field | Required | Input |
|---|---|---|
| **Was the differential appropriate?** | ✅ | `Comprehensive` · `Reasonable` · `Too narrow` · `Included something unlikely` |
| **What would you have added, and why?** | Conditional — required if *too narrow* | Free text |
| **What would you have weighted differently?** | Optional | Free text |

### 2 · The reasoning

| Field | Required | Input |
|---|---|---|
| **Was the rationale sound?** | ✅ | `Sound` · `Sound but under-weighted something` · `A step was missed` · `I'd have reasoned differently` |
| **Say more** | ✅ **Always required** | Free text — **this is the field that carries the teaching, whatever was selected above** |

> ⚠️ **"Sound" does not skip the free text.** *"Your reasoning was sound — particularly that you screened for X before Y, which is the step most people miss"* is more useful than a tick, and it is what makes agreement into teaching.

### 3 · The management

| Field | Required | Input |
|---|---|---|
| **Was the approach reasonable?** | ✅ | `Reasonable` · `Reasonable, with additions` · `I'd have done something different` |
| **What would you have considered additionally?** | Conditional | Free text |
| **Was the safety-netting adequate?** | ✅ | `Yes` · `Would strengthen it` · `Not stated` |

### 4 · Where they referred

*Shown only where the case included a referral (case format §2d).*

| Field | Required |
|---|---|
| **Was referral the right call?** | ✅ `Yes` · `Could reasonably have been managed in-house` · `Should have been more urgent` · `Should have been less urgent` |
| **On their counterfactual — if they couldn't have referred, was their plan sound?** | ✅ Free text |

> This is where the most valuable teaching usually is. **A clinician who referred appropriately still benefits from knowing what they'd have done otherwise was reasonable** — or wasn't.

### 5 · Teaching points

| Field | Required | Notes |
|---|---|---|
| **The transferable learning point** | ✅ | **What generalises beyond this case.** The single most important field on the form |
| **What to read** | Optional | Guideline, reference, or `[CONFIRM: link to the governed Guidelines library where the topic exists]` |
| **Common pitfall this illustrates** | Optional | Feeds the Session library and future teaching slots |

### 6 · Response to their learning question

| Field | Required |
|---|---|
| **Their question** | Displayed, read-only |
| **Your answer** | ✅ |

---

## 🔴 7 · Safety escalation — currently missing

> **What happens when a panel member reads a closed case and thinks the patient may have come to harm?**
>
> Today they would have to write it into the teaching box, where it becomes a discussion point rather than an action. **That is a gap, and it is the kind of gap that matters.**

**Separate, always visible, never buried in free text:**

> ⚠️ **Raise a concern about this case**
> ☐ I am concerned this patient may have come to harm
> ☐ I am concerned about a pattern in this clinician's practice
> ☐ I have a safeguarding concern
> ☐ I am concerned this was outside the clinician's scope or competence

**On any of these:**

| Step | |
|---|---|
| Routed to `[CONFIRM: named clinical lead / governance chair]` | **Not to the submitting clinician in the first instance** |
| Reviewed within `[CONFIRM: default 2 working days]` | |
| **The submitting clinician is told**, supportively, and is the one who acts | They hold the patient relationship. **We do not contact a patient we have no relationship with, on a case we have seen anonymised** |
| Considered by the clinic against **C017** (incident), **C021** (duty of candour), **C08/C032** (safeguarding) | Their duties, not ours |
| Logged in the governance record | |

> **The panel does not manage the patient. It flags to the clinician, who does.** That distinction keeps the escalation inside the education model rather than turning the MDT into a clinical service — and it is also the honest position, since the panel has only ever seen an anonymised summary.

`[CONFIRM: where a concern is about the clinician rather than the case — repeated poor practice, or working beyond competence — the route must be to the governance lead and must not be visible to the clinician as a "flag on your case". That is a fitness-to-practise-adjacent conversation, not a teaching one.]`

---

## Making it quick to complete

**Panel members are volunteers or paid sessionally. A form that takes 40 minutes will not get completed.**

| | |
|---|---|
| **Chips, not prose, for the assessments** | Sections 1–4 are one tap each. Free text only where it adds something |
| **Target: 5–10 minutes** | Show it: *"Most responses take about 8 minutes"* |
| **Save as draft** | Automatically |
| **Snippet library** | Common teaching points reusable across cases. `[CONFIRM: per-member or shared? Shared is better — it builds a house teaching style, and new panel members learn from it]` |
| **Prefilled context** | The case summary and their differential table sit alongside the form, not on a previous screen |
| **Mobile-usable** | Panel members will answer on a phone |

---

## Soft check on the way out

Same pattern as the submission side. Flag before submit:

| Pattern | Prompt |
|---|---|
| "this is…" · "consistent with…" · "the diagnosis is…" | ⚠️ *That reads as a diagnosis. The MDT reviews reasoning on closed cases — try commenting on how they reached theirs* |
| "I would prescribe…" · "start them on…" · "give them…" | ⚠️ *That reads as a treatment instruction. Try "the usual approach here is…" or "worth considering…"* |
| Response under `[CONFIRM: ~40 words]` with no free text beyond an agreement chip | ⚠️ *Agreement on its own doesn't teach. What was done well, and why?* |

**Warn, don't block.** Log overrides for admin review.

---

## Admin and quality

| | |
|---|---|
| **Response SLA** | `[CONFIRM: default 5 working days]`, visible to the panel member and tracked in admin |
| **Reassignment** | Unanswered past SLA → reassign to another member of the same specialty, and tell the clinician it is being reassigned |
| **Response quality review** | `[CONFIRM: who samples panel responses, and how often. A response that only says "agree" is a training need for that panel member, not a fault in the clinician]` |
| **Sign-off** | Per §4B — `[CONFIRM: are panel responses signed off before release to the clinician, or released directly? Risk-tiered separation of duties suggests high-risk cases need a second reviewer]` |
| **Attribution** | Every response carries the responder's **name, role and organisation** — required both for accountability and for the GPhC peer discussion record (see [CPD-LOG-FIX-SPEC.md](CPD-LOG-FIX-SPEC.md) §4) |

---

## What stays

The per-response footer is correct and should remain verbatim:

> *Teaching/discussion points — advisory only. The treating clinician remains responsible for the decision.*

**But it is now true rather than aspirational.** With this form there is no field in which a panel member can write a directive — and that, not the footer, is what makes the statement accurate.

---

**Acceptance test:** a panel member cannot submit *"Consistent with rosacea."* A panel member cannot submit *"Agree with the documented triage & plan"* and nothing else. A panel member who believes a patient came to harm has a route that is not the teaching box. And a complete response takes under ten minutes.
