## Model: `facebook_ads__campaign_report`

`facebook_ads__campaign_report`

*   **Unique ID:** `model.facebook_ads.facebook_ads__campaign_report`
*   **FQN:** `prod.ads_marts.facebook_ads__campaign_report`
*   **Description:** Each record represents the daily performance of a Facebook campaign.
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
    | `START_AT` | 7 | `TIMESTAMP_TZ` | Timestamp of designated campaign start time. | Timestamp of designated campaign start time. | `[]` | `{}` |
    | `END_AT` | 8 | `TIMESTAMP_TZ` | Timestamp of designated campaign end time. | Timestamp of designated campaign end time. | `[]` | `{}` |
    | `STATUS` | 9 | `TEXT` | Status values are - 'ACTIVE', 'PAUSED', 'DELETED', 'ARCHIVED'. | Status values are - 'ACTIVE', 'PAUSED', 'DELETED', 'ARCHIVED'. | `[]` | `{}` |
    | `DAILY_BUDGET` | 10 | `NUMBER` | Daily budget of campaign. | Daily budget of campaign. | `[]` | `{}` |
    | `LIFETIME_BUDGET` | 11 | `NUMBER` | Lifetime budget of the campaign. | Lifetime budget of the campaign. | `[]` | `{}` |
    | `BUDGET_REMAINING` | 12 | `FLOAT` | Remaining budget of campaign. | Remaining budget of campaign. | `[]` | `{}` |
    | `CLICKS` | 13 | `NUMBER` | The number of clicks the ad had on the given day. | The number of clicks the ad had on the given day. | `[]` | `{}` |
    | `IMPRESSIONS` | 14 | `NUMBER` | The number of impressions the ad had on the given day. | The number of impressions the ad had on the given day. | `[]` | `{}` |
    | `SPEND` | 15 | `FLOAT` | The spend on the ad in the given day. | The spend on the ad in the given day. | `[]` | `{}` |
    | `CONVERSIONS` | 16 | `FLOAT` | Total number of conversions using the default attribution window on the given day. See the  [README](https://github.com/fivetran/dbt_facebook_ads?tab=readme-ov-file#configuring-conversion-action-types)  for details around conversion-eligible action types.
 | Total number of conversions using the default attribution window on the given day. See the  [README](https://github.com/fivetran/dbt_facebook_ads?tab=readme-ov-file#configuring-conversion-action-types)  for details around conversion-eligible action types.
 | `[]` | `{}` |
    | `CONVERSIONS_VALUE` | 17 | `FLOAT` | Total monetary of conversions using the default attribution window on the given day. See the  [README](https://github.com/fivetran/dbt_facebook_ads?tab=readme-ov-file#configuring-conversion-action-types)  for details around conversion-eligible action types.
 | Total monetary of conversions using the default attribution window on the given day. See the  [README](https://github.com/fivetran/dbt_facebook_ads?tab=readme-ov-file#configuring-conversion-action-types)  for details around conversion-eligible action types.
 | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt_utils.group_by`
    *   `macro.facebook_ads.facebook_ads_persist_pass_through_columns`
    *   `model.facebook_ads.int_facebook_ads__conversions`
    *   `model.facebook_ads.stg_facebook_ads__account_history`
    *   `model.facebook_ads.stg_facebook_ads__ad_history`
    *   `model.facebook_ads.stg_facebook_ads__basic_ad`
    *   `model.facebook_ads.stg_facebook_ads__campaign_history`

---
