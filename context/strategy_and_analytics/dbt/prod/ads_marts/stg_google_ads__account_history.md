## Model: `stg_google_ads__account_history`

`stg_google_ads__account_history`

*   **Unique ID:** `model.google_ads.stg_google_ads__account_history`
*   **FQN:** `prod.ads_marts.stg_google_ads__account_history`
*   **Description:** Each record represents a version of an account in Google Ads.
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'google_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `SOURCE_RELATION` | 1 | `TEXT` | The source of the record if the unioning functionality is being used. If not this field will be empty. | The source of the record if the unioning functionality is being used. If not this field will be empty. | `[]` | `{}` |
    | `ACCOUNT_ID` | 2 | `NUMBER` | The ID of the Account. | The ID of the Account. | `[]` | `{}` |
    | `UPDATED_AT` | 3 | `TIMESTAMP_TZ` | Timestamp of when a record was last synced. | Timestamp of when a record was last synced. | `[]` | `{}` |
    | `CURRENCY_CODE` | 4 | `TEXT` | The currency of the spend reported. | The currency of the spend reported. | `[]` | `{}` |
    | `AUTO_TAGGING_ENABLED` | 5 | `BOOLEAN` | Boolean indicating if auto tagging is enabled on the account ads. | Boolean indicating if auto tagging is enabled on the account ads. | `[]` | `{}` |
    | `TIME_ZONE` | 6 | `TEXT` | The time zone of the account ads. | The time zone of the account ads. | `[]` | `{}` |
    | `ACCOUNT_NAME` | 7 | `TEXT` | The descriptive name of the Customer account. | The descriptive name of the Customer account. | `[]` | `{}` |
    | `IS_MOST_RECENT_RECORD` | 8 | `BOOLEAN` | Boolean representing whether the record is the most recent version of the object. | Boolean representing whether the record is the most recent version of the object. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.fivetran_utils.fill_staging_columns`
    *   `macro.fivetran_utils.source_relation`
    *   `macro.google_ads.get_account_history_columns`
    *   `model.google_ads.stg_google_ads__account_history_tmp`

---
