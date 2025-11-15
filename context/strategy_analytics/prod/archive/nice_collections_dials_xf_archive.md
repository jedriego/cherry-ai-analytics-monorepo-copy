## Model: `nice_collections_dials_xf_archive`

`nice_collections_dials_xf_archive`

*   **Unique ID:** `model.cherry_data_model.nice_collections_dials_xf_archive`
*   **FQN:** `prod.archive.nice_collections_dials_xf_archive`
*   **Description:** (No description provided)
*   **Tags:** `['archive']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `DIAL_TYPE` | 1 | `TEXT` |  |  | `[]` | `{}` |
    | `CONTACT_ID` | 2 | `NUMBER` |  |  | `[]` | `{}` |
    | `SPECIALIST` | 3 | `TEXT` |  |  | `[]` | `{}` |
    | `CONTACT_START_PT` | 4 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `PHONE_NUMBER` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `MEDIA_TYPE_NAME` | 6 | `TEXT` |  |  | `[]` | `{}` |
    | `SKILL_NAME` | 7 | `TEXT` |  |  | `[]` | `{}` |
    | `LOAN_ID` | 8 | `NUMBER` |  |  | `[]` | `{}` |
    | `BORROWER_ID` | 9 | `NUMBER` |  |  | `[]` | `{}` |
    | `DPD_BUCKET` | 10 | `TEXT` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.daily_loan_xf`
    *   `model.cherry_data_model.int_funded_information_pt`
    *   `model.cherry_data_model.src_borrowers`
    *   `model.cherry_data_model.src_loanpro_chargeoff_transactions`
    *   `model.cherry_data_model.src_nice_contacts`

---
