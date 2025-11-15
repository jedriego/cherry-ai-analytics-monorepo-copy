## Model: `daily_merchant_volume_xf`

`daily_merchant_volume_xf`

*   **Unique ID:** `model.cherry_data_model.daily_merchant_volume_xf`
*   **FQN:** `prod.core_marts.daily_merchant_volume_xf`
*   **Description:** Daily aggregated summary of merchant lending activity and volume metrics, providing a high-level view of business performance across key dimensions. This model aggregates data from the daily_merchant_loans_xf model to create daily summaries of unique merchant counts, practice counts, and transaction volumes grouped by industry, retention ownership, and merchant status. The model serves as a key reporting table for executive dashboards, performance tracking, and business intelligence reporting by providing consolidated metrics that can be easily analyzed across different business segments and time periods. It enables analysis of lending volume trends, merchant portfolio growth, and performance by retention teams and industry segments.

*   **Tags:** `['core']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `CALENDAR_DATE` | 1 | `DATE` | Date dimension representing the calendar day for which metrics are aggregated. Serves as the primary time dimension for this daily summary, enabling time series analysis of merchant volume and activity trends.
 | Date dimension representing the calendar day for which metrics are aggregated. Serves as the primary time dimension for this daily summary, enabling time series analysis of merchant volume and activity trends.
 | `[]` | `{}` |
    | `INDUSTRY_SEGMENT` | 2 | `TEXT` | Granular industry segment classification used for grouping and analyzing merchant performance within specific industry categories. Provides detailed segmentation within broader industry groups for targeted analysis.
 | Granular industry segment classification used for grouping and analyzing merchant performance within specific industry categories. Provides detailed segmentation within broader industry groups for targeted analysis.
 | `[]` | `{}` |
    | `INDUSTRY` | 3 | `TEXT` | Broader industry classification of merchant practices, derived from the cherry_db_industry field. Used for high-level industry performance analysis and segmentation of the merchant portfolio.
 | Broader industry classification of merchant practices, derived from the cherry_db_industry field. Used for high-level industry performance analysis and segmentation of the merchant portfolio.
 | `[]` | `{}` |
    | `RETENTION_OWNER_DEPARTMENT` | 4 | `TEXT` | Department responsible for merchant retention and relationship management. Used as a grouping dimension for analyzing retention team performance and merchant portfolio management across different organizational departments.
 | Department responsible for merchant retention and relationship management. Used as a grouping dimension for analyzing retention team performance and merchant portfolio management across different organizational departments.
 | `[]` | `{}` |
    | `RETENTION_OWNER_TEAM` | 5 | `TEXT` | Specific team within the retention department responsible for merchant relationships. Provides more granular performance tracking and accountability for retention activities within departments.
 | Specific team within the retention department responsible for merchant relationships. Provides more granular performance tracking and accountability for retention activities within departments.
 | `[]` | `{}` |
    | `RETENTION_OWNER` | 6 | `TEXT` | Individual retention specialist or account manager responsible for merchant relationships. Enables individual-level performance tracking and workload analysis for retention team members.
 | Individual retention specialist or account manager responsible for merchant relationships. Enables individual-level performance tracking and workload analysis for retention team members.
 | `[]` | `{}` |
    | `IS_ACTIVE` | 7 | `BOOLEAN` | Boolean flag indicating whether merchants in this grouping are currently active and operational. Used for filtering and segmenting analysis between active and inactive merchant populations.
 | Boolean flag indicating whether merchants in this grouping are currently active and operational. Used for filtering and segmenting analysis between active and inactive merchant populations.
 | `[]` | `{}` |
    | `IS_TERMINATED` | 8 | `BOOLEAN` | Boolean flag indicating whether merchants in this grouping have been terminated. Used for analyzing terminated merchant activity and understanding the impact of merchant terminations on business volume.
 | Boolean flag indicating whether merchants in this grouping have been terminated. Used for analyzing terminated merchant activity and understanding the impact of merchant terminations on business volume.
 | `[]` | `{}` |
    | `UNIQUE_PRACTICE_COUNT` | 9 | `NUMBER` | Count of distinct practices (sf_account_id) that had loan activity on the given date within the specified dimension grouping. This metric represents the number of unique practice-level accounts that generated loans, providing insight into practice-level engagement and market penetration.
 | Count of distinct practices (sf_account_id) that had loan activity on the given date within the specified dimension grouping. This metric represents the number of unique practice-level accounts that generated loans, providing insight into practice-level engagement and market penetration.
 | `[]` | `{}` |
    | `UNIQUE_MERCHANT_COUNT` | 10 | `NUMBER` | Count of distinct merchants (merchant_id) that had loan activity on the given date within the specified dimension grouping. This metric represents the number of unique merchant locations or entities that generated loans, providing insight into merchant-level activity and geographic distribution.
 | Count of distinct merchants (merchant_id) that had loan activity on the given date within the specified dimension grouping. This metric represents the number of unique merchant locations or entities that generated loans, providing insight into merchant-level activity and geographic distribution.
 | `[]` | `{}` |
    | `TRANSACTION_VOLUME` | 11 | `FLOAT` | Total dollar volume of loans funded on the given date within the specified dimension grouping, calculated as the sum of gross_amount from all loans. This metric represents the total lending volume and is a key indicator of business performance, revenue generation, and market activity. Used for tracking growth trends, setting targets, and measuring business success. | Total dollar volume of loans funded on the given date within the specified dimension grouping, calculated as the sum of gross_amount from all loans. This metric represents the total lending volume and is a key indicator of business performance, revenue generation, and market activity. Used for tracking growth trends, setting targets, and measuring business success. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.daily_merchant_loans_xf`

---
