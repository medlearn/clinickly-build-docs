# Field schema — C05 Consent (VERIFIED against the source document)

**The fix for "the fields are not proper copies of what needs to be there."**
Every field below is checked against its actual line in `starters/C05-consent.md`. Nothing invented, nothing missed.

## Count reality check

- **28 raw markers** in the document, but that is **21 clean fields + 1 governance note**, because:
  - `[CLINIC NAME]` = **1 field, inserted 8×** (fill once, apply everywhere).
  - One marker (line 30) is a **governance note to the reviewer**, not a clinic field.
  - The rest are real, but need clean labels + types + categories.

## The label MUST come from document structure, not marker text

This is why labels came out as fragments. Three label sources, and the extractor must use the right one:

| Marker form | Where the label comes from | Example |
|---|---|---|
| **Bare** `[CONFIRM]` | the **table-row header** it sits in | line 14 → **"Authorised by"** |
| **Generic** `[CONFIRM: role]` / `[CONFIRM: route]` | the **sentence** around it | line 158 → **"Who maintains the authorised-to-take-consent record"** |
| **Descriptive** `[CONFIRM: named responsible person]` | the marker text (already clean) | line 13 → **"Responsible person"** |

## Three field categories (different interactions)

- **VALUE** — clinic types a specific value.
- **DECISION** — yes/no gate; can hide/show conditional fields.
- **CLAUSE** — a pre-written default paragraph the clinic **keeps or edits** (NOT a blank box — the default is the safe wording).

---

## The 21 fields

### Global
| id | label | category | type | line | help |
|---|---|---|---|---|---|
| `clinic_name` | Clinic name | VALUE | clinic-name | 8× | Registered name. One field, applied throughout |

### Document control (labels from table rows)
| id | label | category | type | default | line |
|---|---|---|---|---|---|
| `responsible_person` | Responsible person | VALUE | role | Registered Manager / Clinical Lead | 13 |
| `authorised_by` | Authorised by | VALUE | person | — | 14 (bare) |
| `issue_date` | Issue date | VALUE | date | — | 15 (bare) |

### Governance note — NOT a clinic field
| line | treatment |
|---|---|
| 30 | `[NOTE]` — *"DH guide archived; GMC 2020 operative — confirm at review."* Reviewer only. **Never shown to the clinic.** |

### Policy fields
| id | label | category | type | default | gated? | line |
|---|---|---|---|---|---|---|
| `cooling_off` | Cooling-off period (elective/aesthetic) | CLAUSE | paragraph | *Yes — min 14 days; never treat at first appointment* | — | 119 |
| `reconsent_interval` | Re-consent interval | VALUE | duration | 3 months | — | 125 |
| `written_consent_procedures` | Procedures requiring written consent | VALUE | list | — | — | 135 |
| `consent_delegated` | Is consent ever delegated? | DECISION | yes/no | No | gates ↓ | 156 |
| `delegated_consent_owner` | Who maintains the authorised-to-take-consent record | VALUE | role | — | if `consent_delegated=yes` | 158 |
| `interpreter_service` | Interpreting service & booking route | VALUE | text | — | — | 166 |
| `accessible_formats` | Accessible-format arrangements (hearing/sight) | VALUE | text | — | — | 167 |
| `info_between_appointments` | Access to information between appointments | VALUE | text | — | — | 169 |
| `imca_service` | IMCA service & how to instruct | CLAUSE | paragraph | *or: clinic refers serious-medical-treatment decisions on* | — | 235 |
| `sees_under_18s` | Does the clinic see under-18s? | DECISION | yes/no | — | gates ↓ · **must match C032** | 246 |
| `young_person_refusal` | Position on a competent young person refusing necessary treatment | CLAUSE | paragraph | *Escalate to clinical lead; legal advice if serious; never resolve by asking a parent to sign* | if `sees_under_18s=yes` | 252 |
| `marketing_images` | Are recordings/images used for marketing? | DECISION | yes/no | No | if yes → requires explicit separate consent clause | 266 |
| `consent_training_refresh` | Consent training refresh interval | VALUE | duration | 3 years | — | 302 |
| `mca_training_refresh` | MCA training refresh interval | VALUE | duration | 3 years | — | 304 |
| `training_matrix_owner` | Who holds the training matrix | VALUE | role | — | — | 306 |
| `audit_owner` | Audit owner & frequency | VALUE | role+frequency | Clinical Lead, annually | — | 312 |
| `governance_meeting` | Name of the governance meeting | VALUE | text | — | — | 323 |

**21 fields · 1 note. Breakdown: 14 VALUE · 3 DECISION · 3 CLAUSE (+ clinic_name).**

---

## Requirements this puts on the fill UI

1. **Fill inline** in the document, DocuSign-style — not a separate blind Fields tab.
2. **Label from structure** — table-row header for bare `[CONFIRM]`, sentence for generic, marker text where clean.
3. **De-dup** — `clinic_name` is one input.
4. **CLAUSE fields render their default paragraph** with "keep / edit" — never as an empty box.
5. **DECISION fields show the default and gate their conditionals** — hide `delegated_consent_owner` unless delegation = yes; hide `young_person_refusal` unless under-18s = yes.
6. **`[NOTE]` never reaches the clinic.**
7. **Completeness gate (Rule 1)** blocks publish while any required field is unfilled — as the final gate, not a tab.

## Marker convention for the remaining 27 (so extraction is clean)

```
[CONFIRM: id=audit_owner | label="Audit owner & frequency" | cat=VALUE | type=role+frequency | default="Clinical Lead, annually"]
[NOTE: reviewer-only text — never shown to the clinic]
```
Bare `[CONFIRM]` in a table row keeps deriving its label from the row. One `id` = one field.
