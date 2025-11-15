## Model: `stg_google_ads__ad_history_tmp`

`stg_google_ads__ad_history_tmp`

*   **Unique ID:** `model.google_ads.stg_google_ads__ad_history_tmp`
*   **FQN:** `prod.ads_marts.stg_google_ads__ad_history_tmp`
*   **Description:** (No description provided)
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'google_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `AD_GROUP_ID` | 1 | `NUMBER` |  |  | `[]` | `{}` |
    | `ID` | 2 | `NUMBER` |  |  | `[]` | `{}` |
    | `UPDATED_AT` | 3 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `ACTION_ITEMS` | 4 | `TEXT` |  |  | `[]` | `{}` |
    | `AD_STRENGTH` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `ADDED_BY_GOOGLE_ADS` | 6 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `DEVICE_PREFERENCE` | 7 | `TEXT` |  |  | `[]` | `{}` |
    | `DISPLAY_URL` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `FINAL_URL_SUFFIX` | 9 | `TEXT` |  |  | `[]` | `{}` |
    | `FINAL_APP_URLS` | 10 | `TEXT` |  |  | `[]` | `{}` |
    | `FINAL_MOBILE_URLS` | 11 | `TEXT` |  |  | `[]` | `{}` |
    | `FINAL_URLS` | 12 | `TEXT` |  |  | `[]` | `{}` |
    | `NAME` | 13 | `TEXT` |  |  | `[]` | `{}` |
    | `POLICY_SUMMARY_APPROVAL_STATUS` | 14 | `TEXT` |  |  | `[]` | `{}` |
    | `POLICY_SUMMARY_REVIEW_STATUS` | 15 | `TEXT` |  |  | `[]` | `{}` |
    | `STATUS` | 16 | `TEXT` |  |  | `[]` | `{}` |
    | `SYSTEM_MANAGED_RESOURCE_SOURCE` | 17 | `TEXT` |  |  | `[]` | `{}` |
    | `TRACKING_URL_TEMPLATE` | 18 | `TEXT` |  |  | `[]` | `{}` |
    | `TYPE` | 19 | `TEXT` |  |  | `[]` | `{}` |
    | `URL_COLLECTIONS` | 20 | `TEXT` |  |  | `[]` | `{}` |
    | `_FIVETRAN_SYNCED` | 21 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `_FIVETRAN_START` | 22 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `_FIVETRAN_END` | 23 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `_FIVETRAN_ACTIVE` | 24 | `BOOLEAN` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.fivetran_utils.union_data`
    *   `source.google_ads.google_ads.ad_history`

---
