## Model: `stg_google_ads__ad_group_history`

`stg_google_ads__ad_group_history`

*   **Unique ID:** `model.google_ads.stg_google_ads__ad_group_history`
*   **FQN:** `prod.ads_marts.stg_google_ads__ad_group_history`
*   **Description:** Each record represents a version of an ad group in Google Ads.
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'google_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `SOURCE_RELATION` | 1 | `TEXT` | The source of the record if the unioning functionality is being used. If not this field will be empty. | The source of the record if the unioning functionality is being used. If not this field will be empty. | `[]` | `{}` |
    | `AD_GROUP_ID` | 2 | `TEXT` | The ID of the AdGroup. | The ID of the AdGroup. | `[]` | `{}` |
    | `UPDATED_AT` | 3 | `TIMESTAMP_TZ` | Timestamp of when the record was last updated in Google Ads. | Timestamp of when the record was last updated in Google Ads. | `[]` | `{}` |
    | `AD_GROUP_TYPE` | 4 | `TEXT` | The type of the ad group in Google Ads. | The type of the ad group in Google Ads. | `[]` | `{}` |
    | `CAMPAIGN_ID` | 5 | `NUMBER` | The ID of the Campaign. | The ID of the Campaign. | `[]` | `{}` |
    | `CAMPAIGN_NAME` | 6 | `TEXT` | The name of the Campaign. | The name of the Campaign. | `[]` | `{}` |
    | `AD_GROUP_NAME` | 7 | `TEXT` | The name of the AdGroup. | The name of the AdGroup. | `[]` | `{}` |
    | `AD_GROUP_STATUS` | 8 | `TEXT` | Status of the ad group. | Status of the ad group. | `[]` | `{}` |
    | `IS_MOST_RECENT_RECORD` | 9 | `BOOLEAN` | Boolean representing whether the record is the most recent version of the object. | Boolean representing whether the record is the most recent version of the object. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt.type_string`
    *   `macro.fivetran_utils.fill_staging_columns`
    *   `macro.fivetran_utils.source_relation`
    *   `macro.google_ads.get_ad_group_history_columns`
    *   `model.google_ads.stg_google_ads__ad_group_history_tmp`

---
