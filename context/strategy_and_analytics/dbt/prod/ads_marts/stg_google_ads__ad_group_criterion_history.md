## Model: `stg_google_ads__ad_group_criterion_history`

`stg_google_ads__ad_group_criterion_history`

*   **Unique ID:** `model.google_ads.stg_google_ads__ad_group_criterion_history`
*   **FQN:** `prod.ads_marts.stg_google_ads__ad_group_criterion_history`
*   **Description:** Each record represents a historical version of an ad group criterion in Google Ads.
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'google_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `SOURCE_RELATION` | 1 | `TEXT` | The source of the record if the unioning functionality is being used. If not this field will be empty. | The source of the record if the unioning functionality is being used. If not this field will be empty. | `[]` | `{}` |
    | `CRITERION_ID` | 2 | `NUMBER` | Unique identifier of the ad group criterion. | Unique identifier of the ad group criterion. | `[]` | `{}` |
    | `AD_GROUP_ID` | 3 | `TEXT` | The ID of the AdGroup. | The ID of the AdGroup. | `[]` | `{}` |
    | `BASE_CAMPAIGN_ID` | 4 | `NUMBER` | The ID of the Campaign. | The ID of the Campaign. | `[]` | `{}` |
    | `UPDATED_AT` | 5 | `TIMESTAMP_TZ` | Timestamp of when the record was last updated in Google Ads. | Timestamp of when the record was last updated in Google Ads. | `[]` | `{}` |
    | `TYPE` | 6 | `TEXT` | The type of ad group criterion. | The type of ad group criterion. | `[]` | `{}` |
    | `STATUS` | 7 | `TEXT` | The current status of the ad group criterion. | The current status of the ad group criterion. | `[]` | `{}` |
    | `KEYWORD_MATCH_TYPE` | 8 | `TEXT` | The match type which dictate how closely the keyword needs to match with the user’s search query so that the ad can be considered for the auction. | The match type which dictate how closely the keyword needs to match with the user’s search query so that the ad can be considered for the auction. | `[]` | `{}` |
    | `KEYWORD_TEXT` | 9 | `TEXT` | The text used within the keyword criterion that is being matched against. | The text used within the keyword criterion that is being matched against. | `[]` | `{}` |
    | `IS_MOST_RECENT_RECORD` | 10 | `BOOLEAN` | Boolean representing whether the record is the most recent version of the object. | Boolean representing whether the record is the most recent version of the object. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt.type_string`
    *   `macro.fivetran_utils.fill_staging_columns`
    *   `macro.fivetran_utils.source_relation`
    *   `macro.google_ads.get_ad_group_criterion_history_columns`
    *   `model.google_ads.stg_google_ads__ad_group_criterion_history_tmp`

---
