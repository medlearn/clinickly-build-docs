# Field schema — worked example: C05 Consent

**The fix for "the fields are not proper copies of what needs to be there."**

The document has **28 raw `[CONFIRM]` / `[CLINIC NAME]` markers**. But that is NOT 28 fields. Cleaned up, it's **~19 real clinic fields**, because:

- **`[CLINIC NAME]` appears 8 times but is ONE field** — filled once, applied everywhere. (The current UI likely shows it 8 times.)
- **One marker is not a clinic field at all** — it's a governance/editorial note (*"DH Reference Guide is archived; GMC 2020 is operative"*). The clinic should never see it. It needs a different marker.
- **Several fields are decisions with defaults** (the clinic accepts or changes the default), not blank text boxes.
- **Several are conditional** — only shown if a gating question is answered "yes."

This is why a flat auto-extracted "Fields" list is unusable: it de-duplicates nothing, types nothing, and turns prose into labels.

---

## The three things every field needs

| | |
|---|---|
| **Clean label** | A short name, not a sentence fragment |
| **Type** | clinic-name · person · role · date · text · list · decision · duration |
| **Default + help** | What it means, and a sensible pre-filled answer where one exists |

Plus two flags: **decision vs fact**, and **conditional-on** (show only if a gate = yes).

---

## C05 Consent — the clean field set

### Global (fill once, applied everywhere)

| id | label | type | required | help |
|---|---|---|---|---|
| `clinic_name` | Clinic name | clinic-name | ✅ | Registered name of the clinic. Used throughout. **One field, 8 insertions.** |

### Document control

| id | label | type | default | help |
|---|---|---|---|---|
| `responsible_person` | Responsible person | role | Registered Manager / Clinical Lead | Named person accountable for this policy |
| `authorised_by` | Authorised by | person | — | Who signs it off |
| `issue_date` | Issue date | date | — | — |

### Governance note — NOT a clinic field

| marker | treatment |
|---|---|
| *"DH Reference Guide is archived; GMC 2020 is operative"* | **`[NOTE]`, not `[CONFIRM]`.** Editorial reminder for the governance reviewer. **Must not appear in the clinic's fill list.** |

### Policy decisions & facts (the real fill work)

| id | label | type | default | decision? | conditional on | help |
|---|---|---|---|---|---|---|
| `cooling_off` | Cooling-off period (elective/aesthetic) | decision | Yes — min 14 days; never treat at first appointment | ✅ | — | Does any treatment need a gap between decision and procedure? |
| `reconsent_interval` | Re-consent interval | duration | 3 months | ✅ | — | After this long, written consent is re-taken, not just reconfirmed |
| `written_consent_procedures` | Procedures requiring written consent | list | — | — | — | The **real** list of procedures this clinic does — not generic |
| `consent_delegated` | Is consent ever delegated? | decision (yes/no) | No | ✅ | — | Does anyone take consent for a procedure they don't perform? |
| `delegated_consent_owner` | Who maintains the authorised-to-take-consent record | role | — | — | `consent_delegated = yes` | Hidden unless delegation happens |
| `interpreter_service` | Interpreting service & booking route | text | — | — | — | Which professional service, and how to book |
| `accessible_formats` | Accessible-format arrangements | text | — | — | — | BSL route, large print, easy read |
| `info_between_appointments` | Access to information between appointments | text | — | — | — | How a patient gets more detail before deciding |
| `imca_service` | IMCA service & how to instruct | text | — | — | — | Local IMCA; or state the clinic refers serious-medical-treatment decisions on |
| `sees_under_18s` | Does the clinic see under-18s? | decision (yes/no) | — | ✅ | — | **Must match C032.** Gates the young-person fields |
| `young_person_refusal` | Position on a competent young person refusing necessary treatment | decision | Escalate to clinical lead; legal advice if serious; never resolve by asking a parent to sign | ✅ | `sees_under_18s = yes` | — |
| `marketing_images` | Are recordings/images used for marketing? | decision (yes/no) | No | ✅ | — | If yes: explicit, separately signed, freely given, never a condition of treatment/discount |
| `consent_training_refresh` | Consent training refresh interval | duration | 3 years | ✅ | — | — |
| `mca_training_refresh` | MCA training refresh interval | duration | 3 years | ✅ | — | — |
| `training_matrix_owner` | Who holds the training matrix | role | — | — | — | — |
| `audit_owner` | Audit owner & frequency | decision | Clinical Lead, annually | ✅ | — | — |
| `governance_meeting` | Name of the governance meeting | text | — | — | — | Where audit findings are reported |

**Total: 1 global + 3 doc-control + 19 policy fields = 23 clean fields** (vs 28 raw markers, several of which were duplicates, a non-field, or prose).

---

## The marker convention (so extraction is clean going forward)

The reason labels came out as fragments: `[CONFIRM: a printed copy held off-site by a named person]` was written to read in a *document*, not to *be a field*. Fix the encoding:

**Structured marker:**
```
{{field: id=off_site_copy_holder
        label="Off-site copy holder"
        type=person+location
        help="Who keeps the off-site copy, and where"}}
```
or, minimally, `[CONFIRM: label | type | default | help]`.

**And add a separate note marker for governance:**
```
[NOTE: DH Reference Guide is archived; GMC 2020 is operative — confirm at review]
```
→ shown to the reviewer, **never** to the adopting clinic.

**Rule:** one `id` = one field. Repeated insertions of the same `id` (like `clinic_name`) fill once.

---

## What this means for the UI (developer)

1. **Fill inline, DocuSign-style** — the document with highlighted blanks, filled in context, live-rendered. Not a separate blind "Fields" tab.
2. **De-duplicate** — `clinic_name` is one input, not eight.
3. **Types drive the input** — a `date` picker, a `role` field, a `decision` showing its default + accept/change, a `list` builder.
4. **Decisions show their default** — the clinic accepts or overrides; most defaults are already sensible.
5. **Conditionals hide** — don't show `delegated_consent_owner` unless `consent_delegated = yes`.
6. **`[NOTE]` markers never reach the clinic.**
7. **Completeness gate stays** — but it checks *these* fields (Rule 1: no unfilled required field publishes), and it's the gate at the end, not a tab you manage.

---

## Effort for the other 27

Once the marker convention + field types are agreed, the schema for each policy is mechanical to produce — same as authoring the policies was. C05 is the hardest (most fields, most conditionals); the rest are lighter. Estimate: the full set of ~500 fields across 28 policies, cleanly typed, is a day's work once the convention is locked.
