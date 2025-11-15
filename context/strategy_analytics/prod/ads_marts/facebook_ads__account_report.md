## Model: `facebook_ads__account_report`

`facebook_ads__account_report`

*   **Unique ID:** `model.facebook_ads.facebook_ads__account_report`
*   **FQN:** `prod.ads_marts.facebook_ads__account_report`
*   **Description:** Each record represents the daily performance of a Facebook account.
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'facebook_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `SOURCE_RELATION` | 1 | `TEXT` | The source of the record if the unioning functionality is being used. If not this field will be empty. | The source of the record if the unioning functionality is being used. If not this field will be empty. | `[]` | `{}` |
    | `DATE_DAY` | 2 | `DATE` | The date of the performance. | The date of the performance. | `[]` | `{}` |
    | `ACCOUNT_ID` | 3 | `NUMBER` | The ID of the related account. | The ID of the related account. | `[]` | `{}` |
    | `ACCOUNT_NAME` | 4 | `TEXT` | The name of the related account. | The name of the related account. | `[]` | `{}` |
    | `ACCOUNT_STATUS` | 5 | `TEXT` | Current status of account. | Current status of account. | `[]` | `{}` |
    | `BUSINESS_COUNTRY_CODE` | 6 | `TEXT` | Country code of business associated to account. | Country code of business associated to account. | `[]` | `{}` |
    | `CREATED_AT` | 7 | `TIMESTAMP_TZ` | The time account was created. | The time account was created. | `[]` | `{}` |
    | `CURRENCY` | 8 | `TEXT` | Currency associated with account. | Currency associated with account. | `[]` | `{}` |
    | `TIMEZONE_NAME` | 9 | `TEXT` | Timezone associated with account. | Timezone associated with account. | `[]` | `{}` |
    | `CLICKS` | 10 | `NUMBER` | The number of clicks the ad had on the given day. | The number of clicks the ad had on the given day. | `[]` | `{}` |
    | `IMPRESSIONS` | 11 | `NUMBER` | The number of impressions the ad had on the given day. | The number of impressions the ad had on the given day. | `[]` | `{}` |
    | `SPEND` | 12 | `FLOAT` | The spend on the ad in the given day. | The spend on the ad in the given day. | `[]` | `{}` |
    | `CONVERSIONS` | 13 | `FLOAT` | Total number of conversions using the default attribution window on the given day. See the  [README](https://github.com/fivetran/dbt_facebook_ads?tab=readme-ov-file#configuring-conversion-action-types)  for details around conversion-eligible action types.
 | Total number of conversions using the default attribution window on the given day. See the  [README](https://github.com/fivetran/dbt_facebook_ads?tab=readme-ov-file#configuring-conversion-action-types)  for details around conversion-eligible action types.
 | `[]` | `{}` |
    | `CONVERSIONS_VALUE` | 14 | `FLOAT` | Total monetary of conversions using the default attribution window on the given day. See the  [README](https://github.com/fivetran/dbt_facebook_ads?tab=readme-ov-file#configuring-conversion-action-types)  for details around conversion-eligible action types.
 | Total monetary of conversions using the default attribution window on the given day. See the  [README](https://github.com/fivetran/dbt_facebook_ads?tab=readme-ov-file#configuring-conversion-action-types)  for details around conversion-eligible action types.
 | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt_utils.group_by`
    *   `macro.facebook_ads.facebook_ads_persist_pass_through_columns`
    *   `model.facebook_ads.int_facebook_ads__conversions`
    *   `model.facebook_ads.stg_facebook_ads__account_history`
    *   `model.facebook_ads.stg_facebook_ads__basic_ad`

---
