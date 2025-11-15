## Model: `stg_facebook_ads__basic_ad_actions`

`stg_facebook_ads__basic_ad_actions`

*   **Unique ID:** `model.facebook_ads.stg_facebook_ads__basic_ad_actions`
*   **FQN:** `prod.ads_marts.stg_facebook_ads__basic_ad_actions`
*   **Description:** Each record represents the daily conversion performance of an ad in Facebook. This is the prebuilt `basic_ad` report broken down by `action_type`. Include more conversion value metrics by configuring the `facebook_ads__basic_ad_actions_passthrough_metrics` variable.

*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'facebook_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `SOURCE_RELATION` | 1 | `TEXT` | The source of the record if the unioning functionality is being used. If not this field will be empty. | The source of the record if the unioning functionality is being used. If not this field will be empty. | `[]` | `{}` |
    | `ACTION_TYPE` | 2 | `TEXT` | The kind of actions taken on your ad, Page, app or event after your ad was served to someone, even if they didn't click on it. Action types include Page likes, app installs, conversions, event responses and more. Actions prepended by app_custom_event come from mobile app events and actions prepended by offsite_conversion come from the Facebook Pixel.
 | The kind of actions taken on your ad, Page, app or event after your ad was served to someone, even if they didn't click on it. Action types include Page likes, app installs, conversions, event responses and more. Actions prepended by app_custom_event come from mobile app events and actions prepended by offsite_conversion come from the Facebook Pixel.
 | `[]` | `{}` |
    | `AD_ID` | 3 | `NUMBER` | The ID of the ad the report relates to. | The ID of the ad the report relates to. | `[]` | `{}` |
    | `_FIVETRAN_ID` | 4 | `TEXT` | Unique record identifier. | Unique record identifier. | `[]` | `{}` |
    | `DATE_DAY` | 5 | `DATE` | The date of the reported performance. | The date of the reported performance. | `[]` | `{}` |
    | `INDEX` | 6 | `NUMBER` | Index reflecting the `action_type` tracked for this ad on this day. A primary key created by Fivetran utilized for tracking data, specifically when there are multiple rows associated with a single row in the parent table. | Index reflecting the `action_type` tracked for this ad on this day. A primary key created by Fivetran utilized for tracking data, specifically when there are multiple rows associated with a single row in the parent table. | `[]` | `{}` |
    | `CONVERSIONS` | 7 | `FLOAT` | Conversion metric value using the default attribution window. | Conversion metric value using the default attribution window. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt.type_bigint`
    *   `macro.dbt.type_float`
    *   `macro.facebook_ads.facebook_ads_fill_pass_through_columns`
    *   `macro.facebook_ads.get_basic_ad_actions_columns`
    *   `macro.fivetran_utils.fill_staging_columns`
    *   `macro.fivetran_utils.source_relation`
    *   `model.facebook_ads.stg_facebook_ads__basic_ad_actions_tmp`

---
