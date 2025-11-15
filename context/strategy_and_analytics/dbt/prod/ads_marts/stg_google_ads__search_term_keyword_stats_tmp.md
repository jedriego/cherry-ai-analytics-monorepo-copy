## Model: `stg_google_ads__search_term_keyword_stats_tmp`

`stg_google_ads__search_term_keyword_stats_tmp`

*   **Unique ID:** `model.google_ads.stg_google_ads__search_term_keyword_stats_tmp`
*   **FQN:** `prod.ads_marts.stg_google_ads__search_term_keyword_stats_tmp`
*   **Description:** (No description provided)
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'google_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `CUSTOMER_ID` | 1 | `NUMBER` |  |  | `[]` | `{}` |
    | `DATE` | 2 | `DATE` |  |  | `[]` | `{}` |
    | `_FIVETRAN_ID` | 3 | `TEXT` |  |  | `[]` | `{}` |
    | `SEARCH_TERM` | 4 | `TEXT` |  |  | `[]` | `{}` |
    | `RESOURCE_NAME` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `CONVERSIONS_VALUE` | 6 | `FLOAT` |  |  | `[]` | `{}` |
    | `CONVERSIONS` | 7 | `FLOAT` |  |  | `[]` | `{}` |
    | `CAMPAIGN_ID` | 8 | `NUMBER` |  |  | `[]` | `{}` |
    | `SEARCH_TERM_MATCH_TYPE` | 9 | `TEXT` |  |  | `[]` | `{}` |
    | `IMPRESSIONS` | 10 | `NUMBER` |  |  | `[]` | `{}` |
    | `VIEW_THROUGH_CONVERSIONS` | 11 | `NUMBER` |  |  | `[]` | `{}` |
    | `AD_GROUP_ID` | 12 | `NUMBER` |  |  | `[]` | `{}` |
    | `ABSOLUTE_TOP_IMPRESSION_PERCENTAGE` | 13 | `FLOAT` |  |  | `[]` | `{}` |
    | `CLICKS` | 14 | `NUMBER` |  |  | `[]` | `{}` |
    | `KEYWORD_AD_GROUP_CRITERION` | 15 | `TEXT` |  |  | `[]` | `{}` |
    | `TOP_IMPRESSION_PERCENTAGE` | 16 | `FLOAT` |  |  | `[]` | `{}` |
    | `STATUS` | 17 | `TEXT` |  |  | `[]` | `{}` |
    | `INFO_TEXT` | 18 | `TEXT` |  |  | `[]` | `{}` |
    | `CONVERSIONS_FROM_INTERACTIONS_VALUE_PER_INTERACTION` | 19 | `FLOAT` |  |  | `[]` | `{}` |
    | `AVERAGE_CPC` | 20 | `FLOAT` |  |  | `[]` | `{}` |
    | `CONVERSIONS_FROM_INTERACTIONS_RATE` | 21 | `FLOAT` |  |  | `[]` | `{}` |
    | `CTR` | 22 | `FLOAT` |  |  | `[]` | `{}` |
    | `COST_MICROS` | 23 | `NUMBER` |  |  | `[]` | `{}` |
    | `_FIVETRAN_SYNCED` | 24 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.fivetran_utils.union_data`
    *   `source.google_ads.google_ads.search_term_keyword_stats`

---

