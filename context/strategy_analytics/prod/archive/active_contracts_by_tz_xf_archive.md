## Model: `active_contracts_by_tz_xf_archive`

`active_contracts_by_tz_xf_archive`

*   **Unique ID:** `model.cherry_data_model.active_contracts_by_tz_xf_archive`
*   **FQN:** `prod.archive.active_contracts_by_tz_xf_archive`
*   **Description:** (No description provided)
*   **Tags:** `['archive']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `TIMEZONE` | 1 | `TEXT` |  |  | `[]` | `{}` |
    | `NUM_CONTRACTS` | 2 | `NUMBER` |  |  | `[]` | `{}` |
    | `OUTSTANDING_BALANCE` | 3 | `FLOAT` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.int_funded_information_pt`
    *   `model.cherry_data_model.src_borrowers`
    *   `model.cherry_data_model.stg_borrower_addresses_with_tz`
    *   `model.cherry_data_model.stg_loan_plans`
    *   `seed.cherry_data_model.state_codes_and_tz`

---
