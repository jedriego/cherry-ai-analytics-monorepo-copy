## Model: `stg_facebook_ads__basic_ad_tmp`

`stg_facebook_ads__basic_ad_tmp`

*   **Unique ID:** `model.facebook_ads.stg_facebook_ads__basic_ad_tmp`
*   **FQN:** `prod.ads_marts.stg_facebook_ads__basic_ad_tmp`
*   **Description:** (No description provided)
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'facebook_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `AD_ID` | 1 | `TEXT` |  |  | `[]` | `{}` |
    | `DATE` | 2 | `DATE` |  |  | `[]` | `{}` |
    | `_FIVETRAN_ID` | 3 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_ID` | 4 | `NUMBER` |  |  | `[]` | `{}` |
    | `IMPRESSIONS` | 5 | `NUMBER` |  |  | `[]` | `{}` |
    | `INLINE_LINK_CLICKS` | 6 | `NUMBER` |  |  | `[]` | `{}` |
    | `REACH` | 7 | `NUMBER` |  |  | `[]` | `{}` |
    | `CPC` | 8 | `FLOAT` |  |  | `[]` | `{}` |
    | `CPM` | 9 | `FLOAT` |  |  | `[]` | `{}` |
    | `CTR` | 10 | `FLOAT` |  |  | `[]` | `{}` |
    | `FREQUENCY` | 11 | `FLOAT` |  |  | `[]` | `{}` |
    | `SPEND` | 12 | `FLOAT` |  |  | `[]` | `{}` |
    | `AD_NAME` | 13 | `TEXT` |  |  | `[]` | `{}` |
    | `ADSET_NAME` | 14 | `TEXT` |  |  | `[]` | `{}` |
    | `_FIVETRAN_SYNCED` | 15 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `COST_PER_INLINE_LINK_CLICK` | 16 | `FLOAT` |  |  | `[]` | `{}` |
    | `INLINE_LINK_CLICK_CTR` | 17 | `TEXT` |  |  | `[]` | `{}` |
    | `ADSET_ID` | 18 | `NUMBER` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.fivetran_utils.union_data`
    *   `source.facebook_ads.facebook_ads.basic_ad`

---
