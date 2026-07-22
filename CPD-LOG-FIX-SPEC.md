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
- **The prompt should reflect real eligibility.** "You have 8 MDT cases — 2 can become a peer discussion" (i.e. only those where the panel member consented to be named). Do not count cases that cannot produce the record.

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
| **MDT case — panel responded** | **Peer discussion** *where the panel member consented to be named* — otherwise **unplanned learning**. See §4 | Consent is **not** automatic |
| Attending an MDT session | **Unplanned learning** | Or peer discussion if the clinician contributed to the discussion — let them choose |
| Training module completed | **Planned learning** | Q1/Q2 pre-fill from the module outline; Q3 is the user's reflection |
| Something learned in a consultation | **Unplanned learning** | User-initiated |
| Year-end reflection | **Reflective account** | Scaffolded against the year's selected GPhC standards |

**"MDT participation" is not a GPhC record type. Remove that label.** Every entry must carry a real record type.

---

## 4. The named peer — panel members do NOT consent by default

**Decision (Faheem, 21 Jul 2026): panel members do not automatically agree to be named.** This is reasonable — being named in another clinician's revalidation portfolio attaches your name to a clinical opinion you gave, and a panel member should control that.

It has a hard consequence:

> **The GPhC peer discussion form requires the peer's name, role, organisation and contact.** No name means **no peer discussion record**. The system must not produce one anyway with the peer field blank or anonymised — that is an invalid record, and it fails at exactly the moment it matters, when GPhC calls it in for review.

### How it works instead

**The panel member decides, and the default is NO.**

| Setting | Where | Default |
|---|---|---|
| **Standing preference** — "I am willing to be named as a peer for CPD purposes" | Panel member profile | **OFF** |
| **Per-response override** | On the response form, when they answer a case | Inherits the standing preference; can be changed either way for that case |

The per-response control needs to say plainly what it means:

> ☐ **Allow this clinician to name me in their CPD record**
> They can record this as a GPhC peer discussion, which means your name, role and organisation appear in their revalidation portfolio. It is not published, and GPhC may contact you if they review it.
> *You can decline without giving a reason, and it will not be shown to them as a refusal.*

**The clinician is never told the panel member declined.** They see what the record can be, not what was withheld. A visible "declined" would create pressure on panel members and awkwardness between colleagues.

### What the clinician gets in each case

| Peer consented | Record type | Counts toward |
|---|---|---|
| **Yes** | **Peer discussion** — peer pre-filled from the panel record | The 1 peer discussion required annually |
| **No** | **Unplanned learning** — no peer field required | One of the 4 CPD records |

**Both are genuine, countable GPhC records.** An MDT case is never wasted — it just lands in a different box.

### Group discussions — GPhC says "name one"

The GPhC peer discussion form asks for the peer's name, role, organisation and contact — **and where the discussion was with a group, it requires only that you name one of them.**

This materially lowers the bar:

- **A single panel member responds to a case** → that member is the peer, if they consented
- **An MDT session or a multi-member panel response** → the clinician names **one** consenting member. Everyone else can remain unnamed

**So the feature does not need broad opt-in. It needs at least one consenting member per session or per response.**

Build accordingly:

- Where more than one panel member was involved, present the clinician with the **consenting** members and let them choose one
- Where **none** consented, the record becomes unplanned learning as above
- Never surface the non-consenting members as a list of people who said no — show only who is available to name

`[CONFIRM: how "one per session" is tracked where a panel rotates. The record needs the peer who was actually part of that discussion, not simply any consenting panel member.]`

### What this changes commercially

The claim **"your peer discussion, done"** can no longer be made unconditionally. Do not market it that way.

**What can be said honestly:** *every MDT case becomes a CPD record automatically, and where the panel member agrees to be named, it becomes your peer discussion.*

`[CONFIRM: whether to ask panel members to opt in at onboarding — explained properly, with the reasons — and to report the opt-in rate. If uptake is very low, the peer-discussion route is not a feature we can rely on, and the honest response is to build a separate peer-discussion pathway rather than to lean on the MDT one.]`

`[CONFIRM: an alternative worth considering — allow a clinician to request naming after the fact. The panel member receives a request, and can say yes or ignore it. Ignoring is a silent no.]`

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

**Acceptance test:** a clinician with 8 MDT cases and 1 completed module opens this page and sees:
- how many of the 6 required records they hold
- that their MDT cases have become **CPD records** (unplanned learning) automatically
- **which of them can become a peer discussion** — only those where the panel member consented to be named
- a one-click route to add the reflection that makes each one count

Today none of that is possible. **And the system must never generate a peer discussion record without a real named peer** — an invalid record is worse than a missing one, because it fails at the point GPhC reviews it.
