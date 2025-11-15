## Model: `sales_loan_attribution`

`sales_loan_attribution`

*   **Unique ID:** `model.cherry_data_model.sales_loan_attribution`
*   **FQN:** `prod.revenue_marts.sales_loan_attribution`
*   **Description:** (No description provided)
*   **Tags:** `['revenue_analytics', 'revenue', 'hourly', 'revenue_hourly']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `UNIQUE_ID` | 1 | `TEXT` |  |  | `[]` | `{}` |
    | `FUNDED_AT_PT` | 2 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `LOAN_ID` | 3 | `NUMBER` |  |  | `[]` | `{}` |
    | `MERCHANT_ID` | 4 | `NUMBER` |  |  | `[]` | `{}` |
    | `MERCHANT_NAME` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `SF_ACCOUNT_ID` | 6 | `TEXT` |  |  | `[]` | `{}` |
    | `SF_ACCOUNT_NAME` | 7 | `TEXT` |  |  | `[]` | `{}` |
    | `MERCHANT_TYPE` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `ALLE_PRACTICE_TYPE` | 9 | `TEXT` |  |  | `[]` | `{}` |
    | `GO_LIVE_DATE` | 10 | `DATE` |  |  | `[]` | `{}` |
    | `INDUSTRY` | 11 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_INDUSTRY_SEGMENT` | 12 | `TEXT` |  |  | `[]` | `{}` |
    | `INITIAL_LOOK_ASSESSMENT` | 13 | `TEXT` |  |  | `[]` | `{}` |
    | `LATEST_LOOK_ASSESSMENT` | 14 | `TEXT` |  |  | `[]` | `{}` |
    | `LOOK_ASSESSMENT_SEGMENT` | 15 | `TEXT` |  |  | `[]` | `{}` |
    | `IS_ACTIVATION` | 16 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `DEPARTMENT` | 17 | `TEXT` |  |  | `[]` | `{}` |
    | `TEAM` | 18 | `TEXT` |  |  | `[]` | `{}` |
    | `SUBTEAM` | 19 | `TEXT` |  |  | `[]` | `{}` |
    | `NAME` | 20 | `TEXT` |  |  | `[]` | `{}` |
    | `TITLE` | 21 | `TEXT` |  |  | `[]` | `{}` |
    | `ATTRIBUTABLE_VOLUME` | 22 | `FLOAT` |  |  | `[]` | `{}` |
    | `ATTRIBUTION_PERCENTAGE` | 23 | `FLOAT` |  |  | `[]` | `{}` |
    | `ATTRIBUTION_TYPE` | 24 | `TEXT` |  |  | `[]` | `{}` |
    | `OWNER_IS_ACTIVE` | 25 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `QUALIFIED_OPPORTUNITY_SOURCE` | 26 | `TEXT` |  |  | `[]` | `{}` |
    | `DEPARTMENT_OWNERSHIP` | 27 | `TEXT` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt_utils.generate_surrogate_key`
    *   `model.cherry_data_model.loan_info_xf`
    *   `model.cherry_data_model.prospect_attribution_summary`
    *   `model.cherry_data_model.stg_sf_users`

---
