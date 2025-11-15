## Model: `commitment_successes_xf`

`commitment_successes_xf`

*   **Unique ID:** `model.cherry_data_model.commitment_successes_xf`
*   **FQN:** `prod.servicing_marts.commitment_successes_xf`
*   **Description:** A model that tracks and evaluates the success of payment commitments made by agents. This includes standard commitments, same-day virtual terminal payments, and flexible payments. A commitment is considered successful if the total payments received are at least 90% of the committed amount within the commitment window (commitment date to scheduled date + 1 day).

*   **Tags:** `['servicing_and_collections', 'collections_incentive_refresh']`
*   **Meta:** `{'owner': 'Collections Team', 'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}, 'deduplication': 'Commitments are deduplicated based on loan_id, scheduled_date, and commitment_amount, keeping the earliest commitment if multiple exist with the same criteria ', 'payment_sources': ['Standard commitments from src_commitments', 'Same-day virtual terminal payments', 'Flexible payments from src_flexible_payments'], 'success_criteria': 'A commitment is considered successful if total payments received are at least 90% of the committed amount within the payment window (commitment date to scheduled date + 1 day)'}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `LOAN_ID` | 1 | `NUMBER` | The unique identifier for the loan in the Cherry system | The unique identifier for the loan in the Cherry system | `[]` | `{}` |
    | `LOANPRO_LOAN_ID` | 2 | `NUMBER` | The unique identifier for the loan in the LoanPro system | The unique identifier for the loan in the LoanPro system | `[]` | `{}` |
    | `COMMITMENT_CREATED_AT_PT` | 3 | `TIMESTAMP_NTZ` | Timestamp when the commitment was created (Pacific Time) | Timestamp when the commitment was created (Pacific Time) | `[]` | `{}` |
    | `COMMITMENT_CREATED_DATE` | 4 | `DATE` | Date when the commitment was created | Date when the commitment was created | `[]` | `{}` |
    | `SCHEDULED_DATE` | 5 | `TIMESTAMP_NTZ` | The date when the payment was scheduled to be made | The date when the payment was scheduled to be made | `[]` | `{}` |
    | `SAME_DAY_COMMITMENT` | 6 | `BOOLEAN` | Boolean flag indicating if the commitment was scheduled for the same day it was created | Boolean flag indicating if the commitment was scheduled for the same day it was created | `[]` | `{}` |
    | `FIRST_NAME` | 7 | `TEXT` | First name of the agent who created the commitment | First name of the agent who created the commitment | `[]` | `{}` |
    | `LAST_NAME` | 8 | `TEXT` | Last name of the agent who created the commitment | Last name of the agent who created the commitment | `[]` | `{}` |
    | `FULL_NAME` | 9 | `TEXT` | Full name of the agent who created the commitment (first_name + last_name) | Full name of the agent who created the commitment (first_name + last_name) | `[]` | `{}` |
    | `COMMITMENT_AMOUNT` | 10 | `FLOAT` | The amount the borrower committed to pay | The amount the borrower committed to pay | `[]` | `{}` |
    | `COMMITMENT_TYPE` | 11 | `TEXT` | Type of commitment: - Standard commitment - VIRTUAL TERMINAL (same-day payments) - FLEXIBLE PAYMENT
 | Type of commitment: - Standard commitment - VIRTUAL TERMINAL (same-day payments) - FLEXIBLE PAYMENT
 | `[]` | `{}` |
    | `TOTAL_PAYMENTS` | 12 | `FLOAT` | Sum of all payments made between commitment creation date and scheduled date + 1 day
 | Sum of all payments made between commitment creation date and scheduled date + 1 day
 | `[]` | `{}` |
    | `FIRST_PAYMENT_DATE` | 13 | `DATE` | Date of the first payment made toward this commitment | Date of the first payment made toward this commitment | `[]` | `{}` |
    | `AGENT_COLLECTED_PAYMENT` | 14 | `NUMBER` | Boolean flag indicating if any of the payments were agent-initiated (OUT_OF_SYNC or COMMITMENT types) | Boolean flag indicating if any of the payments were agent-initiated (OUT_OF_SYNC or COMMITMENT types) | `[]` | `{}` |
    | `PAYMENT_ID` | 15 | `NUMBER` | ID of the last payment made toward this commitment | ID of the last payment made toward this commitment | `[]` | `{}` |
    | `COMMITMENT_STATUS` | 16 | `TEXT` | Success/Failure indicator based on whether total_payments >= 90% of commitment_amount Success: total_payments >= (commitment_amount * 0.9) Failure: total_payments < (commitment_amount * 0.9)
 | Success/Failure indicator based on whether total_payments >= 90% of commitment_amount Success: total_payments >= (commitment_amount * 0.9) Failure: total_payments < (commitment_amount * 0.9)
 | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.int_all_commitments`
    *   `model.cherry_data_model.int_payment_commitment_matching`

---
