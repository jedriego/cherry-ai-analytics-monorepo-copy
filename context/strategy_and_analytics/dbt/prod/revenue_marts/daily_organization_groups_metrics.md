## Model: `daily_organization_groups_metrics`

`daily_organization_groups_metrics`

*   **Unique ID:** `model.cherry_data_model.daily_organization_groups_metrics`
*   **FQN:** `prod.revenue_marts.daily_organization_groups_metrics`
*   **Description:** This model calculates daily metrics for organization groups, including transaction volumes from loans and application counts. It cross-joins dates with organization group information and merges in loan and application data.
*   **Tags:** `['revenue_analytics']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `UNIQUE_ID` | 1 | `TEXT` | A unique identifier for each row, generated as a surrogate key based on the date and merchant ID. | A unique identifier for each row, generated as a surrogate key based on the date and merchant ID. | `[]` | `{}` |
    | `DATE` | 2 | `DATE` | The date for which metrics are calculated. | The date for which metrics are calculated. | `[]` | `{}` |
    | `ORGANIZATION_GROUP_ID` | 3 | `NUMBER` | The identifier of the organization group. | The identifier of the organization group. | `[]` | `{}` |
    | `ORGANIZATION_GROUP_NAME` | 4 | `TEXT` | The name of the organization group. | The name of the organization group. | `[]` | `{}` |
    | `ORGANIZATION_ID` | 5 | `NUMBER` | The identifier of the organization. | The identifier of the organization. | `[]` | `{}` |
    | `ORGANIZATION_NAME` | 6 | `TEXT` | The name of the organization. | The name of the organization. | `[]` | `{}` |
    | `MERCHANT_ID` | 7 | `NUMBER` | The identifier of the merchant. | The identifier of the merchant. | `[]` | `{}` |
    | `MERCHANT_NAME` | 8 | `TEXT` | The name of the merchant. | The name of the merchant. | `[]` | `{}` |
    | `ACCOUNT_INDUSTRY_SEGMENT` | 9 | `TEXT` | The industry segment of the account. | The industry segment of the account. | `[]` | `{}` |
    | `TRANSACTION_VOLUME` | 10 | `FLOAT` | The total gross amount of funded loans for the merchant on the specified date. This is the sum of 'gross_amount' for the merchant's funded loans. | The total gross amount of funded loans for the merchant on the specified date. This is the sum of 'gross_amount' for the merchant's funded loans. | `[]` | `{}` |
    | `APPLICATION_COUNT` | 11 | `NUMBER` | The count of applications created by the merchant on the specified date. | The count of applications created by the merchant on the specified date. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt_utils.generate_surrogate_key`
    *   `model.cherry_data_model.calendar_table_xf`
    *   `model.cherry_data_model.int_applications_collapsed`
    *   `model.cherry_data_model.loan_info_xf`
    *   `model.cherry_data_model.stg_merchants`

---
