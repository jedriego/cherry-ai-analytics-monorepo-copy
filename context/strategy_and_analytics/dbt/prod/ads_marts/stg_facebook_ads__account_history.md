## Model: `stg_facebook_ads__account_history`

`stg_facebook_ads__account_history`

*   **Unique ID:** `model.facebook_ads.stg_facebook_ads__account_history`
*   **FQN:** `prod.ads_marts.stg_facebook_ads__account_history`
*   **Description:** Each record in this table reflects a Facebook ad account.
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'facebook_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `SOURCE_RELATION` | 1 | `TEXT` | The source of the record if the unioning functionality is being used. If not this field will be empty. | The source of the record if the unioning functionality is being used. If not this field will be empty. | `[]` | `{}` |
    | `ACCOUNT_ID` | 2 | `NUMBER` | The ID of the ad account. | The ID of the ad account. | `[]` | `{}` |
    | `_FIVETRAN_SYNCED` | 3 | `TIMESTAMP_TZ` | When the record was last synced by Fivetran. | When the record was last synced by Fivetran. | `[]` | `{}` |
    | `ACCOUNT_NAME` | 4 | `TEXT` | Name of the account. | Name of the account. | `[]` | `{}` |
    | `ACCOUNT_STATUS` | 5 | `TEXT` | Current status of account. | Current status of account. | `[]` | `{}` |
    | `BUSINESS_COUNTRY_CODE` | 6 | `TEXT` | Country code of business associated to account. | Country code of business associated to account. | `[]` | `{}` |
    | `BUSINESS_STATE` | 7 | `TEXT` | State abbreviation for business address. | State abbreviation for business address. | `[]` | `{}` |
    | `CREATED_AT` | 8 | `TIMESTAMP_TZ` | The time account was created. | The time account was created. | `[]` | `{}` |
    | `CURRENCY` | 9 | `TEXT` | Currency associated with account. | Currency associated with account. | `[]` | `{}` |
    | `TIMEZONE_NAME` | 10 | `TEXT` | Timezone associated with account. | Timezone associated with account. | `[]` | `{}` |
    | `TIMEZONE_OFFSET_HOURS_UTC` | 11 | `FLOAT` | Time zone difference from UTC. | Time zone difference from UTC. | `[]` | `{}` |
    | `MIN_DAILY_BUDGET` | 12 | `NUMBER` | The minimum daily budget for this Ad Account. | The minimum daily budget for this Ad Account. | `[]` | `{}` |
    | `IS_MOST_RECENT_RECORD` | 13 | `BOOLEAN` | Boolean representing whether a record is the most recent version of that record. All records should have this value set to True given we filter on it. | Boolean representing whether a record is the most recent version of that record. All records should have this value set to True given we filter on it. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt.type_bigint`
    *   `macro.facebook_ads.get_account_history_columns`
    *   `macro.fivetran_utils.fill_staging_columns`
    *   `macro.fivetran_utils.source_relation`
    *   `model.facebook_ads.stg_facebook_ads__account_history_tmp`

---
