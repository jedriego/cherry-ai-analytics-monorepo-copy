## Model: `collections_safe_select_dials_archive`

`collections_safe_select_dials_archive`

*   **Unique ID:** `model.cherry_data_model.collections_safe_select_dials_archive`
*   **FQN:** `prod.archive.collections_safe_select_dials_archive`
*   **Description:** (No description provided)
*   **Tags:** `['archive']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `SAFE_SELECT_CONTACT_ID` | 1 | `TEXT` |  |  | `[]` | `{}` |
    | `CONTACT_STATUS` | 2 | `TEXT` |  |  | `[]` | `{}` |
    | `AGENT` | 3 | `TEXT` |  |  | `[]` | `{}` |
    | `AGENT_FLAG` | 4 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `DISPOSITION` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `LOAN_ID` | 6 | `NUMBER` |  |  | `[]` | `{}` |
    | `BORROWER_ID` | 7 | `NUMBER` |  |  | `[]` | `{}` |
    | `PHONE_NUMBER` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `TIMESTAMP_REVISED` | 9 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `TIMESTAMP_REVISED_PT` | 10 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `DPD_BUCKET` | 11 | `TEXT` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.daily_loan_xf`
    *   `model.cherry_data_model.int_funded_information_pt`
    *   `model.cherry_data_model.src_loanpro_chargeoff_transactions`
    *   `model.cherry_data_model.src_safe_select_activity`
    *   `seed.cherry_data_model.ops_user_teams`

---
