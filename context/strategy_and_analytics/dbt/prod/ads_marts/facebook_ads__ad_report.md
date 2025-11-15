## Model: `facebook_ads__ad_report`

`facebook_ads__ad_report`

*   **Unique ID:** `model.facebook_ads.facebook_ads__ad_report`
*   **FQN:** `prod.ads_marts.facebook_ads__ad_report`
*   **Description:** Each record represents the daily performance of a Facebook ad.
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
    | `CONVERSION_DOMAIN` | 11 | `TEXT` | The domain you've configured the ad to convert to. | The domain you've configured the ad to convert to. | `[]` | `{}` |
    | `CLICKS` | 12 | `NUMBER` | The number of clicks the ad had on the given day. | The number of clicks the ad had on the given day. | `[]` | `{}` |
    | `IMPRESSIONS` | 13 | `NUMBER` | The number of impressions the ad had on the given day. | The number of impressions the ad had on the given day. | `[]` | `{}` |
    | `SPEND` | 14 | `FLOAT` | The spend on the ad in the given day. | The spend on the ad in the given day. | `[]` | `{}` |
    | `CONVERSIONS` | 15 | `FLOAT` | Total number of conversions using the default attribution window on the given day. See the  [README](https://github.com/fivetran/dbt_facebook_ads?tab=readme-ov-file#configuring-conversion-action-types)  for details around conversion-eligible action types.
 | Total number of conversions using the default attribution window on the given day. See the  [README](https://github.com/fivetran/dbt_facebook_ads?tab=readme-ov-file#configuring-conversion-action-types)  for details around conversion-eligible action types.
 | `[]` | `{}` |
    | `CONVERSIONS_VALUE` | 16 | `FLOAT` | Total monetary of conversions using the default attribution window on the given day. See the  [README](https://github.com/fivetran/dbt_facebook_ads?tab=readme-ov-file#configuring-conversion-action-types)  for details around conversion-eligible action types.
 | Total monetary of conversions using the default attribution window on the given day. See the  [README](https://github.com/fivetran/dbt_facebook_ads?tab=readme-ov-file#configuring-conversion-action-types)  for details around conversion-eligible action types.
 | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt_utils.group_by`
    *   `macro.facebook_ads.facebook_ads_persist_pass_through_columns`
    *   `model.facebook_ads.int_facebook_ads__conversions`
    *   `model.facebook_ads.stg_facebook_ads__account_history`
    *   `model.facebook_ads.stg_facebook_ads__ad_history`
    *   `model.facebook_ads.stg_facebook_ads__ad_set_history`
    *   `model.facebook_ads.stg_facebook_ads__basic_ad`
    *   `model.facebook_ads.stg_facebook_ads__campaign_history`

---
