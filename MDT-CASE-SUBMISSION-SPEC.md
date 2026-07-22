# MDT case submission and response — build spec

**P0. Replaces the current free-text submission and response forms.** 21 Jul 2026.

Triggered by case **C-241**: question *"Is this rosacea?"*, panel response *"Consistent with rosacea."* That is patient-specific diagnosis, and it is the activity `RED-LINES.md` exists to prevent.

**The disclaimer did not stop it, because a disclaimer cannot.** The fix is structural.

---

## The principle

> **The case must be closed before it is submitted, and the clinician must have already decided.**

Everything below follows from that one line.

| | |
|---|---|
| *"Is this rosacea?"* | The encounter is **open**. The clinician has not decided. Whatever the panel says **influences the management of a live patient** — the MHRA's own trigger wording. **This is device territory** |
| *"I thought it was rosacea and treated it as such — was my reasoning sound?"* | The encounter is **closed**. The decision was made and acted on. Nothing the panel says can change what happened to that patient. **This is education** |

The distinction is not tone or phrasing. **It is whether the patient's care is still in play.** That is enforceable in a form, and it should not depend on clinicians remembering a rule.

---

## 1. Submission — structured, not free text

Replace the single "Question" box.

| Field | Required | Notes |
|---|---|---|
| **Has this episode concluded?** | ✅ **Gate** | If **no**, submission is blocked. See §2 |
| Context / specialty | ✅ | Drives routing — see §5 |
| Age **band** | ✅ | Band only. Never a precise age |
| Presentation | ✅ | Anonymised |
| **Clerking proforma** | ✅ **Mandatory** | **Superseded by [MDT-CASE-FORMAT.md](MDT-CASE-FORMAT.md)** — a structured clerking with mandatory **Differentials (min 2) · Working diagnosis · Rationale · Management**. Does the same boundary work in clinically native language |
| Learning question | ✅ | Constrained — see §3 |
| Image | Optional | See §6 |

### Why the clerking does the work

**A clinician who must record differentials, a working diagnosis, a rationale and what they actually did cannot be asking the panel to make the call — they have already made it.**

It also makes an open case impossible to submit: *Management* cannot be completed if nothing has been done yet. The gate and the proforma reinforce each other, and neither relies on good intentions.

**Minimum two differentials is the boundary.** A clinician who has generated a differential has done the reasoning; one who has not is asking the panel to do it.

**This is the single most important change across both specs.** Everything else is supporting work. See **[MDT-CASE-FORMAT.md](MDT-CASE-FORMAT.md)** for the full field list.

---

## 2. The blocked path

Where **"Has this episode concluded?" = No**:

> **This case isn't ready for the MDT.**
>
> The MDT is case-based education — we discuss decisions that have already been made, so the discussion can't affect a patient's care.
>
> **If you need help with a patient right now**, that's a clinical decision for you, using your own judgement, your usual escalation route, or a referral.
>
> **Come back once the episode is concluded** — that's when the learning is most useful anyway.

**Never soften this into "are you sure?".** It is not a confirmation step, it is a boundary.

`[CONFIRM: whether the clinic wants a "save as draft" so the clinician can return once the episode closes. Recommended — it keeps the case rather than losing it.]`

---

## 3. The learning question

**Offer prompts. Free text is the fallback, not the default.**

✅ **Suggested prompts:**

- *Was my reasoning sound?*
- *What would you have considered that I didn't?*
- *Would you have managed this differently, and why?*
- *What's the learning point for next time?*
- *What should I read on this?*

⚠️ **Soft check on free text.** Flag patterns that seek a decision rather than a review:

| Pattern | |
|---|---|
| "is this…" / "what is this…" | Seeking a diagnosis |
| "what should I do" / "what would you do" *(present tense)* | Seeking a management decision |
| "can you diagnose" / "please advise on this patient" | Explicit |
| "not sure what to do next" | Open case — **currently present in C-248** |

> ⚠️ **That reads like you're asking us to decide.**
> The MDT reviews reasoning on cases that are already closed. Try: *"I thought it was X and did Y — was that reasonable?"*
> `[ Rewrite ]`  `[ Submit anyway ]`

**Warn, don't hard-block.** A hard block teaches nothing and gets worked around. A warning with a rewrite teaches the norm, and the "submit anyway" is logged and reviewable by admin.

---

## 4. The panel response form

