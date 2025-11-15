## Model: `stg_google_ads__search_term_keyword_stats`

`stg_google_ads__search_term_keyword_stats`

*   **Unique ID:** `model.google_ads.stg_google_ads__search_term_keyword_stats`
*   **FQN:** `prod.ads_marts.stg_google_ads__search_term_keyword_stats`
*   **Description:** Each record represents the daily performance of a search term (including associated tracked keywords) in Google Ads.
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'google_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `SOURCE_RELATION` | 1 | `TEXT` | The source of the record if the unioning functionality is being used. If not this field will be empty. | The source of the record if the unioning functionality is being used. If not this field will be empty. | `[]` | `{}` |
    | `ACCOUNT_ID` | 2 | `NUMBER` | The Customer ID. | The Customer ID. | `[]` | `{}` |
    | `DATE_DAY` | 3 | `DATE` | The date being reported on. | The date being reported on. | `[]` | `{}` |
    | `SEARCH_TERM_ID` | 4 | `TEXT` | The unique ID of the search term record. | The unique ID of the search term record. | `[]` | `{}` |
    | `AD_GROUP_ID` | 5 | `TEXT` | The ID of the AdGroup. | The ID of the AdGroup. | `[]` | `{}` |
    | `CAMPAIGN_ID` | 6 | `NUMBER` | The ID of the Campaign. | The ID of the Campaign. | `[]` | `{}` |
    | `KEYWORD_AD_GROUP_CRITERION` | 7 | `TEXT` | The resource name of the keyword's ad group criterion. Ad group criterion resource names have the form: `customers/{customer_id}/adGroupCriteria/{ad_group_id}~{criterion_id}` | The resource name of the keyword's ad group criterion. Ad group criterion resource names have the form: `customers/{customer_id}/adGroupCriteria/{ad_group_id}~{criterion_id}` | `[]` | `{}` |
    | `CRITERION_ID` | 8 | `TEXT` | Reference to the ad group criterion used for the associated keyword. One `keyword_text` may have multiple `criterion_id` values. | Reference to the ad group criterion used for the associated keyword. One `keyword_text` may have multiple `criterion_id` values. | `[]` | `{}` |
    | `SEARCH_TERM` | 9 | `TEXT` | A word or set of words a person enters when searching on Google or one of Google's Search Network sites | A word or set of words a person enters when searching on Google or one of Google's Search Network sites | `[]` | `{}` |
    | `KEYWORD_TEXT` | 10 | `TEXT` | The text of the keyword (at most 80 characters and 10 words). | The text of the keyword (at most 80 characters and 10 words). | `[]` | `{}` |
    | `SEARCH_TERM_MATCH_TYPE` | 11 | `TEXT` | How closely the search terms that triggered your ads on Google are related to the actual keywords in your account. Can be `BROAD` ,`EXACT`, `PHRASE`, `UNKNOWN`, or `UNSPECIFIED`.

See more details [here](https://support.google.com/google-ads/answer/7478529?sjid=15681083914881504235-NC&visit_id=638760377693438101-1187740487&rd=1). | How closely the search terms that triggered your ads on Google are related to the actual keywords in your account. Can be `BROAD` ,`EXACT`, `PHRASE`, `UNKNOWN`, or `UNSPECIFIED`.

See more details [here](https://support.google.com/google-ads/answer/7478529?sjid=15681083914881504235-NC&visit_id=638760377693438101-1187740487&rd=1). | `[]` | `{}` |
    | `STATUS` | 12 | `TEXT` | Indicates whether the search term is currently one of your targeted or excluded keywords. Possible values: `ADDED`, `ADDED_EXCLUDED`, `EXCLUDED`, `NONE`, `UNKNOWN`, or `UNSPECIFIED` | Indicates whether the search term is currently one of your targeted or excluded keywords. Possible values: `ADDED`, `ADDED_EXCLUDED`, `EXCLUDED`, `NONE`, `UNKNOWN`, or `UNSPECIFIED` | `[]` | `{}` |
    | `CLICKS` | 13 | `NUMBER` | The number of clicks. | The number of clicks. | `[]` | `{}` |
    | `SPEND` | 14 | `NUMBER` | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. | The sum of your cost-per-click (CPC) and cost-per-thousand impressions (CPM) costs during this period. | `[]` | `{}` |
    | `IMPRESSIONS` | 15 | `NUMBER` | Count of how often your ad has appeared on a search results page or website on the Google Network. | Count of how often your ad has appeared on a search results page or website on the Google Network. | `[]` | `{}` |
    | `CONVERSIONS` | 16 | `FLOAT` | The number of conversions you've received, across your conversion actions. Conversions are measured with conversion tracking and may include [modeled](https://support.google.com/google-ads/answer/10081327?sjid=12862894247631803415-NC) conversions in cases where you are not able to observe all conversions that took place. You can use this column to see how often your ads led customers to actions that you’ve defined as valuable for your business. | The number of conversions you've received, across your conversion actions. Conversions are measured with conversion tracking and may include [modeled](https://support.google.com/google-ads/answer/10081327?sjid=12862894247631803415-NC) conversions in cases where you are not able to observe all conversions that took place. You can use this column to see how often your ads led customers to actions that you’ve defined as valuable for your business. | `[]` | `{}` |
    | `CONVERSIONS_VALUE` | 17 | `FLOAT` | The sum of monetary values for your `conversions`. You have to enter a value in the Google Ads UI for your conversion actions to make this metric useful. | The sum of monetary values for your `conversions`. You have to enter a value in the Google Ads UI for your conversion actions to make this metric useful. | `[]` | `{}` |
    | `VIEW_THROUGH_CONVERSIONS` | 18 | `NUMBER` | For video campaigns, view-through conversions tell you when an _impression_ of your video ad leads to a conversion on your site. The last impression of a video ad will get credit for the view-through conversion.

Keep in mind: An impression is different than a “view” of a video ad. A “view” is counted when someone watches 30 seconds (or the whole ad if it’s shorter than 30 seconds) or clicks on a part of the ad. A “view” that leads to a conversion is counted in the `conversions` column. | For video campaigns, view-through conversions tell you when an _impression_ of your video ad leads to a conversion on your site. The last impression of a video ad will get credit for the view-through conversion.

Keep in mind: An impression is different than a “view” of a video ad. A “view” is counted when someone watches 30 seconds (or the whole ad if it’s shorter than 30 seconds) or clicks on a part of the ad. A “view” that leads to a conversion is counted in the `conversions` column. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt.split_part`
    *   `macro.dbt.type_string`
    *   `macro.fivetran_utils.fill_staging_columns`
    *   `macro.fivetran_utils.source_relation`
    *   `macro.google_ads.get_search_term_keyword_stats_columns`
    *   `macro.google_ads.google_ads_fill_pass_through_columns`
    *   `model.google_ads.stg_google_ads__search_term_keyword_stats_tmp`

---
