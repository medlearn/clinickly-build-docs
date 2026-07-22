# Round 4 — suggested fix sequence

**~55 items across nine screens.** A list that long gets ignored. This is the order I would work it, and why.

---

## Tier 1 — hours. Do this first.

**Almost all of it is deletion.** It is a day's work, it needs no design decisions, and it will make every subsequent review far cleaner — the real problems are currently buried under test data.

| | |
|---|---|
| Delete test panel members | **Dr P. Word**, **Ep Och** |
| Delete test cases | **ddd** (C-245) · **Case-loop E2E one/two** (C-236, C-239) · **R3 notif case** (C-240) |
| 🔴 **Unpublish test content from the clinician library** | **"R3 sign test"** and **"Impetigo first-line — cross-machine E2E"** — both signed and **live to clinicians**. Highest priority item in this tier |
| 🔴 **Regenerate the 02:50 signature timestamps** | Three governed documents signed in the same minute. The audit trail is the evidence that governance is real; this pattern undermines it |
| Delete gibberish panel responses | C-237, C-238 — both attributed to named members |
| Remove patient initials | **"J.M."** in C-237 and C-238 |
| Remove the canned response chip | *"Agree with the documented triage & plan"* |
| Fix the session date | **15 Aug 2026 is a Saturday**; May and June are both Tuesdays |
| Single-source the schedule | June MDT shows as **1 Jul** (session library) and **30 Jun** (panel sessions) |
| Fix J. Hale's title | Currently a second Chair alongside Dr Okafor |
| Fix Dr Kaur's role label | *"Dermatology"* on one case, *"Panel member"* on two others |

**Then re-share the build.** A clean instance is worth more than another review round on a dirty one.

---

## Tier 2 — days. Gates and routing.

Correctness problems that need code but no new design.

| | |
|---|---|
| **Finish credential gating** | Currently gates task claiming only. Must also gate **case answering**, the **ACTIVE badge** (should read PENDING VETTING), **case assignment**, and **reaching the governance sign-off queue** |
| **Fix specialty tagging at source** | The ADHD case carries a DERMATOLOGY tag. **This is not a routing bug** — the tag is wrong before routing runs |
| **Separate Clinical from Governance** | Merged in the panel directory; a dermatologist holds governance content; the governance chair has answered clinical cases. §4B says they do not cross |
| **Anonymiser: strip precise ages from prose** | *"15-year-old male"*, *"30-year-old"*, *"22-year-old male"* — and reconcile age band against free text |
| **Block or route paediatric cases** | Two currently sitting with adult panels |
| **Self-serve credential upload** | DBS and indemnity are the member's to supply; there is currently no route but "ask the admin" |

---

## Tier 3 — weeks. The forms.

**This is where the medical-device boundary actually gets fixed.** Biggest build, highest value.

| | Spec |
|---|---|
| Case submission — closed-episode gate + clerking proforma | [MDT-CASE-SUBMISSION-SPEC.md](MDT-CASE-SUBMISSION-SPEC.md) · [MDT-CASE-FORMAT.md](MDT-CASE-FORMAT.md) |
| Panel response — structured, no free-text diagnosis | [MDT-PANEL-RESPONSE-FORM.md](MDT-PANEL-RESPONSE-FORM.md) |
| Panel safety-escalation route | [MDT-PANEL-RESPONSE-FORM.md](MDT-PANEL-RESPONSE-FORM.md) §7 |
| CPD — records not minutes, peer discussion typing, consent to be named | [CPD-LOG-FIX-SPEC.md](CPD-LOG-FIX-SPEC.md) |
| Images — which consent (F05 §B vs §C), attestation logging | [MDT-CASE-SUBMISSION-SPEC.md](MDT-CASE-SUBMISSION-SPEC.md) §6 |

**Do case submission before panel response.** A structured response has little to respond to while submissions are still one-liners.

---

## Tier 4 — ongoing. Content and structure.

| | |
|---|---|
| **A home for the 28-policy library** | No existing content library fits. Structural decision needed first |
| **Training catalogue** | 10 modules — six leading to MEDLRN diplomas, four standalone |
| **Completeness check** | [COMPLETENESS-CHECK-SPEC.md](COMPLETENESS-CHECK-SPEC.md) |
| **Ask Clinickly rescope** | Still the biggest open P0 from round 2 |

---

## One thing to say to the developer

**The framing is right on every screen.** Positioning lines, disclaimers, the anonymisation banner, §4B implemented near-verbatim, honest empty states. That is the hard part and it is done.

**And the governance review screen is the best thing in the build** — source passage beside every recommendation, working link-out, sign-off gated until all six are verified, *"the quote alone is not evidence"*. **That is the pattern Ask Clinickly needs.** It is already built; it needs pointing at a different feature.

The gap throughout is not understanding — it is **enforcement**. The words are correct and the structure does not yet make them true.
