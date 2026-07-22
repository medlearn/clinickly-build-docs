# Clinickly Co-pilot — Developer Fix List (all three portals)

Priority-ordered actions from the full screen-by-screen review.
Detail + evidence: [BUILD-REVIEW.md](BUILD-REVIEW.md) (clinician §1–§11) · [BUILD-REVIEW-PANEL.md](BUILD-REVIEW-PANEL.md) (panel P1–P5) · [BUILD-REVIEW-ADMIN.md](BUILD-REVIEW-ADMIN.md) (admin A1–A8).
Spec source of truth: [CLINICKLY-MASTER.md](CLINICKLY-MASTER.md).

Legend: **P0** safety/governance (block real use) · **P1** correctness bugs · **P2** build gaps (specced, not built) · **P3** tidy-ups/UX.

---

## ✅ What's genuinely strong — DON'T break these
- **Governance review workflow** (panel P2) — side-by-side recommendation ⟷ source, "Matches source", hard gate ("nothing publishes until all verified"). The keystone of the whole product.
- **Two-step sign-off, end to end** (panel → admin) — named, dated, versioned; full audit trail (admin A2/A8). This is the defensibility backbone.
- **Guideline detail page** (§6) — real governance state, named reviewer, "verify at source", clinician/patient toggle, BNF-defer, "no single first-line" honesty. The quality bar for all content.
- **Positioning/framing everywhere** — "teaching/CPD, not advice on a live patient", advisory caveats, "decision support not a directive".
- **Form structures** — MDT case dropdowns (Appendices B/C), consent gating, anonymisation banners, real computed metrics (dashboard, CPD minutes).

---

## P0 — Safety & governance (must fix first)
- [ ] **Rescope Ask Clinickly — currently patient-specific diagnostic support (device risk) + uncited** (R2.26). As built it solicits an individual patient's age/symptoms/exam to "refine" a differential — the exact function the positioning and the draft MHRA letter disclaim — and answers from model memory with zero citations (only ungoverned AI surface in the product). **Rescope to guidance navigator:** answers ONLY from the governed library + cited sources (open-entry/verify-at-source links); general frameworks, never "for this patient"; hand-offs — patient-specific → anonymised MDT case, documentation → co-pilot; log question themes to demand analytics. Fix the LIVE MODEL vs "connect your API" label contradiction.
- [x] **Notes draft from the transcript ONLY** — **VERIFIED FIXED (R2.2, 9 Jul):** same cough-transcript test → Subjective contains only transcript content, zero scenario/ADHD leakage.
- [x] **Never fabricate objective data / vitals** — **VERIFIED FIXED (R2.2):** Objective now shows ⚠️ "No vital signs recorded — add if taken" / "No physical examination findings recorded"; Plan flags gaps instead of inventing. Flag-not-fill implemented.
- [x] **Anonymiser strips identifiers — TEXT VERIFIED (R2.4, 9 Jul):** note with patient ref "FS" → case summary contains no trace (age band only; round 1 leaked "J.M."). **Remainder:** AI identifiable-IMAGE check is a stated production integration — verify at launch.
- [x] **Governance-review source passages need a real deep link** — **VERIFIED FIXED, GOLD STANDARD (R2.16):** "↗ Open the source to verify" on every passage; link opens; **tick enforced-gated on opening** (chip flips to "Source opened" → tick unlocks; unopened items stay locked); "the quote alone is not evidence" as stated rule. Remainder: store retrieved text + URL + date snapshot for the audit trail.
- [ ] **Validate all codes** against a SNOMED/ICD terminology server (§3). **STILL BROKEN at R2.2:** `R05.9` again labelled "Fever, unspecified" (R05 = cough; fever = R50.9). "AI-suggested — verify before use" badge added = caveat, not validation. J00/J06.9 correct.
- [x] **Note sign-off = draft → review → attest → sign** — **VERIFIED FIXED (R2.3):** "Attest & sign" dialog with the exact attestation tick ("I have read this note and confirm it is an accurate record of this consultation"), sign button disabled until ticked, lock + addenda-never-edit stated.
- [x] **Content licensing** — **VERIFIED (R2.6 + R2.7):** BNF = "Open at BNF ↗" link-out on the card + `BNF (link-out)` chip on the doses line ("never from this summary"); own summaries cite + link with verify-at-source. Formal BNF licence still required before any deep BNF integration (unchanged).
- [ ] **Separation of duties — risk-tiered** (A1, §8). Reviewer ≠ signer (block same user_id). **High** (prescribing/safety, regulated SOPs) = full two-person; **Medium** = single reviewer + sign-off; **Low** (typo) = light-touch/auto-approve + audit.
- [ ] **Signer qualification matches content type** (A2). Clinical content → **clinically-qualified lead** signs; governance/admin content → admin/governance lead OK. System checks role/registration vs content type.

