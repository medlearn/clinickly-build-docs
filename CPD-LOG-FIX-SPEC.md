# CPD log and Training page — fix spec

**P0. Supersedes the current Training page behaviour.** Review date 21 Jul 2026.

The CPD hub is one of the two things a pharmacist will actually pay for. As built it is an activity feed, not a revalidation portfolio. Seven of eight log entries are identical, none carry a reflection, and the headline metric is the wrong unit.

**Source of truth:** `CLINICKLY-MASTER.md` §5.8, and the real GPhC forms.

---

## The core problem

**GPhC revalidation counts RECORDS, not minutes.** Minutes were the pre-2018 scheme. The current annual requirement is:

| | |
|---|---|
| **4 × CPD records** | at least **2 planned** |
| **1 × peer discussion** | with a **named peer** |
| **1 × reflective account** | against the year's selected GPhC standards |
| **= 6 records** | |

Everything on this page should be built around that number.

---

## 1. Headline stats — replace entirely

**Currently:** `1/6 Modules completed` · `45 CPD minutes completed ≈ 0.8 h` · `CPD`

**Replace with progress against the GPhC requirement:**

```
YOUR REVALIDATION YEAR                          2 of 6 records

CPD records          ●●○○   2 of 4      (1 planned, 1 unplanned) ⚠ need 2 planned
Peer discussion      ○      0 of 1      ← you have 8 eligible MDT cases
Reflective account   ○      0 of 1
```

**Rules:**

- **Records is the headline number.** Time may appear on an individual record as metadata; it must not be a headline stat.
- **Delete "CPD minutes completed" and "≈ 0.8 h".** They teach the wrong model.
- **Show the gap, not just the total.** "2 of 4, but you need at least 2 planned and have 1" is the useful statement.
- **Show the year boundary.** `[CONFIRM: does the clinician's revalidation year run from their renewal date? It should — take it from profile.]`
- **The "you have 8 eligible MDT cases" prompt is the product.** A clinician one click from their peer discussion is the thing worth paying for.

`Modules completed 1/6` can stay — it is a training metric, not a CPD one. Keep them visually separate so they are not read as the same thing.

---

## 2. Log the right event

**Currently:** every entry reads *"Anonymised case **submitted** for panel discussion"*, logged at submission.

**Submitting a case is not CPD.** Nothing has been learned at the moment of submission. The learning happens when the panel responds.

**Fix:**

| Event | Log it? |
|---|---|
| Case submitted | **No CPD record.** Show in case history only |
| **Panel response received and opened by the submitter** | **Yes — create a DRAFT record** |
| Reflection completed | Record becomes **complete and countable** |

A record with no reflection **does not count toward the 6**. Show it as draft, and chase it.

---

## 3. Record types — map correctly

| Trigger | GPhC record type | Notes |
|---|---|---|
| **MDT case — panel responded** | **Peer discussion** | The responding panel member **is** the named peer |
| Attending an MDT session | **Unplanned learning** | Or peer discussion if the clinician contributed to the discussion — let them choose |
| Training module completed | **Planned learning** | Q1/Q2 pre-fill from the module outline; Q3 is the user's reflection |
| Something learned in a consultation | **Unplanned learning** | User-initiated |
| Year-end reflection | **Reflective account** | Scaffolded against the year's selected GPhC standards |

**"MDT participation" is not a GPhC record type. Remove that label.** Every entry must carry a real record type.

---

## 4. The named peer

GPhC peer discussion requires the peer's **name, role, organisation and contact**.

- The panel member who responded is that peer.
- **Their standing consent to be named must be captured at panel onboarding** — `[CONFIRM: is this in the panel member agreement? If not, add it. Without it we cannot auto-populate the field and the feature does not work.]`
- Pre-fill from the panel member record. The clinician should never have to type it.

---

## 5. What a log entry must show

**Currently:**
```
Anonymised case submitted for panel discussion (C-244)
MDT participation · 15 min · 10 Jul 2026, 15:06
```

**Required:**
```
🗣  Peer discussion — ADHD titration in a patient with hypertension
    Panel: Dr A Rahman, Consultant Psychiatrist, [Trust]
    Case C-244 · responded 11 Jul 2026
    ✅ Reflection complete · counts toward revalidation
```

```
🗣  Peer discussion — [case title]              ⚠ DRAFT
    Panel: [name, role]
    Case C-246 · responded 11 Jul 2026
    ⚠ Add your reflection to make this count        [ Add reflection → ]
```

Every entry carries: **record type** · a **meaningful title** (the clinical topic, not the system event) · the **named peer** where applicable · **complete or draft** · and a **route to finish it**.

---

## 6. Reflection prompts — use the GPhC's own wording

The criteria in every GPhC form reduce to one recurring requirement: **benefit to people using your services, with an example.**

For a peer discussion, the form asks:

> **How did this discussion change or influence your practice for the benefit of people using your services?**

**Pre-save criteria check** — same pattern as the SOP gap-check:

> ⚠️ *No concrete example of patient benefit yet. GPhC assessors look for a specific instance, not a general statement.*

Block nothing; prompt clearly.

---

## 7. Fix the duration

Every MDT entry reads **15 min**. All eight. It is hardcoded.

**Either measure it or remove it.** A fabricated duration on a regulatory record is worse than no duration. Given records are the unit, **removing it is the better answer** — keep time only where genuinely measured, such as a training module.

---

## 8. Case ID ordering — likely a real bug

Observed in the log:

| Case | Submitted |
|---|---|
| C-247 | 9 Jul 2026, **10:18** |
| C-245 | 9 Jul 2026, **10:19** |
| C-246 | 10 Jul 2026, 13:46 |
| C-244 | 10 Jul 2026, 15:06 |

**IDs are not monotonic with submission time.** C-247 was submitted a minute *before* C-245, and both carry higher numbers than cases submitted a day later.

`[CONFIRM: is the ID assigned at insert, or later? This may share a root cause with the round-2 finding that failed cases appear in admin **without IDs** — insert half-succeeds, then ID assignment fails.]`

Whatever the cause, IDs presented to clinicians as case references must be stable and assigned once, at creation.

---

## 9. Test data

`Foundations of independent prescribing · 9 Jul 2026, 02:42` — 2:42am. Part of the existing test-data purge.

---

## 10. Regulator rendering

Spec §5.8: **capture once, render per regulator.** One reflection wizard, four questions, serving both schemes:

1. What did you learn?
2. How has it changed, or how will it change, your practice?
3. **What was the benefit to people using your services — with a real example?**
4. What next? (SMART)

**Export renders as either:**

- **GPhC** — typed records matching the real forms (planned / unplanned / peer discussion / reflective account)
- **GMC** — Academy of Medical Royal Colleges reflective template, with supporting-information category and Good Medical Practice domain tags auto-applied

**Default set by the registration on the clinician's profile.** `[CONFIRM: is there a regulator toggle on this page? I could not see one. If absent, it is missing.]`

**NMC is phase 2.**

---

## Priority

1. **§2** — log the right event, and don't count a record with no reflection *(the correctness fix)*
2. **§3 + §4** — record types and named peer *(the marketable feature — "your peer discussion, done")*
3. **§1** — headline stats in records, not minutes
4. **§5 + §6** — entry display and reflection prompts
5. **§7 + §8 + §9** — duration, ID ordering, test data
6. **§10** — regulator rendering and export

**Acceptance test:** a clinician with 8 MDT cases and 1 completed module should be able to open this page, see they are short of a peer discussion, click once, add a reflection, and have a completed GPhC-shaped peer discussion record in their export. Today they cannot do any of that.
