## Model: `stg_facebook_ads__basic_ad`

`stg_facebook_ads__basic_ad`

*   **Unique ID:** `model.facebook_ads.stg_facebook_ads__basic_ad`
*   **FQN:** `prod.ads_marts.stg_facebook_ads__basic_ad`
*   **Description:** Each record represents the daily performance of an ad in Facebook.
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'facebook_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `SOURCE_RELATION` | 1 | `TEXT` | The source of the record if the unioning functionality is being used. If not this field will be empty. | The source of the record if the unioning functionality is being used. If not this field will be empty. | `[]` | `{}` |
    | `AD_ID` | 2 | `NUMBER` | The ID of the ad the report relates to. | The ID of the ad the report relates to. | `[]` | `{}` |
    | `AD_NAME` | 3 | `TEXT` | Name of the ad the report relates to. | Name of the ad the report relates to. | `[]` | `{}` |
    | `AD_SET_NAME` | 4 | `TEXT` | Name of the ad set the report relates to. | Name of the ad set the report relates to. | `[]` | `{}` |
    | `DATE_DAY` | 5 | `DATE` | The date of the reported performance. | The date of the reported performance. | `[]` | `{}` |
    | `ACCOUNT_ID` | 6 | `NUMBER` | The ID of the ad account that this ad belongs to. | The ID of the ad account that this ad belongs to. | `[]` | `{}` |
    | `IMPRESSIONS` | 7 | `NUMBER` | The number of impressions the ad had on the given day. | The number of impressions the ad had on the given day. | `[]` | `{}` |
    | `CLICKS` | 8 | `NUMBER` | The number of clicks the ad had on the given day. | The number of clicks the ad had on the given day. | `[]` | `{}` |
    | `SPEND` | 9 | `FLOAT` | The spend on the ad in the given day. | The spend on the ad in the given day. | `[]` | `{}` |
    | `REACH` | 10 | `NUMBER` | The number of people who saw any content from your Page or about your Page. This metric is estimated. | The number of people who saw any content from your Page or about your Page. This metric is estimated. | `[]` | `{}` |
    | `FREQUENCY` | 11 | `FLOAT` | The average number of times each person saw your ad; it is calculated as impressions divided by reach. | The average number of times each person saw your ad; it is calculated as impressions divided by reach. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt.type_bigint`
    *   `macro.facebook_ads.get_basic_ad_columns`
    *   `macro.fivetran_utils.fill_pass_through_columns`
    *   `macro.fivetran_utils.fill_staging_columns`
    *   `macro.fivetran_utils.source_relation`
    *   `model.facebook_ads.stg_facebook_ads__basic_ad_tmp`

---
