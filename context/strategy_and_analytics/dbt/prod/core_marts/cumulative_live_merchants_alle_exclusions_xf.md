## Model: `cumulative_live_merchants_alle_exclusions_xf`

`cumulative_live_merchants_alle_exclusions_xf`

*   **Unique ID:** `model.cherry_data_model.cumulative_live_merchants_alle_exclusions_xf`
*   **FQN:** `prod.core_marts.cumulative_live_merchants_alle_exclusions_xf`
*   **Description:** Daily time series model that tracks the cumulative count of live merchants, specifically excluding Alle 'New Practice' merchant types. This model provides a refined view of  merchant growth by filtering out new practices that may not yet be fully operational, giving a more accurate picture of established merchant activity. The model captures only active, non-demo, non-terminated Cherry merchants that have gone live, grouped by industry and merchant type. This exclusion-based approach helps differentiate between established practices and newly onboarded practices that may still be in setup or trial phases. The time series runs from September 1, 2020 through yesterday.

*   **Tags:** `['core']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `REFERENCE_DATE` | 1 | `DATE` | Date dimension representing each calendar day for which merchant counts are calculated. Serves as the primary time dimension for this daily time series, covering dates from September 1, 2020 through yesterday (current date minus 1 day). Each merchant is counted as active on their go_live_date and every day thereafter.
 | Date dimension representing each calendar day for which merchant counts are calculated. Serves as the primary time dimension for this daily time series, covering dates from September 1, 2020 through yesterday (current date minus 1 day). Each merchant is counted as active on their go_live_date and every day thereafter.
 | `[]` | `{}` |
    | `INDUSTRY` | 2 | `TEXT` | Industry classification of the merchant practice, derived from the cherry_db_industry field. Industries are grouped under umbrella categories for similar practice types. This dimension allows for analysis of merchant growth and activity patterns across different healthcare and service industry segments.
 | Industry classification of the merchant practice, derived from the cherry_db_industry field. Industries are grouped under umbrella categories for similar practice types. This dimension allows for analysis of merchant growth and activity patterns across different healthcare and service industry segments.
 | `[]` | `{}` |
    | `MERCHANT_TYPE` | 3 | `TEXT` | Type classification of the merchant, filtered to include only 'Cherry' merchant types. This field distinguishes between different merchant categories in the system and ensures consistent reporting by focusing on the primary Cherry merchant classification.
 | Type classification of the merchant, filtered to include only 'Cherry' merchant types. This field distinguishes between different merchant categories in the system and ensures consistent reporting by focusing on the primary Cherry merchant classification.
 | `[]` | `{}` |
    | `CUMULATIVE_MERCHANTS_ACTIVE` | 4 | `NUMBER` | Count of distinct merchants that are considered active on the given reference_date. A merchant is counted as active if they have gone live on or before the reference_date and meet all filtering criteria: non-demo, active status, not terminated, Cherry type, and specifically excludes Alle practices marked as 'New Practice'. This cumulative count represents the total number of established, operational merchant practices available to serve customers on any given day, providing a cleaner metric for business growth analysis by excluding practices that may still be in onboarding phases. | Count of distinct merchants that are considered active on the given reference_date. A merchant is counted as active if they have gone live on or before the reference_date and meet all filtering criteria: non-demo, active status, not terminated, Cherry type, and specifically excludes Alle practices marked as 'New Practice'. This cumulative count represents the total number of established, operational merchant practices available to serve customers on any given day, providing a cleaner metric for business growth analysis by excluding practices that may still be in onboarding phases. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.cherry_data_model.convert_to_pt`
    *   `model.cherry_data_model.calendar_table_xf`
    *   `model.cherry_data_model.stg_merchants`
    *   `model.cherry_data_model.stg_practices`

---
