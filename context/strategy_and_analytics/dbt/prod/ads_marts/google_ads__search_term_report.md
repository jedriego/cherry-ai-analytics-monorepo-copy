## Model: `google_ads__search_term_report`

`google_ads__search_term_report`

*   **Unique ID:** `model.google_ads.google_ads__search_term_report`
*   **FQN:** `prod.ads_marts.google_ads__search_term_report`
*   **Description:** Each record in this table represents the daily performance at the ad group level for search terms matching tracked keywords.
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
    | `CAMPAIGN_NAME` | 6 | `TEXT` | The name of the Campaign. | The name of the Campaign. | `[]` | `{}` |
    | `CAMPAIGN_ID` | 7 | `NUMBER` | The ID of the Campaign. | The ID of the Campaign. | `[]` | `{}` |
    | `AD_GROUP_NAME` | 8 | `TEXT` | The name of the AdGroup. | The name of the AdGroup. | `[]` | `{}` |
    | `AD_GROUP_ID` | 9 | `TEXT` | The ID of the AdGroup. | The ID of the AdGroup. | `[]` | `{}` |
    | `SEARCH_TERM` | 10 | `TEXT` | A word or set of words a person enters when searching on Google or one of Google's Search Network sites | A word or set of words a person enters when searching on Google or one of Google's Search Network sites | `[]` | `{}` |
    | `KEYWORD_TEXT` | 11 | `TEXT` | The text of the keyword (at most 80 characters and 10 words). | The text of the keyword (at most 80 characters and 10 words). | `[]` | `{}` |
    | `CRITERION_ID` | 12 | `TEXT` | Reference to the ad group criterion used for the associated keyword. One `keyword_text` may have multiple `criterion_id` values. | Reference to the ad group criterion used for the associated keyword. One `keyword_text` may have multiple `criterion_id` values. | `[]` | `{}` |
    | `SEARCH_TERM_MATCH_TYPE` | 13 | `TEXT` | How closely the search terms that triggered your ads on Google are related to the actual keywords in your account. Can be `BROAD` ,`EXACT`, `PHRASE`, `UNKNOWN`, or `UNSPECIFIED`.

See more details [here](https://support.google.com/google-ads/answer/7478529?sjid=15681083914881504235-NC&visit_id=638760377693438101-1187740487&rd=1). | How closely the search terms that triggered your ads on Google are related to the actual keywords in your account. Can be `BROAD` ,`EXACT`, `PHRASE`, `UNKNOWN`, or `UNSPECIFIED`.

See more details [here](https://support.google.com/google-ads/answer/7478529?sjid=15681083914881504235-NC&visit_id=638760377693438101-1187740487&rd=1). | `[]` | `{}` |
    | `STATUS` | 14 | `TEXT` | Indicates whether the search term is currently one of your targeted or excluded keywords. Possible values: `ADDED`, `ADDED_EXCLUDED`, `EXCLUDED`, `NONE`, `UNKNOWN`, or `UNSPECIFIED` | Indicates whether the search term is currently one of your targeted or excluded keywords. Possible values: `ADDED`, `ADDED_EXCLUDED`, `EXCLUDED`, `NONE`, `UNKNOWN`, or `UNSPECIFIED` | `[]` | `{}` |
    | `SPEND` | 15 | `NUMBER` | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. | `[]` | `{}` |
    | `CLICKS` | 16 | `NUMBER` | The number of clicks. | The number of clicks. | `[]` | `{}` |
    | `IMPRESSIONS` | 17 | `NUMBER` | Count of how often your ad has appeared on a search results page or website on the Google Network. | Count of how often your ad has appeared on a search results page or website on the Google Network. | `[]` | `{}` |
    | `CONVERSIONS` | 18 | `FLOAT` | The number of conversions you've received, across your conversion actions. Conversions are measured with conversion tracking and may include [modeled](https://support.google.com/google-ads/answer/10081327?sjid=12862894247631803415-NC) conversions in cases where you are not able to observe all conversions that took place. You can use this column to see how often your ads led customers to actions that you’ve defined as valuable for your business. | The number of conversions you've received, across your conversion actions. Conversions are measured with conversion tracking and may include [modeled](https://support.google.com/google-ads/answer/10081327?sjid=12862894247631803415-NC) conversions in cases where you are not able to observe all conversions that took place. You can use this column to see how often your ads led customers to actions that you’ve defined as valuable for your business. | `[]` | `{}` |
    | `CONVERSIONS_VALUE` | 19 | `FLOAT` | The sum of monetary values for your `conversions`. You have to enter a value in the Google Ads UI for your conversion actions to make this metric useful. | The sum of monetary values for your `conversions`. You have to enter a value in the Google Ads UI for your conversion actions to make this metric useful. | `[]` | `{}` |
    | `VIEW_THROUGH_CONVERSIONS` | 20 | `NUMBER` | For video campaigns, view-through conversions tell you when an _impression_ of your video ad leads to a conversion on your site. The last impression of a video ad will get credit for the view-through conversion.

Keep in mind: An impression is different than a “view” of a video ad. A “view” is counted when someone watches 30 seconds (or the whole ad if it’s shorter than 30 seconds) or clicks on a part of the ad. A “view” that leads to a conversion is counted in the `conversions` column. | For video campaigns, view-through conversions tell you when an _impression_ of your video ad leads to a conversion on your site. The last impression of a video ad will get credit for the view-through conversion.

Keep in mind: An impression is different than a “view” of a video ad. A “view” is counted when someone watches 30 seconds (or the whole ad if it’s shorter than 30 seconds) or clicks on a part of the ad. A “view” that leads to a conversion is counted in the `conversions` column. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt_utils.group_by`
    *   `macro.google_ads.google_ads_persist_pass_through_columns`
    *   `model.google_ads.stg_google_ads__account_history`
    *   `model.google_ads.stg_google_ads__ad_group_history`
    *   `model.google_ads.stg_google_ads__campaign_history`
    *   `model.google_ads.stg_google_ads__search_term_keyword_stats`

---
