## Model: `stg_facebook_ads__ad_set_history`

`stg_facebook_ads__ad_set_history`

*   **Unique ID:** `model.facebook_ads.stg_facebook_ads__ad_set_history`
*   **FQN:** `prod.ads_marts.stg_facebook_ads__ad_set_history`
*   **Description:** Each record in this table reflects a Facebook ad set.
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'facebook_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `SOURCE_RELATION` | 1 | `TEXT` | The source of the record if the unioning functionality is being used. If not this field will be empty. | The source of the record if the unioning functionality is being used. If not this field will be empty. | `[]` | `{}` |
    | `UPDATED_AT` | 2 | `TIMESTAMP_TZ` | The timestamp of the last update of a record. | The timestamp of the last update of a record. | `[]` | `{}` |
    | `AD_SET_ID` | 3 | `NUMBER` | The ID of the ad set. | The ID of the ad set. | `[]` | `{}` |
    | `AD_SET_NAME` | 4 | `TEXT` | The name of the ad set. | The name of the ad set. | `[]` | `{}` |
    | `ACCOUNT_ID` | 5 | `NUMBER` | The ID of the ad account that this ad set belongs to. | The ID of the ad account that this ad set belongs to. | `[]` | `{}` |
    | `CAMPAIGN_ID` | 6 | `NUMBER` | Ad campaign that contains this ad set. | Ad campaign that contains this ad set. | `[]` | `{}` |
    | `START_AT` | 7 | `TIMESTAMP_TZ` | Timestamp of designated ad set start time. | Timestamp of designated ad set start time. | `[]` | `{}` |
    | `END_AT` | 8 | `TIMESTAMP_TZ` | Timestamp of designated ad set end time. | Timestamp of designated ad set end time. | `[]` | `{}` |
    | `BID_STRATEGY` | 9 | `TEXT` | Bid strategy values are - 'LOWEST_COST_WITHOUT_CAP', 'LOWEST_COST_WITH_BID_CAP', 'COST_CAP', 'LOWEST_COST_WITH_MIN_ROAS'. | Bid strategy values are - 'LOWEST_COST_WITHOUT_CAP', 'LOWEST_COST_WITH_BID_CAP', 'COST_CAP', 'LOWEST_COST_WITH_MIN_ROAS'. | `[]` | `{}` |
    | `DAILY_BUDGET` | 10 | `NUMBER` | Daily budget of ad set. | Daily budget of ad set. | `[]` | `{}` |
    | `BUDGET_REMAINING` | 11 | `NUMBER` | Remaining budget of ad set. | Remaining budget of ad set. | `[]` | `{}` |
    | `STATUS` | 12 | `TEXT` | Status values are - 'ACTIVE', 'PAUSED', 'DELETED', 'ARCHIVED'. | Status values are - 'ACTIVE', 'PAUSED', 'DELETED', 'ARCHIVED'. | `[]` | `{}` |
    | `OPTIMIZATION_GOAL` | 13 | `TEXT` | The optimization goal this ad set is using. Possible values defined [here](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign/#fields). | The optimization goal this ad set is using. Possible values defined [here](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign/#fields). | `[]` | `{}` |
    | `IS_MOST_RECENT_RECORD` | 14 | `BOOLEAN` | Boolean representing whether a record is the most recent version of that record. All records should have this value set to True given we filter on it. | Boolean representing whether a record is the most recent version of that record. All records should have this value set to True given we filter on it. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt.type_bigint`
    *   `macro.facebook_ads.get_ad_set_history_columns`
    *   `macro.fivetran_utils.fill_staging_columns`
    *   `macro.fivetran_utils.source_relation`
    *   `model.facebook_ads.stg_facebook_ads__ad_set_history_tmp`

---
