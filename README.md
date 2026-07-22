# Clinickly Co-pilot — build review & developer handover

**Round 2 (Jul 2026): start with ROUND-2-SUMMARY.md** — scorecard + round-3 priority order.
Then work DEVELOPER-FIX-LIST.md top-down (unticked items only; [x] = verified fixed).
CLINICKLY-MASTER.md is the spec (updated with all decisions). BUILD-REVIEW*.md = screen-by-screen evidence.

---

## 🆕 Governed policy library — COMPLETE (21 Jul 2026)

**[`/starters/`](starters/) — 28 policies + [4 governed forms](starters/forms/), all APPROVED v1.0.** This is the content a new clinic receives on day one. Build the onboarding questionnaire against these, not placeholders.

**[COMPLETENESS-CHECK-SPEC.md](COMPLETENESS-CHECK-SPEC.md) — new P1 feature.** Eleven rules, every one derived from a real defect found in a real 119-document corpus that had passed a CQC inspection. This is the check that runs before anything publishes to a clinic.

**[MDT-CASE-SUBMISSION-SPEC.md](MDT-CASE-SUBMISSION-SPEC.md) + [MDT-CASE-FORMAT.md](MDT-CASE-FORMAT.md) — P0.** How case submission and panel response stay outside the medical-device definition, structurally rather than by disclaimer — via a closed-episode gate and a full clerking proforma.

**[RED-LINES.md](RED-LINES.md) — read before building anything.** The medical-device boundary, following the MHRA's response. Non-negotiable.

**Also here:** [REGULATOR-MAPPING.md](REGULATOR-MAPPING.md) (CQC × GPhC × the 24 requirement themes) · [MHRA-RESPONSE.md](MHRA-RESPONSE.md).

### The `[CONFIRM: …]` convention

Every starter contains `[CONFIRM: … Default: …]` fields. **These are the adopting clinic's decisions, not unfinished work.** A policy published with another clinic's safeguarding lead or retention schedule in it is broken for the clinic receiving it.

**The completeness check must block publication while any remain unfilled.** The convention is deliberately ugly so an unfinished field is visible — the corpus defects survived precisely because `Xxxx` looks like text.
