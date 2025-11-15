## Model: `stg_google_ads__ad_stats`

`stg_google_ads__ad_stats`

*   **Unique ID:** `model.google_ads.stg_google_ads__ad_stats`
*   **FQN:** `prod.ads_marts.stg_google_ads__ad_stats`
*   **Description:** Each record represents the daily performance of an ad in Google Ads broken down to the ad network, device type, and ad_group_id.
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'google_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `SOURCE_RELATION` | 1 | `TEXT` | The source of the record if the unioning functionality is being used. If not this field will be empty. | The source of the record if the unioning functionality is being used. If not this field will be empty. | `[]` | `{}` |
    | `ACCOUNT_ID` | 2 | `NUMBER` | The Customer ID. | The Customer ID. | `[]` | `{}` |
    | `DATE_DAY` | 3 | `DATE` | The date being reported on. | The date being reported on. | `[]` | `{}` |
    | `AD_GROUP_ID` | 4 | `TEXT` | The ID of the AdGroup. | The ID of the AdGroup. | `[]` | `{}` |
    | `KEYWORD_AD_GROUP_CRITERION` | 5 | `TEXT` | The ad group which the keyword criterion resides. | The ad group which the keyword criterion resides. | `[]` | `{}` |
    | `AD_NETWORK_TYPE` | 6 | `TEXT` | The Google Ad network type used across the account. | The Google Ad network type used across the account. | `[]` | `{}` |
    | `DEVICE` | 7 | `TEXT` | Account ad performance per unique device where the ads were served. | Account ad performance per unique device where the ads were served. | `[]` | `{}` |
    | `AD_ID` | 8 | `NUMBER` | The ID of the Ad. | The ID of the Ad. | `[]` | `{}` |
    | `CAMPAIGN_ID` | 9 | `NUMBER` | The ID of the Campaign. | The ID of the Campaign. | `[]` | `{}` |
    | `CLICKS` | 10 | `NUMBER` | The number of clicks. | The number of clicks. | `[]` | `{}` |
    | `SPEND` | 11 | `NUMBER` | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. | `[]` | `{}` |
    | `IMPRESSIONS` | 12 | `NUMBER` | Count of how often your ad has appeared on a search results page or website on the Google Network. | Count of how often your ad has appeared on a search results page or website on the Google Network. | `[]` | `{}` |
    | `CONVERSIONS` | 13 | `FLOAT` | The number of conversions you've received, across your conversion actions. Conversions are measured with conversion tracking and may include [modeled](https://support.google.com/google-ads/answer/10081327?sjid=12862894247631803415-NC) conversions in cases where you are not able to observe all conversions that took place. You can use this column to see how often your ads led customers to actions that you’ve defined as valuable for your business. | The number of conversions you've received, across your conversion actions. Conversions are measured with conversion tracking and may include [modeled](https://support.google.com/google-ads/answer/10081327?sjid=12862894247631803415-NC) conversions in cases where you are not able to observe all conversions that took place. You can use this column to see how often your ads led customers to actions that you’ve defined as valuable for your business. | `[]` | `{}` |
    | `CONVERSIONS_VALUE` | 14 | `FLOAT` | The sum of monetary values for your `conversions`. You have to enter a value in the Google Ads UI for your conversion actions to make this metric useful. | The sum of monetary values for your `conversions`. You have to enter a value in the Google Ads UI for your conversion actions to make this metric useful. | `[]` | `{}` |
    | `VIEW_THROUGH_CONVERSIONS` | 15 | `NUMBER` | For video campaigns, view-through conversions tell you when an _impression_ of your video ad leads to a conversion on your site. The last impression of a video ad will get credit for the view-through conversion.

Keep in mind: An impression is different than a “view” of a video ad. A “view” is counted when someone watches 30 seconds (or the whole ad if it’s shorter than 30 seconds) or clicks on a part of the ad. A “view” that leads to a conversion is counted in the `conversions` column. | For video campaigns, view-through conversions tell you when an _impression_ of your video ad leads to a conversion on your site. The last impression of a video ad will get credit for the view-through conversion.

Keep in mind: An impression is different than a “view” of a video ad. A “view” is counted when someone watches 30 seconds (or the whole ad if it’s shorter than 30 seconds) or clicks on a part of the ad. A “view” that leads to a conversion is counted in the `conversions` column. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt.split_part`
    *   `macro.dbt.type_string`
    *   `macro.fivetran_utils.fill_staging_columns`
    *   `macro.fivetran_utils.source_relation`
    *   `macro.google_ads.get_ad_stats_columns`
    *   `macro.google_ads.google_ads_fill_pass_through_columns`
    *   `model.google_ads.stg_google_ads__ad_stats_tmp`

---
