## Model: `stg_google_ads__campaign_history_tmp`

`stg_google_ads__campaign_history_tmp`

*   **Unique ID:** `model.google_ads.stg_google_ads__campaign_history_tmp`
*   **FQN:** `prod.ads_marts.stg_google_ads__campaign_history_tmp`
*   **Description:** (No description provided)
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'google_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `ID` | 1 | `NUMBER` |  |  | `[]` | `{}` |
    | `UPDATED_AT` | 2 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `CUSTOMER_ID` | 3 | `NUMBER` |  |  | `[]` | `{}` |
    | `BASE_CAMPAIGN_ID` | 4 | `NUMBER` |  |  | `[]` | `{}` |
    | `AD_SERVING_OPTIMIZATION_STATUS` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `ADVERTISING_CHANNEL_SUBTYPE` | 6 | `TEXT` |  |  | `[]` | `{}` |
    | `ADVERTISING_CHANNEL_TYPE` | 7 | `TEXT` |  |  | `[]` | `{}` |
    | `EXPERIMENT_TYPE` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `END_DATE` | 9 | `TEXT` |  |  | `[]` | `{}` |
    | `FINAL_URL_SUFFIX` | 10 | `TEXT` |  |  | `[]` | `{}` |
    | `FREQUENCY_CAPS` | 11 | `TEXT` |  |  | `[]` | `{}` |
    | `NAME` | 12 | `TEXT` |  |  | `[]` | `{}` |
    | `OPTIMIZATION_SCORE` | 13 | `FLOAT` |  |  | `[]` | `{}` |
    | `PAYMENT_MODE` | 14 | `TEXT` |  |  | `[]` | `{}` |
    | `SERVING_STATUS` | 15 | `TEXT` |  |  | `[]` | `{}` |
    | `START_DATE` | 16 | `TEXT` |  |  | `[]` | `{}` |
    | `STATUS` | 17 | `TEXT` |  |  | `[]` | `{}` |
    | `TRACKING_URL_TEMPLATE` | 18 | `TEXT` |  |  | `[]` | `{}` |
    | `VANITY_PHARMA_DISPLAY_URL_MODE` | 19 | `TEXT` |  |  | `[]` | `{}` |
    | `VANITY_PHARMA_TEXT` | 20 | `TEXT` |  |  | `[]` | `{}` |
    | `VIDEO_BRAND_SAFETY_SUITABILITY` | 21 | `TEXT` |  |  | `[]` | `{}` |
    | `_FIVETRAN_SYNCED` | 22 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `_FIVETRAN_START` | 23 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `_FIVETRAN_END` | 24 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `_FIVETRAN_ACTIVE` | 25 | `BOOLEAN` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.fivetran_utils.union_data`
    *   `source.google_ads.google_ads.campaign_history`

---
