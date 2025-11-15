## Model: `stg_google_ads__keyword_stats_tmp`

`stg_google_ads__keyword_stats_tmp`

*   **Unique ID:** `model.google_ads.stg_google_ads__keyword_stats_tmp`
*   **FQN:** `prod.ads_marts.stg_google_ads__keyword_stats_tmp`
*   **Description:** (No description provided)
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'google_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `CUSTOMER_ID` | 1 | `NUMBER` |  |  | `[]` | `{}` |
    | `DATE` | 2 | `DATE` |  |  | `[]` | `{}` |
    | `_FIVETRAN_ID` | 3 | `TEXT` |  |  | `[]` | `{}` |
    | `CAMPAIGN_BASE_CAMPAIGN` | 4 | `TEXT` |  |  | `[]` | `{}` |
    | `CONVERSIONS_VALUE` | 5 | `FLOAT` |  |  | `[]` | `{}` |
    | `CONVERSIONS` | 6 | `FLOAT` |  |  | `[]` | `{}` |
    | `INTERACTIONS` | 7 | `NUMBER` |  |  | `[]` | `{}` |
    | `AD_NETWORK_TYPE` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `INTERACTION_EVENT_TYPES` | 9 | `TEXT` |  |  | `[]` | `{}` |
    | `CAMPAIGN_ID` | 10 | `NUMBER` |  |  | `[]` | `{}` |
    | `IMPRESSIONS` | 11 | `NUMBER` |  |  | `[]` | `{}` |
    | `ACTIVE_VIEW_VIEWABILITY` | 12 | `FLOAT` |  |  | `[]` | `{}` |
    | `AD_GROUP_ID` | 13 | `NUMBER` |  |  | `[]` | `{}` |
    | `DEVICE` | 14 | `TEXT` |  |  | `[]` | `{}` |
    | `VIEW_THROUGH_CONVERSIONS` | 15 | `NUMBER` |  |  | `[]` | `{}` |
    | `ACTIVE_VIEW_IMPRESSIONS` | 16 | `NUMBER` |  |  | `[]` | `{}` |
    | `CLICKS` | 17 | `NUMBER` |  |  | `[]` | `{}` |
    | `AD_GROUP_CRITERION_CRITERION_ID` | 18 | `NUMBER` |  |  | `[]` | `{}` |
    | `ACTIVE_VIEW_MEASURABLE_IMPRESSIONS` | 19 | `NUMBER` |  |  | `[]` | `{}` |
    | `ACTIVE_VIEW_MEASURABLE_COST_MICROS` | 20 | `NUMBER` |  |  | `[]` | `{}` |
    | `ACTIVE_VIEW_MEASURABILITY` | 21 | `FLOAT` |  |  | `[]` | `{}` |
    | `AD_GROUP_BASE_AD_GROUP` | 22 | `TEXT` |  |  | `[]` | `{}` |
    | `COST_MICROS` | 23 | `NUMBER` |  |  | `[]` | `{}` |
    | `_FIVETRAN_SYNCED` | 24 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.fivetran_utils.union_data`
    *   `source.google_ads.google_ads.keyword_stats`

---
