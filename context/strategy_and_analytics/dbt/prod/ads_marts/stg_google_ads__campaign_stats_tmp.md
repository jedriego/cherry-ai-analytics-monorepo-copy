## Model: `stg_google_ads__campaign_stats_tmp`

`stg_google_ads__campaign_stats_tmp`

*   **Unique ID:** `model.google_ads.stg_google_ads__campaign_stats_tmp`
*   **FQN:** `prod.ads_marts.stg_google_ads__campaign_stats_tmp`
*   **Description:** (No description provided)
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'google_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `CUSTOMER_ID` | 1 | `NUMBER` |  |  | `[]` | `{}` |
    | `DATE` | 2 | `DATE` |  |  | `[]` | `{}` |
    | `_FIVETRAN_ID` | 3 | `TEXT` |  |  | `[]` | `{}` |
    | `BASE_CAMPAIGN` | 4 | `TEXT` |  |  | `[]` | `{}` |
    | `CONVERSIONS_VALUE` | 5 | `FLOAT` |  |  | `[]` | `{}` |
    | `CONVERSIONS` | 6 | `FLOAT` |  |  | `[]` | `{}` |
    | `INTERACTIONS` | 7 | `NUMBER` |  |  | `[]` | `{}` |
    | `AD_NETWORK_TYPE` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `INTERACTION_EVENT_TYPES` | 9 | `TEXT` |  |  | `[]` | `{}` |
    | `ID` | 10 | `NUMBER` |  |  | `[]` | `{}` |
    | `IMPRESSIONS` | 11 | `NUMBER` |  |  | `[]` | `{}` |
    | `ACTIVE_VIEW_VIEWABILITY` | 12 | `FLOAT` |  |  | `[]` | `{}` |
    | `DEVICE` | 13 | `TEXT` |  |  | `[]` | `{}` |
    | `VIEW_THROUGH_CONVERSIONS` | 14 | `NUMBER` |  |  | `[]` | `{}` |
    | `ACTIVE_VIEW_IMPRESSIONS` | 15 | `NUMBER` |  |  | `[]` | `{}` |
    | `CLICKS` | 16 | `NUMBER` |  |  | `[]` | `{}` |
    | `ACTIVE_VIEW_MEASURABLE_IMPRESSIONS` | 17 | `NUMBER` |  |  | `[]` | `{}` |
    | `ACTIVE_VIEW_MEASURABLE_COST_MICROS` | 18 | `NUMBER` |  |  | `[]` | `{}` |
    | `ACTIVE_VIEW_MEASURABILITY` | 19 | `FLOAT` |  |  | `[]` | `{}` |
    | `COST_MICROS` | 20 | `NUMBER` |  |  | `[]` | `{}` |
    | `_FIVETRAN_SYNCED` | 21 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.fivetran_utils.union_data`
    *   `source.google_ads.google_ads.campaign_stats`

---