**Superseded by [MDT-PANEL-RESPONSE-FORM.md](MDT-PANEL-RESPONSE-FORM.md).**

The response mirrors the submission — the panel responds to the clinician's differential, reasoning, management and referral, section by section. Two rules carry it:

> **Answer the clinician's reasoning, not the patient's problem.**
> **Agreement alone is not a response.**

It also adds the missing **safety escalation route** (§7 of that spec) for a panel member who reads a closed case and believes the patient may have come to harm.

---

## 5. Routing

Currently broken — see fix list X12–X14.

- **Governance and Clinical panels must never cross.** A governance/ethics chair cannot answer a clinical case (§4B separation of duties). Enforce at assignment, not by convention
- **Route by specialty to a member who holds that specialty.** A dermatologist must not receive an ADHD case
- **Every selectable specialty must have at least one active member behind it.** Where it does not, remove the option rather than accept a case nobody can answer
- `[CONFIRM: does the service accept under-18 cases? If yes, a paediatric-competent member is required. If no, block at submission — two paediatric cases are currently sitting with adult panels]`

---

## 6. Images

**Dermatology is not workable without images.** The controls below make them possible.

### Consent — attestation, never upload

> ⚠️ **The clinician must not upload the signed consent form.** It carries the patient's **name and signature**. Uploading it puts a direct identifier into the case system — the opposite of what it is meant to prove — and exposes it to every panel member who opens the case.

**Attestation instead:**

> ☑ **I hold written consent from this patient** for this image to be used for anonymised professional education. The signed consent form is retained in the patient's clinical record.

Logged with the clinician's name, role, registration number, timestamp and case ID. **Auditable, and the responsibility sits with the clinician** — which is correct, because they are the one with the patient relationship.

`[CLINIC NAME]` provides the consent form: **[F05 Consent for Clinical Photography and Educational Use](starters/forms/F05-photography-consent.md)**.

### Technical controls — the platform's job

Consent does not make an image anonymous. Regardless of consent:

| Control | Behaviour |
|---|---|
| **Strip EXIF on upload** | **Mandatory, silent, server-side.** Phone images carry device ID, timestamp and frequently **GPS coordinates of the patient's home**. The clinician will not know this and cannot be asked to handle it |
| **Face detection** | **Block the upload.** A face is not anonymisable, with or without consent |
| **In-frame identifier warning** | Prompt before submit: tattoos · jewellery · name bands · documents or screens in shot · another person · distinctive scars |
| **Crop tool** | Provided, and the clinician confirms they have reviewed the frame |
| **Site guidance** | A lesion on a forearm is far less identifiable than one on a face or a distinctive tattoo. Prompt accordingly |

### Storage and withdrawal

- `[CONFIRM: retention period for case images. Recommend the shortest that supports the teaching purpose — images should not persist for the life of the case archive by default]`
- **Consent can be withdrawn.** Under C05 §14 withdrawal must be honoured, which means **images must be findable and deletable per patient** — even though the case is anonymised. `[CONFIRM: how. The clinician who submitted it holds the link between patient and case; a withdrawal route through them is the only workable design]`
- Images are never downloadable by panel members. Display only, watermarked with the case ID
- Images are excluded from any export, session recording or published library material unless separately consented

`[CONFIRM: whether images may appear in the published Session library. Default: NO. Teaching-library use is a broader consent than case-discussion use, and F05 treats them separately.]`

---

## 7. What this does not change

The framing already on the page is correct and should be kept verbatim:

- *"Submit and track anonymised cases — case-based education, not advice on a live patient"*
- *"Anonymised cases only — age range, presentation and your clinical question. Never include names, dates of birth, addresses or identifiers."*
- *"Teaching/discussion points — advisory only. The treating clinician reviews, decides and remains responsible."*

**The framing was never the problem.** The problem is that nothing in the form made the framing true. This spec makes the structure enforce what the words already claim.

---

## Build order

1. **§1 two mandatory fields + §2 the gate** — the whole boundary rests on these
2. **§4 panel response structure** — the breach happened on this side
3. **§5 routing** — governance/clinical separation first
4. **§3 prompts and soft checks**
5. **§6 images** — EXIF stripping and face detection before anything else here goes live

**Acceptance test:** a clinician cannot submit *"Is this rosacea?"* about an open case, and a panel member cannot answer *"Consistent with rosacea."* Today both are possible, and both happened.