## P1 — Correctness bugs
- [ ] **Strip patient refs from the central audit trail** (R2.25). Audit entries read "Signed clinical note — ADHD — patient N.R" / "patient JS" — clinicians' private patient codes are written into the platform-level log visible to central admin. Item descriptions must carry the item/type only, never patient refs (same anonymisation boundary as the J.M. fix; include existing rows in the retro-scrub).
- [ ] **MDT schedule bug — panel view reads wrong/stale source** (R2.17, pinpointed R2.21). Admin schedule is CORRECT (July 28 next, last-Tuesday rule). Panel Sessions page shows "August · 15 Aug" (a Saturday) and drops July. Fix: both portals read the single schedule source; validate any override against the recurrence rule.
- [ ] **Retro-scrub legacy records** (R2.14). The anonymiser fix did not clean pre-fix data: old case C-236 **still shows "J.M."** to panel members (and keeps its mis-tag). One-off migration: strip identifiers + correct tags on all existing cases/notes created before the fix.
- [x] **Fix routing — cases AND content — by specialty/type** — **VERIFIED FIXED (R2.6 + R2.14):** content reviewed by matching specialist (NG87→Dr Bright); dermatologist's inbox shows only dermatology-tagged cases; badge = awaiting-count. Remainder: legacy C-236 keeps its round-1 mis-tag (fix with the legacy scrub below).
- [x] **Remove the demo scenario from the real product** — **VERIFIED (R2.2):** real inputs (area · encounter · age band · ref · reason "never analysed"); no hidden injection. "Load demo consultation" remains as demo-mode affordance (acceptable).
- [x] **Age range → one standardised dropdown** — **VERIFIED (R2.2):** dropdown with agreed bands (0–17 shown).
- [x] **Tags / title / content follow actual content** — **VERIFIED (R2.4):** note titled "Consultation note", tags match selections/content; case title auto-generated from tags, no patient info.
- [x] **Surface per-statement citations on the published page** — **VERIFIED FIXED (R2.7):** statements carry source+section chips (NICE CKS Rosacea – Diagnosis/Management/etc). Remainder: chip coverage ~70% — agree rule that every *recommendation* gets a chip; fix the duplicated "Management approach" section (rendering bug).
- [ ] **Two-tier tenancy + RLS isolation** (A7, §5.7). **STILL OPEN at R2.24, now inconsistent:** some panel members filed under the demo clinic, others unscoped (no clinic); no clinics list/management (cannot add clinic #2 to prove isolation). Plus NEW: **two mystery gmail CLINICIAN accounts with random-string names and no clinic** — (a) confirm/close **open self-registration** (clinician accounts = clinic-admin invite only); (b) **require a proper display name** (audit trail is stamped with it); (c) unscoped users must be impossible.
- [x] **Wire reports to real data** — **VERIFIED FIXED (R2.25):** both charts count real usage. Minor: "Not recorded — 5" = legacy pre-dropdown consultations → tag/exclude in retro-scrub.
- [x] **Reconcile case counts** — **RESOLVED IN SPIRIT (R2.19):** all counts now live (3 clinicians · 8 panel · 8 open cases); round-1 0-vs-1 gone. Spot-check cross-portal tallies after test-data purge.

## P2 — Build gaps (specced, not built)
- [ ] **Reports v2 — the current page is an audit trail + two counters, not a reporting suite** (R2.25, Faheem). Build: (a) **date ranges + trends** (weekly/monthly, not all-time totals); (b) **per-clinician & per-clinic breakdowns** (adoption/churn radar); (c) **MDT service levels** — avg time-to-answer, open-vs-answered trend, urgent SLA compliance; (d) **governance health** — items overdue review, draft→published throughput, reviewer workload; (e) **CPD compliance matrix** per clinician (inspection evidence); (f) **chart exports** (PDF/CSV); (g) later: **one-click inspection pack** (audit extract + CPD matrix + Master Policy Index + content freshness — sellable).
- [x] **Admin fee-band table** — **VERIFIED BUILT (R2.20):** editable, "ADMIN-SET · NO BIDDING", audit-logged edits, rationale as footer copy. Remainder: current fees are dev placeholders — Faheem to enter the real §4B bands (anchored to £150/hr); confirm fee shows on Available-tasks cards.
- [ ] **Upgrade CPD log/export to GPhC + GMC native formats** (§5.8 decisions 9 Jul, from the real forms). **Capture once** — 4-question reflection wizard (learned · practice change · benefit-to-service-users with example · SMART next steps) — **render per regulator**: GPhC = record types, records not minutes (6/yr = 4 CPD [≥2 planned] + 1 peer discussion + 1 reflective account; **MDT response→peer discussion with named panel peer**); GMC = Academy reflective template (activity + supporting-info category + GMP-domain tags + influence + SMART next steps). Auto-category/domain tagging; **AI criteria pre-check** (concrete patient-benefit example present? beyond one-word/descriptive?); profile registration sets default. Replace minutes-led framing. NMC phase 2.
- [ ] **⭐ Grounded, cited AI content generation** (§6, §7, A5) — THE big one. "Create draft" is a shell; the AI drafting from *retrieved source text* with *per-statement citations* isn't built. Underpins guideline citations, the SOP builder, and content drafts. Treat as one core capability, not three gaps. **Also includes standards RAG-ingestion (R2.23):** gap-checks currently run on a deterministic theme checklist, not the uploaded standards' text — and until RAG lands, relabel the clinic-facing claim ("checked against the compliance theme checklist", not "gap-checked vs GPhC/CQC/MHRA/NHS").
- [ ] **MDT case submission — FIX THE REGRESSION** (R2.5/R2.14/R2.20). Loop worked 6–8 Jul; fails 9 Jul. **Diagnostic (R2.20): failed submissions ARE visible in admin Case assignment with no ID ("C-…", waiting 1d/2d)** — the insert half-succeeds but never gets a server ID and never reaches the panel. Find where ID assignment / panel handoff fails (compare vs the working notes path).
- [ ] **SOP builder — output must be a COMPLETE best-practice SOP, never a skeleton** (§5.7 decision 9 Jul, R2.10). Current build: minimal input → empty headings ("unfilled sections stay visibly unfinished") = inspection liability. Fix the rule split: clinic FACTS never invented (form/profile or flagged `[CONFIRM: …]` placeholder); process CONTENT always the full pre-authored best-practice default (zero input still yields an adoptable SOP); clinic DECISIONS get default + flag (`[CONFIRM: controlled drugs? Default NO]`); sign-off warns on unresolved placeholders. **Output anatomy = real CQC policy** (version-control block: Policy No · Responsible Person · Authorised · Issue/Review date · Version; References; Scope; AIM→POLICY→PROCEDURE). Also: duplicate guard (re-build → v2, never second v1) + clinic name from clinic profile not free text. **KEEP the "How this process actually runs in your clinic" field** (Faheem — it is what makes the SOP true to the clinic; empty = defaults, filled = woven in). **Catalogue taxonomy now = the Ahmeys CQC master index** (spec Appendix D — 5 categories, policy numbering, review cycles); phased via starter set + demand data. **New feature: auto-generated Master Policy Index per clinic** (number · title · version · signed-by · review date — the first thing inspectors ask for).
- [x] **Case image upload** — **MOSTLY BUILT (R2.4):** photo upload (max 2 — spec said 1–5, OK for pilot) + crop-to-lesion guidance + EXIF/GPS strip on import + consent gate. **Remainder for production:** AI identifiable-image pre-check + encrypted UK/EU storage (verify at launch).
- [ ] **Training content + reflection + CPD log + PDF export** (§8). Modules are empty toggles; build embedded content + reflection capture + the accumulating CPD/revalidation record (auto-fed from modules + MDT participation) that exports as a reflective-account portfolio.
- [ ] **Panel member credentialing — structure BUILT, GATING missing** (R2.20). Status chips track Registration/PIN · contract · DBS · indemnity, and verified tags exist. **Remaining: (a) ENFORCE gating** — incomplete credentials → cannot be ACTIVE / claim / review ("vetting gates access"); (b) confirm "Edit identity" captures PIN (register-verified), CV, photo; (c) show tags in the panel directory.
- [ ] **Session library: recording pipeline BUILT — playback remains** (R2.21). HOLDING → PII REVIEWED → CONSENT CONFIRMED → PUBLISHED with named accountability + "Promote to training module" all verified. Remainder: real **Bunny Stream playback** (signed URLs) behind the play buttons (prototype = illustrative); eventually SoD on high-sensitivity recordings (PII reviewer ≠ signer).
- [ ] **Demand analytics — structure exists, LOGGING UNVERIFIED; most signals missing** (R2.25, downgraded — Faheem). "Top missed searches" box exists (aggregate/PII-scrubbed) but was empty — **verify it logs**: search gibberish in Guidelines → confirm it appears in the report. Then build the rest of the demand intelligence: **top successful searches + most-opened guidelines** (what's valued), **pointer-entry opens** (INDEX→SOURCE promotion signal), **SOP demand** (builds per template + requests), **Ask-Clinickly question themes**, CPD team roll-up. The two-tier library and SOP catalogue prioritisation depend on these.
- [x] **Audit trail: immutable/append-only + exportable** — **VERIFIED (R2.25):** "server-side log is append-only" stated + Export CSV. Bonus: flag-back-with-reason, NEEDS-UPDATE flag, recording steps, fee-band claims all audited.

## P3 — Tidy-ups & UX
- [ ] **Per-member workload on Panel management** (R2.20, Faheem). Show each panel member's **open-case count** (and ideally avg response time) in the Panel members list — without it, the Case-assignment "rebalance" override is used blind (you can't see who's overloaded before reassigning).
- [ ] **Templates & SOPs page: add SEARCH + a visible "Request an SOP" button** (R2.10, §5.7). Currently 8 fixed cards + category tabs only — a clinic wanting an SOP not in the catalogue (e.g. chaperoning) has no way to search for it or request it. The request mechanism exists admin-side ("submissions arrive as drafts") — expose the front door. Requests feed the demand analytics above.
- [ ] **Library entry tiers — DECISION locked (spec §5.6), implement it** (R2.8). Two tiers with **mandatory card badges**: `FULL SUMMARY` (Rosacea layout) vs `INDEX → SOURCE` (interim placeholder, no own content). Pointer entries are stopgaps promoted by search demand. **Starter-set topics (incl. NG112 recurrent UTI) must be FULL summaries before launch.** List which current entries are which.
- [ ] **Delete "Saved records" page** + **remove "Release to patient"** (deferred patient feature) (§4).
- [ ] **Note-template footer**: "standard · not customisable per clinic"; keep "customise → governance" only for SOPs/leaflets (§7).
- [ ] **Nav badges = unread-count that clears on open** (My cases §11; Governance review P2/P3) — not total-count.
- [ ] **"Recently published"** visually distinct from the actionable queue + clickable-to-view (A2).
- [x] **"Panel members" tile subtitle** — **VERIFIED FIXED (R2.19):** now "across 5 specialties".
- [x] **Soften "Auto-logged for revalidation"** — **VERIFIED (R2.11):** now "CPD evidence for your portfolio · reflections included in export".
- [x] **Govern clinical training modules** — **VERIFIED (R2.11 + R1 P3):** modules badge "MDT-governed content" and appear in the governance review queue.
- [x] **MDT overview: shield card + two panels** — **VERIFIED FIXED (R2.12):** Clinical MDT vs Governance MDT shown with correct remits; shield card gone; pharmacist (Dr N. Newman) added. Remainders: **delete test members "Dr P. Word"/"Ep Och" from the roster**; verified qualification tags in the panel directory still to check (P5).
- [x] **Regulatory standards: central upload restriction + named currency owner + review cadence** — **VERIFIED FIXED (R2.23)** verbatim ("currency owner: Governance lead · review due ~3-monthly"; "upload restricted to central admin/governance").
- [ ] **Teaching-slot free text**: add "general topic — no patient identifiers" hint + light PII check (A4). *(Free text itself is correct here.)*

---

## 🆕 Round 4 — Training / CPD (21 Jul 2026)

**Full spec: [CPD-LOG-FIX-SPEC.md](CPD-LOG-FIX-SPEC.md)**

| # | Item | Severity |
|---|---|---|
| T1 | **CPD log records the wrong event.** Logs case *submission*; nothing is learned at submission. Log when the **panel responds and the submitter opens it** | **P0** |
| T2 | **A record with no reflection is counted.** All 8 MDT entries have no reflection and none can count toward GPhC revalidation. Draft until reflected | **P0** |
| T3 | **"MDT participation" is not a GPhC record type.** MDT case + panel response = **peer discussion where the panel member consented to be named**, otherwise **unplanned learning**. Never emit a peer discussion record with a blank or anonymised peer | **P0** |
| T4 | **Headline metric is minutes.** GPhC counts **records**. Replace with progress against 6 records (4 CPD ≥2 planned · 1 peer discussion · 1 reflective account). Delete "45 CPD minutes" and "≈0.8 h" | **P0** |
| T5a | **Group discussions — GPhC requires only ONE named peer.** Where several panel members were involved, offer the clinician the consenting members and let them pick one. The bar is one consenting member per session, not broad opt-in | **P1** |
| T5 | **Panel consent to be named is NOT automatic** (decision 21 Jul). Build a standing preference on the panel profile, default **OFF**, with a per-response override. Clinician is never shown that a peer declined | **P0** |
| T6 | **Duration hardcoded to 15 min** on all 8 MDT entries. Measure it or remove it — prefer remove | **P1** |
| T7 | **Case IDs not monotonic with time.** C-247 submitted before C-245; both numbered above cases from the following day. Possibly shares a root cause with the round-2 no-ID insert failure | **P1** |
| T8 | **Log entries show system events, not clinical topics.** "Anonymised case submitted" tells the clinician nothing about what they learned | **P1** |
| T9 | **No regulator toggle visible.** Spec requires capture-once / render-per-regulator (GPhC forms or GMC Academy template), defaulting from profile registration | **P1** |
| T10 | Test data — module completed 02:42 | P2 |

**Acceptance test:** a clinician with 8 MDT cases and 1 completed module opens the page, sees they are short a peer discussion, clicks once, adds a reflection, and has a GPhC-shaped peer discussion record in their export. **None of that is possible today.**

### Round 4 — Training catalogue

**Full spec: [TRAINING-CATALOGUE.md](TRAINING-CATALOGUE.md)**

| # | Item | Severity |
|---|---|---|
| T11 | **Short modules in Clinickly, diplomas on MEDLRN.** Clinickly hosts standalone 30–45 min modules that lead to the six Level 7 diplomas. It does **not** host the diplomas | **P1** |
| T12 | **Each module must stand alone.** A module that is a truncated advert produces a CPD record with nothing behind it and damages trust in the rest of the product | **P1** |
| T13 | **Module completion order: reflection first, promotion second.** Never gate the CPD reflection behind the diploma offer | **P1** |
| T14 | **Onward link to the mapped diploma** on module completion, with tracked attribution | **P1** |
| T15 | **Funnel measurement** — module completions → diploma click-through → attributed purchases. This makes Clinickly a measurable acquisition channel for MEDLRN | **P1** |
| T16 | **Version and date every unit**, with an admin flag for overdue review. Clinical content ages — the corpus review found guidance twelve years out of date | **P1** |
| T17 | **Modules with no content behind them should not be visible.** Several are titles only. A module that opens to nothing is worse than an absent one | **P1** |
| T18 | **Remove *Rosacea & common facial dermatoses*.** Not a MEDLRN diploma, no onward route, no content | **P2** |
| T19 | **Final module list = 10** — six leading to the MEDLRN diplomas (ADHD · Mental Health · Women's Health · TRT · Minor Illness · Weight Management) plus four standalone (Foundations of independent prescribing · Documentation that stands up to inspection · Recognising the deteriorating patient · Reflective practice & revalidation) | **P1** |

### Round 4 — MDT overview (21 Jul 2026)

| # | Item | Severity |
|---|---|---|
| M1 | **Test data still in the live panel list — "Dr P. Word" and "Ep Och".** Both were on the round-2 purge list. Still present, on the first page a clinician sees. "Ep Och" is not a plausible name and carries no title | **P0 — regression, previously flagged** |
| M2 | **Session date is 15 Aug 2026, which is a Saturday.** Identical to the round-2 finding (admin 28 Jul vs panel 15 Aug). **The schedule is still not single-sourced.** A 19:00–20:30 monthly MDT on a Saturday evening is not plausible | **P0 — regression, previously flagged** |
| M3 | **Two chairs in the Governance MDT.** Dr A. Okafor is "Chair / Clinical lead (Chair)" and J. Hale is "Panel member (Chair)". Hale is both a member and a chair, and there cannot be two | **P1** |
| M4 | **"Panel member" is used where a role should be.** Mehta/Bright/Kaur show GP, Psychiatrist, Dermatologist; Newman/Word/Och show only "Panel member". **Role and organisation must be mandatory fields on the panel profile** — the GPhC peer discussion record requires peer name, role AND organisation, and cannot be populated from "Panel member" | **P1** |
| M5 | ~~Panel composition does not match the diploma catalogue~~ — **withdrawn.** Overstated: the apparent 3-dermatologist skew was mostly the test data (M1). Once Word and Och are removed the panel is GP + psychiatrist + dermatologist + pharmacist, which is a reasonable starting composition. The diplomas are a MEDLRN product and do not determine panel makeup | ~~P1~~ **withdrawn** |
| M5a | **Real question: does every routable specialty have a panel member behind it?** Round 2 verified specialty routing works. If a clinician can select a specialty on the submit form with nobody assigned to it, the case goes nowhere. **Check the submit-a-case specialty list against the live panel and close any gap** — either add a member or remove the option | **P1** |
| M6 | Banner reads **"Live session"** for a date three weeks away. Should read *Next session* | **P2** |

**Note on M1 and M2:** both were raised in round 2 and both are unchanged. Worth confirming with the developer whether the round-2 items were actioned and regressed, or never picked up — the answer changes how the rest of the round-2 list should be treated.

**Good on this page:** the positioning line — *"Anonymised case-based teaching, discussion & CPD"* — is correct and consistent with RED-LINES. The four explainer cards and three-part agenda are clear and land well.

### Round 4 — My MDT cases (21 Jul 2026)

> ⚠️ **Read this section first.** Most items below were raised in **round 2** and are unchanged. Before further review rounds, please confirm whether the round-2 data-quality list was actioned at all.

#### 🔴 The device-boundary breach

| # | Item | Severity |
|---|---|---|
| **X1** | **Case C-241 "Rash photo case": question — *"Is this rosacea?"* Panel response — *"Consistent with rosacea."*** This is **patient-specific diagnosis**, not case-based education. It is the exact activity `RED-LINES.md` prohibits and the basis on which the MHRA position rests. **The per-card disclaimer does not cure it** — a regulator reads the question and the answer, not the footer | **P0 — device risk** |
| X1a | **Fix at the design level, not by deleting the case.** Specs: **[MDT-CASE-SUBMISSION-SPEC.md](MDT-CASE-SUBMISSION-SPEC.md)** (the boundary) + **[MDT-CASE-FORMAT.md](MDT-CASE-FORMAT.md)** (clerking proforma) + **[MDT-PANEL-RESPONSE-FORM.md](MDT-PANEL-RESPONSE-FORM.md)** (structured response). Core change: closed-episode gate + a clerking with a mandatory **differential table** (each row: differential · what made me consider it · what ruled it in/out), **working diagnosis · confidence · rationale · management · safety-netting**, and — where referred — a **counterfactual block** (why refer rather than manage · what you thought it was · what you would have done if you could not refer · what you recommended and why). Also fixes the unusable-case problem — *"dddd"* and *"Age 30-39 rash, is this rosacea?"* both become unsubmittable | **P0** |
| X1b | **Images: permitted, with controls.** Dermatology is not workable without them. Clinician **attests** to holding consent — the signed form ([F05](starters/forms/F05-photography-consent.md)) stays in the patient's record and is **never uploaded**. Platform must strip EXIF server-side (phone images carry GPS of the patient's home), block faces by detection, warn on in-frame identifiers, and support per-patient deletion on withdrawal. See spec §6 | **P0** |

#### 🔴 Patient identifiers — all previously flagged

| # | Item | Severity |
|---|---|---|
| X2 | **Patient initials "J.M." still present** in C-237 and C-238. Round 2 raised this exact case | **P0 — regression** |
| X3 | **Precise ages still in prose** — "15-year-old male", "30-year-old", "22-year-old male" — despite the on-screen rule stating age range only. Round 2 raised the anonymiser gap | **P0 — regression** |
| X4 | **Age band contradicts the prose** — C-244 banded **18-29**, text says **30-year-old**. Round 2 raised age-band vs transcript checks | **P0 — regression** |
| X5 | **Reason field contradicts the content** — C-248 reason "Ear ache", history is headache and shortness of breath. Round 2 raised reason vs transcript checks | **P1 — regression** |
| X6 | **Truncated reason fields** — "Reason: Head", "Reason: Pot" | **P2** |

#### 🔴 Test data in the live case list — all previously flagged

| # | Item | Severity |
|---|---|---|
| X7 | **"ddd"** (C-245) — summary "dddd", question "dddd" | **P0 — regression** |
| X8 | **"please advise on xxxxx"** (C-246) | **P0 — regression** |
| X9 | **"Case-loop E2E one" / "two"** (C-236, C-239) | **P0 — regression** |
| X10 | **"R3 notif case"** (C-240) | **P0 — regression** |
| X11 | **Two panel responses are keyboard mash** — *"djdjdjjsddjfhdfhndhdjdjdjjssjssjssjsdsss"* (C-237) and *"djdjdjsdkdsmkcmmcndsddsdsdsdsjdcmknkjqkcmkskcdcjkc/dsnkownieocdcdes"* (C-238). **Both are attributed to named panel members** — one to Faheem Ahmed, one to Dr R. Kaur | **P0 — regression** |

#### 🔴 Routing failures

| # | Item | Severity |
|---|---|---|
| X12 | **A dermatologist answered an ADHD stimulant monitoring query** (C-238, Dr R. Kaur) | **P0** |
| X13 | **The Governance/ethics chair answered two clinical cases** (C-237 Faheem Ahmed, C-242 Dr A. Okafor). **Governance and clinical panels must not cross** — §4B separation of duties | **P0** |
| X14 | **Two paediatric cases routed to adult panels** — C-247 banded 0-17, and C-248 describing a 15-year-old. `[CONFIRM: does the service accept under-18 cases at all? If yes, a paediatric-competent panel member is required. If no, submission must block it]` | **P0** |
| X15 | **Duplicate case** — C-237 and C-238 are the same "Stable adult ADHD on stimulant" J.M. case submitted to two different panels | **P1** |

#### What is right on this page

- Positioning line: *"Submit and track anonymised cases — case-based education, not advice on a live patient"* ✅
- Submission rule banner: *"Anonymised cases only — age range, presentation and your clinical question. Never include names, dates of birth, addresses or identifiers"* ✅
- Per-response footer: *"Teaching/discussion points — advisory only. The treating clinician remains responsible for the decision."* ✅
- Page footer disclaimer ✅

**The framing is correct throughout. The content underneath it is not** — which is the more dangerous combination, because the page reads as compliant while the cases in it are not.

| # | Item | Severity |
|---|---|---|
| X16 | **Panel response form must be structured, not free text.** Full spec: [MDT-PANEL-RESPONSE-FORM.md](MDT-PANEL-RESPONSE-FORM.md). Mirrors the submission — differential, reasoning, management, referral, teaching points. No field named *diagnosis*, *assessment*, *plan* or *recommendation* | **P0** |
| X17 | **"Agree with the documented triage & plan" must be insufficient.** Three live responses say essentially this and teach nothing. Agreement requires saying what was sound and why | **P1** |
| X18 | 🔴 **No safety escalation route for panel members.** A panel member who reads a closed case and believes the patient came to harm currently has only the teaching box. Needs a separate, always-visible flag routed to the clinical lead — **not** to the submitting clinician in the first instance, and never handled as a discussion point | **P0** |
| X19 | **Response SLA, reassignment and quality sampling.** Unanswered past SLA → reassign within specialty and tell the clinician. Sample responses for quality — a response that only says "agree" is a panel training need | **P1** |
| X20 | **Every response must carry responder name, role and organisation** — required for accountability and for the GPhC peer discussion record | **P1** |

### Round 4 — Session library (21 Jul 2026)

| # | Item | Severity |
|---|---|---|
| S1 | **Only 1 of 5 sessions shows governance sign-off.** "June MDT" shows *signed off by Faheem Ahmed · governance-signed*; the other four show only presenter and tags. Round 2 verified the HOLDING → PII REVIEWED → CONSENT → PUBLISHED pipeline exists — **every published item must display its sign-off, and anything unsigned must not appear here** | **P0** |
| S2 | **Consent scope for images in published sessions is undefined.** Library publication is a **broader consent than case discussion** — [F05](starters/forms/F05-photography-consent.md) treats them as separate (section B education vs section C publication). If a session shows patient photographs, section C consent is required. `[CONFIRM: default should be NO images in published sessions unless separately consented]` | **P0** |
| S3 | **Watching a session generates no CPD record.** The Training page footer states *"MDT sessions you attend also generate reflective material"*, but nothing here does. Should create an **unplanned learning** draft record on completion, with a reflection prompt — same pattern as [CPD-LOG-FIX-SPEC.md](CPD-LOG-FIX-SPEC.md) §3 | **P1** |
| S4 | **87-minute full session recording is unusable.** Higher PII risk than a prepared teaching slot (live discussion), and nobody watches it end to end. **Chapter it, or extract the teaching segments and publish those**, retaining the full recording for reference. `[CONFIRM: is a full live session published at all, or only extracted segments? A full session is also far harder to PII-review]` | **P1** |
| S5 | **No filtering despite full tagging.** Every entry carries tags (adhd · psychiatry · dermatology · safety · governance · documentation) and the only route in is free-text search. Add tag and specialty filters | **P2** |
| S6 | **Session date vs publish date ambiguous.** "June MDT" is dated **1 Jul 2026**. Show both, or label which is displayed | **P2** |
| S7 | **No description, chapters, learning outcomes or watched-state.** Title, presenter, tags and duration only. `[CONFIRM: minimum metadata per session]` | **P2** |
| S8 | **No PII reviewer attribution.** The pipeline requires a mandatory human PII review before publish (§5.10). Who did it, and when, should be visible alongside the governance sign-off | **P2** |
| S9 | `[CONFIRM: retention and consent duration. Panel members consented to a recording being published — is that indefinite? Can a panel member withdraw consent for a published session later?]` | **P2** |

#### What is right on this page

- **The titles are genuinely good** — *"Writing notes for the inspection you hope never comes"*, *"Safety-netting that actually protects you"*. Most clinical CPD libraries read like a filing cabinet; these read like something a clinician would click
- **"Facial rashes: rosacea, acne or something else"** is the correct form of that content — same clinician, same topic as the C-241 breach, but as **general teaching** rather than a diagnosis on a live patient. Worth keeping as the reference example of the boundary working
- Footer states the consent, anonymisation and sign-off requirement clearly ✅
- Named attribution and tagging present throughout ✅

### Round 4 — Panel portal · My assigned cases (21 Jul 2026)

Dr R. Kaur's view. Confirms several clinician-side findings from the panel end, and adds four new ones.

| # | Item | Severity |
|---|---|---|
| **P1** | 🔴 **"Agree with the documented triage & plan" is a canned one-click chip**, not typed text. **The product is offering the useless response as the path of least resistance**, and two cases used it. Either remove it, or make it a starting point that still requires the *"what was sound, and why"* free text. See [MDT-PANEL-RESPONSE-FORM.md](MDT-PANEL-RESPONSE-FORM.md) §2 | **P0** |
| **P2** | 🔴 **Mis-routing is actually mis-tagging at source.** *"Stable adult ADHD on stimulant — monitoring query"* carries a **DERMATOLOGY** tag, which is why a dermatologist received it. **Fixing the router will not fix this** — the tag is wrong before routing runs. Check how the specialty tag is assigned at submission | **P0 — changes where to look for X12** |
| **P3** | **"URGENT" flag is inconsistent with the closed-case model.** If cases must be concluded episodes, nothing about them is clinically urgent — the patient has already been managed. An urgency flag implies someone is waiting on an answer to act, which is the wrong model. Remove it, or redefine as *"panel member is waiting"* not *"patient is waiting"* | **P1 — positioning** |
| **P4** | **Response box is a single free-text field.** Confirms X16 from the clinician side. The placeholder text is well written — *"Teaching/discussion points… cite the guidance to verify against; no patient-specific directives, no doses"* — **but nothing enforces it**, which is exactly how *"Consistent with rosacea"* got typed | **P0** |
| **P5** | **Same responder shows two different roles** — *"Dr R. Kaur · Dermatology"* on C-241, *"Dr R. Kaur · Panel member"* on C-240 and C-239. Confirms M4, and it breaks the GPhC peer discussion record, which needs a consistent role and organisation | **P1** |
| **P6** | **A dermatologist has "2 content to review · governance."** Crosses the clinical/governance separation (§4B). `[CONFIRM: what governance content is assigned to clinical panel members, and why]` | **P1** |
| **P7** | **No response SLA or deadline** on any assigned case. Submitted dates are shown; nothing indicates when a response is due. See [MDT-PANEL-RESPONSE-FORM.md](MDT-PANEL-RESPONSE-FORM.md) — Admin and quality | **P1** |
| **P8** | **Stats card reads "4 Answered · last 3 months"** but three answered cases are visible. `[CONFIRM: counting logic]` | **P2** |

#### ✅ Better than assumed — images are partly built

The rosacea case displays **"CLINICAL PHOTOS · CONSENTED · METADATA STRIPPED."**

**Consent flagging and EXIF stripping already exist** — that is most of [MDT-CASE-SUBMISSION-SPEC.md](MDT-CASE-SUBMISSION-SPEC.md) §6 already in place. Two gaps remain:

- **Consented to what?** [F05](starters/forms/F05-photography-consent.md) separates section B (professional education) from section C (publication). The badge does not distinguish them, and the distinction determines whether the image may appear in the Session library
- **Who attested, and when?** The attestation must be logged against the clinician's name, role, registration number and timestamp

#### Also observed

- The co-pilot's documentation-gap warnings (*"⚠️ No distribution, extent, or morphological detail of rash documented"*) are embedded in the case text sent to the panel. `[CONFIRM: intended? It is arguably useful teaching context, but it is noisy and it shows the panel member the submitting clinician's documentation deficiencies]`
- Banner states **"Synthetic data only"**, yet the cases contain *"J.M."* initials and unfilled test strings. If genuinely synthetic this is presentational only — but the anonymiser gaps still need fixing before real use
- *"Cases routed to you — advisory input only"* — `[CONFIRM: "advisory" is doing a lot of work here. "Teaching input only" is closer to the positioning and further from the device line]`

### Round 4 — Panel portal · Available tasks (21 Jul 2026)

#### ✅ Round-2 P0 FIXED — credential gating

Round 2 found members ACTIVE with *"Registration/PIN missing / DBS pending"*. **Now properly gated:** tasks hidden, the four missing items named (Registration/PIN · signed contract · DBS · indemnity), with a clear statement of what unlocks. **Genuine fix, well implemented.**

| # | Item | Severity |
|---|---|---|
| **A1** | 🔴 **The credential gate is applied to task claiming but NOT to case answering.** Dr Kaur is blocked from claiming tasks for missing Registration/PIN, contract, DBS and **indemnity** — yet holds **3 assigned cases and has answered 3 more**, including *"Consistent with rosacea."* The banner states case answering is gated. **It is not.** Answering a clinical case is the higher-risk activity, and an uncredentialed member without indemnity has given what reads as a diagnosis. **A partial fix that presents as a complete one** | **P0** |
| A2 | **No self-serve route to complete credentialing.** *"Ask the admin to complete your record"* — no upload, no form, no progress indicator, no timescale. **DBS and indemnity certificates are the member's to supply** and should be uploadable, with the admin verifying rather than collecting. Otherwise onboarding stalls on email chasing | **P1** |
| A3 | **Fee bands still unset?** Page promises *"claim at the fixed fee shown"* but no tasks exist to check. `[CONFIRM: have the five §4B fee-band figures been set? Outstanding since round 3]` | **P1 — decision** |

#### What is right

- Info banner is **§4B implemented near-verbatim** — fixed fees, admin-set, **no bidding**, tag-gated eligibility, claiming records the reviewer's name ✅
- Footer states the separation-of-duties rule correctly: *"One item → one owner → one sign-off gate. High-risk items still require an independent clinical-lead sign-off after your review."* ✅
- Honest empty state rather than fabricated content ✅

### Round 4 — Panel portal · Governance review, Sessions, Panel directory (21 Jul 2026)

#### ⭐ Governance review — the best screen in the build

*"Open the source link and confirm the passage is really there (**the quote alone is not evidence**)"* — six recommendations paired with source passages, working link-outs, and sign-off gated until every item is verified. **The round-2 gold-standard item, still working.**

**Two things follow from this:**

1. **This is the pattern Ask Clinickly should use.** It is the strongest available evidence that grounded-and-cited output is buildable here — because it is already built, on this screen
2. **It has something real to catch.** Recommendation 2 states *"daily SPF 30+"*; the quoted source says only *"advise sun protection."* **The SPF 30+ is an extrapolation beyond the source.** A useful live test of whether reviewers are reading or ticking. `[CONFIRM: keep this as a deliberate test case?]`

| # | Item | Severity |
|---|---|---|
| **G1** | 🔴 **Panel directory shows all eight members ACTIVE — including Dr R. Kaur, who is uncredentialed** (missing Registration/PIN, contract, DBS, indemnity). **The round-2 credential-gating P0 is only one-third fixed:** claiming is gated ✅ · **case answering is not** ❌ · **ACTIVE status is not** ❌. The badge asserts something untrue. Should read **PENDING VETTING**, and her cases should not be assignable | **P0 — extends A1** |
| **G2** | 🔴 **The Saturday session date is provably a bug.** The other two sessions are **30 Jun** and **26 May 2026** — **both Tuesdays**. August is **15 Aug — a Saturday**. Not a deliberate weekend session; an anomaly against an established pattern | **P0 — extends M2** |
| **G2a** | 🔴 **Second date conflict for the same session.** Session library shows the June MDT as **1 Jul 2026**; panel Sessions shows it as **30 Jun 2026**. **Same session, two dates, two screens** — the schedule is still not single-sourced, on a third surface | **P0** |
| **G3** | **Clinical and Governance panels are merged in the directory.** MDT overview presents them as two separate lists; the panel directory shows all eight under *"The panel"*, including Okafor and Hale from Governance. **Undercuts §4B separation of duties** and is likely related to P6 (a dermatologist holding governance content to review) | **P1** |
| G4 | Confirmed for the third time: **Dr P. Word** and **Ep Och** (M1), and **J. Hale as a second Chair** (M3) | **P0 / P1 — see M1, M3** |

#### Also right on these screens

- Sessions page footer restates the consent, anonymisation and governance-sign-off requirement ✅
- Panel directory footer correctly points membership and login management at the admin console ✅
- The escalation recommendation in the Rosacea draft reads *"Doses and cautions from the BNF, not this summary"* — **exactly the RED-LINES discipline, in the content itself** ✅

### Round 4 — Admin console · Overview (21 Jul 2026)

| # | Item | Severity |
|---|---|---|
| **AD1** | 🔴 **The item awaiting clinical-lead signature was reviewed by an uncredentialed panel member.** *"Dermatology note template v2 — AI-drafted · reviewed by Dr R. Kaur"* with a live **Sign off** button. Dr Kaur has no Registration/PIN, no signed contract, no DBS and **no indemnity**. **The credential gap has propagated into the governance chain** — the sign-off would rest on a review by someone the system itself flags as unvetted. Reviews by uncredentialed members must not reach the sign-off queue | **P0 — extends G1** |
| **AD2** | 🔴 **The 28-policy library has no home.** Four content libraries exist: Guidelines · SOPs & templates · Training · Regulatory standards. **None is a policy library.** SOPs are clinic-specific by design; governed policies are a distinct content type with their own versioning, theme mapping and completeness check. `[CONFIRM: add a fifth library, or restructure. This blocks loading the starters]` | **P1 — structural** |
| AD3 | **"8 Panel members" counts the two test entries** (Dr P. Word, Ep Och). Real figure is 6 | **P1 — see M1** |
| AD4 | **"Training: 6 modules"** — should be **10** per [TRAINING-CATALOGUE.md](TRAINING-CATALOGUE.md): six leading to MEDLRN diplomas plus four standalone | **P1** |
| AD5 | **"⚡ Urgent case C-244"** — urgency flag again, on the case with the age-band contradiction (banded 18-29, text says 30-year-old). See P3 and X4 | **P1** |
| AD6 | `[CONFIRM: "3 Active clinicians across clinics" — has the round-2 finding on unscoped gmail clinician accounts and open signup been addressed? Not assessable from this screen — check Users & clinics]` | **P1** |

#### ✅ Genuinely good

**"C-248 — Other — has no active panel member — assign someone."** The system **detected a case nobody is able to answer and surfaced it to the admin**. That is the M5a problem catching itself, which is exactly the behaviour wanted. Keep it, and extend it: the same check should run at submission so the specialty cannot be selected in the first place.

Also right: the governance pipeline statement — *"All libraries are governed: AI-drafted → MDT-reviewed → human-signed → versioned"* — matches §8 and is displayed where it matters ✅

### Round 4 — Admin console · Governance sign-off (21 Jul 2026)

| # | Item | Severity |
|---|---|---|
| **GS1** | 🔴 **Test content is PUBLISHED and live in the clinician library.** *"R3 sign test"* (v1) and *"Impetigo first-line — cross-machine E2E"* (v1), both **signed by Faheem Ahmed** on 7 Jul and listed under *Recently published — live in the clinician library*. Both were on the round-2 purge list. **This is not test data sitting in a queue — it passed the full governance pipeline, received a human signature, and is now clinician-facing.** The page footer states *"nothing reaches clinicians without it"*; these reached clinicians **with** it | **P0 — worst instance of the test-data regression** |
| **GS2** | 🔴 **Three governed documents signed in the same minute, at 02:50.** ADHD titration note template · Consent & confidentiality SOP v2 · NICE NG87 (ADHD) update — all *"signed by Faheem Ahmed · 9 Jul 2026, 02:50"*. **The audit trail now records a pattern that reads as rubber-stamping**, on the exact artefact that would be produced to demonstrate the governance is real. If seeded, regenerate with plausible, spread timestamps. If real behaviour, **the flow must make bulk-signing impossible** — one item, one deliberate action | **P0 — evidential** |
| **GS3** | 🔴 **Sign-off is available for content reviewed by an uncredentialed member.** Confirms AD1 and G1 — *"reviewed by Dr R. Kaur"*, who has no Registration/PIN, contract, DBS or indemnity. **Reviews by unvetted members must not reach this queue** | **P0** |
| **GS4** | **"Flag stale" is manual, and no published item shows a review date.** Nothing expires automatically. This is the C029 document-control gap and Rule 11 of [COMPLETENESS-CHECK-SPEC.md](COMPLETENESS-CHECK-SPEC.md) — **the corpus review found guidance up to twelve years out of date precisely because nothing told anyone it had expired.** Every published item needs an issue date, a review date, and automatic flagging | **P1** |
| **GS5** | **No "send back" or reject path from the sign-off queue** — only *Sign off*. Round 2 verified flag-back-with-reason exists elsewhere; it is absent here. `[CONFIRM: what happens when the clinical lead disagrees with the reviewer?]` | **P1** |
| GS6 | **Reviewer role and registration not displayed** — *"reviewed by Dr R. Kaur"* with no role or registration number. Both matter for an audit trail and for the peer-discussion record | **P2** |

#### What is right

- **MEDIUM RISK · CLINICAL MDT** tags — §4B risk-tiering visible on the item, and a medium-risk item correctly took a single reviewer ✅ `[CONFIRM: do high-risk items actually enforce two-person sign-off? Not observable here]`
- Version numbers throughout (v1, v2, v3) ✅
- Pipeline statement accurate and well placed: *"Every step is audit-logged (AI draft, reviewer, signer, when). Signing is a named, dated clinical-lead action."* ✅

### Round 4 — Admin console · Panel management (21 Jul 2026)

**This screen explains the credentialing findings across the whole review.** It is not a Dr Kaur problem.

| # | Item | Severity |
|---|---|---|
| **PM1** | 🔴 **All eight panel members are unvetted, all show ACTIVE, and they hold 14 open cases between them.** Every card carries *"Registration/PIN missing · Contract not signed · DBS pending · Indemnity pending · **Vetting incomplete — cannot claim/review**"* — and every card shows **ACTIVE**. Kaur, Newman, **Word** and **Och** hold **3 open cases each**; Mehta and Bright 1 each. **Six of those cases are held by two people who do not exist.** The badge prints *"cannot claim/review"* beside a member holding three cases: **the system detects the state and does not enforce it** | **P0 — root cause of A1, G1, AD1, GS3** |
| **PM2** | 🔴 **Cases have been waiting 11–15 days.** `URGENT · 11D`, `SOON · 15D`, most others 13–15 days. Nobody can answer them because nobody is vetted — **the SLA badges are counting up against a structurally blocked panel** | **P0** |
| **PM3** | 🔴 **"Other" cases route to Governance/ethics (Chair).** This is why C-248 reports *"No active panel member can see this case."* A clinical case is routed to a **governance** specialty, which under §4B must not receive clinical cases at all | **P0 — root cause of X13, X14, M5a** |
| **PM4** | 🔴 **Duplicate case, two different specialties.** C-236 *"Stable adult ADHD on stimulant"* → **Dermatology**; C-237, the same case → **General practice**. Neither is correct. Confirms P2 (mis-tagging at source) and X15 | **P0** |
| PM5 | **Register defaults to GMC for every member**, including Dr N. Newman (Pharmacy & prescribing), who requires **GPhC**. The register must follow the member's profession | **P1** |
| PM6 | **CV is a free-text filename field, not an upload** — *"e.g. cv-j-example.pdf"*. It records the name of a file held elsewhere, which is not a file record | **P1** |
| PM7 | **No expiry dates on DBS or indemnity.** Both capture a "checked/confirmed" date with no renewal date, so **nothing ever triggers re-verification.** C025 requires annual registration and indemnity re-checks and DBS renewal | **P1** |
| **PM8** | 🔴 **CONFIRMED (Faheem, 21 Jul): a member can be added with a name alone.** No credentialing required, and they land **ACTIVE** immediately. **This is the root cause of the entire credentialing failure** — the vetting block displays what is missing and then lets them straight through. **Adding a member and activating one are currently the same action.** They must be separated — see below | **P0 — root cause** |

#### PM8 — the fix: adding ≠ activating

Creating a member record before their DBS certificate arrives is normal and must stay possible. What must change is **where they land**.

| | Added (name only) | Activated |
|---|---|---|
| Member record exists | ✅ | ✅ |
| Status shown | **PENDING VETTING** | ACTIVE |
| Can be assigned cases | ❌ | ✅ |
| Can log in and answer cases | ❌ | ✅ |
| Can claim tasks | ❌ | ✅ |
| Appears ACTIVE in the panel directory | ❌ | ✅ |
| Their review can reach the governance sign-off queue | ❌ | ✅ |

**Activation is a separate, deliberate admin action**, available only once register, registration/PIN, signed contract, DBS and indemnity are all recorded — never a side effect of creating the record.

`[CONFIRM: what happens to the 14 open cases currently held by unvetted members when this is enforced. They cannot simply vanish. Recommend: return to the unassigned pool, notify the submitting clinicians of the delay, and prioritise vetting the four real members who hold them.]`

#### ✅ Fee bands are set — closes a round-3 open item

| Task type | Complexity | Fixed fee |
|---|---|---|
| Content review — minor | Low | **£25** |
| Content review — standard | Medium | **£60** |
| Content review — high-risk clinical | High | **£120** |
| Case answer (teaching/CPD) | Medium | **£45** |
| SOP / governance review | High | **£90** |

Coherent against the §4B £150/hr sessional anchor. **£45 for a case answer is generous for a 10-minute structured response** — which is the right direction, since it buys considered answers rather than *"agree with the plan"*.

#### Also right

- `ADMIN-SET · NO BIDDING` badge, and the rationale stated in full: *"an upfront fixed fare, never an auction. Bidding is rejected for anything that gets signed off (drives quality and accountability down). Edits are audit-logged."* — **§4B verbatim** ✅
- Add-member form is well designed: §4B **one domain** enforced in the panel dropdown, verified tags explicitly gating claims, credentialing block labelled **"THE VETTING GATE"**, honest note that register lookup is a licensed integration recorded manually in the prototype ✅
- Login email provisions a real account with a one-time password to hand over ✅
- Case assignment correctly described as **overriding** specialty routing and audit-logged ✅

### Round 4 — Admin console · MDT schedule (21 Jul 2026)

**This screen fully diagnoses the schedule bug reported since round 2.**

| # | Item | Severity |
|---|---|---|
| **MS1** | 🔴 **The admin schedule is correct; the clinician and panel views are wrong.** Admin: **28 Jul 2026**, rule *"Last Tuesday monthly"*, auto-advancing — **verified: 28 Jul 2026 is a Tuesday and is the last Tuesday of July.** The clinician MDT overview and the panel Sessions page both show **15 Aug 2026, a Saturday**. **Practical effect: a clinician is told the next session is 15 August when it is actually 28 July — they miss it, then turn up on a Saturday.** The recurring rule works; the downstream views are not reading from it | **P0 — diagnosed, resolves M2/G2** |
| **MS2** | 🔴 **All three recording gates signed by the same person.** *"PII review: Faheem Ahmed. Consent confirmed: Faheem Ahmed. Signed off: Faheem Ahmed."* The pipeline HOLDING → PII REVIEWED → CONSENT CONFIRMED → PUBLISHED is designed as a chain of **independent** checks; with one person doing all three it is **one check labelled three times**. An 87-minute recording of live discussion is the highest-PII-risk content in the product, and §4B requires two people on high-risk items | **P0** |
| **MS3** | 🔴 **The agenda auto-pulls the test cases.** *"Case discussion — 9 open cases (auto-pulled)"* — those nine include **ddd**, **Case-loop E2E one/two** and **R3 notif case**. They would appear on a live MDT agenda | **P0 — resolved by the Tier 1 purge** |
| **MS4** | **Recording date and session date are displayed identically and unlabelled.** The June recording is dated **1 Jul** (recorded/published); the session was **30 Jun** (last Tuesday). Both fields are correct for what they hold — but shown without labels, the same session appears to have two dates. **This is the source of the session-library discrepancy (G2a).** Label them: *session date* vs *published* | **P1 — resolves G2a** |

#### ✅ Genuinely good on this screen

- **The recurring-rule design is right:** date auto-advances on the rule, an override applies to the **next session only** and is **audit-logged**. That is the correct shape — the bug is downstream consumption, not the rule ✅
- **Four-stage recording pipeline visible with named actors at each stage** — the structure is right even though one person currently fills all three roles ✅
- `PRIVATE UNTIL SIGNED OFF` badge ✅
- **The PII footer is the best-written warning in the build:** *"Video leaks PII in ways you cannot auto-strip — spoken names, shared screens, faces and badges. Published recordings play embedded with signed URLs (Bunny Stream — licensed integration); prefer audio-only or slides+voiceover for sensitive content."* Honest about the limits of automation, and the audio-only recommendation is real advice rather than reassurance ✅
- **Promote to training module** present, connecting §5.10 to the training catalogue ✅

### Round 4 — Admin console · Content libraries (21 Jul 2026)

#### ⭐⭐ The grounded-generation model is fully built

The **New item** form implements the entire RED-LINES position as a form:

> **DRAFT FROM SOURCE (GROUNDED — EVERY STATEMENT CARRIES ITS PASSAGE + LINK)** · Source reference · **Source URL (the reviewer verifies against this)** · Retrieved source text — *"Each paragraph becomes one draft statement bound to its passage — never drafted from memory."*
>
> *"**We never draft clinical content from AI memory — only from retrieved source text, cited per statement.**"*

Plus **risk tier drives the sign-off path** (*"Medium — reviewer + independent sign-off"*) — §4B tiering wired into the workflow, not a label.

**This is the second place the correct grounded pattern exists** — alongside the governance review verification screen. **It materially reframes the Ask Clinickly P0: the work is not "build grounded retrieval", it is "point the mechanism that already exists at a third feature."**

| # | Item | Severity |
|---|---|---|
| **CL1** | **"ear ache" — SOP routed to Governance/ethics (Chair).** Clinical content sent to governance for review. **Same root cause as PM3.** Title also reads as test input | **P0 — see PM3** |
| **CL2** | **"Dermatology note template v2 · claimed by Dr R. Kaur" — REVIEWED, AWAITING SIGN-OFF.** Third screen showing an unvetted reviewer one click from published | **P0 — see PM1** |
| **CL3** | **"SOPs & templates" conflates two opposite content models.** Per `CLINICKLY-MASTER.md` §5.7: **SOPs are clinic-specific by design and are meant to differ; note templates are central, standard and must not fork.** They share one library and one GOVERNED badge. **Policies would be a third model** (governed, standard, same-for-all, theme-mapped). This is the real shape of AD2 — not simply "policies need a home", but that the library already carries incompatible rules. `[CONFIRM: restructure into Guidelines · Note templates (central) · SOP starters (clinic-specific) · Policies (governed) · Training · Regulatory standards]` | **P1 — structural** |
| CL4 | **Training shows 6 modules** — should be 10 per [TRAINING-CATALOGUE.md](TRAINING-CATALOGUE.md) | **P1 — see AD4** |
| CL5 | `[CONFIRM: "Consent & confidentiality SOP v2" is PUBLISHED at **high risk**. §4B requires two-person sign-off for high-risk items. Did it receive one, given governance sign-off shows a single signer throughout?]` | **P1** |

#### Also right

- *"'Request an SOP/template' submissions from clinics arrive here as drafts. Every transition is audit-logged"* — the §5.7 clinic request route, working ✅
- *"Leave empty to create a bare shell (it will demand sources before review)"* — a bare shell is permitted but cannot progress without sources. Exactly the right compromise ✅
- *"Nothing publishes until the MDT has verified every statement against its linked source and the clinical lead signs off (risk-tiered separation of duties)"* ✅

### Round 4 — Admin console · Regulatory standards (21 Jul 2026)

#### ✅ Round-2 fix — honest labelling of what the gap-check actually does

Every entry carries **"REFERENCE ONLY — NOT YET RAG-INGESTED"**, and the footer states plainly: *"parsing/chunking the document text for AI gap-checks (RAG ingestion) is the licensed-integration step — until then **the gap-check runs on the deterministic theme checklist**."*

Round 2 asked for the clinic-facing claim to be relabelled until the capability was real. **Done properly.** The product now describes what it actually does rather than implying analysis it is not performing.

Also right: **GPhC is listed first** — appropriate for a product whose source corpus contained the GPhC in **0 of 119** documents. Upload correctly restricted to central admin/governance ✅

| # | Item | Severity |
|---|---|---|
| **RS1** | **GPhC is only half loaded.** *Standards for Pharmacy Professionals* (the nine standards) is present; ***Standards for Registered Pharmacies*** (the five principles — governance, staff, premises, pharmacy services, equipment) **is not**. **Every starter policy maps to both** — e.g. *"GPhC Pharmacy Principle 1 (governance)"* — so the theme mapping cannot be verified against a source that is not loaded. See [REGULATOR-MAPPING.md](REGULATOR-MAPPING.md) | **P1** |
| **RS2** | **"NHS — Information governance" is not a citable document.** Which one — the Data Security and Protection Toolkit, the Records Management Code of Practice, something else? **This is the exact defect Rule 8 of [COMPLETENESS-CHECK-SPEC.md](COMPLETENESS-CHECK-SPEC.md) exists to catch** (the corpus review flagged *"British Medical Association"* and *"NHS England"* for the same reason) — now present in the regulatory standards library itself | **P1** |
| **RS3** | **No edition, version or date on any entry.** *"GPhC — Standards for pharmacy professionals"* — which edition? *"CQC — Fundamental standards"* — as amended when? **This is precisely how the source corpus reached twelve years out of date.** Each entry needs: title · publisher · **edition** · publication date · URL · date loaded · **date last checked**. Without them, *"review due ~3-monthly"* has nothing to review against | **P1** |
| **RS4** | **The MHRA entry is the wrong MHRA material for the biggest regulatory risk.** *"Drug safety updates"* is the monthly prescribing bulletin — useful, but **the material `RED-LINES.md` depends on is the software / medical-device guidance**: the classification flowchart, *Crafting an intended purpose*, and the Medical Devices Regulations 2002. Given the device boundary is the largest regulatory exposure in the product, those belong here | **P1** |
| RS5 | `[CONFIRM: which further standards are in scope. Candidates already cited across the 28 starters: GPhC guidance on providing pharmacy services at a distance (C039/C040) · NICE · GMC Good Medical Practice 2024 and Decision making and consent 2020 · UK GDPR / DPA 2018 · Resuscitation Council UK Guidelines 2021 · Records Management Code of Practice]` | **P2** |
| RS6 | **"Review due ~3-monthly" with no last-reviewed date shown.** Same pattern as the manual "Flag stale" on published content (GS4) — a cadence with nothing recording when it last happened | **P2** |

### Round 4 — Admin console · Users & clinics (21 Jul 2026)

#### ✅ Round-2 fix — two-tier tenancy is now built

*"Each clinic is an isolated tenancy — its clinicians and patients see only their own clinic's data. Panel members and admins are platform (central) scope unless assigned to a clinic."*

Round 2 found tenancy and clinics management conflated. There is now a clinics list, an add-clinic route, per-user scope selection and a clear statement of the isolation rule. **Proper fix, and the harder half of the problem.**

| # | Item | Severity |
|---|---|---|
| **UC1** | 🔴 **Two unknown accounts still hold the CLINICIAN role.** `bksLQkfUfNDDhqBEmGMxn` / **i.ber.af.i.r.ura.761@gmail.com** and `lfLDHKraqPRxXeBJW` / **d.ot.og.oxira.0.3@gmail.com**. Raised in round 2; unchanged. **They look worse on inspection:** display names are random strings, and both addresses use **Gmail dot injection** (`i.ber.af.i.r.ura.761`, `d.ot.og.oxira.0.3`) — Gmail ignores dots, so that pattern makes one address present as many. **This is automated signup behaviour, not a mistyped name.** Two unknown parties currently hold a clinician role | **P0 — regression** |
| **UC2** | 🔴 **Open signup is still open.** UC1 is the evidence. **Deleting the two accounts without closing self-registration only means new ones appear.** Require invite-only provisioning, or admin approval plus a real display name and a verified professional email domain. **This is the only finding in the entire review where the system is exposed to people outside the project** — recommend doing it before anything else on the list | **P0 — regression** |
| **UC3** | **The scope display contradicts itself.** Dr A. Demo shows *"Clinickly Demo Clinic"* in the description line and **"No clinic — pick one"** in the scope dropdown. Two fields asserting different things about the same user. `[CONFIRM: which is authoritative, and what the description line is actually showing — creating clinic vs assigned scope?]` | **P1** |
| **UC4** | **Clinic counts do not reconcile.** *"Clinickly Demo Clinic — 3 clinicians · 7 patients · 6 staff"*, but only one clinician in the user list is scoped to that clinic and **no staff users appear at all**. `[CONFIRM: what these counters count]` | **P1** |
| UC5 | **Auto-generated test emails confirm seeded accounts** — `pw1783424985@clinickly.test` and `epoch1783429322@clinickly.test` are Unix timestamps. Removed with Word and Och in the Tier 1 purge | **P1 — see M1** |
| UC6 | **`newdoc@clinickly.test` for Dr N. Newman**, a *Pharmacy & prescribing* panel member. Test artefact, and reinforces the doctor-centric naming found throughout the corpus | **P2** |

### Round 4 — Admin console · Reports & audit (21 Jul 2026)

#### ✅ Round-2 fix — demand analytics is fully built

Round 2 found only the missed-searches box, with logging unverified. **All four signals now exist:** top successful searches · most-opened guidelines · **pointer-entry opens (promotion signal)** · **Ask Clinickly question themes** · plus **SOP demand as builds-vs-requests**.

And **"Add to authoring backlog"** on each missed search — *"confirm the differential for ear ache"* routing straight into the content pipeline. **That is the demand loop working end to end.** Substantial fix.

The audit trail itself is detailed and correctly shaped: actor, role, action, item and timestamp on every entry ✅

| # | Item | Severity |
|---|---|---|
| **RA1** | 🔴 **The service-level metrics contradict the case data.** Reports show **"0 h avg time to first response"** and **"100% urgent answered within 48h"**. Panel management shows cases waiting **11–15 days**, with the urgent case **C-244 waiting 11 days**. **A report that states the opposite of the underlying data is worse than no report** — this is the artefact that would be produced to demonstrate the service works | **P0** |
| **RA2** | 🔴 **Three further internal contradictions.** *"5 clinicians · 3 clinicians"* in one line · **Reviewer workload shows Dr R. Kaur at 0 in review** while Content libraries shows her holding the Dermatology note template awaiting sign-off · **Audit trail claims "newest first"** but runs 11:37 → 11:07 → 13:00 | **P0** |
| **RA3** | 🔴 **Unknown clinician accounts hold SOP sign-off authority.** The audit trail records **"ddd (clinician)"** signing off *Private prescribing SOP v1*, and **"Kazoom (clinician)"** signing off SOPs for **Riverside Pharmacy Clinic** and **Demo pharmacy clinic**. **Neither clinic appears in Users & clinics**, which lists only Clinickly Demo Clinic. *"ddd"* is therefore not only a test case but a **user with sign-off rights**. Connects to UC1/UC2 (open signup) and the round-2 duplicate-Riverside-SOPs finding | **P0** |
| **RA4** | 🔴 **Deactivation does not stick, and the audit trail has a silent state change.** Dr A. Okafor was **deactivated twice** (11:07 and 13:00) and still shows **ACTIVE** on every screen. Either the action fails, or something reactivated him **with no audit entry**. Also: **"Ep Och (panel) Changed own password"** — a test account with a live session | **P0** |
| **RA5** | **"Activity trends" renders twice**, each with its own filters and Export CSV. Same class as the round-2 Rosacea duplicate-section render | **P1** |
| RA6 | `[CONFIRM: "Governance health — 1 items published in range · 0d avg days since published", and a flagged item "R3 flag test pipeline · high risk · in review 14d · Unclaimed". A high-risk item unclaimed for 14 days should escalate, not sit in a report]` | **P1** |
| RA7 | **Team CPD roll-up not built** — *"team roll-up reporting arrives with the CPD formats build"*. Honest labelling, and correctly sequenced behind [CPD-LOG-FIX-SPEC.md](CPD-LOG-FIX-SPEC.md) | **P2 — noted, not a defect** |

#### The pattern on this screen

**Every number that could be checked against another screen disagreed with it.** Service levels, clinician counts, reviewer workload, audit ordering, and activation state. The reporting layer is not reading from the same source as the operational screens — which is the same root cause as the schedule bug (MS1), where the admin rule was correct and two downstream views were not reading from it.

`[CONFIRM: is there a single source of truth for these counters, or is each screen computing its own?]`

---

# Round 4 — complete

**Twelve screens reviewed, 21 Jul 2026.** Clinician portal · panel portal · admin console.

**Start here:** [FIX-SEQUENCE.md](FIX-SEQUENCE.md) — the items below sequenced into Tier 0 → Tier 4.

## What was genuinely fixed since round 2

| | |
|---|---|
| **Credential gating** | Built and well presented — though only applied to task claiming (see PM1) |
| **Two-tier tenancy** | Clinics list, add-clinic route, per-user scope, isolation rule stated |
| **Demand analytics** | All four signals, plus add-to-backlog routing |
| **Honest RAG labelling** | *"REFERENCE ONLY — NOT YET RAG-INGESTED"* rather than overclaiming |
| **Fee bands** | Five bands set, coherent with the §4B rate anchor |

## What is excellent and should not be changed

- **Governance review** — source passage beside every recommendation, working link-out, sign-off gated until all verified. *"The quote alone is not evidence."*
- **Content libraries → New item** — *"We never draft clinical content from AI memory — only from retrieved source text, cited per statement."*
- **The MDT schedule PII footer** — honest about what automation cannot strip, and recommends audio-only for sensitive content
- **The framing on every screen** — positioning lines, disclaimers, anonymisation banner, §4B implemented near-verbatim

**The grounded, cited, verify-before-publish pattern is already built twice.** The Ask Clinickly rescope is pointing an existing mechanism at a third feature, not building one.

## The three root causes

Most of the ~60 items trace back to three things:

1. **Adding a panel member and activating one are the same action** → all eight members unvetted-but-ACTIVE, holding 14 cases; uncredentialed reviewers reaching the sign-off queue
2. **"Other"/unassigned content routes to Governance/ethics** → clinical cases to governance, cases nobody can answer, an "ear ache" SOP in the governance queue
3. **Downstream views do not read from the source of truth** → the Saturday session date, contradictory service levels, reviewer workload, clinician counts

## The pattern

**The framing is right everywhere. The enforcement is not.** Every screen says the correct thing; the structure does not yet make it true. That is a far better position than the reverse — but it is the whole of the remaining work.
