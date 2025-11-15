## Model: `int_facebook_ads__creative_history`

`int_facebook_ads__creative_history`

*   **Unique ID:** `model.facebook_ads.int_facebook_ads__creative_history`
*   **FQN:** `prod.ads_marts.int_facebook_ads__creative_history`
*   **Description:** (No description provided)
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'facebook_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `SOURCE_RELATION` | 1 | `TEXT` |  |  | `[]` | `{}` |
    | `_FIVETRAN_ID` | 2 | `TEXT` |  |  | `[]` | `{}` |
    | `CREATIVE_ID` | 3 | `NUMBER` |  |  | `[]` | `{}` |
    | `ACCOUNT_ID` | 4 | `NUMBER` |  |  | `[]` | `{}` |
    | `CREATIVE_NAME` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `URL` | 6 | `TEXT` |  |  | `[]` | `{}` |
    | `BASE_URL` | 7 | `TEXT` |  |  | `[]` | `{}` |
    | `URL_HOST` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `URL_PATH` | 9 | `TEXT` |  |  | `[]` | `{}` |
    | `UTM_SOURCE` | 10 | `TEXT` |  |  | `[]` | `{}` |
    | `UTM_MEDIUM` | 11 | `TEXT` |  |  | `[]` | `{}` |
    | `UTM_CAMPAIGN` | 12 | `TEXT` |  |  | `[]` | `{}` |
    | `UTM_CONTENT` | 13 | `TEXT` |  |  | `[]` | `{}` |
    | `UTM_TERM` | 14 | `TEXT` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt.split_part`
    *   `macro.dbt_utils.get_url_host`
    *   `macro.dbt_utils.get_url_path`
    *   `macro.facebook_ads.facebook_ads_extract_url_parameter`
    *   `model.facebook_ads.facebook_ads__url_tags`
    *   `model.facebook_ads.stg_facebook_ads__creative_history`

---
