## Model: `daily_churn_details_xf`

`daily_churn_details_xf`

*   **Unique ID:** `model.cherry_data_model.daily_churn_details_xf`
*   **FQN:** `prod.core_marts.daily_churn_details_xf`
*   **Description:** - This model predicts the likelihood of a merchant churning within 60 days, leveraging a pre-trained machine learning algorithm stored in a Snowflake Stage.  - The algorithm uses historical data and various merchant-specific features to provide a probability score, which helps identify customers at risk of churn.  - This enables businesses to take proactive measures to improve customer retention and target resources more effectively.

*   **Tags:** `['core', 'churn', 'machine learning', 'predictive analytics']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `MERCHANT_ID` | 1 | `NUMBER` | Unique identifier for the merchant. | Unique identifier for the merchant. | `[]` | `{}` |
    | `DATE` | 2 | `DATE` | Date associated with the specific record. | Date associated with the specific record. | `[]` | `{}` |
    | `MONTH` | 3 | `NUMBER` | The month extracted from the date. | The month extracted from the date. | `[]` | `{}` |
    | `QUARTER` | 4 | `NUMBER` | The quarter extracted from the date. | The quarter extracted from the date. | `[]` | `{}` |
    | `IS_CHURNED` | 5 | `BOOLEAN` | A flag indicating if the merchant has churned or not. | A flag indicating if the merchant has churned or not. | `[]` | `{}` |
    | `CHURN_PERSONA` | 6 | `TEXT` | A categorical variable representing the merchant's churn persona. | A categorical variable representing the merchant's churn persona. | `[]` | `{}` |
    | `FULL_TIME_VS_PART_TIME` | 7 | `TEXT` | A categorical variable indicating if the merchant is working full-time or part-time. | A categorical variable indicating if the merchant is working full-time or part-time. | `[]` | `{}` |
    | `PATIENTS_PER_WEEK` | 8 | `TEXT` | The number of patients the merchant sees per week. | The number of patients the merchant sees per week. | `[]` | `{}` |
    | `INDUSTRY_SEGMENT` | 9 | `TEXT` | The industry segment the merchant belongs to. | The industry segment the merchant belongs to. | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_TEAM` | 10 | `TEXT` | The account executive team responsible for the merchant. | The account executive team responsible for the merchant. | `[]` | `{}` |
    | `ONBOARDING_SPECIALIST_TEAM` | 11 | `TEXT` | The onboarding specialist team responsible for the merchant. | The onboarding specialist team responsible for the merchant. | `[]` | `{}` |
    | `PRACTICE_DEVELOPMENT_MANAGER_REGION` | 12 | `TEXT` | The region where the practice development manager responsible for the merchant is located. | The region where the practice development manager responsible for the merchant is located. | `[]` | `{}` |
    | `MOST_RECENT_LOAN` | 13 | `DATE` | The date of the most recent loan the merchant received. | The date of the most recent loan the merchant received. | `[]` | `{}` |
    | `DAYS_SINCE_MOST_RECENT_LOAN` | 14 | `NUMBER` | The number of days since the most recent loan the merchant received. | The number of days since the most recent loan the merchant received. | `[]` | `{}` |
    | `DAYS_SINCE_FIRST_LOAN` | 15 | `NUMBER` | The number of days since the merchant's first loan. | The number of days since the merchant's first loan. | `[]` | `{}` |
    | `DAYS_UNTIL_CHURN` | 16 | `NUMBER` | The number of days until the merchant churns. | The number of days until the merchant churns. | `[]` | `{}` |
    | `CHURNED_WITHIN_60_DAYS` | 17 | `NUMBER` | A flag indicating if the merchant churned within 60 days. | A flag indicating if the merchant churned within 60 days. | `[]` | `{}` |
    | `CHURN_WITHIN_60_DAYS_PROBABILITY` | 18 | `FLOAT` | The predicted probability of the merchant churning within 60 days. | The predicted probability of the merchant churning within 60 days. | `[]` | `{}` |
    | `CHURN_EVENT_START_DATE` | 19 | `DATE` | The start date of the churn event for the merchant. | The start date of the churn event for the merchant. | `[]` | `{}` |
    | `TOTAL_CHURN_EVENTS` | 20 | `NUMBER` | The total number of churn events the merchant has experienced. | The total number of churn events the merchant has experienced. | `[]` | `{}` |
    | `CUMULATIVE_VOLUME` | 21 | `FLOAT` | The cumulative loan volume for the merchant. | The cumulative loan volume for the merchant. | `[]` | `{}` |
    | `AVG_30_DAY_VOLUME` | 22 | `FLOAT` | The average loan volume for the merchant in the last 30 days. | The average loan volume for the merchant in the last 30 days. | `[]` | `{}` |
    | `CUMULATIVE_DAYS_WITH_LOANS_COUNT` | 23 | `NUMBER` | The cumulative number of days the merchant had loans. | The cumulative number of days the merchant had loans. | `[]` | `{}` |
    | `DAILY_TRANSACTION_RATE` | 24 | `NUMBER` | The merchant's daily transaction rate. | The merchant's daily transaction rate. | `[]` | `{}` |
    | `TRANSACTION_COUNT` | 25 | `NUMBER` | The total number of transactions for the merchant. | The total number of transactions for the merchant. | `[]` | `{}` |
    | `TRANSACTION_COUNT_LAST_30_DAYS` | 26 | `NUMBER` | The total number of transactions for the merchant in the last 30 days. | The total number of transactions for the merchant in the last 30 days. | `[]` | `{}` |
    | `TRANSACTION_VOLUME_LAST_30_DAYS` | 27 | `FLOAT` | The total transaction volume for the merchant in the last 30 days. | The total transaction volume for the merchant in the last 30 days. | `[]` | `{}` |
    | `APPLICATION_COUNT` | 28 | `NUMBER` | The total number of applications the merchant has submitted. | The total number of applications the merchant has submitted. | `[]` | `{}` |
    | `APPLICATION_COUNT_LAST_30_DAYS` | 29 | `NUMBER` | The total number of applications the merchant has submitted in the last 30 days. | The total number of applications the merchant has submitted in the last 30 days. | `[]` | `{}` |
    | `APPROVED_APPLICATION_COUNT_LAST_30_DAYS` | 30 | `NUMBER` | The total number of approved applications for the merchant in the last 30 days. | The total number of approved applications for the merchant in the last 30 days. | `[]` | `{}` |
    | `APPROVED_RATE_LAST_30_DAYS` | 31 | `NUMBER` | The approval rate for the merchant's applications in the last 30 days. | The approval rate for the merchant's applications in the last 30 days. | `[]` | `{}` |
    | `DENIED_APPLICATION_COUNT_LAST_30_DAYS` | 32 | `NUMBER` | The total number of denied applications for the merchant in the last 30 days. | The total number of denied applications for the merchant in the last 30 days. | `[]` | `{}` |
    | `DENIAL_RATE_LAST_30_DAYS` | 33 | `NUMBER` | The denial rate for the merchant's applications in the last 30 days. | The denial rate for the merchant's applications in the last 30 days. | `[]` | `{}` |
    | `DAYS_SINCE_MOST_RECENT_APPLICATION` | 34 | `NUMBER` | The number of days since the merchant's most recent application. | The number of days since the merchant's most recent application. | `[]` | `{}` |
    | `APPLICATIONS_WITHOUT_TRANSACTIONS_LAST_30_DAYS` | 35 | `NUMBER` |  |  | `[]` | `{}` |
    | `APPLICATIONS_WITHOUT_TRANSACTIONS_RATE_LAST_30_DAYS` | 36 | `NUMBER` |  |  | `[]` | `{}` |
    | `SUPPORT_INBOUND_COUNT_LAST_30_DAYS` | 37 | `NUMBER` | The total number of inbound support requests from the merchant in the last 30 days. | The total number of inbound support requests from the merchant in the last 30 days. | `[]` | `{}` |
    | `CHERRY_OUTREACH_COUNT_LAST_30_DAYS` | 38 | `NUMBER` | The total number of Cherry outreach events for the merchant in the last 30 days. | The total number of Cherry outreach events for the merchant in the last 30 days. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt.py_script_postfix`
    *   `model.cherry_data_model.stg_churn`

---
