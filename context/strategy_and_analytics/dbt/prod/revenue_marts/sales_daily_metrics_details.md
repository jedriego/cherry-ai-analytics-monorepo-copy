## Model: `sales_daily_metrics_details`

`sales_daily_metrics_details`

*   **Unique ID:** `model.cherry_data_model.sales_daily_metrics_details`
*   **FQN:** `prod.revenue_marts.sales_daily_metrics_details`
*   **Description:** (No description provided)
*   **Tags:** `['revenue_analytics']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `TYPE` | 1 | `TEXT` |  |  | `[]` | `{}` |
    | `ID` | 2 | `TEXT` |  |  | `[]` | `{}` |
    | `DATE` | 3 | `DATE` |  |  | `[]` | `{}` |
    | `AMOUNT` | 4 | `FLOAT` |  |  | `[]` | `{}` |
    | `ACCOUNT_NAME` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `URL` | 6 | `TEXT` |  |  | `[]` | `{}` |
    | `INDUSTRY_SEGMENT` | 7 | `TEXT` |  |  | `[]` | `{}` |
    | `INDUSTRY` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_DEPARTMENT` | 9 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_TEAM` | 10 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_SUBTEAM` | 11 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE` | 12 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_TITLE` | 13 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_IS_ACTIVE` | 14 | `BOOLEAN` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.calendar_table_xf`
    *   `model.cherry_data_model.demo_details_xf`
    *   `model.cherry_data_model.sales_loan_attribution`
    *   `model.cherry_data_model.stg_leads`
    *   `model.cherry_data_model.stg_merchants`
    *   `model.cherry_data_model.stg_practices`
    *   `model.cherry_data_model.stg_registrations_new`
    *   `model.cherry_data_model.stg_sf_users`

---
