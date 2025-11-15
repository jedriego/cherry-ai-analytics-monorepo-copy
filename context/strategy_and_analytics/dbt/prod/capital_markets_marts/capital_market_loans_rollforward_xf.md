## Model: `capital_market_loans_rollforward_xf`

`capital_market_loans_rollforward_xf`

*   **Unique ID:** `model.cherry_data_model.capital_market_loans_rollforward_xf`
*   **FQN:** `prod.capital_markets_marts.capital_market_loans_rollforward_xf`
*   **Description:** Daily capital markets loan rollforward table with balance calculations, ownership tracking,  and eligibility rules for various securitization programs (SEC24, SEC25, CRB, CITI). Consolidates loan origination data with daily activity and ownership changes.

*   **Tags:** `['capital_markets']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `REPORT_DATE` | 1 | `DATE` | Current date for this rollforward report | Current date for this rollforward report | `[]` | `{}` |
    | `ID` | 2 | `NUMBER` | Cherry loan identifier (primary key) | Cherry loan identifier (primary key) | `[]` | `{}` |
    | `DAYS_PAST_DUE` | 3 | `NUMBER` | Number of days past due on scheduled payments | Number of days past due on scheduled payments | `[]` | `{}` |
    | `LOAN_STATUS` | 4 | `TEXT` | Current loan status (OPEN, LATE, CLOSED, CHARGED_OFF, BANKRUPTCY, DEBT_SALE) | Current loan status (OPEN, LATE, CLOSED, CHARGED_OFF, BANKRUPTCY, DEBT_SALE) | `[]` | `{}` |
    | `LOAN_SUB_STATUS` | 5 | `TEXT` | Detailed loan sub-status | Detailed loan sub-status | `[]` | `{}` |
    | `VANTAGE_SCORE` | 6 | `FLOAT` | Borrower's Vantage credit score at origination | Borrower's Vantage credit score at origination | `[]` | `{}` |
    | `TERM` | 7 | `NUMBER` | Loan term in months | Loan term in months | `[]` | `{}` |
    | `REMAINING_TERM` | 8 | `NUMBER` | Remaining months until final scheduled payment | Remaining months until final scheduled payment | `[]` | `{}` |
    | `PRINCIPAL_BALANCE` | 9 | `FLOAT` | Current outstanding principal balance | Current outstanding principal balance | `[]` | `{}` |
    | `DOWN_PAYMENT_AMOUNT` | 10 | `FLOAT` | Down payment made at origination | Down payment made at origination | `[]` | `{}` |
    | `LOAN_AMOUNT` | 11 | `FLOAT` | Original loan amount at origination | Original loan amount at origination | `[]` | `{}` |
    | `DOWN_PAYMENT_PERCENTAGE` | 12 | `FLOAT` | Down payment as percentage of purchase amount | Down payment as percentage of purchase amount | `[]` | `{}` |
    | `APR` | 13 | `FLOAT` | Annual percentage rate | Annual percentage rate | `[]` | `{}` |
    | `PROJECTED_CLOSE_AT_ORIGINATION` | 14 | `DATE` |  |  | `[]` | `{}` |
    | `ID_MERCHANT` | 15 | `NUMBER` |  |  | `[]` | `{}` |
    | `MERCHANT_NAME` | 16 | `TEXT` |  |  | `[]` | `{}` |
    | `INCORPORATION_DATE` | 17 | `DATE` |  |  | `[]` | `{}` |
    | `MERCHANT_AGE_IN_MONTHS` | 18 | `TEXT` |  |  | `[]` | `{}` |
    | `MERCHANT_STATE` | 19 | `TEXT` |  |  | `[]` | `{}` |
    | `BORROWER_STATE` | 20 | `TEXT` |  |  | `[]` | `{}` |
    | `AUTO_PAY` | 21 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `FINAL_SCHEDULED_PAYMENT_DATE` | 22 | `DATE` |  |  | `[]` | `{}` |
    | `ORIGINATION_DATE` | 23 | `TIMESTAMP_NTZ` | Date loan was originated (Pacific Time) | Date loan was originated (Pacific Time) | `[]` | `{}` |
    | `MDR` | 24 | `FLOAT` | Merchant discount rate (merchant fees / purchase amount) | Merchant discount rate (merchant fees / purchase amount) | `[]` | `{}` |
    | `VERTICAL` | 25 | `TEXT` | Industry vertical (Dental, Medspa, Cosmetic Surgery, Veterinary, etc.) | Industry vertical (Dental, Medspa, Cosmetic Surgery, Veterinary, etc.) | `[]` | `{}` |
    | `NON_APPROVED_VERTICAL` | 26 | `NUMBER` |  |  | `[]` | `{}` |
    | `MERCHANT_GROUP` | 27 | `TEXT` |  |  | `[]` | `{}` |
    | `ELIGIBLE_MERCHANT` | 28 | `NUMBER` |  |  | `[]` | `{}` |
    | `DELINQUENT` | 29 | `NUMBER` | Whether loan is 30+ days past due (1/0) | Whether loan is 30+ days past due (1/0) | `[]` | `{}` |
    | `DEFAULTED` | 30 | `NUMBER` | Whether loan has been charged off (1/0) | Whether loan has been charged off (1/0) | `[]` | `{}` |
    | `MODIFIED` | 31 | `NUMBER` |  |  | `[]` | `{}` |
    | `FRAUDULENT` | 32 | `NUMBER` | Whether loan is flagged as fraudulent (1/0) | Whether loan is flagged as fraudulent (1/0) | `[]` | `{}` |
    | `BANKRUPTCY` | 33 | `NUMBER` | Whether borrower has filed bankruptcy (1/0) | Whether borrower has filed bankruptcy (1/0) | `[]` | `{}` |
    | `OTHER_CHARGEOFF` | 34 | `NUMBER` |  |  | `[]` | `{}` |
    | `MODIFIED_DATE` | 35 | `TEXT` |  |  | `[]` | `{}` |
    | `CO_DATE` | 36 | `DATE` |  |  | `[]` | `{}` |
    | `CO_AMOUNT` | 37 | `FLOAT` |  |  | `[]` | `{}` |
    | `RECOVERY_DATE` | 38 | `DATE` |  |  | `[]` | `{}` |
    | `RECOVERIES` | 39 | `FLOAT` |  |  | `[]` | `{}` |
    | `REPURCHASE_DATE` | 40 | `TEXT` |  |  | `[]` | `{}` |
    | `FORBEARANCE` | 41 | `NUMBER` | Whether loan is currently in forbearance (1/0) | Whether loan is currently in forbearance (1/0) | `[]` | `{}` |
    | `FORBEARANCE_DATE` | 42 | `DATE` |  |  | `[]` | `{}` |
    | `TOTAL_FORBEARANCE_DAYS` | 43 | `NUMBER` |  |  | `[]` | `{}` |
    | `INELIGIBLE_MODIFICATION` | 44 | `NUMBER` |  |  | `[]` | `{}` |
    | `IS_REFUNDED` | 45 | `BOOLEAN` | Whether loan has been refunded (true/false) | Whether loan has been refunded (true/false) | `[]` | `{}` |
    | `REFUND_TIMESTAMP_PT` | 46 | `DATE` |  |  | `[]` | `{}` |
    | `FINAL_PAYMENT_DATE` | 47 | `DATE` |  |  | `[]` | `{}` |
    | `LOAN_ORIGINATOR` | 48 | `TEXT` |  |  | `[]` | `{}` |
    | `CURRENT_OWNER` | 49 | `TEXT` | Current loan owner with pending owner overrides applied | Current loan owner with pending owner overrides applied | `[]` | `{}` |
    | `IS_RETAIL_INSTALLMENT_CONTRACT` | 50 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `REMAINING_INSTALLMENT_COUNT` | 51 | `NUMBER` |  |  | `[]` | `{}` |
    | `LEGAL_ACTION` | 52 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `CHERRY_AFFILIATE` | 53 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `SUCCESSFUL_PAYMENT_COUNT` | 54 | `NUMBER` | Total number of successful payments made | Total number of successful payments made | `[]` | `{}` |
    | `NEGATIVE_LEGAL_DEVELOPMENT` | 55 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `RISK_SCORE` | 56 | `FLOAT` |  |  | `[]` | `{}` |
    | `SSN` | 57 | `TEXT` |  |  | `[]` | `{}` |
    | `DEBT_TO_INCOME` | 58 | `FLOAT` |  |  | `[]` | `{}` |
    | `PROMO_USED` | 59 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ACCRUED_INTEREST` | 60 | `FLOAT` | Total accrued interest since last payment | Total accrued interest since last payment | `[]` | `{}` |
    | `SEC24_ELIGIBLE` | 61 | `NUMBER` | Eligibility for SEC24 securitization program (1/0) | Eligibility for SEC24 securitization program (1/0) | `[]` | `{}` |
    | `SEC25_ELIGIBLE` | 62 | `NUMBER` | Eligibility for SEC25 securitization program (1/0) | Eligibility for SEC25 securitization program (1/0) | `[]` | `{}` |
    | `CRB_ELIGIBLE` | 63 | `NUMBER` | Eligibility for CRB securitization program (1/0) | Eligibility for CRB securitization program (1/0) | `[]` | `{}` |
    | `CITI_ELIGIBLE` | 64 | `NUMBER` | Eligibility for CITI securitization program (1/0) | Eligibility for CITI securitization program (1/0) | `[]` | `{}` |
    | `MANUAL_EXCESS_ADJUSTMENT` | 65 | `NUMBER` |  |  | `[]` | `{}` |
    | `BEGINNING_PRINCIPAL_BALANCE` | 66 | `FLOAT` | Principal balance at start of day | Principal balance at start of day | `[]` | `{}` |
    | `PAYDOWNS_DAILY` | 67 | `FLOAT` | Principal payments received on report date | Principal payments received on report date | `[]` | `{}` |
    | `INTEREST_DAILY` | 68 | `FLOAT` | Interest collected on report date | Interest collected on report date | `[]` | `{}` |
    | `FEES_DAILY` | 69 | `FLOAT` | Fees collected on report date | Fees collected on report date | `[]` | `{}` |
    | `REFUNDS_DAILY` | 70 | `FLOAT` | Refunds issued on report date | Refunds issued on report date | `[]` | `{}` |
    | `CHARGE_OFFS_DAILY` | 71 | `FLOAT` | Charge-offs recorded on report date | Charge-offs recorded on report date | `[]` | `{}` |
    | `RECOVERIES_DAILY` | 72 | `FLOAT` | Recoveries collected on report date | Recoveries collected on report date | `[]` | `{}` |
    | `ENDING_PRINCIPAL_BALANCE` | 73 | `FLOAT` | Principal balance at end of day | Principal balance at end of day | `[]` | `{}` |
    | `OTHER_ADJ` | 74 | `FLOAT` | Other adjustments calculated as balance reconciliation | Other adjustments calculated as balance reconciliation | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.daily_loan_xf`
    *   `model.cherry_data_model.src_loan_schedule`
    *   `model.cherry_data_model.stg_capital_market_loan_activity`
    *   `model.cherry_data_model.stg_capital_market_loan_ownership`
    *   `model.cherry_data_model.stg_capital_market_loans_dim`
    *   `model.cherry_data_model.stg_forbearances`

---
