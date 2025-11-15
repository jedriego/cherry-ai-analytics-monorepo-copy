## Model: `sales_daily_metrics`

`sales_daily_metrics`

*   **Unique ID:** `model.cherry_data_model.sales_daily_metrics`
*   **FQN:** `prod.revenue_marts.sales_daily_metrics`
*   **Description:** This model is designed to capture daily trends for key metrics related to Account Executives. It combines data from multiple sources to provide an overview of various metrics, such as first 60-day volume, registrations, activations, and go-lives, grouped by various dimensions including industry segments and Account Executive teams.

*   **Tags:** `['revenue_analytics']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `DATE` | 1 | `DATE` | The date for which the metrics are reported. | The date for which the metrics are reported. | `[]` | `{}` |
    | `INDUSTRY_SEGMENT` | 2 | `TEXT` | Broad categorization of industry segments for the Account Executive. | Broad categorization of industry segments for the Account Executive. | `[]` | `{}` |
    | `INDUSTRY` | 3 | `TEXT` | Industry category based on either merchant or lead information. | Industry category based on either merchant or lead information. | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_DEPARTMENT` | 4 | `TEXT` | Department to which the Account Executive belongs. | Department to which the Account Executive belongs. | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_TEAM` | 5 | `TEXT` | Team to which the Account Executive belongs. | Team to which the Account Executive belongs. | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_SUBTEAM` | 6 | `TEXT` | Subteam to which the Account Executive belongs. | Subteam to which the Account Executive belongs. | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE` | 7 | `TEXT` | The name of the Account Executive. | The name of the Account Executive. | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_TITLE` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_IS_ACTIVE` | 9 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `DEMOS` | 10 | `NUMBER` |  |  | `[]` | `{}` |
    | `REGISTRATIONS` | 11 | `NUMBER` | The number of new registrations for the given date, industry segment, and Account Executive. | The number of new registrations for the given date, industry segment, and Account Executive. | `[]` | `{}` |
    | `GO_LIVES` | 12 | `NUMBER` | The number of merchants that went live on the given date, for the given Account Executive and industry segment. | The number of merchants that went live on the given date, for the given Account Executive and industry segment. | `[]` | `{}` |
    | `LOANS` | 13 | `NUMBER` |  |  | `[]` | `{}` |
    | `FIRST_60_VOLUME` | 14 | `FLOAT` | The volume of loans funded within the first 60 days after commission start date for the given Account Executive and industry segment. | The volume of loans funded within the first 60 days after commission start date for the given Account Executive and industry segment. | `[]` | `{}` |
    | `FIRST_30_ACTIVATIONS` | 15 | `NUMBER` |  |  | `[]` | `{}` |
    | `FIRST_60_ACTIVATIONS` | 16 | `NUMBER` | The number of first loans activated within the first 60 days after commission start date for the given Account Executive and industry segment. | The number of first loans activated within the first 60 days after commission start date for the given Account Executive and industry segment. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.sales_daily_metrics_details`

---
