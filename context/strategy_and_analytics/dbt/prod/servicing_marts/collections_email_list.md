## Model: `collections_email_list`

`collections_email_list`

*   **Unique ID:** `model.cherry_data_model.collections_email_list`
*   **FQN:** `prod.servicing_marts.collections_email_list`
*   **Description:** This model generates an email list for the collections and recovery teams to follow. It includes email tags relevant to experiments for email, as well as metadata surrounding the borrower and loan.
*   **Tags:** `['servicing_and_collections', 'daily']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `EMAIL_TAG` | 1 | `TEXT` | Label or category indicating which email campaign or template a borrower belongs to
 | Label or category indicating which email campaign or template a borrower belongs to
 | `[]` | `{}` |
    | `TEST_GROUP` | 2 | `TEXT` | Experimental or control group assignment used for A/B testing and campaign segmentation
 | Experimental or control group assignment used for A/B testing and campaign segmentation
 | `[]` | `{}` |
    | `SEND_DAY` | 3 | `TEXT` | Assigned weekday for sending borrower communications based on email_tag grouping logic
 | Assigned weekday for sending borrower communications based on email_tag grouping logic
 | `[]` | `{}` |
    | `LOAN_ID` | 4 | `NUMBER` | Unique identifier for the borrower’s loan within the servicing system
 | Unique identifier for the borrower’s loan within the servicing system
 | `[]` | `{}` |
    | `BORROWER_ID` | 5 | `NUMBER` | Unique identifier for the borrower across all loans
 | Unique identifier for the borrower across all loans
 | `[]` | `{}` |
    | `EMAIL_ON_FILE` | 6 | `TEXT` | Borrower’s valid email address on record; null if no email is available
 | Borrower’s valid email address on record; null if no email is available
 | `[]` | `{}` |
    | `SENDER_NAME` | 7 | `TEXT` |  | Display name used as the sender in outgoing borrower communications
 | `[]` | `{}` |
    | `FIRST_NAME` | 8 | `TEXT` | Borrower’s first name used for personalization in communications
 | Borrower’s first name used for personalization in communications
 | `[]` | `{}` |
    | `CONTRACT_ID` | 9 | `TEXT` | Contract identifier associated with the borrower’s loan agreement
 | Contract identifier associated with the borrower’s loan agreement
 | `[]` | `{}` |
    | `REMAINING_INSTALLMENTS` | 10 | `NUMBER` | Number of scheduled installments remaining until loan maturity
 | Number of scheduled installments remaining until loan maturity
 | `[]` | `{}` |
    | `MONTHLYPAYMENT` | 11 | `FLOAT` | Regular monthly payment amount due on the borrower’s loan
 | Regular monthly payment amount due on the borrower’s loan
 | `[]` | `{}` |
    | `DISCOUNTMONTHLYPAYMENT` | 12 | `FLOAT` | Discounted monthly payment amount offered under a settlement or hardship plan
 | Discounted monthly payment amount offered under a settlement or hardship plan
 | `[]` | `{}` |
    | `CO_DATE` | 13 | `DATE` | Charge-off date of the loan, indicating when it was written off
 | Charge-off date of the loan, indicating when it was written off
 | `[]` | `{}` |
    | `NET_CHARGE_OFF` | 14 | `FLOAT` | Net dollar amount charged off
 | Net dollar amount charged off
 | `[]` | `{}` |
    | `SETTLEMENT_DISCOUNT` | 15 | `NUMBER` | Discount offered to settle the outstanding balance
 | Discount offered to settle the outstanding balance
 | `[]` | `{}` |
    | `SETTLEMENT_AMOUNT` | 16 | `FLOAT` | Total amount required from borrower to complete settlement
 | Total amount required from borrower to complete settlement
 | `[]` | `{}` |
    | `SETTLEMENT_MAX_TERM` | 17 | `NUMBER` | Maximum number of months permitted for the settlement payment plan
 | Maximum number of months permitted for the settlement payment plan
 | `[]` | `{}` |
    | `SETTLEMENT_MONTHLY_PAYMENT` | 18 | `FLOAT` | Monthly payment amount under the settlement agreement
 | Monthly payment amount under the settlement agreement
 | `[]` | `{}` |
    | `NEXT_DUE_DATE` | 19 | `DATE` | Date of the borrower’s next scheduled payment due
 | Date of the borrower’s next scheduled payment due
 | `[]` | `{}` |
    | `DAYS_SINCE_CO` | 20 | `NUMBER` | Number of days elapsed since loan charge-off date
 | Number of days elapsed since loan charge-off date
 | `[]` | `{}` |
    | `AMOUNTDUE` | 21 | `FLOAT` | Current payment amount due from the borrower (alias for amount_due)
 | Current payment amount due from the borrower (alias for amount_due)
 | `[]` | `{}` |
    | `AMT_DUE_INC_FEES` | 22 | `FLOAT` | Total amount due including late fees and other charges
 | Total amount due including late fees and other charges
 | `[]` | `{}` |
    | `CURRENTFEESACCRUED` | 23 | `FLOAT` | Accumulated unpaid fees currently applied to the loan
 | Accumulated unpaid fees currently applied to the loan
 | `[]` | `{}` |
    | `STATE_CODE` | 24 | `TEXT` | Two-letter state abbreviation of borrower’s residence or loan origination
 | Two-letter state abbreviation of borrower’s residence or loan origination
 | `[]` | `{}` |
    | `DAYSPASTDUE` | 25 | `NUMBER` | Number of days borrower is delinquent on latest due payment (alias for dpd) | Number of days borrower is delinquent on latest due payment (alias for dpd) | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.applications_loans_xf`
    *   `model.cherry_data_model.collections_compliance_list`
    *   `model.cherry_data_model.daily_loan_xf`
    *   `model.cherry_data_model.int_funded_information_pt`
    *   `model.cherry_data_model.int_post_chargeoff_email_list`
    *   `model.cherry_data_model.int_pre_chargeoff_email_list`
    *   `model.cherry_data_model.src_borrower_segmentation`
    *   `model.cherry_data_model.src_borrowers`
    *   `model.cherry_data_model.src_loan_offers`
    *   `model.cherry_data_model.src_loan_plans`
    *   `model.cherry_data_model.src_loan_schedule`
    *   `model.cherry_data_model.src_loanpro_chargeoff_transactions`
    *   `model.cherry_data_model.src_segments`

---
