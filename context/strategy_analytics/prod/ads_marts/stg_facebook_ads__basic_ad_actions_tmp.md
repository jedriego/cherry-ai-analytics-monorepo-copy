## Model: `stg_facebook_ads__basic_ad_actions_tmp`

`stg_facebook_ads__basic_ad_actions_tmp`

*   **Unique ID:** `model.facebook_ads.stg_facebook_ads__basic_ad_actions_tmp`
*   **FQN:** `prod.ads_marts.stg_facebook_ads__basic_ad_actions_tmp`
*   **Description:** (No description provided)
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'facebook_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `AD_ID` | 1 | `TEXT` |  |  | `[]` | `{}` |
    | `DATE` | 2 | `DATE` |  |  | `[]` | `{}` |
    | `_FIVETRAN_ID` | 3 | `TEXT` |  |  | `[]` | `{}` |
    | `INDEX` | 4 | `NUMBER` |  |  | `[]` | `{}` |
    | `ACTION_TYPE` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `VALUE` | 6 | `FLOAT` |  |  | `[]` | `{}` |
    | `_7_D_CLICK` | 7 | `FLOAT` |  |  | `[]` | `{}` |
    | `_FIVETRAN_SYNCED` | 8 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `INLINE` | 9 | `FLOAT` |  |  | `[]` | `{}` |
    | `_1_D_VIEW` | 10 | `FLOAT` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.fivetran_utils.union_data`
    *   `source.facebook_ads.facebook_ads.basic_ad_actions`

---
