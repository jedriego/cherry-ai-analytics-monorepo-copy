## Model: `stg_facebook_ads__ad_set_history_tmp`

`stg_facebook_ads__ad_set_history_tmp`

*   **Unique ID:** `model.facebook_ads.stg_facebook_ads__ad_set_history_tmp`
*   **FQN:** `prod.ads_marts.stg_facebook_ads__ad_set_history_tmp`
*   **Description:** (No description provided)
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'facebook_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `ID` | 1 | `NUMBER` |  |  | `[]` | `{}` |
    | `UPDATED_TIME` | 2 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `CAMPAIGN_ID` | 3 | `NUMBER` |  |  | `[]` | `{}` |
    | `ACCOUNT_ID` | 4 | `NUMBER` |  |  | `[]` | `{}` |
    | `ASSET_FEED_ID` | 5 | `NUMBER` |  |  | `[]` | `{}` |
    | `BID_AMOUNT` | 6 | `NUMBER` |  |  | `[]` | `{}` |
    | `BID_STRATEGY` | 7 | `TEXT` |  |  | `[]` | `{}` |
    | `BILLING_EVENT` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `BUDGET_REMAINING` | 9 | `NUMBER` |  |  | `[]` | `{}` |
    | `CONFIGURED_STATUS` | 10 | `TEXT` |  |  | `[]` | `{}` |
    | `CREATED_TIME` | 11 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `DAILY_BUDGET` | 12 | `NUMBER` |  |  | `[]` | `{}` |
    | `DAILY_MIN_SPEND_TARGET` | 13 | `NUMBER` |  |  | `[]` | `{}` |
    | `DAILY_SPEND_CAP` | 14 | `NUMBER` |  |  | `[]` | `{}` |
    | `DESTINATION_TYPE` | 15 | `TEXT` |  |  | `[]` | `{}` |
    | `EFFECTIVE_STATUS` | 16 | `TEXT` |  |  | `[]` | `{}` |
    | `END_TIME` | 17 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `INSTAGRAM_ACTOR_ID` | 18 | `NUMBER` |  |  | `[]` | `{}` |
    | `IS_DYNAMIC_CREATIVE` | 19 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `LIFETIME_BUDGET` | 20 | `NUMBER` |  |  | `[]` | `{}` |
    | `LIFETIME_IMPS` | 21 | `NUMBER` |  |  | `[]` | `{}` |
    | `LIFETIME_MIN_SPEND_TARGET` | 22 | `NUMBER` |  |  | `[]` | `{}` |
    | `LIFETIME_SPEND_CAP` | 23 | `NUMBER` |  |  | `[]` | `{}` |
    | `MULTI_OPTIMIZATION_GOAL_WEIGHT` | 24 | `TEXT` |  |  | `[]` | `{}` |
    | `NAME` | 25 | `TEXT` |  |  | `[]` | `{}` |
    | `OPTIMIZATION_GOAL` | 26 | `TEXT` |  |  | `[]` | `{}` |
    | `OPTIMIZATION_SUB_EVENT` | 27 | `TEXT` |  |  | `[]` | `{}` |
    | `RECURRING_BUDGET_SEMANTICS` | 28 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `REVIEW_FEEDBACK` | 29 | `TEXT` |  |  | `[]` | `{}` |
    | `RF_PREDICTION_ID` | 30 | `TEXT` |  |  | `[]` | `{}` |
    | `STATUS` | 31 | `TEXT` |  |  | `[]` | `{}` |
    | `START_TIME` | 32 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `USE_NEW_APP_CLICK` | 33 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_APPLICATION_ID` | 34 | `TEXT` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_CUSTOM_EVENT_TYPE` | 35 | `TEXT` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_EVENT_ID` | 36 | `NUMBER` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_OBJECT_STORE_URL` | 37 | `TEXT` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_OFFER_ID` | 38 | `NUMBER` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_PAGE_ID` | 39 | `NUMBER` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_PIXEL_ID` | 40 | `NUMBER` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_PLACE_PAGE_SET_ID` | 41 | `NUMBER` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_PRODUCT_CATALOG_ID` | 42 | `NUMBER` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_PRODUCT_SET_ID` | 43 | `NUMBER` |  |  | `[]` | `{}` |
    | `LEARNING_STAGE_INFO_ATTRIBUTION_WINDOWS` | 44 | `VARIANT` |  |  | `[]` | `{}` |
    | `LEARNING_STAGE_INFO_CONVERSIONS` | 45 | `NUMBER` |  |  | `[]` | `{}` |
    | `LEARNING_STAGE_INFO_LAST_SIG_EDIT_TS` | 46 | `NUMBER` |  |  | `[]` | `{}` |
    | `LEARNING_STAGE_INFO_STATUS` | 47 | `TEXT` |  |  | `[]` | `{}` |
    | `TARGETING_APP_INSTALL_STATE` | 48 | `TEXT` |  |  | `[]` | `{}` |
    | `TARGETING_AGE_MAX` | 49 | `NUMBER` |  |  | `[]` | `{}` |
    | `TARGETING_AGE_MIN` | 50 | `NUMBER` |  |  | `[]` | `{}` |
    | `TARGETING_AUDIENCE_NETWORK_POSITIONS` | 51 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_CONNECTIONS` | 52 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_DEVICE_PLATFORMS` | 53 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_EFFECTIVE_AUDIENCE_NETWORK_POSITIONS` | 54 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_EXCLUDED_CONNECTIONS` | 55 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_EXCLUDED_PUBLISHER_CATEGORIES` | 56 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_EXCLUDED_PUBLISHER_LIST_IDS` | 57 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_EXCLUDED_USER_DEVICE` | 58 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_FACEBOOK_POSITIONS` | 59 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_FRIENDS_OF_CONNECTIONS` | 60 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_INSTAGRAM_POSITIONS` | 61 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_PUBLISHER_PLATFORMS` | 62 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_USER_OS` | 63 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_USER_DEVICE` | 64 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_WIRELESS_CARRIER` | 65 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_EDUCATION_SCHOOLS` | 66 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_EDUCATION_STATUSES` | 67 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_COLLEGE_YEARS` | 68 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_EDUCATION_MAJORS` | 69 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_WORK_EMPLOYERS` | 70 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_WORK_POSITIONS` | 71 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_LOCALES` | 72 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_USER_ADCLUSTERS` | 73 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_FLEXIBLE_SPEC` | 74 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_EXCLUSIONS` | 75 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_GEO_LOCATIONS_COUNTRIES` | 76 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_GEO_LOCATIONS_LOCATION_TYPES` | 77 | `VARIANT` |  |  | `[]` | `{}` |
    | `ADSET_SOURCE_ID` | 78 | `NUMBER` |  |  | `[]` | `{}` |
    | `_FIVETRAN_SYNCED` | 79 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_PIXEL_RULE` | 80 | `TEXT` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_PIXEL_AGGREGATION_RULE` | 81 | `TEXT` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_CUSTOM_CONVERSION_ID` | 82 | `NUMBER` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_OFFLINE_CONVERSION_DATA_SET_ID` | 83 | `NUMBER` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_RETENTION_DAYS` | 84 | `TEXT` |  |  | `[]` | `{}` |
    | `PROMOTED_OBJECT_CUSTOM_EVENT_STR` | 85 | `TEXT` |  |  | `[]` | `{}` |
    | `TARGETING_EXCLUDED_GEO_LOCATIONS_REGIONS` | 86 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_LIFE_EVENTS` | 87 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_EXCLUDED_GEO_LOCATIONS_ELECTORAL_DISTRICT` | 88 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_EXCLUDED_GEO_LOCATIONS_LOCATION_TYPES` | 89 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_GENDERS` | 90 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_EXCLUDED_GEO_LOCATIONS_CUSTOM_LOCATIONS` | 91 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_GEO_LOCATIONS_ELECTORAL_DISTRICT` | 92 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_RELATIONSHIP_STATUSES` | 93 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_EXCLUDED_GEO_LOCATIONS_COUNTRIES` | 94 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_GEO_LOCATIONS_GEO_MARKETS` | 95 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_INTERESTS` | 96 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_INDUSTRIES` | 97 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_EXCLUDED_GEO_LOCATIONS_GEO_MARKETS` | 98 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_INCOME` | 99 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_GEO_LOCATIONS_CUSTOM_LOCATIONS` | 100 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_GEO_LOCATIONS_CITIES` | 101 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_EXCLUDED_GEO_LOCATIONS_PLACES` | 102 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_GEO_LOCATIONS_COUNTRY_GROUPS` | 103 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_EXCLUDED_GEO_LOCATIONS_CITIES` | 104 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_FAMILY_STATUSES` | 105 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_EXCLUDED_GEO_LOCATIONS_COUNTRY_GROUPS` | 106 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_BEHAVIORS` | 107 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_EXCLUDED_GEO_LOCATIONS_ZIPS` | 108 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_GEO_LOCATIONS_REGIONS` | 109 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_GEO_LOCATIONS_ZIPS` | 110 | `VARIANT` |  |  | `[]` | `{}` |
    | `TARGETING_GEO_LOCATIONS_PLACES` | 111 | `VARIANT` |  |  | `[]` | `{}` |
    | `BID_INFO_ACTIONS` | 112 | `NUMBER` |  |  | `[]` | `{}` |
    | `INSTAGRAM_USER_ID` | 113 | `NUMBER` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.fivetran_utils.union_data`
    *   `source.facebook_ads.facebook_ads.ad_set_history`

---
