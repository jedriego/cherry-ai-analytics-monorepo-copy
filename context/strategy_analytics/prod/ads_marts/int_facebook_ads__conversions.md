## Model: `int_facebook_ads__conversions`

`int_facebook_ads__conversions`

*   **Unique ID:** `model.facebook_ads.int_facebook_ads__conversions`
*   **FQN:** `prod.ads_marts.int_facebook_ads__conversions`
*   **Description:** (No description provided)
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'facebook_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `SOURCE_RELATION` | 1 | `TEXT` |  |  | `[]` | `{}` |
    | `AD_ID` | 2 | `NUMBER` |  |  | `[]` | `{}` |
    | `DATE_DAY` | 3 | `DATE` |  |  | `[]` | `{}` |
    | `CONVERSIONS` | 4 | `FLOAT` |  |  | `[]` | `{}` |
    | `CONVERSIONS_VALUE` | 5 | `FLOAT` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.fivetran_utils.persist_pass_through_columns`
    *   `model.facebook_ads.stg_facebook_ads__basic_ad_action_values`
    *   `model.facebook_ads.stg_facebook_ads__basic_ad_actions`

---
