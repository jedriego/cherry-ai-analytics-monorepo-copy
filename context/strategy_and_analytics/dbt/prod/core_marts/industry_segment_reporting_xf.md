## Model: `industry_segment_reporting_xf`

`industry_segment_reporting_xf`

*   **Unique ID:** `model.cherry_data_model.industry_segment_reporting_xf`
*   **FQN:** `prod.core_marts.industry_segment_reporting_xf`
*   **Description:** Comprehensive reporting table that tracks industry segment classification changes over time for leads and accounts. This model analyzes the slowly changing dimension aspects of industry segment assignments by capturing initial values, current values, and historical changes. It provides visibility into how industry segment classifications evolve from initial assignment through various evaluation processes, including lead-level segments, account-level segments, and coalesced segments. The model serves as a key reporting table for understanding industry segment accuracy, tracking classification changes, and analyzing the effectiveness of automated vs. manual segment assignments. It enables analysis of segment stability, classification accuracy trends, and operational efficiency of industry segment management processes.

*   **Tags:** `['core']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `LEAD_ID` | 1 | `TEXT` | Foreign key reference to the lead record. Serves as the primary identifier for tracking industry segment changes at the lead level across all snapshots and time periods.
 | Foreign key reference to the lead record. Serves as the primary identifier for tracking industry segment changes at the lead level across all snapshots and time periods.
 | `[]` | `{}` |
    | `LEAD_CREATED_DATE` | 2 | `TIMESTAMP_TZ` | Date when the original lead was created in the system. Provides temporal context for understanding when the lead first entered the system and began the industry segment classification process.
 | Date when the original lead was created in the system. Provides temporal context for understanding when the lead first entered the system and began the industry segment classification process.
 | `[]` | `{}` |
    | `SCRAPED_SERVICES_INDUSTRY_SEGMENT` | 3 | `TEXT` | Industry segment classification derived from scraped or automated analysis of services offered by the business. Provides an additional data source for industry segment determination based on observed business activities.
 | Industry segment classification derived from scraped or automated analysis of services offered by the business. Provides an additional data source for industry segment determination based on observed business activities.
 | `[]` | `{}` |
    | `CURRENT_LEAD_INDUSTRY_SEGMENT` | 4 | `TEXT` | Current industry segment classification at the lead level. Represents the most recent lead-specific industry segment assignment, which may be automatically determined or manually assigned through evaluation processes.
 | Current industry segment classification at the lead level. Represents the most recent lead-specific industry segment assignment, which may be automatically determined or manually assigned through evaluation processes.
 | `[]` | `{}` |
    | `CURRENT_LEAD_INDUSTRY_SEGMENT_EVALUATION` | 5 | `TEXT` | Current evaluation status or confidence level for the lead industry segment classification. Indicates whether the current lead segment has been verified, is pending review, or requires additional evaluation.
 | Current evaluation status or confidence level for the lead industry segment classification. Indicates whether the current lead segment has been verified, is pending review, or requires additional evaluation.
 | `[]` | `{}` |
    | `CURRENT_ACCOUNT_INDUSTRY_SEGMENT` | 6 | `TEXT` | Current industry segment classification at the account level. Represents the most recent account-level industry segment assignment, which may differ from the lead-level classification due to account-specific business characteristics.
 | Current industry segment classification at the account level. Represents the most recent account-level industry segment assignment, which may differ from the lead-level classification due to account-specific business characteristics.
 | `[]` | `{}` |
    | `CURRENT_ACCOUNT_INDUSTRY_SEGMENT_EVALUATION` | 7 | `TEXT` | Current evaluation status or confidence level for the account industry segment classification. Indicates the validation state of the account-level segment assignment.
 | Current evaluation status or confidence level for the account industry segment classification. Indicates the validation state of the account-level segment assignment.
 | `[]` | `{}` |
    | `CURRENT_INDUSTRY_SEGMENT_COALESCE` | 8 | `TEXT` | Current final industry segment classification derived from coalescing multiple segment sources. Represents the authoritative industry segment assignment that combines lead-level and account-level classifications according to business rules.
 | Current final industry segment classification derived from coalescing multiple segment sources. Represents the authoritative industry segment assignment that combines lead-level and account-level classifications according to business rules.
 | `[]` | `{}` |
    | `INITIAL_LEAD_HISTORY_CREATED_DATE` | 9 | `TIMESTAMP_NTZ` | Timestamp when the first industry segment history record was created for this lead. Marks the beginning of industry segment tracking and provides context for understanding the duration of segment classification evolution.
 | Timestamp when the first industry segment history record was created for this lead. Marks the beginning of industry segment tracking and provides context for understanding the duration of segment classification evolution.
 | `[]` | `{}` |
    | `LAST_LEAD_HISTORY_UPDATED_DATE` | 10 | `TIMESTAMP_NTZ` | Timestamp when the most recent industry segment history record was created for this lead. Indicates when the last segment classification change occurred.
 | Timestamp when the most recent industry segment history record was created for this lead. Indicates when the last segment classification change occurred.
 | `[]` | `{}` |
    | `INITIAL_LEAD_INDUSTRY_SEGMENT` | 11 | `TEXT` | Initial industry segment classification at the lead level when first recorded. Calculated using min_by(lead_industry_segment, dbt_valid_from) to capture the earliest lead segment assignment for comparison with current values.
 | Initial industry segment classification at the lead level when first recorded. Calculated using min_by(lead_industry_segment, dbt_valid_from) to capture the earliest lead segment assignment for comparison with current values.
 | `[]` | `{}` |
    | `LAST_LEAD_INDUSTRY_SEGMENT` | 12 | `TEXT` | Most recent historical industry segment classification at the lead level. Calculated using max_by(lead_industry_segment, dbt_valid_from) to capture the latest lead segment assignment from historical snapshots.
 | Most recent historical industry segment classification at the lead level. Calculated using max_by(lead_industry_segment, dbt_valid_from) to capture the latest lead segment assignment from historical snapshots.
 | `[]` | `{}` |
    | `INITIAL_LEAD_INDUSTRY_SEGMENT_EVALUATION` | 13 | `TEXT` | Initial evaluation status for the lead industry segment classification. Captures the original evaluation state when industry segment tracking began, enabling analysis of evaluation process improvements over time.
 | Initial evaluation status for the lead industry segment classification. Captures the original evaluation state when industry segment tracking began, enabling analysis of evaluation process improvements over time.
 | `[]` | `{}` |
    | `LAST_LEAD_INDUSTRY_SEGMENT_EVALUATION` | 14 | `TEXT` | Most recent historical evaluation status for the lead industry segment. Captures the latest evaluation state from historical records for comparison with current evaluation status.
 | Most recent historical evaluation status for the lead industry segment. Captures the latest evaluation state from historical records for comparison with current evaluation status.
 | `[]` | `{}` |
    | `INITIAL_ACCOUNT_INDUSTRY_SEGMENT` | 15 | `TEXT` | Initial industry segment classification at the account level when first recorded. Calculated using min_by(account_industry_segment, dbt_valid_from) to capture the earliest account segment assignment for historical comparison.
 | Initial industry segment classification at the account level when first recorded. Calculated using min_by(account_industry_segment, dbt_valid_from) to capture the earliest account segment assignment for historical comparison.
 | `[]` | `{}` |
    | `LAST_ACCOUNT_INDUSTRY_SEGMENT` | 16 | `TEXT` | Most recent historical industry segment classification at the account level. Calculated using max_by(account_industry_segment, dbt_valid_from) to capture the latest account segment assignment from historical snapshots.
 | Most recent historical industry segment classification at the account level. Calculated using max_by(account_industry_segment, dbt_valid_from) to capture the latest account segment assignment from historical snapshots.
 | `[]` | `{}` |
    | `INITIAL_ACCOUNT_INDUSTRY_SEGMENT_EVALUATION` | 17 | `TEXT` | Initial evaluation status for the account industry segment classification. Captures the original account-level evaluation state for tracking evaluation process evolution and accuracy improvements.
 | Initial evaluation status for the account industry segment classification. Captures the original account-level evaluation state for tracking evaluation process evolution and accuracy improvements.
 | `[]` | `{}` |
    | `LAST_ACCOUNT_INDUSTRY_SEGMENT_EVALUATION` | 18 | `TEXT` | Most recent historical evaluation status for the account industry segment. Captures the latest account-level evaluation state from historical records for tracking evaluation process progression.
 | Most recent historical evaluation status for the account industry segment. Captures the latest account-level evaluation state from historical records for tracking evaluation process progression.
 | `[]` | `{}` |
    | `INITIAL_INDUSTRY_SEGMENT_COALESCE` | 19 | `TEXT` | Initial coalesced industry segment classification when first recorded. Calculated using min_by(industry_segment_coalesce, dbt_valid_from) to capture the earliest final segment assignment for analyzing classification stability.
 | Initial coalesced industry segment classification when first recorded. Calculated using min_by(industry_segment_coalesce, dbt_valid_from) to capture the earliest final segment assignment for analyzing classification stability.
 | `[]` | `{}` |
    | `LAST_INDUSTRY_SEGMENT_COALESCE` | 20 | `TEXT` | Most recent historical coalesced industry segment classification. Calculated using max_by(industry_segment_coalesce, dbt_valid_from) to capture the latest final segment assignment from historical snapshots for comparison with current values.
 | Most recent historical coalesced industry segment classification. Calculated using max_by(industry_segment_coalesce, dbt_valid_from) to capture the latest final segment assignment from historical snapshots for comparison with current values.
 | `[]` | `{}` |
    | `NUM_UPDATES` | 21 | `NUMBER` | Count of industry segment history updates for this lead, calculated as count(dbt_valid_from). This metric indicates how frequently the industry segment classifications have changed, providing insight into segment stability and the effectiveness of initial classification processes. Higher values may indicate leads with complex or evolving business models requiring multiple segment refinements. | Count of industry segment history updates for this lead, calculated as count(dbt_valid_from). This metric indicates how frequently the industry segment classifications have changed, providing insight into segment stability and the effectiveness of initial classification processes. Higher values may indicate leads with complex or evolving business models requiring multiple segment refinements. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.stg_industry_segment_history`

---
