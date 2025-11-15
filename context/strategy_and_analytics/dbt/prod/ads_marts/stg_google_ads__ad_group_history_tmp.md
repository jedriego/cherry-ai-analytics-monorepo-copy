## Model: `stg_google_ads__ad_group_history_tmp`

`stg_google_ads__ad_group_history_tmp`

*   **Unique ID:** `model.google_ads.stg_google_ads__ad_group_history_tmp`
*   **FQN:** `prod.ads_marts.stg_google_ads__ad_group_history_tmp`
*   **Description:** (No description provided)
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'google_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `ID` | 1 | `NUMBER` |  |  | `[]` | `{}` |
    | `UPDATED_AT` | 2 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `CAMPAIGN_ID` | 3 | `NUMBER` |  |  | `[]` | `{}` |
    | `BASE_AD_GROUP_ID` | 4 | `NUMBER` |  |  | `[]` | `{}` |
    | `AD_ROTATION_MODE` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `CAMPAIGN_NAME` | 6 | `TEXT` |  |  | `[]` | `{}` |
    | `DISPLAY_CUSTOM_BID_DIMENSION` | 7 | `TEXT` |  |  | `[]` | `{}` |
    | `EXPLORER_AUTO_OPTIMIZER_SETTING_OPT_IN` | 8 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `FINAL_URL_SUFFIX` | 9 | `TEXT` |  |  | `[]` | `{}` |
    | `NAME` | 10 | `TEXT` |  |  | `[]` | `{}` |
    | `STATUS` | 11 | `TEXT` |  |  | `[]` | `{}` |
    | `TARGET_RESTRICTIONS` | 12 | `TEXT` |  |  | `[]` | `{}` |
    | `TRACKING_URL_TEMPLATE` | 13 | `TEXT` |  |  | `[]` | `{}` |
    | `TYPE` | 14 | `TEXT` |  |  | `[]` | `{}` |
    | `_FIVETRAN_SYNCED` | 15 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `_FIVETRAN_START` | 16 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `_FIVETRAN_END` | 17 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `_FIVETRAN_ACTIVE` | 18 | `BOOLEAN` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.fivetran_utils.union_data`
    *   `source.google_ads.google_ads.ad_group_history`

---
