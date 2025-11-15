## Model: `stg_google_ads__ad_stats_tmp`

`stg_google_ads__ad_stats_tmp`

*   **Unique ID:** `model.google_ads.stg_google_ads__ad_stats_tmp`
*   **FQN:** `prod.ads_marts.stg_google_ads__ad_stats_tmp`
*   **Description:** (No description provided)
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'google_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `CUSTOMER_ID` | 1 | `NUMBER` |  |  | `[]` | `{}` |
    | `DATE` | 2 | `DATE` |  |  | `[]` | `{}` |
    | `_FIVETRAN_ID` | 3 | `TEXT` |  |  | `[]` | `{}` |
    | `AD_GROUP` | 4 | `TEXT` |  |  | `[]` | `{}` |
    | `CAMPAIGN_BASE_CAMPAIGN` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `CONVERSIONS_VALUE` | 6 | `FLOAT` |  |  | `[]` | `{}` |
    | `CONVERSIONS` | 7 | `FLOAT` |  |  | `[]` | `{}` |
    | `INTERACTIONS` | 8 | `NUMBER` |  |  | `[]` | `{}` |
    | `AD_ID` | 9 | `NUMBER` |  |  | `[]` | `{}` |
    | `AD_NETWORK_TYPE` | 10 | `TEXT` |  |  | `[]` | `{}` |
    | `INTERACTION_EVENT_TYPES` | 11 | `TEXT` |  |  | `[]` | `{}` |
    | `CAMPAIGN_ID` | 12 | `NUMBER` |  |  | `[]` | `{}` |
    | `IMPRESSIONS` | 13 | `NUMBER` |  |  | `[]` | `{}` |
    | `ACTIVE_VIEW_VIEWABILITY` | 14 | `FLOAT` |  |  | `[]` | `{}` |
    | `DEVICE` | 15 | `TEXT` |  |  | `[]` | `{}` |
    | `VIEW_THROUGH_CONVERSIONS` | 16 | `NUMBER` |  |  | `[]` | `{}` |
    | `ACTIVE_VIEW_IMPRESSIONS` | 17 | `NUMBER` |  |  | `[]` | `{}` |
    | `CLICKS` | 18 | `NUMBER` |  |  | `[]` | `{}` |
    | `KEYWORD_AD_GROUP_CRITERION` | 19 | `TEXT` |  |  | `[]` | `{}` |
    | `ACTIVE_VIEW_MEASURABLE_IMPRESSIONS` | 20 | `NUMBER` |  |  | `[]` | `{}` |
    | `ACTIVE_VIEW_MEASURABLE_COST_MICROS` | 21 | `NUMBER` |  |  | `[]` | `{}` |
    | `ACTIVE_VIEW_MEASURABILITY` | 22 | `FLOAT` |  |  | `[]` | `{}` |
    | `AD_GROUP_BASE_AD_GROUP` | 23 | `TEXT` |  |  | `[]` | `{}` |
    | `COST_MICROS` | 24 | `NUMBER` |  |  | `[]` | `{}` |
    | `_FIVETRAN_SYNCED` | 25 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `AD_GROUP_ID` | 26 | `NUMBER` |  |  | `[]` | `{}` |
    | `VIDEO_VIEWS` | 27 | `NUMBER` |  |  | `[]` | `{}` |
    | `COST_PER_CONVERSION` | 28 | `FLOAT` |  |  | `[]` | `{}` |
    | `VIDEO_TRUEVIEW_VIEWS` | 29 | `NUMBER` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.fivetran_utils.union_data`
    *   `source.google_ads.google_ads.ad_stats`

---
