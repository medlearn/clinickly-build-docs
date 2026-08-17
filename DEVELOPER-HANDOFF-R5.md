# Clinickly — Round 5 developer hand-off

**From:** Faheem Ahmed (clinical lead / product owner)
**Date:** 17 Aug 2026
**Scope:** Full round-5 review of the connected-AI build — every clinician, panel and admin screen.

**The good news first:** the structural work has landed. Both device-boundary P0s are fixed, the MDT case breach is fixed at the design level, and the credentialing root cause is closed. **Nothing below is a new device-boundary breach.** What's left is mostly (a) scrub test/synthetic data, (b) fix one timestamp defect, (c) finish a few setup steps, (d) two relabels.

Please work the **five workstreams** below — they group the 17 items by root cause, which is faster than fixing them one screen at a time. Full per-item detail and acceptance criteria follow the summary table.

---

## The 17 items at a glance

| P | ID | Screen | One-line fix |
|---|----|--------|--------------|
| P1 | AO-R1 | Overview / case queue | Close/archive test & legacy cases that are still assignable (ddd C-245, E2E C-238, rosacea C-241) |
| P1 | AO-R2 | Overview / MDT | Submit form offers specialties with no vetted panel member — add members or stop offering those specialties |
| P1 | GS-R1 | Governance sign-off | 28 policies "signed 21 Jul 01:00" in one minute — real timestamps OR relabel as bulk *source approval* |
| P1 | GS-R2 | Governance sign-off | "signed by" is blank — record and show the signer's name |
| P1 | SO-R1 | Safety operations | Assign a real named Primary + Deputy for the 3 safety routes |
| P1 | IMG-R2 | Image operations | Confirm a DPIA covers image storage, retention clock, consent-withdrawal deletion |
| P1 | CL-R2 | Content libraries | Ingest licensed reference sources — unblocks the empty Guidelines + grounded content |
| P1 | UC-R1 | Users & clinics | Purge test-data pollution; confirm no real personal Gmail is in demo data (DP risk) |
| P1 | RA-R1 | Reports & audit | Fix negative "−8.1 d draft → published" — same timestamp defect as GS-R1 |
| P2 | PM-R1 | Panel management | Remove duplicate Newman record (Dr N. Newman inactive + N. Newman active) |
| P2 | PM-R2 | Panel management | Hide "SYNTHETIC Expired Panel" test fixture from the live member list |
| P2 | IMG-R1 | Image operations | Wire/approve the 5 blocked image production components |
| P2 | UC-R2 | Users & clinics | Make a synthetic ADMIN/countersigner account impossible in a production tenant |
| P2 | RA-R2 | Reports & audit | "0 h first response" is a same-minute test artefact — resolves with clean data |
| P3 | MDT-R1 | MDT schedule | Prefill create-session date from the recurring rule, not today |
| P3 | CL-R1 | Content libraries | Relabel "published" — distinguish central-library from adopted-live-in-clinic |
| P3 | RA-R3 | Reports & audit | "No clinician accounts yet" contradicts audit history — resolves with UC-R1 scrub |

---

## Workstream A — Fix the timestamp model (closes GS-R1, GS-R2, RA-R1)

**This is the highest-value fix — it makes the evidence layer trustworthy.** Three symptoms, one cause: governance and audit records carry bulk-load timestamps instead of real event times.

- **GS-R1** — all 28 policies show `v1 · signed … 21 Jul 2026, 01:00` — identical minute. Reads as a rubber-stamp. Either (a) stamp each with its real approval time, or (b) relabel the action honestly: these are **approved starter *sources*** (a legitimate bulk approval), not individual clinic clinical sign-offs — so call it "source approved", not "signed".
- **GS-R2** — every row reads `signed by · …` with **no name**. An audit trail exists to record *who*. Show `signed by Faheem Ahmed`.
- **RA-R1** — Reports & audit → Governance health shows **`−8.1 d avg days draft → published`**. A negative lead time = published *before* drafted. Same bulk-timestamp cause.

**Done when:** no sign-off shares an identical bulk timestamp with an unrelated document; every sign-off names a signer; draft→published lead time is ≥ 0 for every item.

---

## Workstream B — Scrub test/synthetic data before launch (AO-R1, PM-R1, PM-R2, UC-R1, UC-R2, RA-R2, RA-R3)

Demo/test fixtures are leaking into live-looking views. Establish one rule: **synthetic data is either clearly labelled `SYNTHETIC` or removed — never sitting unlabelled next to real data, and never carrying a real person's contact details.**

