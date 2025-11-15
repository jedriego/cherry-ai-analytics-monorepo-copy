## Model: `stg_google_ads__account_history_tmp`

`stg_google_ads__account_history_tmp`

*   **Unique ID:** `model.google_ads.stg_google_ads__account_history_tmp`
*   **FQN:** `prod.ads_marts.stg_google_ads__account_history_tmp`
*   **Description:** (No description provided)
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'google_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `ID` | 1 | `NUMBER` |  |  | `[]` | `{}` |
    | `UPDATED_AT` | 2 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `MANAGER_CUSTOMER_ID` | 3 | `NUMBER` |  |  | `[]` | `{}` |
    | `AUTO_TAGGING_ENABLED` | 4 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `CURRENCY_CODE` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `DESCRIPTIVE_NAME` | 6 | `TEXT` |  |  | `[]` | `{}` |
    | `FINAL_URL_SUFFIX` | 7 | `TEXT` |  |  | `[]` | `{}` |
    | `HIDDEN` | 8 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `MANAGER` | 9 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `OPTIMIZATION_SCORE` | 10 | `FLOAT` |  |  | `[]` | `{}` |
    | `PAY_PER_CONVERSION_ELIGIBILITY_FAILURE_REASONS` | 11 | `TEXT` |  |  | `[]` | `{}` |
    | `TEST_ACCOUNT` | 12 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `TIME_ZONE` | 13 | `TEXT` |  |  | `[]` | `{}` |
    | `TRACKING_URL_TEMPLATE` | 14 | `TEXT` |  |  | `[]` | `{}` |
    | `_FIVETRAN_SYNCED` | 15 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `_FIVETRAN_START` | 16 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `_FIVETRAN_END` | 17 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `_FIVETRAN_ACTIVE` | 18 | `BOOLEAN` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.fivetran_utils.union_data`
    *   `source.google_ads.google_ads.account_history`

---
