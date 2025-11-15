## Model: `stg_google_ads__account_stats_tmp`

`stg_google_ads__account_stats_tmp`

*   **Unique ID:** `model.google_ads.stg_google_ads__account_stats_tmp`
*   **FQN:** `prod.ads_marts.stg_google_ads__account_stats_tmp`
*   **Description:** (No description provided)
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'google_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `CUSTOMER_ID` | 1 | `NUMBER` |  |  | `[]` | `{}` |
    | `DATE` | 2 | `DATE` |  |  | `[]` | `{}` |
    | `_FIVETRAN_ID` | 3 | `TEXT` |  |  | `[]` | `{}` |
    | `CONVERSIONS_VALUE` | 4 | `FLOAT` |  |  | `[]` | `{}` |
    | `CONVERSIONS` | 5 | `FLOAT` |  |  | `[]` | `{}` |
    | `INTERACTIONS` | 6 | `NUMBER` |  |  | `[]` | `{}` |
    | `AD_NETWORK_TYPE` | 7 | `TEXT` |  |  | `[]` | `{}` |
    | `INTERACTION_EVENT_TYPES` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `IMPRESSIONS` | 9 | `NUMBER` |  |  | `[]` | `{}` |
    | `ACTIVE_VIEW_VIEWABILITY` | 10 | `FLOAT` |  |  | `[]` | `{}` |
    | `DEVICE` | 11 | `TEXT` |  |  | `[]` | `{}` |
    | `VIEW_THROUGH_CONVERSIONS` | 12 | `NUMBER` |  |  | `[]` | `{}` |
    | `ACTIVE_VIEW_IMPRESSIONS` | 13 | `NUMBER` |  |  | `[]` | `{}` |
    | `CLICKS` | 14 | `NUMBER` |  |  | `[]` | `{}` |
    | `ACTIVE_VIEW_MEASURABLE_IMPRESSIONS` | 15 | `NUMBER` |  |  | `[]` | `{}` |
    | `ACTIVE_VIEW_MEASURABLE_COST_MICROS` | 16 | `NUMBER` |  |  | `[]` | `{}` |
    | `ACTIVE_VIEW_MEASURABILITY` | 17 | `FLOAT` |  |  | `[]` | `{}` |
    | `COST_MICROS` | 18 | `NUMBER` |  |  | `[]` | `{}` |
    | `_FIVETRAN_SYNCED` | 19 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.fivetran_utils.union_data`
    *   `source.google_ads.google_ads.account_stats`

---
