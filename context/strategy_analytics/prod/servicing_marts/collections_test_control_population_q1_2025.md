## Model: `collections_test_control_population_q1_2025`

`collections_test_control_population_q1_2025`

*   **Unique ID:** `model.cherry_data_model.collections_test_control_population_q1_2025`
*   **FQN:** `prod.servicing_marts.collections_test_control_population_q1_2025`
*   **Description:** A model that tracks borrower assignments for the Collections Q1 2025 Company OKR experiment. This includes both initial assignments and subsequent changes, tracking treatment/control groups and dial/no-dial subgroups within the treatment population. The model maintains temporal validity of these assignments through valid_from/valid_to dates.

*   **Tags:** `['servicing_and_collections', 'collections_hourly']`
*   **Meta:** `{'owner': 'Collections Team', 'sources': ['Initial CSV split assignments', 'Automated assignments via borrower_flags table', 'Subsequent changes tracked in borrower_flags_aud'], 'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}, 'temporal_validity': 'Model maintains temporal validity of assignments through valid_from/valid_to dates, ensuring accurate historical tracking of group changes. '}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `BORROWER_ID` | 1 | `NUMBER` | Unique identifier for the borrower | Unique identifier for the borrower | `[]` | `{}` |
    | `VALID_FROM` | 2 | `DATE` | Date when the group assignment became effective | Date when the group assignment became effective | `[]` | `{}` |
    | `VALID_TO` | 3 | `DATE` | Date when the group assignment expires (defaults to 2100-01-01 if current) | Date when the group assignment expires (defaults to 2100-01-01 if current) | `[]` | `{}` |
    | `MIN_LOAN_FUNDED` | 4 | `DATE` | Date of the borrower's first funded loan | Date of the borrower's first funded loan | `[]` | `{}` |
    | `CONTROL_GROUP` | 5 | `BOOLEAN` | Boolean flag indicating if the borrower is in the control group | Boolean flag indicating if the borrower is in the control group | `[]` | `{}` |
    | `HOLDOUT` | 6 | `BOOLEAN` | Boolean flag indicating if the borrower is in the holdout (no-dial) group within treatment | Boolean flag indicating if the borrower is in the holdout (no-dial) group within treatment | `[]` | `{}` |
    | `ELIGIBLE_FOR_DIALS_30D` | 7 | `BOOLEAN` | Flag indicating if the borrower is eligible for dials based on a 30-day waiting period after funding. Set to false if: - No funded loan exists - Loan was funded within the last 30 days
 | Flag indicating if the borrower is eligible for dials based on a 30-day waiting period after funding. Set to false if: - No funded loan exists - Loan was funded within the last 30 days
 | `[]` | `{}` |
    | `COLLECTIONS_GROUP` | 8 | `TEXT` | Final group assignment categorization: - Control: control_group = true - Treatment - No Dials: control_group = false AND holdout = true - Treatment - With Dials: control_group = false AND holdout = false
 | Final group assignment categorization: - Control: control_group = true - Treatment - No Dials: control_group = false AND holdout = true - Treatment - With Dials: control_group = false AND holdout = false
 | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.src_cherry_loans`
    *   `source.cherry_data_model.cherry_data.borrower_flags`
    *   `source.cherry_data_model.cherry_data.borrower_flags_aud`
    *   `source.cherry_data_model.collections_efficiency_q1_group_splits.q1_initial_dial_no_dial_split`
    *   `source.cherry_data_model.collections_efficiency_q1_group_splits.q1_initial_treatment_control_split`

---
