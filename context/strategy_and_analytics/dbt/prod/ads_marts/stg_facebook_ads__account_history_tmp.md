## Model: `stg_facebook_ads__account_history_tmp`

`stg_facebook_ads__account_history_tmp`

*   **Unique ID:** `model.facebook_ads.stg_facebook_ads__account_history_tmp`
*   **FQN:** `prod.ads_marts.stg_facebook_ads__account_history_tmp`
*   **Description:** (No description provided)
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'facebook_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `_FIVETRAN_ID` | 1 | `TEXT` |  |  | `[]` | `{}` |
    | `AGE` | 2 | `FLOAT` |  |  | `[]` | `{}` |
    | `AMOUNT_SPENT` | 3 | `NUMBER` |  |  | `[]` | `{}` |
    | `BALANCE` | 4 | `NUMBER` |  |  | `[]` | `{}` |
    | `BUSINESS_CITY` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `BUSINESS_COUNTRY_CODE` | 6 | `TEXT` |  |  | `[]` | `{}` |
    | `BUSINESS_NAME` | 7 | `TEXT` |  |  | `[]` | `{}` |
    | `BUSINESS_STATE` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `BUSINESS_STREET` | 9 | `TEXT` |  |  | `[]` | `{}` |
    | `BUSINESS_STREET_2` | 10 | `TEXT` |  |  | `[]` | `{}` |
    | `BUSINESS_ZIP` | 11 | `TEXT` |  |  | `[]` | `{}` |
    | `CAN_CREATE_BRAND_LIFT_STUDY` | 12 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `CREATED_TIME` | 13 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `CURRENCY` | 14 | `TEXT` |  |  | `[]` | `{}` |
    | `END_ADVERTISER` | 15 | `NUMBER` |  |  | `[]` | `{}` |
    | `END_ADVERTISER_NAME` | 16 | `TEXT` |  |  | `[]` | `{}` |
    | `HAS_MIGRATED_PERMISSIONS` | 17 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IO_NUMBER` | 18 | `NUMBER` |  |  | `[]` | `{}` |
    | `IS_ATTRIBUTION_SPEC_SYSTEM_DEFAULT` | 19 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_DIRECT_DEALS_ENABLED` | 20 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_IN_3_DS_AUTHORIZATION_ENABLED_MARKET` | 21 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_NOTIFICATIONS_ENABLED` | 22 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_PERSONAL` | 23 | `NUMBER` |  |  | `[]` | `{}` |
    | `IS_PREPAY_ACCOUNT` | 24 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_TAX_ID_REQUIRED` | 25 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `MEDIA_AGENCY` | 26 | `NUMBER` |  |  | `[]` | `{}` |
    | `MIN_CAMPAIGN_GROUP_SPEND_CAP` | 27 | `NUMBER` |  |  | `[]` | `{}` |
    | `MIN_DAILY_BUDGET` | 28 | `NUMBER` |  |  | `[]` | `{}` |
    | `NAME` | 29 | `TEXT` |  |  | `[]` | `{}` |
    | `NEXT_BILL_DATE` | 30 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `OFFSITE_PIXELS_TOS_ACCEPTED` | 31 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `OWNER` | 32 | `NUMBER` |  |  | `[]` | `{}` |
    | `PARTNER` | 33 | `NUMBER` |  |  | `[]` | `{}` |
    | `SALESFORCE_INVOICE_GROUP_ID` | 34 | `TEXT` |  |  | `[]` | `{}` |
    | `SPEND_CAP` | 35 | `NUMBER` |  |  | `[]` | `{}` |
    | `TAX_ID` | 36 | `TEXT` |  |  | `[]` | `{}` |
    | `TAX_ID_TYPE` | 37 | `TEXT` |  |  | `[]` | `{}` |
    | `TIMEZONE_ID` | 38 | `NUMBER` |  |  | `[]` | `{}` |
    | `TIMEZONE_NAME` | 39 | `TEXT` |  |  | `[]` | `{}` |
    | `TIMEZONE_OFFSET_HOURS_UTC` | 40 | `FLOAT` |  |  | `[]` | `{}` |
    | `ACCOUNT_STATUS` | 41 | `TEXT` |  |  | `[]` | `{}` |
    | `DISABLE_REASON` | 42 | `TEXT` |  |  | `[]` | `{}` |
    | `TAX_ID_STATUS` | 43 | `TEXT` |  |  | `[]` | `{}` |
    | `AGENCY_CLIENT_DECLARATION_AGENCY_REPRESENTING_CLIENT` | 44 | `NUMBER` |  |  | `[]` | `{}` |
    | `AGENCY_CLIENT_DECLARATION_CLIENT_BASED_IN_FRANCE` | 45 | `NUMBER` |  |  | `[]` | `{}` |
    | `AGENCY_CLIENT_DECLARATION_CLIENT_CITY` | 46 | `TEXT` |  |  | `[]` | `{}` |
    | `AGENCY_CLIENT_DECLARATION_CLIENT_COUNTRY_CODE` | 47 | `TEXT` |  |  | `[]` | `{}` |
    | `AGENCY_CLIENT_DECLARATION_CLIENT_EMAIL_ADDRESS` | 48 | `TEXT` |  |  | `[]` | `{}` |
    | `AGENCY_CLIENT_DECLARATION_CLIENT_NAME` | 49 | `TEXT` |  |  | `[]` | `{}` |
    | `AGENCY_CLIENT_DECLARATION_CLIENT_POSTAL_CODE` | 50 | `TEXT` |  |  | `[]` | `{}` |
    | `AGENCY_CLIENT_DECLARATION_CLIENT_PROVINCE` | 51 | `TEXT` |  |  | `[]` | `{}` |
    | `AGENCY_CLIENT_DECLARATION_CLIENT_STREET` | 52 | `TEXT` |  |  | `[]` | `{}` |
    | `AGENCY_CLIENT_DECLARATION_CLIENT_STREET_2` | 53 | `TEXT` |  |  | `[]` | `{}` |
    | `AGENCY_CLIENT_DECLARATION_HAS_WRITTEN_MANDATE_FROM_ADVERTISER` | 54 | `NUMBER` |  |  | `[]` | `{}` |
    | `AGENCY_CLIENT_DECLARATION_IS_CLIENT_PAYING_INVOICES` | 55 | `NUMBER` |  |  | `[]` | `{}` |
    | `BUSINESS_MANAGER_NAME` | 56 | `TEXT` |  |  | `[]` | `{}` |
    | `BUSINESS_MANAGER_TIMEZONE_ID` | 57 | `NUMBER` |  |  | `[]` | `{}` |
    | `BUSINESS_MANAGER_PRIMARY_PAGE` | 58 | `TEXT` |  |  | `[]` | `{}` |
    | `BUSINESS_MANAGER_UPDATED_BY` | 59 | `TEXT` |  |  | `[]` | `{}` |
    | `BUSINESS_MANAGER_CREATED_BY` | 60 | `TEXT` |  |  | `[]` | `{}` |
    | `BUSINESS_MANAGER_UPDATE_TIME` | 61 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `BUSINESS_MANAGER_CREATED_TIME` | 62 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `BUSINESS_MANAGER_MANAGER_ID` | 63 | `NUMBER` |  |  | `[]` | `{}` |
    | `EXTENDED_CREDIT_INVOICE_GROUP_ID` | 64 | `NUMBER` |  |  | `[]` | `{}` |
    | `EXTENDED_CREDIT_INVOICE_GROUP_AUTO_ENROLL` | 65 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `EXTENDED_CREDIT_INVOICE_GROUP_CUSTOMER_PO_NUMBER` | 66 | `TEXT` |  |  | `[]` | `{}` |
    | `EXTENDED_CREDIT_INVOICE_GROUP_EMAILS` | 67 | `VARIANT` |  |  | `[]` | `{}` |
    | `EXTENDED_CREDIT_INVOICE_GROUP_NAME` | 68 | `TEXT` |  |  | `[]` | `{}` |
    | `CAPABILITIES` | 69 | `VARIANT` |  |  | `[]` | `{}` |
    | `ID` | 70 | `NUMBER` |  |  | `[]` | `{}` |
    | `_FIVETRAN_SYNCED` | 71 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `BUSINESS_MANAGER_PROFILE_PICTURE_URI` | 72 | `TEXT` |  |  | `[]` | `{}` |
    | `BUSINESS_MANAGER_EXTENDED_UPDATED_TIME` | 73 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `BUSINESS_MANAGER_VERIFICATION_STATUS` | 74 | `TEXT` |  |  | `[]` | `{}` |
    | `BUSINESS_MANAGER_BLOCK_OFFLINE_ANALYTICS` | 75 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `HAS_ADVERTISER_OPTED_IN_ODAX` | 76 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `BUSINESS_MANAGER_VERTICAL_ID` | 77 | `NUMBER` |  |  | `[]` | `{}` |
    | `BUSINESS_MANAGER_LINK` | 78 | `TEXT` |  |  | `[]` | `{}` |
    | `BUSINESS_MANAGER_IS_HIDDEN` | 79 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `BUSINESS_MANAGER_VERTICAL` | 80 | `TEXT` |  |  | `[]` | `{}` |
    | `EXTENDED_CREDIT_INVOICE_GROUP_EMAIL` | 81 | `TEXT` |  |  | `[]` | `{}` |
    | `BUSINESS_MANAGER_PAYMENT_ACCOUNT_ID` | 82 | `NUMBER` |  |  | `[]` | `{}` |
    | `BUSINESS_MANAGER_TWO_FACTOR_TYPE` | 83 | `TEXT` |  |  | `[]` | `{}` |
    | `FUNDING_SOURCE_DETAILS_ID` | 84 | `NUMBER` |  |  | `[]` | `{}` |
    | `FUNDING_SOURCE_DETAILS_CAMPAIGN_IDS` | 85 | `VARIANT` |  |  | `[]` | `{}` |
    | `FUNDING_SOURCE_DETAILS_AMOUNT` | 86 | `NUMBER` |  |  | `[]` | `{}` |
    | `FUNDING_SOURCE_DETAILS_TYPE` | 87 | `TEXT` |  |  | `[]` | `{}` |
    | `FUNDING_SOURCE_DETAILS_CURRENCY` | 88 | `TEXT` |  |  | `[]` | `{}` |
    | `FUNDING_SOURCE_DETAILS_COUPON_ID` | 89 | `NUMBER` |  |  | `[]` | `{}` |
    | `FUNDING_SOURCE_DETAILS_DISPLAY_AMOUNT` | 90 | `TEXT` |  |  | `[]` | `{}` |
    | `FUNDING_SOURCE_DETAILS_EXPIRATION` | 91 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `FUNDING_SOURCE_DETAILS_ORIGINAL_DISPLAY_AMOUNT` | 92 | `TEXT` |  |  | `[]` | `{}` |
    | `FUNDING_SOURCE` | 93 | `NUMBER` |  |  | `[]` | `{}` |
    | `FUNDING_SOURCE_DETAILS_ORIGINAL_AMOUNT` | 94 | `NUMBER` |  |  | `[]` | `{}` |
    | `FUNDING_SOURCE_DETAILS_DISPLAY_STRING` | 95 | `TEXT` |  |  | `[]` | `{}` |
    | `FUNDING_SOURCE_DETAILS_COUPONS` | 96 | `VARIANT` |  |  | `[]` | `{}` |
    | `FUNDING_SOURCE_DETAILS_COUPON` | 97 | `VARIANT` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.fivetran_utils.union_data`
    *   `source.facebook_ads.facebook_ads.account_history`

---
