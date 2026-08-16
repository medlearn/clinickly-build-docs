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
