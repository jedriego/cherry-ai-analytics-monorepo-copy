## Model: `collections_approved_payments_xf`

`collections_approved_payments_xf`

*   **Unique ID:** `model.cherry_data_model.collections_approved_payments_xf`
*   **FQN:** `prod.servicing_marts.collections_approved_payments_xf`
*   **Description:** This model tracks all approved collections payments with enhanced DPD (Days Past Due) tracking.
It consolidates payments from multiple channels (agent-led, self-service, AI, etc.) and enriches
them with delinquency status at the time of payment. Includes special handling for charged-off
accounts where DPD is automatically set to 120 days.

Key features:
- Only includes approved payments on past due or charged-off accounts
- Tracks DPD status at payment time using multiple data sources
- Categorizes payments into standard delinquency buckets (Current, Late 1-4, Charge-off)
- Maintains payment channel attribution for collections performance analysis

*   **Tags:** `['servicing_and_collections', 'servicing', 'collections', 'payments']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `PAYMENT_CHANNEL` | 1 | `TEXT` | Channel through which the payment was collected
Values: AGENT_LED_SAME_DAY, AGENT_LED_COMMITMENT, SELF_SERVICE, LOCKBOX, PAYBOT, INSTALLMENT, 
FLEXIBLE_PAYMENT, SELF_SERVICE_COMMITMENT, CUSTOMER_INITIATED_OUT_OF_SYNC, AI, OTHER
 | Channel through which the payment was collected
Values: AGENT_LED_SAME_DAY, AGENT_LED_COMMITMENT, SELF_SERVICE, LOCKBOX, PAYBOT, INSTALLMENT, 
FLEXIBLE_PAYMENT, SELF_SERVICE_COMMITMENT, CUSTOMER_INITIATED_OUT_OF_SYNC, AI, OTHER
 | `[]` | `{}` |
    | `AGENT_NAME` | 2 | `TEXT` | Name of the collections agent who collected the payment (NULL for non-agent channels) | Name of the collections agent who collected the payment (NULL for non-agent channels) | `[]` | `{}` |
    | `PAYMENT_DATE` | 3 | `DATE` | Date the payment was applied to the account | Date the payment was applied to the account | `[]` | `{}` |
    | `LOAN_ID` | 4 | `NUMBER` | Cherry loan identifier | Cherry loan identifier | `[]` | `{}` |
    | `PAYMENT_ID` | 5 | `NUMBER` | Cherry payment identifier (Note: may have duplicates due to payment channel attribution) | Cherry payment identifier (Note: may have duplicates due to payment channel attribution) | `[]` | `{}` |
    | `PAYMENT_AMOUNT` | 6 | `FLOAT` | Amount of the payment collected | Amount of the payment collected | `[]` | `{}` |
    | `LOANPRO_LOAN_ID` | 7 | `NUMBER` | LoanPro loan identifier for joining with servicing data | LoanPro loan identifier for joining with servicing data | `[]` | `{}` |
    | `LOANPRO_PAYMENT_ID` | 8 | `NUMBER` | LoanPro payment identifier | LoanPro payment identifier | `[]` | `{}` |
    | `DPD_BEFORE_PAYMENT` | 9 | `NUMBER` | Days past due before the payment was made (from int_cherry_and_loanpro_payments) | Days past due before the payment was made (from int_cherry_and_loanpro_payments) | `[]` | `{}` |
    | `DPD_DAY_BEFORE` | 10 | `NUMBER` | Days past due on the day before payment (from daily_loan_xf) | Days past due on the day before payment (from daily_loan_xf) | `[]` | `{}` |
    | `INFERRED_DPD_AT_PAYMENT` | 11 | `NUMBER` | Inferred/calculated days past due at the time of payment using fallback logic
Logic:
- 120 if loan was charged off before payment date
- DPD_BEFORE_PAYMENT if available (most accurate from LoanPro)
- DPD_DAY_BEFORE if > 0 (fallback from daily snapshot)
- 120 if loan shows charge-off balance but 0 DPD
- 0 otherwise
 | Inferred/calculated days past due at the time of payment using fallback logic
Logic:
- 120 if loan was charged off before payment date
- DPD_BEFORE_PAYMENT if available (most accurate from LoanPro)
- DPD_DAY_BEFORE if > 0 (fallback from daily snapshot)
- 120 if loan shows charge-off balance but 0 DPD
- 0 otherwise
 | `[]` | `{}` |
    | `DPD_AFTER_PAYMENT` | 12 | `NUMBER` | Days past due after the payment was applied (from int_cherry_and_loanpro_payments)
Shows the effectiveness of the payment in reducing delinquency
 | Days past due after the payment was applied (from int_cherry_and_loanpro_payments)
Shows the effectiveness of the payment in reducing delinquency
 | `[]` | `{}` |
    | `DPD_BUCKET` | 13 | `TEXT` | Delinquency bucket classification:
- Current: 0 DPD
- Late 1: 1-29 DPD
- Late 30: 30-59 DPD
- Late 60: 60-89 DPD
- Late 90: 90-119 DPD
- Charged-off: 120+ DPD or charged-off loans
 | Delinquency bucket classification:
- Current: 0 DPD
- Late 1: 1-29 DPD
- Late 30: 30-59 DPD
- Late 60: 60-89 DPD
- Late 90: 90-119 DPD
- Charged-off: 120+ DPD or charged-off loans
 | `[]` | `{}` |
    | `CHARGE_OFF_DATE` | 14 | `DATE` | Date the loan was charged off (if applicable) | Date the loan was charged off (if applicable) | `[]` | `{}` |
    | `IS_CHARGED_OFF` | 15 | `BOOLEAN` | Boolean flag indicating if the loan was charged off at payment time | Boolean flag indicating if the loan was charged off at payment time | `[]` | `{}` |
    | `CHARGE_OFF_BALANCE` | 16 | `NUMBER` | Charge-off balance from daily_loan_xf | Charge-off balance from daily_loan_xf | `[]` | `{}` |
    | `DAYS_SINCE_CHARGE_OFF` | 17 | `NUMBER` | Number of days between charge-off and payment (NULL if not charged off) | Number of days between charge-off and payment (NULL if not charged off) | `[]` | `{}` |
    | `PRINCIPAL_BALANCE_DAY_BEFORE` | 18 | `NUMBER` | Principal balance on the day before payment | Principal balance on the day before payment | `[]` | `{}` |
    | `DELINQUENCY_BUCKET_DAY_BEFORE` | 19 | `NUMBER` | Delinquency bucket from daily_loan_xf on the day before payment | Delinquency bucket from daily_loan_xf on the day before payment | `[]` | `{}` |
    | `PAYMENT_TYPE` | 20 | `TEXT` | Type of payment (SELF, MANUAL, INSTALLMENT, etc.) | Type of payment (SELF, MANUAL, INSTALLMENT, etc.) | `[]` | `{}` |
    | `PAYMENT_METHOD_TYPE` | 21 | `TEXT` | Payment method used (CHECK, CARD, ACH, etc.) | Payment method used (CHECK, CARD, ACH, etc.) | `[]` | `{}` |
    | `PAYMENT_STATUS` | 22 | `TEXT` | Status of the payment (always APPROVED in this model) | Status of the payment (always APPROVED in this model) | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.daily_loan_xf`
    *   `model.cherry_data_model.int_cherry_and_loanpro_payments`
    *   `model.cherry_data_model.int_funded_information_pt`
    *   `model.cherry_data_model.int_ivr_payment_collections`
    *   `model.cherry_data_model.servicing_rep_incentive_xf`
    *   `model.cherry_data_model.src_loanpro_chargeoff_transactions`
    *   `model.cherry_data_model.src_pay_by_text_bot_messages_and_payments`
    *   `model.cherry_data_model.stg_joined_cherry_payments_and_transactions`
    *   `seed.cherry_data_model.ops_user_teams`

---
