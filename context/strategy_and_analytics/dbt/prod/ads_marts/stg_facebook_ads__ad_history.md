## Model: `stg_facebook_ads__ad_history`

`stg_facebook_ads__ad_history`

*   **Unique ID:** `model.facebook_ads.stg_facebook_ads__ad_history`
*   **FQN:** `prod.ads_marts.stg_facebook_ads__ad_history`
*   **Description:** Each record in this table reflects a Facebook ad.
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'facebook_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `SOURCE_RELATION` | 1 | `TEXT` | The source of the record if the unioning functionality is being used. If not this field will be empty. | The source of the record if the unioning functionality is being used. If not this field will be empty. | `[]` | `{}` |
    | `UPDATED_AT` | 2 | `TIMESTAMP_TZ` | The timestamp of the last update of a record. | The timestamp of the last update of a record. | `[]` | `{}` |
    | `AD_ID` | 3 | `NUMBER` | The ID of this ad. | The ID of this ad. | `[]` | `{}` |
    | `AD_NAME` | 4 | `TEXT` | Name of the ad. | Name of the ad. | `[]` | `{}` |
    | `ACCOUNT_ID` | 5 | `NUMBER` | The ID of the ad account that this ad belongs to. | The ID of the ad account that this ad belongs to. | `[]` | `{}` |
    | `AD_SET_ID` | 6 | `NUMBER` | ID of the ad set that contains the ad. | ID of the ad set that contains the ad. | `[]` | `{}` |
    | `CAMPAIGN_ID` | 7 | `NUMBER` | Ad campaign that contains this ad. | Ad campaign that contains this ad. | `[]` | `{}` |
    | `CREATIVE_ID` | 8 | `NUMBER` | The ID of the ad creative to be used by this ad. | The ID of the ad creative to be used by this ad. | `[]` | `{}` |
    | `CONVERSION_DOMAIN` | 9 | `TEXT` | The domain you've configured the ad to convert to. | The domain you've configured the ad to convert to. | `[]` | `{}` |
    | `IS_MOST_RECENT_RECORD` | 10 | `BOOLEAN` | Boolean representing whether a record is the most recent version of that record. All records should have this value set to True given we filter on it. | Boolean representing whether a record is the most recent version of that record. All records should have this value set to True given we filter on it. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt.type_bigint`
    *   `macro.facebook_ads.get_ad_history_columns`
    *   `macro.fivetran_utils.fill_staging_columns`
    *   `macro.fivetran_utils.source_relation`
    *   `model.facebook_ads.stg_facebook_ads__ad_history_tmp`

---