- **UC-R1** *(DP-sensitive — do this carefully)* — the Users list mixes garbled machine-name accounts with **real-looking personal Gmail addresses**: `i.ber.af.i.r.ura.761@gmail.com`, `d.ot.og.oxira.0.3@gmail.com`, and **`drfiza33@gmail.com` on an account named "Faheem"**. Confirm none is a real person's address; if any is real, it must be removed (data-protection issue). Purge/quarantine the junk accounts.
- **UC-R2** — `SYNTHETIC Credential Countersigner` holds **Admin · Clinical lead**. A test admin with countersigning rights must be structurally impossible to exist in a production tenant. Add a guard.
- **AO-R1** — test/legacy cases (`ddd` C-245, `Case-loop E2E two` C-238, `Rash photo case` C-241) are still **assignable** in the admin queue. They should be closed/archived, not assignable. (C-241 is the rosacea case — already quarantined on the panel side; apply the same on the admin side.)
- **PM-R1** — duplicate Newman: `Dr N. Newman` (inactive) + `N. Newman` (active). Remove the stale record.
- **PM-R2** — `SYNTHETIC Expired Panel` fixture is visible in the live panel list. Hide test fixtures from live views.
- **RA-R2 / RA-R3** — both resolve once the above is done: the "0 h first response" SLA (test cases submitted+answered in the same minute) and "No clinician accounts yet" (only clinician is a deactivated synthetic) both go away with clean data.

**Done when:** no unlabelled synthetic account, case, or panel member appears in any live view; no real personal email exists in demo data; a production tenant cannot contain a synthetic admin.

---

## Workstream C — Ingest licensed reference sources (CL-R2)

- The **Guidelines library is empty** and grounded content is "Preview only" because **no licensed source has completed ingestion** (Content libraries → Licensed source workspace = 0 governed sources). This is the single dependency behind several "Preview only" states across the app.
- Run the licensed-source ingestion path (immutable snapshot → licence validation → human approval) for the clinical sources (e.g. BNF / NICE) so retrieval can activate.

**Done when:** at least the core clinical sources show as governed/approved, Ask Clinickly answers cite live governed entries, and Guidelines is no longer empty.

---

## Workstream D — Finish setup/config (SO-R1, IMG-R1, IMG-R2, AO-R2)

These are honest "Action required / Blocked" states the UI already flags — they need real configuration, not code.

- **SO-R1** — Safety operations: assign a real named **Primary + Deputy** for each of the 3 concern routes (clinical safety / governance / safeguarding). Until then a raised concern has nowhere to land.
- **IMG-R1** — Image operations: wire and approve the 5 blocked production components (private storage adapter, privacy detector, view-grant keyring, alert seam, production activation).
- **IMG-R2** — confirm a **DPIA** covers clinical-image storage, the retention clock, and the consent-withdrawal deletion path before enabling real image handling.
- **AO-R2** — coverage gap: the case-submit form offers clinical areas (e.g. *General & acute prescribing*, *Other*) that have **no vetted panel member**, so those cases can't be answered. Either add members for those specialties or remove them from the submit form.

**Done when:** no safety route reads "Action required"; image handling stays blocked until its 5 components + DPIA are in place; every specialty the submit form offers has at least one eligible panel member.

---

## Workstream E — Two relabels (CL-R1, MDT-R1) — cosmetic

- **CL-R1** — "published" means two different things and they collide on screen: pipeline rows say `PUBLISHED` (in the central master library) while the card/badge says `0 current published / Not adopted` (live in this clinic). Relabel to distinguish them, e.g. **"In library"** vs **"Adopted / live here"**.
- **MDT-R1** — the Create-session form defaults Starts/Ends to **today** rather than the next scheduled session (25 Aug, 19:00). Prefill from the recurring rule.

---

## Verify before launch (not bugs — confirm these hold on the live path)

These are the device-boundary guarantees. They looked correct in review, but the live AI path wasn't exercised (it fell back every time), so please confirm:

1. **Consultation Assessment stays clinician-owned.** When the live AI drafts a note, the Assessment/impression must remain the clinician's — the governed database powers *support* (cited prompts, criteria to check), it must **not** write a patient-specific diagnosis or management decision. (The current fallback behaviour is correct; confirm the live path matches it.)
2. **Two-layer citation on Ask Clinickly.** A source chip links to your governed Guidelines entry (correct — that's what the AI read). That entry must then carry the **primary-source link (real NICE/BNF URL) + a "verified against source on [date]" stamp**, so "verify at source" is actionable and staleness is visible.
3. **Identifier gate on the Ask Clinickly free-text input** — same block-on-detect used on the Consultation anonymiser.

---

*Questions on any item: ask Faheem. Full screen-by-screen review with rationale is in `ROUND-5-REVIEW.md`.*
