## Model: `stg_facebook_ads__campaign_history_tmp`

`stg_facebook_ads__campaign_history_tmp`

*   **Unique ID:** `model.facebook_ads.stg_facebook_ads__campaign_history_tmp`
*   **FQN:** `prod.ads_marts.stg_facebook_ads__campaign_history_tmp`
*   **Description:** (No description provided)
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'facebook_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `ID` | 1 | `NUMBER` |  |  | `[]` | `{}` |
    | `UPDATED_TIME` | 2 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `ACCOUNT_ID` | 3 | `NUMBER` |  |  | `[]` | `{}` |
    | `SOURCE_CAMPAIGN_ID` | 4 | `NUMBER` |  |  | `[]` | `{}` |
    | `AD_STRATEGY_ID` | 5 | `NUMBER` |  |  | `[]` | `{}` |
    | `BOOSTED_OBJECT_ID` | 6 | `NUMBER` |  |  | `[]` | `{}` |
    | `BUDGET_REBALANCE_FLAG` | 7 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `BUDGET_REMAINING` | 8 | `FLOAT` |  |  | `[]` | `{}` |
    | `BUYING_TYPE` | 9 | `TEXT` |  |  | `[]` | `{}` |
    | `CAN_CREATE_BRAND_LIFT_STUDY` | 10 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `CAN_USE_SPEND_CAP` | 11 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `CONFIGURED_STATUS` | 12 | `TEXT` |  |  | `[]` | `{}` |
    | `CREATED_TIME` | 13 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `DAILY_BUDGET` | 14 | `NUMBER` |  |  | `[]` | `{}` |
    | `EFFECTIVE_STATUS` | 15 | `TEXT` |  |  | `[]` | `{}` |
    | `IS_SKADNETWORK_ATTRIBUTION` | 16 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `LAST_BUDGET_TOGGLING_TIME` | 17 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `LIFETIME_BUDGET` | 18 | `NUMBER` |  |  | `[]` | `{}` |
    | `NAME` | 19 | `TEXT` |  |  | `[]` | `{}` |
    | `OBJECTIVE` | 20 | `TEXT` |  |  | `[]` | `{}` |
    | `SMART_PROMOTION_TYPE` | 21 | `TEXT` |  |  | `[]` | `{}` |
    | `SPECIAL_AD_CATEGORY` | 22 | `TEXT` |  |  | `[]` | `{}` |
    | `SPEND_CAP` | 23 | `NUMBER` |  |  | `[]` | `{}` |
    | `START_TIME` | 24 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `STATUS` | 25 | `TEXT` |  |  | `[]` | `{}` |
    | `STOP_TIME` | 26 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `TOPLINE_ID` | 27 | `NUMBER` |  |  | `[]` | `{}` |
    | `PACING_TYPE` | 28 | `VARIANT` |  |  | `[]` | `{}` |
    | `SPECIAL_AD_CATEGORIES` | 29 | `VARIANT` |  |  | `[]` | `{}` |
    | `SPECIAL_AD_CATEGORY_COUNTRY` | 30 | `VARIANT` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_APPLICATION_ID` | 31 | `NUMBER` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_CUSTOM_CONVERSION_ID` | 32 | `NUMBER` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_CUSTOM_EVENT_STR` | 33 | `TEXT` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_CUSTOM_EVENT_TYPE` | 34 | `TEXT` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_EVENT_ID` | 35 | `NUMBER` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_OBJECT_STORE_URL` | 36 | `TEXT` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_OFFER_ID` | 37 | `NUMBER` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_OFFLINE_CONVERSION_DATA_SET_ID` | 38 | `NUMBER` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_PAGE_ID` | 39 | `NUMBER` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_PIXEL_AGGREGATION_RULE` | 40 | `TEXT` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_PIXEL_ID` | 41 | `NUMBER` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_PIXEL_RULE` | 42 | `TEXT` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_PLACE_PAGE_SET_ID` | 43 | `NUMBER` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_PRODUCT_CATALOG_ID` | 44 | `NUMBER` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_PRODUCT_SET_ID` | 45 | `NUMBER` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_RETENTION_DAYS` | 46 | `TEXT` |  |  | `[]` | `{}` |
    | `_FIVETRAN_SYNCED` | 47 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `BID_STRATEGY` | 48 | `TEXT` |  |  | `[]` | `{}` |
    | `AD_STRATEGY_GROUP_ID` | 49 | `NUMBER` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.fivetran_utils.union_data`
    *   `source.facebook_ads.facebook_ads.campaign_history`

---
