## Model: `stg_facebook_ads__campaign_history`

`stg_facebook_ads__campaign_history`

*   **Unique ID:** `model.facebook_ads.stg_facebook_ads__campaign_history`
*   **FQN:** `prod.ads_marts.stg_facebook_ads__campaign_history`
*   **Description:** Each record in this table reflects a Facebook campaign.
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'facebook_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `SOURCE_RELATION` | 1 | `TEXT` | The source of the record if the unioning functionality is being used. If not this field will be empty. | The source of the record if the unioning functionality is being used. If not this field will be empty. | `[]` | `{}` |
    | `UPDATED_AT` | 2 | `TIMESTAMP_TZ` | The timestamp of the last update of a record. | The timestamp of the last update of a record. | `[]` | `{}` |
    | `CREATED_AT` | 3 | `TIMESTAMP_TZ` | The time the campaign was created. | The time the campaign was created. | `[]` | `{}` |
    | `ACCOUNT_ID` | 4 | `NUMBER` | The ID of the ad account that this campaign belongs to. | The ID of the ad account that this campaign belongs to. | `[]` | `{}` |
    | `CAMPAIGN_ID` | 5 | `NUMBER` | The ID of the campaign. | The ID of the campaign. | `[]` | `{}` |
    | `CAMPAIGN_NAME` | 6 | `TEXT` | The name of the campaign. | The name of the campaign. | `[]` | `{}` |
    | `START_AT` | 7 | `TIMESTAMP_TZ` | Timestamp of designated campaign start time. | Timestamp of designated campaign start time. | `[]` | `{}` |
    | `END_AT` | 8 | `TIMESTAMP_TZ` | Timestamp of designated campaign end time. | Timestamp of designated campaign end time. | `[]` | `{}` |
    | `STATUS` | 9 | `TEXT` | Status values are - 'ACTIVE', 'PAUSED', 'DELETED', 'ARCHIVED'. | Status values are - 'ACTIVE', 'PAUSED', 'DELETED', 'ARCHIVED'. | `[]` | `{}` |
    | `DAILY_BUDGET` | 10 | `NUMBER` | Daily budget of campaign. | Daily budget of campaign. | `[]` | `{}` |
    | `LIFETIME_BUDGET` | 11 | `NUMBER` | Lifetime budget of the campaign. | Lifetime budget of the campaign. | `[]` | `{}` |
    | `BUDGET_REMAINING` | 12 | `FLOAT` | Remaining budget of campaign. | Remaining budget of campaign. | `[]` | `{}` |
    | `IS_MOST_RECENT_RECORD` | 13 | `BOOLEAN` | Boolean representing whether a record is the most recent version of that record. All records should have this value set to True given we filter on it. | Boolean representing whether a record is the most recent version of that record. All records should have this value set to True given we filter on it. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt.type_bigint`
    *   `macro.facebook_ads.get_campaign_history_columns`
    *   `macro.fivetran_utils.fill_staging_columns`
    *   `macro.fivetran_utils.source_relation`
    *   `model.facebook_ads.stg_facebook_ads__campaign_history_tmp`

---
