## Model: `propensity_to_pay_model_xf`

`propensity_to_pay_model_xf`

*   **Unique ID:** `model.cherry_data_model.propensity_to_pay_model_xf`
*   **FQN:** `prod.servicing_marts.propensity_to_pay_model_xf`
*   **Description:** - This is the output feature set for version 1 of the Recoveries Propensity to Pay Model, which predicts the likelihood of a customer to: - 1. Make a promise to pay - 2. Fulfill above promise to pay on the date promise was made (or backdated in the case of multiple payments or payment plans) - This model uses the features xf set during model training to create a risk score from 0 to 1 on likelihood of propensity to pay

*   **Tags:** `['servicing_and_collections', 'recoveries', 'collections', 'machine learning', 'predictive analytics']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `APPLICATION_ID` | 1 | `NUMBER` |  |  | `[]` | `{}` |
    | `LOAN_ID` | 2 | `NUMBER` | Unique identifier for funded patient loans.
 | Unique identifier for funded patient loans.
 | `[]` | `{}` |
    | `BORROWER_ID` | 3 | `NUMBER` | Unique identifier for borrowers, does not need to be unique as a borrower may have multiple applications and loans.
 | Unique identifier for borrowers, does not need to be unique as a borrower may have multiple applications and loans.
 | `[]` | `{}` |
    | `TOTAL_AMOUNT` | 4 | `FLOAT` |  |  | `[]` | `{}` |
    | `LOAN_TERM` | 5 | `NUMBER` |  |  | `[]` | `{}` |
    | `APR_DECIMAL` | 6 | `FLOAT` |  |  | `[]` | `{}` |
    | `VANTAGE_SCORE` | 7 | `FLOAT` |  |  | `[]` | `{}` |
    | `RPC_PHONE_CONTACTS_COLLECTIONS` | 8 | `NUMBER` |  |  | `[]` | `{}` |
    | `TOTAL_PHONE_CONTACTS_COLLECTIONS` | 9 | `NUMBER` |  |  | `[]` | `{}` |
    | `FUNDING_DATE_TO_CHARGE_OFF_DAYS` | 10 | `NUMBER` |  |  | `[]` | `{}` |
    | `CHARGE_OFF_AMOUNT` | 11 | `NUMBER` |  |  | `[]` | `{}` |
    | `PROP_OF_TOTAL_AMOUNT_CHARGED_OFF` | 12 | `FLOAT` |  |  | `[]` | `{}` |
    | `FPD_IND` | 13 | `FLOAT` |  |  | `[]` | `{}` |
    | `STRAIGHT_ROLLER_IND` | 14 | `NUMBER` |  |  | `[]` | `{}` |
    | `PHONE_MATCH_SCORE` | 15 | `FLOAT` |  |  | `[]` | `{}` |
    | `RISK_STATUS_FROZEN` | 16 | `NUMBER` |  |  | `[]` | `{}` |
    | `RISK_STATUS_INITIALIZED` | 17 | `NUMBER` |  |  | `[]` | `{}` |
    | `RISK_STATUS_KYC_REVIEW` | 18 | `NUMBER` |  |  | `[]` | `{}` |
    | `RISK_STATUS_IV_REQUIRED` | 19 | `NUMBER` |  |  | `[]` | `{}` |
    | `RISK_STATUS_IV_REVIEW` | 20 | `NUMBER` |  |  | `[]` | `{}` |
    | `KYC_STATUS_SSN_CONFLICT` | 21 | `NUMBER` |  |  | `[]` | `{}` |
    | `KYC_STATUS_ID_REVIEW` | 22 | `NUMBER` |  |  | `[]` | `{}` |
    | `KYC_STATUS_SSN_REQUIRED_1` | 23 | `NUMBER` |  |  | `[]` | `{}` |
    | `KYC_STATUS_SSN_REQUIRED_2` | 24 | `NUMBER` |  |  | `[]` | `{}` |
    | `KYC_STATUS_FAILED` | 25 | `NUMBER` |  |  | `[]` | `{}` |
    | `KYC_STATUS_MANUAL_REVIEW` | 26 | `NUMBER` |  |  | `[]` | `{}` |
    | `KYC_STATUS_ADDRESS_VERIFICATION` | 27 | `NUMBER` |  |  | `[]` | `{}` |
    | `KYC_STATUS_CREDIT_FROZEN` | 28 | `NUMBER` |  |  | `[]` | `{}` |
    | `KYC_STATUS_FRAUD_REVIEW` | 29 | `NUMBER` |  |  | `[]` | `{}` |
    | `KYC_STATUS_COMPLIANCE_REVIEW` | 30 | `NUMBER` |  |  | `[]` | `{}` |
    | `PATIENT_PORTAL_LOGIN_ATTEMPTS` | 31 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRE_CHARGE_OFF_DPD_INSTANCES` | 32 | `NUMBER` |  |  | `[]` | `{}` |
    | `COMPLAINT_CNT` | 33 | `NUMBER` |  |  | `[]` | `{}` |
    | `FORBEARANCE_CNT` | 34 | `NUMBER` |  |  | `[]` | `{}` |
    | `UNIQUE_PRE_CHARGEOFF_PAYMENTS` | 35 | `NUMBER` |  |  | `[]` | `{}` |
    | `TOTAL_PRE_CHARGEOFF_PAYMENT_AMOUNT` | 36 | `FLOAT` |  |  | `[]` | `{}` |
    | `UNIQUE_PRE_CHARGEOFF_PAYMENT_FAILURES` | 37 | `NUMBER` |  |  | `[]` | `{}` |
    | `TOTAL_PRE_CHARGEOFF_PAYMENT_FAILURE_AMOUNT` | 38 | `FLOAT` |  |  | `[]` | `{}` |
    | `IS_AUTOPAY` | 39 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_FRAUD` | 40 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_FINANCIAL_HARDSHIP` | 41 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_DO_NOT_CALL` | 42 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `PROJECTED_INCOME_BUCKET` | 43 | `NUMBER` |  |  | `[]` | `{}` |
    | `AVERAGE_DAILY_BALANCE_BUCKET` | 44 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRACTICE_INDUSTRY_SEGMENT_CORE_AESTHETICS` | 45 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `PRACTICE_INDUSTRY_SEGMENT_DENTAL` | 46 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `PRACTICE_INDUSTRY_SEGMENT_OTHER_AND_PART_TIME` | 47 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `PRACTICE_INDUSTRY_SEGMENT_PLASTIC_AND_COSMETIC_SURGERY` | 48 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `PRACTICE_PRICING_TIER_BRONZE` | 49 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `PRACTICE_PRICING_TIER_SILVER` | 50 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `PRACTICE_PRICING_TIER_GOLD` | 51 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `BROKEN_COMMITMENT_COLLECTIONS` | 52 | `NUMBER` |  |  | `[]` | `{}` |
    | `SUCCESSFUL_COMMITMENT_COLLECTIONS` | 53 | `NUMBER` |  |  | `[]` | `{}` |
    | `PROPENSITY_TO_PAY_SCORE` | 54 | `FLOAT` | Output propensity to pay score used by XGBoost algorithm to denote a charged-off loan's likelihood of repayment | Output propensity to pay score used by XGBoost algorithm to denote a charged-off loan's likelihood of repayment | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt.py_script_postfix`
    *   `model.cherry_data_model.propensity_to_pay_model_features_xf`

---
