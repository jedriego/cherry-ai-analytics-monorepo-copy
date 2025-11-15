## Model: `failed_refunds_xf`

`failed_refunds_xf`

*   **Unique ID:** `model.cherry_data_model.failed_refunds_xf`
*   **FQN:** `prod.servicing_marts.failed_refunds_xf`
*   **Description:** Failed refunds automatically go through Jira. This table is related to the status and outcome of the failed refunds.

*   **Tags:** `['servicing_and_collections']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `JIRA_ID` | 1 | `NUMBER` | The unique identifier of the Jira issue | The unique identifier of the Jira issue | `[]` | `{}` |
    | `ASSIGNEE_ID` | 2 | `TEXT` | ID for the Jira user assigned to the ticket | ID for the Jira user assigned to the ticket | `[]` | `{}` |
    | `ASSIGNEE_USER_NAME` | 3 | `TEXT` | User name associated with the Jira user assigned to the ticket | User name associated with the Jira user assigned to the ticket | `[]` | `{}` |
    | `RECEIVABLE_INDICATOR` | 4 | `TEXT` | A categorical variable, either of Refund Recovered or Practice Receivable. If refund is not resolved, then consider refund recovered, else practice receivable.
 | A categorical variable, either of Refund Recovered or Practice Receivable. If refund is not resolved, then consider refund recovered, else practice receivable.
 | `[]` | `{}` |
    | `REFUND_FAILED_AT` | 5 | `TIMESTAMP_NTZ` | Time at which refund failed at, PT | Time at which refund failed at, PT | `[]` | `{}` |
    | `REFUND_ATTEMPTED_AT` | 6 | `TIMESTAMP_NTZ` | Time at which refund attempted at, PT | Time at which refund attempted at, PT | `[]` | `{}` |
    | `REFUND_RECOVERED_AT` | 7 | `TIMESTAMP_TZ` | Time at which refund was recovered at, PT. NULL if it has yet to be recovered. | Time at which refund was recovered at, PT. NULL if it has yet to be recovered. | `[]` | `{}` |
    | `DAYS_SINCE_FAIL` | 8 | `NUMBER` | Days it took to resolve the issue. If issue is yet to be resolved, number of days since it has failed.
 | Days it took to resolve the issue. If issue is yet to be resolved, number of days since it has failed.
 | `[]` | `{}` |
    | `CONTRACT_ID` | 9 | `TEXT` | Unique ID of contract | Unique ID of contract | `[]` | `{}` |
    | `LOAN_ID` | 10 | `NUMBER` | Primary Key. The unique ID per loan | Primary Key. The unique ID per loan | `[]` | `{}` |
    | `MERCHANT_ID` | 11 | `NUMBER` | The unique identifier for every merchant | The unique identifier for every merchant | `[]` | `{}` |
    | `MERCHANT_NAME` | 12 | `TEXT` | Name of the merchant | Name of the merchant | `[]` | `{}` |
    | `REFUND_AMOUNT` | 13 | `FLOAT` | Amount refunded in USD | Amount refunded in USD | `[]` | `{}` |
    | `MERCHANT_FEE` | 14 | `FLOAT` | Merchant fee in USD | Merchant fee in USD | `[]` | `{}` |
    | `TRANSACTION_AMOUNT` | 15 | `FLOAT` | Amount transacted in USD | Amount transacted in USD | `[]` | `{}` |
    | `FAILURE_REASON` | 16 | `TEXT` | Funding failure reason | Funding failure reason | `[]` | `{}` |
    | `STATUS` | 17 | `TEXT` | Status of the fund | Status of the fund | `[]` | `{}` |
    | `ACCOUNT_LAST_4` | 18 | `TEXT` | Last 4 digits of the account number | Last 4 digits of the account number | `[]` | `{}` |
    | `ACTIVE_FLAG` | 19 | `TEXT` | Whether or not the organization is active Accepted values = ['Active', 'Inactive']
 | Whether or not the organization is active Accepted values = ['Active', 'Inactive']
 | `[]` | `{}` |
    | `PROCESSED_PATIENT_CREDIT_FLAG` | 20 | `TEXT` | Whether the credit was properly processed Accepted values = ['Successful processed credit', 'No processed credit']
 | Whether the credit was properly processed Accepted values = ['Successful processed credit', 'No processed credit']
 | `[]` | `{}` |
    | `AUTOFUNDING` | 21 | `TEXT` | Whether or not autofunding is on or off Accepted values = ['ON', 'OFF']
 | Whether or not autofunding is on or off Accepted values = ['ON', 'OFF']
 | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.int_failed_refund_events`
    *   `model.cherry_data_model.int_funded_information_pt`
    *   `model.cherry_data_model.src_all_practice_fraud_loans`
    *   `model.cherry_data_model.src_cherry_loans`
    *   `model.cherry_data_model.src_cherry_merchant_funds`
    *   `model.cherry_data_model.src_loan_fund`
    *   `model.cherry_data_model.src_loan_tx`
    *   `model.cherry_data_model.src_merchant_features`
    *   `model.cherry_data_model.stg_merchants`

---
