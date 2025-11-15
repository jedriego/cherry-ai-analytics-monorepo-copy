## Model: `facebook_ads__url_report`

`facebook_ads__url_report`

*   **Unique ID:** `model.facebook_ads.facebook_ads__url_report`
*   **FQN:** `prod.ads_marts.facebook_ads__url_report`
*   **Description:** Each record represents the daily performance of a Facebook ad at the URL level.
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'facebook_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `SOURCE_RELATION` | 1 | `TEXT` | The source of the record if the unioning functionality is being used. If not this field will be empty. | The source of the record if the unioning functionality is being used. If not this field will be empty. | `[]` | `{}` |
    | `DATE_DAY` | 2 | `DATE` | The date of the performance. | The date of the performance. | `[]` | `{}` |
    | `ACCOUNT_ID` | 3 | `NUMBER` | The ID of the related account. | The ID of the related account. | `[]` | `{}` |
    | `ACCOUNT_NAME` | 4 | `TEXT` | The name of the related account. | The name of the related account. | `[]` | `{}` |
    | `CAMPAIGN_ID` | 5 | `NUMBER` | The ID of the related campaign. | The ID of the related campaign. | `[]` | `{}` |
    | `CAMPAIGN_NAME` | 6 | `TEXT` | The name of the related campaign. | The name of the related campaign. | `[]` | `{}` |
    | `AD_SET_ID` | 7 | `NUMBER` | The ID of the related ad set. | The ID of the related ad set. | `[]` | `{}` |
    | `AD_SET_NAME` | 8 | `TEXT` | The name of the related ad set. | The name of the related ad set. | `[]` | `{}` |
    | `AD_ID` | 9 | `NUMBER` | The ID of the related ad. | The ID of the related ad. | `[]` | `{}` |
    | `AD_NAME` | 10 | `TEXT` | The name of the related ad. | The name of the related ad. | `[]` | `{}` |
    | `CREATIVE_ID` | 11 | `NUMBER` | The ID of the related creative. | The ID of the related creative. | `[]` | `{}` |
    | `CREATIVE_NAME` | 12 | `TEXT` | The name of the related creative. | The name of the related creative. | `[]` | `{}` |
    | `BASE_URL` | 13 | `TEXT` | The base URL of the ad, extracted from the page_link and template_page_link. | The base URL of the ad, extracted from the page_link and template_page_link. | `[]` | `{}` |
    | `URL_HOST` | 14 | `TEXT` | The URL host of the ad, extracted from the page_link and template_page_link. | The URL host of the ad, extracted from the page_link and template_page_link. | `[]` | `{}` |
    | `URL_PATH` | 15 | `TEXT` | The URL path of the ad, extracted from the page_link and template_page_link. | The URL path of the ad, extracted from the page_link and template_page_link. | `[]` | `{}` |
    | `UTM_SOURCE` | 16 | `TEXT` | The utm_source parameter of the ad, extracted from the page_link and template_page_link. | The utm_source parameter of the ad, extracted from the page_link and template_page_link. | `[]` | `{}` |
    | `UTM_MEDIUM` | 17 | `TEXT` | The utm_medium parameter of the ad, extracted from the page_link and template_page_link. | The utm_medium parameter of the ad, extracted from the page_link and template_page_link. | `[]` | `{}` |
    | `UTM_CAMPAIGN` | 18 | `TEXT` | The utm_campaign parameter of the ad, extracted from the page_link and template_page_link. | The utm_campaign parameter of the ad, extracted from the page_link and template_page_link. | `[]` | `{}` |
    | `UTM_CONTENT` | 19 | `TEXT` | The utm_content parameter of the ad, extracted from the page_link and template_page_link. | The utm_content parameter of the ad, extracted from the page_link and template_page_link. | `[]` | `{}` |
    | `UTM_TERM` | 20 | `TEXT` | The utm_term parameter of the ad, extracted from the page_link and template_page_link. | The utm_term parameter of the ad, extracted from the page_link and template_page_link. | `[]` | `{}` |
    | `CLICKS` | 21 | `NUMBER` | The number of clicks the ad had on the given day. | The number of clicks the ad had on the given day. | `[]` | `{}` |
    | `IMPRESSIONS` | 22 | `NUMBER` | The number of impressions the ad had on the given day. | The number of impressions the ad had on the given day. | `[]` | `{}` |
    | `SPEND` | 23 | `FLOAT` | The spend on the ad in the given day. | The spend on the ad in the given day. | `[]` | `{}` |
    | `CONVERSIONS` | 24 | `FLOAT` | Total number of conversions using the default attribution window on the given day. See the  [README](https://github.com/fivetran/dbt_facebook_ads?tab=readme-ov-file#configuring-conversion-action-types)  for details around conversion-eligible action types.
 | Total number of conversions using the default attribution window on the given day. See the  [README](https://github.com/fivetran/dbt_facebook_ads?tab=readme-ov-file#configuring-conversion-action-types)  for details around conversion-eligible action types.
 | `[]` | `{}` |
    | `CONVERSIONS_VALUE` | 25 | `FLOAT` | Total monetary of conversions using the default attribution window on the given day. See the  [README](https://github.com/fivetran/dbt_facebook_ads?tab=readme-ov-file#configuring-conversion-action-types)  for details around conversion-eligible action types.
 | Total monetary of conversions using the default attribution window on the given day. See the  [README](https://github.com/fivetran/dbt_facebook_ads?tab=readme-ov-file#configuring-conversion-action-types)  for details around conversion-eligible action types.
 | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt_utils.group_by`
    *   `macro.facebook_ads.facebook_ads_persist_pass_through_columns`
    *   `model.facebook_ads.int_facebook_ads__conversions`
    *   `model.facebook_ads.int_facebook_ads__creative_history`
    *   `model.facebook_ads.stg_facebook_ads__account_history`
    *   `model.facebook_ads.stg_facebook_ads__ad_history`
    *   `model.facebook_ads.stg_facebook_ads__ad_set_history`
    *   `model.facebook_ads.stg_facebook_ads__basic_ad`
    *   `model.facebook_ads.stg_facebook_ads__campaign_history`

---
