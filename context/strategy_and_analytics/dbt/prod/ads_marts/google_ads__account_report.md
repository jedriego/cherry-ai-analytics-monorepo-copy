## Model: `google_ads__account_report`

`google_ads__account_report`

*   **Unique ID:** `model.google_ads.google_ads__account_report`
*   **FQN:** `prod.ads_marts.google_ads__account_report`
*   **Description:** Each record in this table represents the daily performance at the account level.
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'google_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `SOURCE_RELATION` | 1 | `TEXT` | The source of the record if the unioning functionality is being used. If not this field will be empty. | The source of the record if the unioning functionality is being used. If not this field will be empty. | `[]` | `{}` |
    | `DATE_DAY` | 2 | `DATE` | The date being reported on. | The date being reported on. | `[]` | `{}` |
    | `ACCOUNT_NAME` | 3 | `TEXT` | The descriptive name of the Customer account. | The descriptive name of the Customer account. | `[]` | `{}` |
    | `ACCOUNT_ID` | 4 | `NUMBER` | The Customer ID. | The Customer ID. | `[]` | `{}` |
    | `CURRENCY_CODE` | 5 | `TEXT` | The currency which the account uses. | The currency which the account uses. | `[]` | `{}` |
    | `AUTO_TAGGING_ENABLED` | 6 | `BOOLEAN` | Boolean indicating if the account uses auto tagging within ad urls. | Boolean indicating if the account uses auto tagging within ad urls. | `[]` | `{}` |
    | `TIME_ZONE` | 7 | `TEXT` | The time zone which the account is located. | The time zone which the account is located. | `[]` | `{}` |
    | `SPEND` | 8 | `NUMBER` | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. | `[]` | `{}` |
    | `CLICKS` | 9 | `NUMBER` | The number of clicks. | The number of clicks. | `[]` | `{}` |
    | `IMPRESSIONS` | 10 | `NUMBER` | Count of how often your ad has appeared on a search results page or website on the Google Network. | Count of how often your ad has appeared on a search results page or website on the Google Network. | `[]` | `{}` |
    | `CONVERSIONS` | 11 | `FLOAT` | The number of conversions you've received, across your conversion actions. Conversions are measured with conversion tracking and may include [modeled](https://support.google.com/google-ads/answer/10081327?sjid=12862894247631803415-NC) conversions in cases where you are not able to observe all conversions that took place. You can use this column to see how often your ads led customers to actions that you’ve defined as valuable for your business. | The number of conversions you've received, across your conversion actions. Conversions are measured with conversion tracking and may include [modeled](https://support.google.com/google-ads/answer/10081327?sjid=12862894247631803415-NC) conversions in cases where you are not able to observe all conversions that took place. You can use this column to see how often your ads led customers to actions that you’ve defined as valuable for your business. | `[]` | `{}` |
    | `CONVERSIONS_VALUE` | 12 | `FLOAT` | The sum of monetary values for your `conversions`. You have to enter a value in the Google Ads UI for your conversion actions to make this metric useful. | The sum of monetary values for your `conversions`. You have to enter a value in the Google Ads UI for your conversion actions to make this metric useful. | `[]` | `{}` |
    | `VIEW_THROUGH_CONVERSIONS` | 13 | `NUMBER` | For video campaigns, view-through conversions tell you when an _impression_ of your video ad leads to a conversion on your site. The last impression of a video ad will get credit for the view-through conversion.

Keep in mind: An impression is different than a “view” of a video ad. A “view” is counted when someone watches 30 seconds (or the whole ad if it’s shorter than 30 seconds) or clicks on a part of the ad. A “view” that leads to a conversion is counted in the `conversions` column. | For video campaigns, view-through conversions tell you when an _impression_ of your video ad leads to a conversion on your site. The last impression of a video ad will get credit for the view-through conversion.

Keep in mind: An impression is different than a “view” of a video ad. A “view” is counted when someone watches 30 seconds (or the whole ad if it’s shorter than 30 seconds) or clicks on a part of the ad. A “view” that leads to a conversion is counted in the `conversions` column. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt_utils.group_by`
    *   `macro.google_ads.google_ads_persist_pass_through_columns`
    *   `model.google_ads.stg_google_ads__account_history`
    *   `model.google_ads.stg_google_ads__account_stats`

---
