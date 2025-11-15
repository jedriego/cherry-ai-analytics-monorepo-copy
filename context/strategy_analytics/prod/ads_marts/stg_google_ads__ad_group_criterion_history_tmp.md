## Model: `stg_google_ads__ad_group_criterion_history_tmp`

`stg_google_ads__ad_group_criterion_history_tmp`

*   **Unique ID:** `model.google_ads.stg_google_ads__ad_group_criterion_history_tmp`
*   **FQN:** `prod.ads_marts.stg_google_ads__ad_group_criterion_history_tmp`
*   **Description:** (No description provided)
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'google_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `AD_GROUP_ID` | 1 | `NUMBER` |  |  | `[]` | `{}` |
    | `ID` | 2 | `NUMBER` |  |  | `[]` | `{}` |
    | `UPDATED_AT` | 3 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `USER_INTEREST_ID` | 4 | `NUMBER` |  |  | `[]` | `{}` |
    | `USER_LIST_ID` | 5 | `NUMBER` |  |  | `[]` | `{}` |
    | `AGE_RANGE_TYPE` | 6 | `TEXT` |  |  | `[]` | `{}` |
    | `APP_PAYMENT_MODEL_TYPE` | 7 | `TEXT` |  |  | `[]` | `{}` |
    | `APPROVAL_STATUS` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `BID_MODIFIER` | 9 | `FLOAT` |  |  | `[]` | `{}` |
    | `CUSTOM_AFFINITY_ID` | 10 | `NUMBER` |  |  | `[]` | `{}` |
    | `CUSTOM_AUDIENCE_ID` | 11 | `NUMBER` |  |  | `[]` | `{}` |
    | `CUSTOM_INTENT_ID` | 12 | `NUMBER` |  |  | `[]` | `{}` |
    | `DISAPPROVAL_REASONS` | 13 | `TEXT` |  |  | `[]` | `{}` |
    | `DISPLAY_NAME` | 14 | `TEXT` |  |  | `[]` | `{}` |
    | `FINAL_MOBILE_URLS` | 15 | `TEXT` |  |  | `[]` | `{}` |
    | `FINAL_URLS` | 16 | `TEXT` |  |  | `[]` | `{}` |
    | `FINAL_URL_SUFFIX` | 17 | `TEXT` |  |  | `[]` | `{}` |
    | `FIRST_PAGE_CPC_MICROS` | 18 | `NUMBER` |  |  | `[]` | `{}` |
    | `FIRST_POSITION_CPC_MICROS` | 19 | `NUMBER` |  |  | `[]` | `{}` |
    | `GENDER_TYPE` | 20 | `TEXT` |  |  | `[]` | `{}` |
    | `INCOME_RANGE_TYPE` | 21 | `TEXT` |  |  | `[]` | `{}` |
    | `KEYWORD_MATCH_TYPE` | 22 | `TEXT` |  |  | `[]` | `{}` |
    | `KEYWORD_TEXT` | 23 | `TEXT` |  |  | `[]` | `{}` |
    | `MOBILE_APP_CATEGORY_CONSTANT_ID` | 24 | `NUMBER` |  |  | `[]` | `{}` |
    | `MOBILE_APP_CATEGORY_CONSTANT_NAME` | 25 | `TEXT` |  |  | `[]` | `{}` |
    | `MOBILE_APPLICATION_APP_ID` | 26 | `TEXT` |  |  | `[]` | `{}` |
    | `MOBILE_APPLICATION_NAME` | 27 | `TEXT` |  |  | `[]` | `{}` |
    | `NEGATIVE` | 28 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `PARENT_AD_GROUP_CRITERION_ID` | 29 | `NUMBER` |  |  | `[]` | `{}` |
    | `PARENTAL_STATUS_TYPE` | 30 | `TEXT` |  |  | `[]` | `{}` |
    | `PLACEMENT_URL` | 31 | `TEXT` |  |  | `[]` | `{}` |
    | `QUALITY_INFO_SCORE` | 32 | `NUMBER` |  |  | `[]` | `{}` |
    | `QUALITY_INFO_CREATIVE_SCORE` | 33 | `TEXT` |  |  | `[]` | `{}` |
    | `QUALITY_INFO_POST_CLICK_SCORE` | 34 | `TEXT` |  |  | `[]` | `{}` |
    | `QUALITY_INFO_SEARCH_PREDICTED_CTR` | 35 | `TEXT` |  |  | `[]` | `{}` |
    | `STATUS` | 36 | `TEXT` |  |  | `[]` | `{}` |
    | `SYSTEM_SERVING_STATUS` | 37 | `TEXT` |  |  | `[]` | `{}` |
    | `TOP_OF_PAGE_CPC_MICROS` | 38 | `NUMBER` |  |  | `[]` | `{}` |
    | `TOPIC_CONSTANT_ID` | 39 | `NUMBER` |  |  | `[]` | `{}` |
    | `TRACKING_URL_TEMPLATE` | 40 | `TEXT` |  |  | `[]` | `{}` |
    | `TYPE` | 41 | `TEXT` |  |  | `[]` | `{}` |
    | `WEBPAGE_CONDITIONS` | 42 | `TEXT` |  |  | `[]` | `{}` |
    | `YOUTUBE_CHANNEL_ID` | 43 | `TEXT` |  |  | `[]` | `{}` |
    | `YOUTUBE_VIDEO_ID` | 44 | `TEXT` |  |  | `[]` | `{}` |
    | `_FIVETRAN_SYNCED` | 45 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `CPM_BID_MICROS` | 46 | `NUMBER` |  |  | `[]` | `{}` |
    | `CPV_BID_MICROS` | 47 | `NUMBER` |  |  | `[]` | `{}` |
    | `CPC_BID_MICROS` | 48 | `NUMBER` |  |  | `[]` | `{}` |
    | `_FIVETRAN_START` | 49 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `_FIVETRAN_END` | 50 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `_FIVETRAN_ACTIVE` | 51 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `COMBINED_AUDIENCE_ID` | 52 | `NUMBER` |  |  | `[]` | `{}` |
    | `AUDIENCE_ID` | 53 | `NUMBER` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.fivetran_utils.union_data`
    *   `source.google_ads.google_ads.ad_group_criterion_history`

---
