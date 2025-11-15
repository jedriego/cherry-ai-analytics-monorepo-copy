## Model: `stg_facebook_ads__ad_history_tmp`

`stg_facebook_ads__ad_history_tmp`

*   **Unique ID:** `model.facebook_ads.stg_facebook_ads__ad_history_tmp`
*   **FQN:** `prod.ads_marts.stg_facebook_ads__ad_history_tmp`
*   **Description:** (No description provided)
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'facebook_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `ID` | 1 | `NUMBER` |  |  | `[]` | `{}` |
    | `UPDATED_TIME` | 2 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `ACCOUNT_ID` | 3 | `NUMBER` |  |  | `[]` | `{}` |
    | `CAMPAIGN_ID` | 4 | `NUMBER` |  |  | `[]` | `{}` |
    | `CREATIVE_ID` | 5 | `NUMBER` |  |  | `[]` | `{}` |
    | `BID_AMOUNT` | 6 | `NUMBER` |  |  | `[]` | `{}` |
    | `BID_TYPE` | 7 | `TEXT` |  |  | `[]` | `{}` |
    | `CONFIGURED_STATUS` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `CONVERSION_DOMAIN` | 9 | `TEXT` |  |  | `[]` | `{}` |
    | `CREATED_TIME` | 10 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `EFFECTIVE_STATUS` | 11 | `TEXT` |  |  | `[]` | `{}` |
    | `LAST_UPDATED_BY_APP_ID` | 12 | `TEXT` |  |  | `[]` | `{}` |
    | `NAME` | 13 | `TEXT` |  |  | `[]` | `{}` |
    | `STATUS` | 14 | `TEXT` |  |  | `[]` | `{}` |
    | `AD_SET_ID` | 15 | `NUMBER` |  |  | `[]` | `{}` |
    | `AD_SOURCE_ID` | 16 | `NUMBER` |  |  | `[]` | `{}` |
    | `_FIVETRAN_SYNCED` | 17 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `PLACEMENT_SPECIFIC_INSTAGRAM_DISCRIMINATORY_PRACTICES` | 18 | `TEXT` |  |  | `[]` | `{}` |
    | `GLOBAL_DISCRIMINATORY_PRACTICES` | 19 | `TEXT` |  |  | `[]` | `{}` |
    | `PLACEMENT_SPECIFIC_FACEBOOK_DISCRIMINATORY_PRACTICES` | 20 | `TEXT` |  |  | `[]` | `{}` |
    | `PREVIEW_SHAREABLE_LINK` | 21 | `TEXT` |  |  | `[]` | `{}` |
    | `PLACEMENT_SPECIFIC_FACEBOOK_SENSATIONAL_CONTENT` | 22 | `TEXT` |  |  | `[]` | `{}` |
    | `GLOBAL_SENSATIONAL_CONTENT` | 23 | `TEXT` |  |  | `[]` | `{}` |
    | `PLACEMENT_SPECIFIC_INSTAGRAM_SENSATIONAL_CONTENT` | 24 | `TEXT` |  |  | `[]` | `{}` |
    | `PLACEMENT_SPECIFIC_FACEBOOK_VIOLENCE_GRAPHIC_CONTENT` | 25 | `TEXT` |  |  | `[]` | `{}` |
    | `GLOBAL_ADVERTISING_POLICIES` | 26 | `TEXT` |  |  | `[]` | `{}` |
    | `GLOBAL_VIOLENCE_GRAPHIC_CONTENT` | 27 | `TEXT` |  |  | `[]` | `{}` |
    | `PLACEMENT_SPECIFIC_INSTAGRAM_VIOLENCE_GRAPHIC_CONTENT` | 28 | `TEXT` |  |  | `[]` | `{}` |
    | `GLOBAL_PERSONAL_HEALTH_AND_APPEARANCE` | 29 | `TEXT` |  |  | `[]` | `{}` |
    | `BID_INFO_ACTIONS` | 30 | `NUMBER` |  |  | `[]` | `{}` |
    | `GLOBAL_FINANCIAL_AND_INSURANCE_PRODUCTS_AND_SERVICES` | 31 | `TEXT` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.fivetran_utils.union_data`
    *   `source.facebook_ads.facebook_ads.ad_history`

---
