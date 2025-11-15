## Model: `stg_google_ads__ad_history`

`stg_google_ads__ad_history`

*   **Unique ID:** `model.google_ads.stg_google_ads__ad_history`
*   **FQN:** `prod.ads_marts.stg_google_ads__ad_history`
*   **Description:** Each record represents a version of an ad in Google Ads.
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'google_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `SOURCE_RELATION` | 1 | `TEXT` | The source of the record if the unioning functionality is being used. If not this field will be empty. | The source of the record if the unioning functionality is being used. If not this field will be empty. | `[]` | `{}` |
    | `AD_GROUP_ID` | 2 | `TEXT` | The ID of the AdGroup. | The ID of the AdGroup. | `[]` | `{}` |
    | `AD_ID` | 3 | `NUMBER` | The ID of the Ad. | The ID of the Ad. | `[]` | `{}` |
    | `AD_NAME` | 4 | `TEXT` |  |  | `[]` | `{}` |
    | `UPDATED_AT` | 5 | `TIMESTAMP_TZ` | Timestamp of when the record was last updated in Google Ads. | Timestamp of when the record was last updated in Google Ads. | `[]` | `{}` |
    | `AD_TYPE` | 6 | `TEXT` | The type of the ad in Google Ads. | The type of the ad in Google Ads. | `[]` | `{}` |
    | `AD_STATUS` | 7 | `TEXT` | Status of the Ad. | Status of the Ad. | `[]` | `{}` |
    | `DISPLAY_URL` | 8 | `TEXT` | The display url of the ad that is being served. | The display url of the ad that is being served. | `[]` | `{}` |
    | `SOURCE_FINAL_URLS` | 9 | `TEXT` | The original list of final urls expressed as an array. Please be aware the test used on this field is intended to warn you if you have fields with multiple urls. If you do, the `final_url` field will filter down the urls within the array to just the first. Therefore, this package will only leverage one of possibly many urls within this field array. | The original list of final urls expressed as an array. Please be aware the test used on this field is intended to warn you if you have fields with multiple urls. If you do, the `final_url` field will filter down the urls within the array to just the first. Therefore, this package will only leverage one of possibly many urls within this field array. | `[]` | `{}` |
    | `FINAL_URLS` | 10 | `TEXT` |  |  | `[]` | `{}` |
    | `IS_MOST_RECENT_RECORD` | 11 | `BOOLEAN` | Boolean representing whether the record is the most recent version of the object. | Boolean representing whether the record is the most recent version of the object. | `[]` | `{}` |
    | `FINAL_URL` | 12 | `TEXT` | The first url in the list of the urls within the `final_urls` source field. | The first url in the list of the urls within the `final_urls` source field. | `[]` | `{}` |
    | `BASE_URL` | 13 | `TEXT` | The base URL of the ad, extracted from the `final_urls`. | The base URL of the ad, extracted from the `final_urls`. | `[]` | `{}` |
    | `URL_HOST` | 14 | `TEXT` | The URL host of the ad, extracted from the `final_urls`. | The URL host of the ad, extracted from the `final_urls`. | `[]` | `{}` |
    | `URL_PATH` | 15 | `TEXT` | The URL path of the ad, extracted from the `final_urls`. | The URL path of the ad, extracted from the `final_urls`. | `[]` | `{}` |
    | `UTM_SOURCE` | 16 | `TEXT` | The utm_source parameter of the ad, extracted from the `final_urls`. | The utm_source parameter of the ad, extracted from the `final_urls`. | `[]` | `{}` |
    | `UTM_MEDIUM` | 17 | `TEXT` | The utm_medium parameter of the ad, extracted from the `final_urls`. | The utm_medium parameter of the ad, extracted from the `final_urls`. | `[]` | `{}` |
    | `UTM_CAMPAIGN` | 18 | `TEXT` | The utm_campaign parameter of the ad, extracted from the `final_urls`. | The utm_campaign parameter of the ad, extracted from the `final_urls`. | `[]` | `{}` |
    | `UTM_CONTENT` | 19 | `TEXT` | The utm_content parameter of the ad, extracted from the `final_urls`. | The utm_content parameter of the ad, extracted from the `final_urls`. | `[]` | `{}` |
    | `UTM_TERM` | 20 | `TEXT` | The utm_term parameter of the ad, extracted from the `final_urls`. | The utm_term parameter of the ad, extracted from the `final_urls`. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt.split_part`
    *   `macro.dbt.type_string`
    *   `macro.dbt_utils.get_url_host`
    *   `macro.dbt_utils.get_url_path`
    *   `macro.fivetran_utils.fill_staging_columns`
    *   `macro.fivetran_utils.source_relation`
    *   `macro.google_ads.get_ad_history_columns`
    *   `macro.google_ads.google_ads_extract_url_parameter`
    *   `model.google_ads.stg_google_ads__ad_history_tmp`

---
