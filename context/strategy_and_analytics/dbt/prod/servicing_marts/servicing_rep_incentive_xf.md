## Model: `servicing_rep_incentive_xf`

`servicing_rep_incentive_xf`

*   **Unique ID:** `model.cherry_data_model.servicing_rep_incentive_xf`
*   **FQN:** `prod.servicing_marts.servicing_rep_incentive_xf`
*   **Description:** A model that calculates servicing representative incentives based on payment commitments and collections. This model enriches commitment data with detailed payment information from LoanPro, including past due amounts, late fees, and credit card fees to provide a comprehensive view of agent collection effectiveness. Used for tracking agent performance and calculating incentive compensation.

*   **Tags:** `['servicing_and_collections', 'collections_incentive_refresh']`
*   **Meta:** `{'owner': 'Collections Team', 'usage': 'Primary source for agent performance tracking and incentive calculations. Links agent commitments to actual payment outcomes and collection effectiveness. ', 'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}, 'deduplication': 'Records are deduplicated based on loan_id, past_due_amt_paid,  principal_balance_before_pmt, and pmt_apply_date, keeping the  earliest commitment if multiple exist', 'payment_matching': 'Payments are matched to commitments when either: 1. Payment date matches the first payment date for the commitment 2. Payment date matches the scheduled commitment date', 'incentive_calculation': 'This model is used to calculate agent incentives based on: 1. Successful commitment fulfillment 2. Past due amount collected 3. Late fee collection 4. Payment timing relative to commitment date'}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `LOAN_ID` | 1 | `NUMBER` | The unique identifier for the loan in the Cherry system | The unique identifier for the loan in the Cherry system | `[]` | `{}` |
    | `LOANPRO_LOAN_ID` | 2 | `NUMBER` |  |  | `[]` | `{}` |
    | `COMMITMENT_CREATED_AT_PT` | 3 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `COMMITMENT_CREATED_DATE` | 4 | `DATE` |  |  | `[]` | `{}` |
    | `SCHEDULED_DATE` | 5 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `SAME_DAY_COMMITMENT` | 6 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `FIRST_NAME` | 7 | `TEXT` |  |  | `[]` | `{}` |
    | `LAST_NAME` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `FULL_NAME` | 9 | `TEXT` | Full name of the agent who created the commitment and is eligible for incentives | Full name of the agent who created the commitment and is eligible for incentives | `[]` | `{}` |
    | `COMMITMENT_AMOUNT` | 10 | `FLOAT` | The amount the borrower committed to pay to the agent | The amount the borrower committed to pay to the agent | `[]` | `{}` |
    | `COMMITMENT_TYPE` | 11 | `TEXT` |  |  | `[]` | `{}` |
    | `TOTAL_PAYMENTS` | 12 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_PAYMENT_DATE` | 13 | `DATE` |  |  | `[]` | `{}` |
    | `AGENT_COLLECTED_PAYMENT` | 14 | `NUMBER` |  |  | `[]` | `{}` |
    | `PAYMENT_ID` | 15 | `NUMBER` |  |  | `[]` | `{}` |
    | `COMMITMENT_STATUS` | 16 | `TEXT` | Whether the commitment was successful (≥90% of committed amount paid) | Whether the commitment was successful (≥90% of committed amount paid) | `[]` | `{}` |
    | `LOANPRO_PMT_ID` | 17 | `NUMBER` | Unique identifier for the payment in LoanPro | Unique identifier for the payment in LoanPro | `[]` | `{}` |
    | `PMT_APPLY_DATE` | 18 | `DATE` | Date when the payment was applied in LoanPro | Date when the payment was applied in LoanPro | `[]` | `{}` |
    | `PMT_CREATED_TIMESTAMP` | 19 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `DPD_BEFORE_PMT` | 20 | `NUMBER` | Days Past Due before the payment was applied | Days Past Due before the payment was applied | `[]` | `{}` |
    | `DPD_AFTER_PMT` | 21 | `NUMBER` | Days Past Due after the payment was applied | Days Past Due after the payment was applied | `[]` | `{}` |
    | `PRINCIPAL_BALANCE_BEFORE_PMT` | 22 | `NUMBER` | Principal balance before payment application | Principal balance before payment application | `[]` | `{}` |
    | `PRINCIPAL_BALANCE_AFTER_PMT` | 23 | `NUMBER` | Principal balance after payment application | Principal balance after payment application | `[]` | `{}` |
    | `PMT_AMT` | 24 | `NUMBER` | Total payment amount | Total payment amount | `[]` | `{}` |
    | `PAYMENT_NUMBER` | 25 | `NUMBER` | Sequential number of the payment for this loan | Sequential number of the payment for this loan | `[]` | `{}` |
    | `PAST_DUE_AMT_PAID` | 26 | `NUMBER` | Amount applied to past due balance, calculated as: For non-charge-off recoveries:
  (amt_past_due_before - amt_past_due_after) + late_fees - credit_card_fees
For charge-off recoveries:
  entire payment amount
 | Amount applied to past due balance, calculated as: For non-charge-off recoveries:
  (amt_past_due_before - amt_past_due_after) + late_fees - credit_card_fees
For charge-off recoveries:
  entire payment amount
 | `[]` | `{}` |
    | `LATE_FEES` | 27 | `NUMBER` | Sum of late fees and NSF fees paid with this payment | Sum of late fees and NSF fees paid with this payment | `[]` | `{}` |
    | `IS_PAYOFF` | 28 | `BOOLEAN` | Boolean indicating if this payment paid off the loan | Boolean indicating if this payment paid off the loan | `[]` | `{}` |
    | `LAST_UPDATED_BY_PT` | 29 | `TIMESTAMP_LTZ` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.commitment_successes_xf`
    *   `model.cherry_data_model.int_cherry_and_loanpro_payments`
    *   `model.cherry_data_model.stg_active_loanpro_payments`
    *   `model.cherry_data_model.stg_loanpro_charges`

---
