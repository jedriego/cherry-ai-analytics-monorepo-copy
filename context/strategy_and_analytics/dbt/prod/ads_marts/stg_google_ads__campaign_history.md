## Model: `stg_google_ads__campaign_history`

`stg_google_ads__campaign_history`

*   **Unique ID:** `model.google_ads.stg_google_ads__campaign_history`
*   **FQN:** `prod.ads_marts.stg_google_ads__campaign_history`
*   **Description:** Each record represents a version of a campaign in Google Ads.
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'google_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `SOURCE_RELATION` | 1 | `TEXT` | The source of the record if the unioning functionality is being used. If not this field will be empty. | The source of the record if the unioning functionality is being used. If not this field will be empty. | `[]` | `{}` |
    | `CAMPAIGN_ID` | 2 | `NUMBER` | The ID of the Campaign. | The ID of the Campaign. | `[]` | `{}` |
    | `UPDATED_AT` | 3 | `TIMESTAMP_TZ` | Timestamp of when the record was last updated in Google Ads. | Timestamp of when the record was last updated in Google Ads. | `[]` | `{}` |
    | `CAMPAIGN_NAME` | 4 | `TEXT` | The name of the Campaign. | The name of the Campaign. | `[]` | `{}` |
    | `ACCOUNT_ID` | 5 | `NUMBER` | The Customer ID. | The Customer ID. | `[]` | `{}` |
    | `ADVERTISING_CHANNEL_TYPE` | 6 | `TEXT` | The type of advertising channel being used by the campaign. | The type of advertising channel being used by the campaign. | `[]` | `{}` |
    | `ADVERTISING_CHANNEL_SUBTYPE` | 7 | `TEXT` | The advertising channel subtype that is being used by the campaign. | The advertising channel subtype that is being used by the campaign. | `[]` | `{}` |
    | `START_DATE` | 8 | `TEXT` | The start date of the campaign. | The start date of the campaign. | `[]` | `{}` |
    | `END_DATE` | 9 | `TEXT` | The end date of the campaign. | The end date of the campaign. | `[]` | `{}` |
    | `SERVING_STATUS` | 10 | `TEXT` | Status of the ads and how they are currently being served. | Status of the ads and how they are currently being served. | `[]` | `{}` |
    | `STATUS` | 11 | `TEXT` | General status of the campaign. | General status of the campaign. | `[]` | `{}` |
    | `TRACKING_URL_TEMPLATE` | 12 | `TEXT` | The tracking url template being used throughout the campaign ads. | The tracking url template being used throughout the campaign ads. | `[]` | `{}` |
    | `IS_MOST_RECENT_RECORD` | 13 | `BOOLEAN` | Boolean representing whether the record is the most recent version of the object. | Boolean representing whether the record is the most recent version of the object. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.fivetran_utils.fill_staging_columns`
    *   `macro.fivetran_utils.source_relation`
    *   `macro.google_ads.get_campaign_history_columns`
    *   `model.google_ads.stg_google_ads__campaign_history_tmp`

---
