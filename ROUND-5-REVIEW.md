# Round 5 — re-review after fixes (21 Jul 2026)

**Live local preview, connected-AI build.** Section-by-section: what's fixed (keep), what to fix, what to verify.

**Headline: the device-boundary rework has largely landed.** The two biggest P0s from earlier rounds — Ask Clinickly's positioning and Decision-support-on-consultation — are now on the safe side of the line. The framing was always right; this round the enforcement has started to catch up.

---

## §1 — Ask Clinickly ✅ (the round-2 P0, fixed)

**Keep:**
- *"Guidance navigator — answers from the governed library, cited to source."* — the rescope, verbatim.
- *"General guidance questions only — never about an individual patient (submit an anonymised MDT case for that)."* — MDT hand-off built into the framing.
- Every claim tagged (`[g-ng87]`, `[g-bnf-ldx]`), resolving to **clickable source chips** (`BNF LDX ↗`, `NICE NG87 ↗`).
- **Honest gap-admission:** *"the specific excerpt does not detail the pre-titration checks."* A grounded system declining to fill a gap from memory. Best behaviour on the screen.
- Closing disclaimer: *"This is decision support, not a diagnosis or prescription… use your clinical judgement."*
- `LIVE AI · GOVERNED SOURCES` provenance badge.

**Fix / verify:**
- **Two-layer citation.** The chip correctly links to your **own governed Guidelines entry** (right — that's what the AI actually read). But that entry must then carry the **primary-source link (real NICE/BNF URL) + a "verified against source on [date]" stamp**, so the answer's own *"verify at source"* instruction is actionable and staleness is visible. Layer 1 built; confirm layer 2.
- **Does every claim trace to a cited source?** Test: click each chip, confirm the specific statements (HR/BP before escalation; height/weight/appetite/sleep/mood) actually appear there. If any drift beyond source → the "governed sources" badge overclaims (same class as the governance-review SPF-30 catch).
- **Identifier gate on the free-text input** — is it the same block-on-detect used on Consultation? Must be.
- **Patient-specific phrasing detection.** Banner instructs "never about an individual patient" but nothing stops *"my 34-yo patient on 30mg, should I increase?"* Detect "my patient / should I" → redirect to Submit an MDT case (soft-check pattern).

---

## §2 — Consultation co-pilot ✅ (decision-support rescope — the other big P0 — fixed)

**Keep:**
- **Structured intake:** Clinical area · Encounter type · **Age band (not free-text age)** · anonymised subject reference · reason "context only — never analysed".
- **Clerking spine** auto-selected from encounter type (PC · HPC · PMH · DH · FH · SH · ROS).
- **Decision support reframed to DOCUMENTATION PROMPTS** — *"did you document X?"* not *"do X to the patient"*; *"a documentation aid, not clinical instructions."* This is the fix that pulls it off the device line.
- **Note drafts from transcript only**; missing data flagged never fabricated (*"No vital signs recorded — add if taken"*).
- **Fallback degrades safe:** transcript preserved in Subjective, Assessment + Plan handed to clinician.
- **Anonymiser blocks on detected identifiers** (*"Draft blocked — remove direct identifiers"*) — stronger than strip-and-proceed; nothing identifiable reaches the draft. Clean text drafts through.
- **Consent-gated meeting capture:** named-bot disclosure, retention setting, attestation checkbox, *"meeting link is not stored,"* *"never becomes published learning content automatically."*

**Fix / verify:**
- 🔴 **The AI has never successfully drafted** — every attempt returns FALLBACK DRAFT / "AI drafting unavailable." Connected-AI path isn't executing in the eval build. **The one thing that most needs review — what the AI writes in Assessment when it succeeds — is untested.**
- 🔴 **The device question turns entirely on that Assessment.** Decision (Faheem): the note AI will be grounded on the governed database only. **Grounding fixes accuracy, NOT the device boundary.** Required behaviour: Assessment/impression **stays with the clinician** (design A); the governed DB powers *support* (cited prompts, criteria to check) — it must **not** write a patient-specific impression (design B is over the line, grounded or not). Current fallback = design A = safe. Confirm the *live* path keeps it that way.
- **Live-transcription UX:** hard block fights ambient capture (patient says their name naturally). Add **auto-redact-and-flag** for the live path (show `[name]` placeholders for the clinician to verify), keep hard block as backstop.
- Fallback bullet-splitting is crude (fragments like "Reports: and phone.") — cosmetic, use a real sentence splitter.

---

## §2b — Governed sources (clarified this round)

- **Clinical:** NICE (CKS + guidelines) + **BNF** → powers Ask Clinickly & consultation support.
- **Regulatory:** GPhC · CQC · MHRA · NHS → powers SOP/policy gap-checks ("reference only, not yet RAG-ingested").
- AI draws only from **Clinickly's own governed items** (drafted-from-source, MDT-verified, signed, versioned) — never model memory.
- 🔴 **BNF is licensed content** (BMJ/RPS/Pharmaceutical Press). A licence is required before BNF text goes into the live library, or swap source. **Resolve before launch.**
- **Currency:** each governed item needs a review date tied to its primary source (connects to round-4 staleness findings).
- **The source list is the build roadmap** — the library only answers what's been governed.

---

## §3 — Dashboard ✅ (date fix landed)

**Keep:**
- **Date corrected:** *"August cycle · 25 Aug 2026"* — verified a Tuesday and the last Tuesday of August, i.e. following the recurring rule. Clinician view now reads from the schedule (was the P0 Saturday bug, MS1/M2/G2).
- Honest empty states throughout (0 consults, no notes, empty activity).

**Fix / verify:**
- **Confirm 25 Aug shows identically on MDT overview and panel Sessions** — the bug spanned three surfaces; only single-source if all three agree.
- **"10 open MDT cases" still counts the test cases** — honest once Tier 1 purge runs.
- **"≈31 min/consult" admin-hours metric needs a defensible basis/footnote** — it's a sales claim.
- **Consultation counter stayed 0** after drafting — confirm rule is "only signed notes count" (intended), not "counter unwired."
- Minor: source-naming drift — "NICE, GMC & GPhC" (quick action) vs NICE+BNF (Ask Clinickly). Align.

---

## Running verdict

**Fixed and verified this round:** Ask Clinickly rescope · consultation decision-support rescope · anonymiser input gate · clinician-side schedule date · structured clerking intake · consent-gated capture.

**The one thing still unseen:** a successful live AI draft. Until the connected-AI path executes, the final device question — what the model writes as an Assessment — cannot be closed. Everything observable is on the safe side; the unobservable bit is the one that matters most.

**Sections still to review:** Clinical notes · Guidelines · Templates & SOPs · Training · MDT overview · My cases · Session library (clinician side), then the panel + admin re-review.


---

## §2 UPDATE — AI draft confirmed NOT executing (3/3 fallback)

Three drafting attempts, all **FALLBACK DRAFT / "AI drafting unavailable."** The connected-AI path does not run in this build. The "AI DRAFT" badge shows only in the empty state; on draft it flips to FALLBACK every time.

**Confirmed robust (the safe floor):** fed a textbook ADHD transcript, the fallback still did **not** write "ADHD" — Assessment handed to the clinician, transcript preserved, nothing fabricated. The system does not manufacture a diagnosis even when it is obvious.

**🔴 The critical open question — developer must answer:**

> Is the note falling back because **(a)** the AI call errors (a bug), or **(b)** the governed database has no ADHD assessment content, so it correctly declines to draft an impression it cannot ground (the design working)?

- If **(a)** — build defect; the live Assessment cannot be reviewed until fixed, and the device question stays open.
- If **(b)** — reassuring: the system refuses to write a clinical impression without governed grounding and defaults to clinician-completes. Reframes the device question to: *when governed content exists, does it write an impression, or only surface cited support?* (Latter = safe.)

**Nothing observable is over the device line. The unobservable part — a successful AI Assessment — is the one thing still blocking device-line sign-off, and it is now the top diagnostic for the developer.**


---

## §4 — Guidelines ✅✅ (strong governance; answers the §2 fallback question)

Banner: **"No approved licensed source snapshots available. Ask Clinickly retrieves only current, licence-approved, human-approved snapshots. Curated sample cards are visible only in Local Preview."**

**This resolves the §2 fallback question in favour of (b) — the design working.** The governed library has no approved content loaded, so grounding-gated features (the consultation Assessment) correctly decline. Not a bug — the absence of approved content is why it hands to the clinician.

**Keep — this is excellent governance architecture:**
- Content is triple-gated: **licence-approved + human-approved + current snapshot (versioned).**
- **Directly de-risks the BNF licensing flag** — the gate is built; unlicensed/unapproved content cannot reach production.
- **Sample content walled off to Local Preview** — nothing fake presented as real. Honest empty state.
- Source taxonomy filters: NICE · GPhC · GMC · BNF · MHRA.

**Fix / verify:**
- **Inconsistency between the two AI features in preview:** Ask Clinickly serves the Local Preview sample cards (so it answers), but the Consultation path requires approved snapshots (so it falls back). **Consequence: the consultation Assessment cannot be evaluated in preview at all.** Ask developer to wire the sample cards into the consultation path so the Assessment behaviour is testable before real content exists.
- **"Kept current" (subtitle) is vacuous with zero content.** When snapshots load, each needs a **review-date + verified-against-source stamp** (the layer-2 citation point from §1) to make the claim real.
- Confirm the licence-approval + human-approval gate is enforced server-side, not just a display label.


---

## §5 — Templates & SOPs → Governed policies & forms ⭐⭐⭐ (the handover pack, implemented)

**The biggest implementation win of the round. AD2 (round 4: "the 28 policies have no home") is fully resolved, and the whole handover pack is now the backbone of the governance product.**

**Verified present and correct:**
- **Dedicated policy library** — "Governed policies & forms," separate from SOPs. The structural fix.
- **All 28 policies loaded** — every code confirmed (BCP, C01–C041, S01–S13).
- **All 5 forms** (Forms tab).
- **"33 approved sources · 11 rules"** — 28 + 5 = 33; **11 rules = COMPLETENESS-CHECK-SPEC Rules 1–11.** The check was built.
- **24-theme taxonomy** ("All 24 themes" filter) with per-policy theme tags.
- **Pipeline verbatim:** *Approved sources → clinic fields → completeness → review → sign → publish.*
- **Theme mapping is correct** — spot-checked against source: C05→T2/T8/T18/T19 (exact), C08→T1/T2/T12/T15 (exact), C034→T5/T6/T13/T15 + **HIGH** (correct).
- **Two-stage model right:** "Approved source · not adopted" (pristine starter) vs "Draft"/"Open workspace" (clinic completing [CONFIRM] fields).
- Master Policy Index + Form Register tabs; audience + risk-tier + adoption-state filters.

**Fix / verify:**
- 🔴 **Risk tiers almost all "UNCLASSIFIED"** — only C034 is HIGH. **Risk tier drives the §4B sign-off path (high-risk = two-person).** C05, C07f, C08, C032, C021, C07, C04, C025, C017 should be classified. As-is, the two-person gate never fires for the highest-stakes policies. **Classify them.**
- **Verify Rule 1 is enforced, not just counted:** click Review & adopt on a policy with [CONFIRM] fields present — it must BLOCK publish while placeholders remain. That's the completeness check earning its place vs being a label.
- **Confirm the corrected GPhC mappings made it into the policy bodies** — the 4 regulator-mapping corrections (Principle 1 vs 5, Standard 7, Reg 20(9) non-NHS thresholds). T-codes are the requirement themes and look right; the GPhC principle/standard citations live in the body.
- **Currency stamps** — each "approved source" needs the review-date / verified-against-source metadata (same layer-2 point as Guidelines §4).

**This closes AD2 and CL3 from round 4, and puts COMPLETENESS-CHECK-SPEC, the 28 starters, the 5 forms and the 24-theme taxonomy into the live product. The single most substantial fix of the whole engagement.**


---

## §5b — Adoption workspace (fill-in UX) 🔴 Faheem's feedback — the fill flow is over-complicated

**Faheem, 21 Jul:** *"You have the template, then the source, then a flat list of fields, and some fields are just a fragment with an asterisk — you have to keep flipping back to understand the question. It should be one form in front of you, fill in the blanks, like DocuSign."* **Correct on both counts.**

**Two root causes:**

1. **(Content — my fault) The `[CONFIRM]` markers were written as document prose, not field definitions.** So the extractor turns *"a printed copy held off-site by a named person"* into a field label. Labels come out as sentence fragments (*"- Are all"*, *"all locations. This is the first thing to get right."*). And nothing is de-duplicated: `[CLINIC NAME]` is ONE field but shows 8 times; one marker is an editorial note, not a clinic field at all.

2. **(UX — developer) The fill happens on a separate blind "Fields" tab**, divorced from the document, so the clinic fills naked boxes then flips to Source/Preview to understand and check them. **Should be inline DocuSign-style fill in the document itself.**

**Keep:** the field *typing* (FACT/DECISION, POSTAL_ADDRESS/PERSON_NAME) is good — attach it to clean labels shown in context. The **Coverage panel** (governed fields · mapped regulator requirements · CQC-R10, GPhC-P6…) and the **commit/SHA-256/version** audit are genuinely valuable — keep as reference.

**Deliverable produced:** [C05-FIELD-SCHEMA.md](C05-FIELD-SCHEMA.md) — the worked example. 28 raw markers → 23 clean typed fields (deduped clinic_name, removed the editorial note, defaults + conditionals surfaced). Includes the marker convention (`[CONFIRM: label|type|default|help]`, `[NOTE]` for governance-only) so extraction is clean, and the UI requirements (inline fill, dedup, type-driven inputs, decisions show defaults, conditionals hide, notes never reach the clinic). **If the shape is right, the other 27 follow — ~a day's work for the full ~500 fields.**


---

## §6 — Training / CPD ✅✅ (CPD-LOG-FIX-SPEC largely implemented)

Near-complete implementation of the round-4 CPD fix spec. Every headline P0 addressed.

**Fixed & verified:**
- **T4 — minutes gone.** No "CPD minutes" metric anywhere. Now records/completions-based: *"Exact versions completed," "Evidence-eligible completions," "no prescribed numeric completion target."*
- **T1 — logs the right event.** *"Case submission and response receipt create no CPD; first opening a response can create one draft."* Exactly §2.
- **T2 — drafts don't count.** *"Drafts are not counted as complete."*
- **T3 — records typed.** Record shown as *"unplanned"* learning (real GPhC type).
- **Capture-once 4-question wizard** with the GPhC criterion wording verbatim: Q3 *"How will this benefit people using your services? Give a real, anonymised example…"*
- **Privacy by design:** *"Administrators can see completion status, not these answers."* Owner-private reflections + identifier warnings.
- **Portfolio export:** JSON / printable / PDF.
- **Nice governance details:** *"Exact versions completed"* ties completion to the content version done (no silent version-drift); *"reflection portfolio with gaps, not a false numeric target"* shows gaps honestly.

**Verify:**
- **Regulator rendering (T9).** This is the **GMC** view (appraisal supporting information, domains, cycle). Spec = capture-once / render-per-regulator. **Is there a GPhC view** rendering the 6-record model (4 CPD ≥2 planned · 1 peer discussion · 1 reflective account) and the named-peer consent flow? No toggle visible — check a GPhC profile re-renders it.
- **Peer-discussion + named-peer consent flow (T3/T5)** — not visible on this screen (needs an MDT-case-derived record). Confirm MDT case → peer discussion, with the panel-consent-to-be-named model (default off, group=name-one).
- Test-data purge (T10) — page is clean/empty here.


---

## §7 — MDT overview ✅ (round-4 P0 regressions fixed)

The Tier 1 purge + schedule fix landed.
- **M1 fixed** — test members Dr P. Word and Ep Och removed. Clinical MDT: Kaur (Derm), Mehta (GP), Bright (Psych).
- **M2 fixed** — date now 25 Aug 2026 (Tuesday, last Tuesday of Aug), **matching the dashboard** → schedule single-sourced across surfaces.
- **M3 fixed** — one chair (Okafor); J. Hale duplicate-chair gone.
- **M4 fixed** — specialties shown on every member (needed for routing + peer-discussion record).

**Verify:**
- **Is pharmacy still represented?** Round 4 had Dr N. Newman (Pharmacy & prescribing) in the clinical list; only Derm/GP/Psych shown here. Removing Word/Och was right — confirm Newman wasn't removed too, or a pharmacist-led product has no pharmacy voice on its clinical panel.
- **M6 not fixed** — banner still reads "Live session" for a future date (25 Aug); should be "Next session." P2.


---

## §8 — My MDT cases ⭐⭐⭐ (the device breach is fixed structurally — headline result)

The X1 breach (*"Is this rosacea?" → "Consistent with rosacea"*) is fixed at the design level. The structured case format from MDT-CASE-FORMAT + MDT-CASE-SUBMISSION-SPEC is built.

**Fixed & verified:**
- **Closed-episode gate is a field:** *"EPISODE: Concluded before submission."* An open-episode diagnostic question is now unsubmittable. Positioning: *"Structured retrospective learning cases — never advice on a live patient."*
- **Retrospective framing throughout** — title, *"RETROSPECTIVE QUERY: Diagnostic reasoning review,"* presentation text.
- **Structured clerking** — Context and Boundary · Demographics · Core Clerking sections.
- **Age band not precise age** (18–29); sex Not Stated.
- **Routing fixed (PM3/X13):** *"Awaiting an eligible Psychiatry/mental health clinical panel member"* — routed by requested expertise, honest about why it waits.
- **Legacy quarantine (elegant):** old cases tagged *"Legacy v0 — completeness not asserted … predates the structured contract. Missing evidence has not been inferred,"* *"Historical Read-Only."* Old *"Agree with the documented triage & plan"* response tagged historical/not-validated. Better than deletion — preserves audit trail, refuses to retrofit.

**Verify (scroll down):**
- **Full clerking sections** — the differential table (min 2 with reasoning per differential) and the referral counterfactual (MDT-CASE-FORMAT §2, the real teaching work). Header/demographics confirmed; reasoning block not yet seen.
- **A NEW structured panel response** — only the legacy "Agree…" response is visible (correctly marked historical). Confirm MDT-PANEL-RESPONSE-FORM is built for new cases and the "Agree" chip is gone from the current form.

**This resolves X1 (device breach), X2/X3 (identifiers), X13/PM3 (routing), and the test-data concern (via quarantine). The single most important fix of the engagement, on the highest-risk screen.**


---

## §8b — Structured clerking ✅ (CORRECTED)

**Structure fully built (MDT-CASE-FORMAT complete):** core clerking (PC·HPC·PMH·DH·allergies·FH·surgical·occupation·social·ROS pos+neg·obs·exam·investigations, honest "Not Recorded" states) · **differential reasoning table (Differential · Supporting · Opposing evidence)** · working decision **with Confidence: Uncertain** · completed management (actions·rationale·safety-netting·follow-up) · ADHD specialty block. Complete and correct.

**CORRECTION to an earlier read:** the identical-transcript content in every field was **Faheem's own test input** (he pasted the transcript into each field to fill it quickly) — **NOT an AI-extraction fallback bug.** This actually confirms the correct design: **the reasoning fields are clinician-entered, not auto-populated** — which is the load-bearing requirement for the retrospective-teaching / device boundary. No extraction bug on this screen.

*(The transcript-dump fallback IS real on the Consultation co-pilot — that one is machine-generated with a FALLBACK DRAFT badge. Don't conflate the two.)*

**Optional quality guard (not a bug):** because a clinician can paste the same text into every field, the completeness/quality check could flag low-quality cases — e.g. "differential duplicates the HPC" or "differential is not a distinct differential" — to nudge quality without blocking. Nice-to-have.


---

## §9 — Session library ✅ (raised bar, honest empty state)

Round 4's five test recordings are gone; library empty and honest. Footer states the full contract: *"Only persisted, privacy-reviewed, consent-confirmed and **independently signed** recordings appear here. Playback URLs expire and access is audit-logged."*

**Fixed:**
- **"Independently signed"** — fixes MS2/S1 (round 4: 1 of 5 signed, and that one had the same person on all three gates). Contract now requires independent sign-off.
- **Expiring playback URLs + audit-logged access** — §5.10 secure-playback requirement.
- **Privacy-review + consent gates** stated.
- Unsigned/legacy recordings removed rather than shown mislabelled (consistent with Guidelines + case legacy handling).

**Deferred (empty library — needs one governed session to test):**
- S3: does watching a session generate a CPD record?
- S4: are long recordings chaptered / segment-extracted (vs one 87-min block)?
- S2: image consent scope for published sessions (F05 §B vs §C).


---

## §10 — Panel · My credentials ✅✅ (credentialing root cause addressed)

Dr Kaur — the round-4 poster child for "unvetted but ACTIVE" — now shows a **full 14-item vetting record, all verified**, with expiry dates. This is the strongest evidence the PM1/PM8 root cause is fixed.

**Fixed & verified:**
- **Full Reg 19 / Schedule 3 set verified:** identity+photo · right to work · CV · **DBS** · **employment history + gap review** · **two genuine references** · fitness-to-work decision · recorded induction before independent work · **registration** · **role-scoped indemnity** · original qualifications · competence assessed · annual appraisal + revalidation. Several near-verbatim from the C025 v2 policy — the content shaped the credentialing model.
- **PM7 fixed — expiry dates.** DBS, indemnity, registration, right-to-work, appraisal all *expires 29/07/2027*. Renewals now tracked (round 4 had none).
- **Capabilities gated to verified credentials** (*Clinical Area / Clinical Case Dermatology*), not to a name.
- **Privacy by design:** verifier notes + evidence not visible to the member; suspension messages don't expose DBS/health/provider detail.

**Verify (needs admin Panel management):**
- **PM8/PM1 close-out:** is a *new* member **PENDING (not ACTIVE)** until all 14 are verified, and **blocked from holding/answering cases** meanwhile? This member-view shows a fully-vetted member; the admin add-flow is where "add with a name → ACTIVE" lived, so that's the screen that proves the gate.


---

## §11 — Admin Overview

**Good (fixed):** new admin sections — Credentialing · Safety operations · Image operations (dedicated homes for the specced features). Panel = **5 real members across 5 specialties, pharmacy (Newman) retained** (answers the §7 question). **Clinic scope locked** (tenancy working). Governance sign-off pipeline **empty and honest** (round-4 test-published content + uncredentialed reviewer both gone). **Training = 10 modules** (AD4 fixed). The "no active panel member — assign someone" alerts are the routing-coverage check working (detects unanswerable cases).

**Issues to fix:**
| # | Issue | Severity |
|---|---|---|
| AO-R1 | **Test/legacy cases still in the admin action queue.** `ddd` (C-245), `Case-loop E2E two` (C-238), `Rash photo case` (C-241 legacy rosacea) show as *"assign someone."* The clinician-side legacy quarantine has NOT been applied to the admin case list — they should be **closed/archived, not assignable** | **P1** |
| AO-R2 | **Real cases have no eligible panel member — coverage gap.** 11 open, most flagged unanswerable. Panel is 5; specialties a clinician can submit to (e.g. *General & acute prescribing, Other*) have no vetted member. **Either add members for those specialties or stop the submit form offering them.** The detection is correct; the gap is real (round-4 M5a) | **P1** |
| AO-R3 | **Count mismatch.** Admin shows *"SOPs & templates: 8 published"*; clinician library shows *28 policies*. The two views count different things — reconcile | **P2** |

**One-liner:** the system now correctly *detects* cases nobody can answer, but nothing *resolves* them — junk should be closed; genuine ones expose that the panel doesn't cover every submittable specialty.


---

## §12 — Admin Governance sign-off

**Good:** sign-off *queue* empty and honest (*"pipeline is clear"*). *Recently published* is a correct read-only audit list of the 28 governed policies, labelled *"no action needed here."* Round-4 GS1 (test content published) and GS3 (uncredentialed reviewer in queue) both gone.

**Issues (same class as round-4 GS2 — audit trail undermining the governance claim):**
| # | Issue | Severity |
|---|---|---|
| GS-R1 | **All 28 policies signed at the identical minute — "21 Jul 2026, 01:00."** The rubber-stamp pattern, now across 28 docs (round-4 GS2 was 3 at 02:50). The audit trail is the artefact that proves governance is real; "all signed at 1am in one minute" reads as the opposite. **Fix:** either spread timestamps to real review times, OR **relabel** — these are *approved starter sources* (a legitimate bulk approval), not clinic-adopted clinical sign-offs; calling it "signed … 01:00" misrepresents a bulk source-load as individual clinical sign-off | **P1 — evidential** |
| GS-R2 | **"signed by" is blank** — every row reads *"v1 · signed by · 21 Jul 2026"* with no name. An audit trail exists to record *who* signed. Should show *"signed by Faheem Ahmed."* | **P1** |
