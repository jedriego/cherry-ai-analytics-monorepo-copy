## Model: `facebook_ads__ad_set_report`

`facebook_ads__ad_set_report`

*   **Unique ID:** `model.facebook_ads.facebook_ads__ad_set_report`
*   **FQN:** `prod.ads_marts.facebook_ads__ad_set_report`
*   **Description:** Each record represents the daily performance of a Facebook ad set.
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
    | `START_AT` | 9 | `TIMESTAMP_TZ` | Timestamp of designated ad set start time. | Timestamp of designated ad set start time. | `[]` | `{}` |
    | `END_AT` | 10 | `TIMESTAMP_TZ` | Timestamp of designated ad set end time. | Timestamp of designated ad set end time. | `[]` | `{}` |
    | `BID_STRATEGY` | 11 | `TEXT` | Bid strategy values are - 'LOWEST_COST_WITHOUT_CAP', 'LOWEST_COST_WITH_BID_CAP', 'COST_CAP', 'LOWEST_COST_WITH_MIN_ROAS'. | Bid strategy values are - 'LOWEST_COST_WITHOUT_CAP', 'LOWEST_COST_WITH_BID_CAP', 'COST_CAP', 'LOWEST_COST_WITH_MIN_ROAS'. | `[]` | `{}` |
    | `DAILY_BUDGET` | 12 | `NUMBER` | Daily budget of ad set. | Daily budget of ad set. | `[]` | `{}` |
    | `BUDGET_REMAINING` | 13 | `NUMBER` | Remaining budget of ad set. | Remaining budget of ad set. | `[]` | `{}` |
    | `OPTIMIZATION_GOAL` | 14 | `TEXT` | The optimization goal this ad set is using. Possible values defined [here](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign/#fields). | The optimization goal this ad set is using. Possible values defined [here](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign/#fields). | `[]` | `{}` |
    | `CLICKS` | 15 | `NUMBER` | The number of clicks the ad had on the given day. | The number of clicks the ad had on the given day. | `[]` | `{}` |
    | `IMPRESSIONS` | 16 | `NUMBER` | The number of impressions the ad had on the given day. | The number of impressions the ad had on the given day. | `[]` | `{}` |
    | `SPEND` | 17 | `FLOAT` | The spend on the ad in the given day. | The spend on the ad in the given day. | `[]` | `{}` |
    | `CONVERSIONS` | 18 | `FLOAT` | Total number of conversions using the default attribution window on the given day. See the  [README](https://github.com/fivetran/dbt_facebook_ads?tab=readme-ov-file#configuring-conversion-action-types)  for details around conversion-eligible action types.
 | Total number of conversions using the default attribution window on the given day. See the  [README](https://github.com/fivetran/dbt_facebook_ads?tab=readme-ov-file#configuring-conversion-action-types)  for details around conversion-eligible action types.
 | `[]` | `{}` |
    | `CONVERSIONS_VALUE` | 19 | `FLOAT` | Total monetary of conversions using the default attribution window on the given day. See the  [README](https://github.com/fivetran/dbt_facebook_ads?tab=readme-ov-file#configuring-conversion-action-types)  for details around conversion-eligible action types.
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
