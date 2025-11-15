## Model: `stg_facebook_ads__creative_history_tmp`

`stg_facebook_ads__creative_history_tmp`

*   **Unique ID:** `model.facebook_ads.stg_facebook_ads__creative_history_tmp`
*   **FQN:** `prod.ads_marts.stg_facebook_ads__creative_history_tmp`
*   **Description:** (No description provided)
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'facebook_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `_FIVETRAN_ID` | 1 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_ID` | 2 | `NUMBER` |  |  | `[]` | `{}` |
    | `ID` | 3 | `NUMBER` |  |  | `[]` | `{}` |
    | `ACTOR_ID` | 4 | `NUMBER` |  |  | `[]` | `{}` |
    | `APPLINK_TREATMENT` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `AUTHORIZATION_CATEGORY` | 6 | `TEXT` |  |  | `[]` | `{}` |
    | `BODY` | 7 | `TEXT` |  |  | `[]` | `{}` |
    | `BRANDED_CONTENT_SPONSOR_PAGE_ID` | 8 | `NUMBER` |  |  | `[]` | `{}` |
    | `BUNDLE_FOLDER_ID` | 9 | `NUMBER` |  |  | `[]` | `{}` |
    | `CALL_TO_ACTION_TYPE` | 10 | `TEXT` |  |  | `[]` | `{}` |
    | `CATEGORIZATION_CRITERIA` | 11 | `TEXT` |  |  | `[]` | `{}` |
    | `CATEGORY_MEDIA_SOURCE` | 12 | `TEXT` |  |  | `[]` | `{}` |
    | `DESTINATION_SET_ID` | 13 | `NUMBER` |  |  | `[]` | `{}` |
    | `DYNAMIC_AD_VOICE` | 14 | `TEXT` |  |  | `[]` | `{}` |
    | `EFFECTIVE_AUTHORIZATION_CATEGORY` | 15 | `TEXT` |  |  | `[]` | `{}` |
    | `EFFECTIVE_INSTAGRAM_MEDIA_ID` | 16 | `NUMBER` |  |  | `[]` | `{}` |
    | `EFFECTIVE_INSTAGRAM_STORY_ID` | 17 | `NUMBER` |  |  | `[]` | `{}` |
    | `EFFECTIVE_OBJECT_STORY_ID` | 18 | `TEXT` |  |  | `[]` | `{}` |
    | `ENABLE_DIRECT_INSTALL` | 19 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IMAGE_FILE` | 20 | `TEXT` |  |  | `[]` | `{}` |
    | `IMAGE_HASH` | 21 | `TEXT` |  |  | `[]` | `{}` |
    | `IMAGE_URL` | 22 | `TEXT` |  |  | `[]` | `{}` |
    | `INSTAGRAM_ACTOR_ID` | 23 | `NUMBER` |  |  | `[]` | `{}` |
    | `INSTAGRAM_PERMALINK_URL` | 24 | `TEXT` |  |  | `[]` | `{}` |
    | `INSTAGRAM_STORY_ID` | 25 | `NUMBER` |  |  | `[]` | `{}` |
    | `LINK_OG_ID` | 26 | `NUMBER` |  |  | `[]` | `{}` |
    | `LINK_URL` | 27 | `TEXT` |  |  | `[]` | `{}` |
    | `MESSENGER_SPONSORED_MESSAGE` | 28 | `TEXT` |  |  | `[]` | `{}` |
    | `NAME` | 29 | `TEXT` |  |  | `[]` | `{}` |
    | `OBJECT_ID` | 30 | `NUMBER` |  |  | `[]` | `{}` |
    | `OBJECT_STORE_URL` | 31 | `TEXT` |  |  | `[]` | `{}` |
    | `OBJECT_STORY_ID` | 32 | `TEXT` |  |  | `[]` | `{}` |
    | `OBJECT_TYPE` | 33 | `TEXT` |  |  | `[]` | `{}` |
    | `OBJECT_URL` | 34 | `TEXT` |  |  | `[]` | `{}` |
    | `PLACE_PAGE_SET_ID` | 35 | `NUMBER` |  |  | `[]` | `{}` |
    | `PLAYABLE_ASSET_ID` | 36 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRODUCT_SET_ID` | 37 | `NUMBER` |  |  | `[]` | `{}` |
    | `STATUS` | 38 | `TEXT` |  |  | `[]` | `{}` |
    | `TEMPLATE_URL` | 39 | `TEXT` |  |  | `[]` | `{}` |
    | `THUMBNAIL_URL` | 40 | `TEXT` |  |  | `[]` | `{}` |
    | `TITLE` | 41 | `TEXT` |  |  | `[]` | `{}` |
    | `USE_PAGE_ACTOR_OVERRIDE` | 42 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `VIDEO_ID` | 43 | `NUMBER` |  |  | `[]` | `{}` |
    | `CAROUSEL_AD_LINK` | 44 | `TEXT` |  |  | `[]` | `{}` |
    | `PAGE_LINK` | 45 | `TEXT` |  |  | `[]` | `{}` |
    | `TEMPLATE_PAGE_LINK` | 46 | `TEXT` |  |  | `[]` | `{}` |
    | `URL_TAGS` | 47 | `VARIANT` |  |  | `[]` | `{}` |
    | `OBJECT_STORY_LINK_DATA_CAPTION` | 48 | `TEXT` |  |  | `[]` | `{}` |
    | `OBJECT_STORY_LINK_DATA_MESSAGE` | 49 | `TEXT` |  |  | `[]` | `{}` |
    | `OBJECT_STORY_LINK_DATA_DESCRIPTION` | 50 | `TEXT` |  |  | `[]` | `{}` |
    | `OBJECT_STORY_LINK_DATA_LINK` | 51 | `TEXT` |  |  | `[]` | `{}` |
    | `OBJECT_STORY_LINK_DATA_CHILD_ATTACHMENTS` | 52 | `VARIANT` |  |  | `[]` | `{}` |
    | `OBJECT_STORY_LINK_DATA_APP_LINK_SPEC_ANDROID` | 53 | `VARIANT` |  |  | `[]` | `{}` |
    | `OBJECT_STORY_LINK_DATA_APP_LINK_SPEC_IOS` | 54 | `VARIANT` |  |  | `[]` | `{}` |
    | `OBJECT_STORY_LINK_DATA_APP_LINK_SPEC_IPAD` | 55 | `VARIANT` |  |  | `[]` | `{}` |
    | `OBJECT_STORY_LINK_DATA_APP_LINK_SPEC_IPHONE` | 56 | `VARIANT` |  |  | `[]` | `{}` |
    | `TEMPLATE_CAPTION` | 57 | `TEXT` |  |  | `[]` | `{}` |
    | `TEMPLATE_MESSAGE` | 58 | `TEXT` |  |  | `[]` | `{}` |
    | `TEMPLATE_DESCRIPTION` | 59 | `TEXT` |  |  | `[]` | `{}` |
    | `TEMPLATE_LINK` | 60 | `TEXT` |  |  | `[]` | `{}` |
    | `TEMPLATE_CHILD_ATTACHMENTS` | 61 | `VARIANT` |  |  | `[]` | `{}` |
    | `TEMPLATE_APP_LINK_SPEC_ANDROID` | 62 | `VARIANT` |  |  | `[]` | `{}` |
    | `TEMPLATE_APP_LINK_SPEC_IOS` | 63 | `VARIANT` |  |  | `[]` | `{}` |
    | `TEMPLATE_APP_LINK_SPEC_IPAD` | 64 | `VARIANT` |  |  | `[]` | `{}` |
    | `TEMPLATE_APP_LINK_SPEC_IPHONE` | 65 | `VARIANT` |  |  | `[]` | `{}` |
    | `PAGE_MESSAGE` | 66 | `TEXT` |  |  | `[]` | `{}` |
    | `VIDEO_CALL_TO_ACTION_VALUE_LINK` | 67 | `TEXT` |  |  | `[]` | `{}` |
    | `ASSET_FEED_SPEC_LINK_URLS` | 68 | `VARIANT` |  |  | `[]` | `{}` |
    | `_FIVETRAN_SYNCED` | 69 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `TEMPLATE_URL_SPEC_ANDROID_APP_NAME` | 70 | `TEXT` |  |  | `[]` | `{}` |
    | `PLATFORM_CUSTOMIZATIONS_INSTAGRAM_VIDEO_ID` | 71 | `NUMBER` |  |  | `[]` | `{}` |
    | `TEMPLATE_URL_SPEC_WINDOWS_PHONE_APP_NAME` | 72 | `TEXT` |  |  | `[]` | `{}` |
    | `TEMPLATE_URL_SPEC_CONFIG_APP_ID` | 73 | `TEXT` |  |  | `[]` | `{}` |
    | `TEMPLATE_URL_SPEC_IPHONE_APP_STORE_ID` | 74 | `TEXT` |  |  | `[]` | `{}` |
    | `TEMPLATE_URL_SPEC_WEB_URL` | 75 | `TEXT` |  |  | `[]` | `{}` |
    | `PLATFORM_CUSTOMIZATIONS_INSTAGRAM_IMAGE_URL` | 76 | `TEXT` |  |  | `[]` | `{}` |
    | `TEMPLATE_URL_SPEC_IPHONE_URL` | 77 | `TEXT` |  |  | `[]` | `{}` |
    | `TEMPLATE_URL_SPEC_IPAD_APP_STORE_ID` | 78 | `TEXT` |  |  | `[]` | `{}` |
    | `LINK_DESTINATION_DISPLAY_URL` | 79 | `TEXT` |  |  | `[]` | `{}` |
    | `TEMPLATE_URL_SPEC_IOS_URL` | 80 | `TEXT` |  |  | `[]` | `{}` |
    | `TEMPLATE_URL_SPEC_IPAD_URL` | 81 | `TEXT` |  |  | `[]` | `{}` |
    | `PLATFORM_CUSTOMIZATIONS_INSTAGRAM_IMAGE_HASH` | 82 | `TEXT` |  |  | `[]` | `{}` |
    | `TEMPLATE_URL_SPEC_IPHONE_APP_NAME` | 83 | `TEXT` |  |  | `[]` | `{}` |
    | `PLATFORM_CUSTOMIZATIONS_INSTAGRAM_CAPTION_IDS` | 84 | `VARIANT` |  |  | `[]` | `{}` |
    | `TEMPLATE_URL_SPEC_ANDROID_PACKAGE` | 85 | `TEXT` |  |  | `[]` | `{}` |
    | `TEMPLATE_URL_SPEC_IOS_APP_STORE_ID` | 86 | `TEXT` |  |  | `[]` | `{}` |
    | `TEMPLATE_URL_SPEC_WEB_SHOULD_FALLBACK` | 87 | `TEXT` |  |  | `[]` | `{}` |
    | `SOURCE_INSTAGRAM_MEDIA_ID` | 88 | `NUMBER` |  |  | `[]` | `{}` |
    | `TEMPLATE_URL_SPEC_WINDOWS_PHONE_URL` | 89 | `TEXT` |  |  | `[]` | `{}` |
    | `THUMBNAIL_ID` | 90 | `NUMBER` |  |  | `[]` | `{}` |
    | `TEMPLATE_URL_SPEC_IPAD_APP_NAME` | 91 | `TEXT` |  |  | `[]` | `{}` |
    | `TEMPLATE_URL_SPEC_WINDOWS_PHONE_APP_ID` | 92 | `TEXT` |  |  | `[]` | `{}` |
    | `TEMPLATE_URL_SPEC_IOS_APP_NAME` | 93 | `TEXT` |  |  | `[]` | `{}` |
    | `TEMPLATE_URL_SPEC_ANDROID_URL` | 94 | `TEXT` |  |  | `[]` | `{}` |
    | `VIDEO_VIDEO_ID` | 95 | `NUMBER` |  |  | `[]` | `{}` |
    | `ASSET_FEED_SPEC_ADDITIONAL_DATA_MULTI_SHARE_END_CARD` | 96 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ASSET_FEED_SPEC_ADDITIONAL_DATA_IS_CLICK_TO_MESSAGE` | 97 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ASSET_FEED_SPEC_ADDITIONAL_DATA_BRAND_PAGE_ID` | 98 | `TEXT` |  |  | `[]` | `{}` |
    | `ASSET_FEED_SPEC_APP_PRODUCT_PAGE_ID` | 99 | `TEXT` |  |  | `[]` | `{}` |
    | `ASSET_FEED_SPEC_SHOPS_BUNDLE` | 100 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ASSET_FEED_SPEC_ADDITIONAL_DATA_PARTNER_APP_WELCOME_MESSAGE_FLOW_ID` | 101 | `TEXT` |  |  | `[]` | `{}` |
    | `ASSET_FEED_SPEC_PROMOTIONAL_METADATA_ALLOWED_COUPON_CODE_SOURCES` | 102 | `VARIANT` |  |  | `[]` | `{}` |
    | `ASSET_FEED_SPEC_CALL_ADS_CONFIGURATION` | 103 | `VARIANT` |  |  | `[]` | `{}` |
    | `ASSET_FEED_SPEC_REASONS_TO_SHOP` | 104 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ASSET_FEED_SPEC_OPTIMIZATION_TYPE` | 105 | `TEXT` |  |  | `[]` | `{}` |
    | `ASSET_FEED_SPEC_ADDITIONAL_DATA_PAGE_WELCOME_MESSAGE` | 106 | `TEXT` |  |  | `[]` | `{}` |
    | `ASSET_FEED_SPEC_ADDITIONAL_DATA_AUTOMATED_PRODUCT_TAGS` | 107 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ASSET_FEED_SPEC_PROMOTIONAL_METADATA_MANUAL_COUPON_CODES` | 108 | `VARIANT` |  |  | `[]` | `{}` |
    | `ASSET_FEED_SPEC_PROMOTIONAL_METADATA_COUPON_CODES` | 109 | `VARIANT` |  |  | `[]` | `{}` |
    | `INSTAGRAM_USER_ID` | 110 | `NUMBER` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.fivetran_utils.union_data`
    *   `source.facebook_ads.facebook_ads.creative_history`

---
