## Model: `scratchfi_loan_tape_xf_archive`

`scratchfi_loan_tape_xf_archive`

*   **Unique ID:** `model.cherry_data_model.scratchfi_loan_tape_xf_archive`
*   **FQN:** `prod.archive.scratchfi_loan_tape_xf_archive`
*   **Description:** This model serves as the loan tape for Scratchfi the backup servicer for Cherry. It is delivered to their SFTP each day so that they have an up to date record of the *status* of each Cherry contract that has been boarded with them. This information includes the payment and delinquency statuses of each account.

*   **Tags:** `['archive', 'partners', 'servicing']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `ORIGINATOR_LOAN_ID` | 1 | `TEXT` | The auto-generated *"friendly"* name for a borrower's Cherry loan. It has been generated in
different ways over time, but generally has included a short code to identify the merchant or
organization that is was originated under as well as the integer loan ID.


This is the ID number for the loan that the borrower is familiar with as it is presented to them in
communications and within their portal. | The auto-generated *"friendly"* name for a borrower's Cherry loan. It has been generated in
different ways over time, but generally has included a short code to identify the merchant or
organization that is was originated under as well as the integer loan ID.


This is the ID number for the loan that the borrower is familiar with as it is presented to them in
communications and within their portal. | `[]` | `{}` |
    | `BORROWER_ID` | 2 | `NUMBER` | The auto-increment ID for the borrower within Cherry's systems. Each borrower should have only a
single borrower ID.

The controls for ensuring that the same person does not have *multiple* borrower IDs within Cherry
is a uniqueness constraint on the SSN and the phone number. These are not enforced directly on the
borrower table, but via the KYC (Know Your Customer) workflow and rule engine. | The auto-increment ID for the borrower within Cherry's systems. Each borrower should have only a
single borrower ID.

The controls for ensuring that the same person does not have *multiple* borrower IDs within Cherry
is a uniqueness constraint on the SSN and the phone number. These are not enforced directly on the
borrower table, but via the KYC (Know Your Customer) workflow and rule engine. | `[]` | `{}` |
    | `REPORT_DATE` | 3 | `DATE` |  |  | `[]` | `{}` |
    | `CREDITOR_NAME` | 4 | `TEXT` |  |  | `[]` | `{}` |
    | `LOAN_DISPLAY_NAME` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `ANNUAL_INTEREST_RATE` | 6 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_FULL_REPAYMENT_DATE` | 7 | `DATE` |  |  | `[]` | `{}` |
    | `FIRST_INSTALLMENT_DUE_DATE` | 8 | `DATE` |  |  | `[]` | `{}` |
    | `LOAN_STATUS` | 9 | `TEXT` |  |  | `[]` | `{}` |
    | `CURRENT_INSTALLMENT_DUE_DATE` | 10 | `DATE` |  |  | `[]` | `{}` |
    | `NEXT_INSTALLMENT_DUE_DATE` | 11 | `DATE` |  |  | `[]` | `{}` |
    | `DAYS_DELINQUENT` | 12 | `NUMBER` |  |  | `[]` | `{}` |
    | `INSTALLMENT_PERIODS_REMAINING` | 13 | `NUMBER` |  |  | `[]` | `{}` |
    | `REPAYMENT_POLICY` | 14 | `TEXT` |  |  | `[]` | `{}` |
    | `REPAYMENT_STATUS` | 15 | `TEXT` |  |  | `[]` | `{}` |
    | `ACOMMODATION_START_DATE` | 16 | `DATE` |  |  | `[]` | `{}` |
    | `ACCOMMODATION_REPAYMENT_START_DATE` | 17 | `DATE` |  |  | `[]` | `{}` |
    | `ACOMMODATION_END_DATE` | 18 | `DATE` | When an acommodation for non-payment on a loan ends | When an acommodation for non-payment on a loan ends | `[]` | `{}` |
    | `IS_AUTOPAY_ON` | 19 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ORIGINATION_DATE` | 20 | `DATE` |  |  | `[]` | `{}` |
    | `INTEREST_ACCRUAL_START_DATE` | 21 | `DATE` |  |  | `[]` | `{}` |
    | `DISBURSEMENT_DATE` | 22 | `DATE` |  |  | `[]` | `{}` |
    | `PAID_OFF_DATE` | 23 | `DATE` |  |  | `[]` | `{}` |
    | `MATURITY_DATE` | 24 | `DATE` |  |  | `[]` | `{}` |
    | `CHARGE_OFF_DATE` | 25 | `DATE` |  |  | `[]` | `{}` |
    | `SOLD_DATE` | 26 | `TEXT` |  |  | `[]` | `{}` |
    | `FIRST_DELINQUENT_DATE` | 27 | `DATE` | When the account first went delinuent | When the account first went delinuent | `[]` | `{}` |
    | `SCRA_STATUS` | 28 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `SCRA_START_DATE` | 29 | `TEXT` |  |  | `[]` | `{}` |
    | `SCRA_END_DATE` | 30 | `TEXT` |  |  | `[]` | `{}` |
    | `IS_BANKRUPTCY` | 31 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `BANKRUPTCY_STATUS` | 32 | `TEXT` |  |  | `[]` | `{}` |
    | `BANKRUPTCY_CHAPTER` | 33 | `TEXT` |  |  | `[]` | `{}` |
    | `HAS_ASSETS` | 34 | `TEXT` |  |  | `[]` | `{}` |
    | `BANKRUPTCY_FILE_DATE` | 35 | `TEXT` |  |  | `[]` | `{}` |
    | `BANKRUPTCY_DISCHARGE_DATE` | 36 | `DATE` |  |  | `[]` | `{}` |
    | `IS_CASE_DISCHARGED` | 37 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `BANKRUPTCY_LOAN_DISCHARGED_STATUS` | 38 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `SATISFACTION_AMOUNT` | 39 | `NUMBER` |  |  | `[]` | `{}` |
    | `SATISFACTION_DATE` | 40 | `TEXT` |  |  | `[]` | `{}` |
    | `FORBEARANCE_APPLICATION_RECEIVED_DATE` | 41 | `DATE` |  |  | `[]` | `{}` |
    | `FORBEARANCE_PROCESSED_DATE` | 42 | `DATE` |  |  | `[]` | `{}` |
    | `FORBEARANCE_DECISION_DATE` | 43 | `DATE` |  |  | `[]` | `{}` |
    | `FORBEARANCE_REASON` | 44 | `TEXT` |  |  | `[]` | `{}` |
    | `FORBEARANCE_START_DATE` | 45 | `DATE` |  |  | `[]` | `{}` |
    | `FORBEARANCE_END_DATE` | 46 | `DATE` |  |  | `[]` | `{}` |
    | `FORBEARANCE_DURATION` | 47 | `NUMBER` | The number of billing cycles the acommodation lasts for | The number of billing cycles the acommodation lasts for | `[]` | `{}` |
    | `PAID_PRINCIPAL` | 48 | `NUMBER` |  |  | `[]` | `{}` |
    | `PAID_INTEREST` | 49 | `NUMBER` |  |  | `[]` | `{}` |
    | `PAID_FEES` | 50 | `NUMBER` |  |  | `[]` | `{}` |
    | `UNPAID_PRINCIPAL` | 51 | `NUMBER` | The amount of unpaid principal on the loan | The amount of unpaid principal on the loan | `[]` | `{}` |
    | `UNPAID_INTEREST` | 52 | `NUMBER` |  |  | `[]` | `{}` |
    | `UNPAID_FEES` | 53 | `NUMBER` |  |  | `[]` | `{}` |
    | `TOTAL_ACCRUED_INTEREST` | 54 | `NUMBER` |  |  | `[]` | `{}` |
    | `STATEMENT_INSTALLMENT_AMOUNT_DUE` | 55 | `NUMBER` |  |  | `[]` | `{}` |
    | `STATEMENT_PROJECTED_PRINCIPAL_ALLOCATION` | 56 | `NUMBER` |  |  | `[]` | `{}` |
    | `STATEMENT_PROJECTED_INTEREST_ALLOCATION` | 57 | `NUMBER` |  |  | `[]` | `{}` |
    | `REGULAR_INSTALLMENT_AMOUNT_DUE` | 58 | `NUMBER` |  |  | `[]` | `{}` |
    | `PAYOFF_AMOUNT` | 59 | `NUMBER` |  |  | `[]` | `{}` |
    | `AMOUNT_TO_BRING_CURRENT` | 60 | `NUMBER` |  |  | `[]` | `{}` |
    | `WRITTEN_OFF_PRINCIPAL` | 61 | `NUMBER` |  |  | `[]` | `{}` |
    | `WRITTEN_OFF_INTEREST` | 62 | `NUMBER` |  |  | `[]` | `{}` |
    | `WRITTEN_OFF_FEES` | 63 | `NUMBER` |  |  | `[]` | `{}` |
    | `WAIVED_OFF_PRINCIPAL` | 64 | `NUMBER` |  |  | `[]` | `{}` |
    | `WAIVED_OFF_INTEREST` | 65 | `NUMBER` |  |  | `[]` | `{}` |
    | `WAIVED_OFF_FEES` | 66 | `NUMBER` |  |  | `[]` | `{}` |
    | `CHARGE_OFF_TOTAL` | 67 | `NUMBER` |  |  | `[]` | `{}` |
    | `CHARGE_OFF_PRINCIPAL` | 68 | `NUMBER` |  |  | `[]` | `{}` |
    | `CHARGE_OFF_INTEREST` | 69 | `NUMBER` |  |  | `[]` | `{}` |
    | `CHARGE_OFF_FEES` | 70 | `NUMBER` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.cherry_data_model.convert_to_pt`
    *   `model.cherry_data_model.charged_off_view_xf`
    *   `model.cherry_data_model.int_funded_information_pt`
    *   `model.cherry_data_model.loan_statuses_today_xf`
    *   `model.cherry_data_model.src_loan_tx`
    *   `model.cherry_data_model.stg_active_forbearances`
    *   `model.cherry_data_model.stg_active_loan_setups`
    *   `model.cherry_data_model.stg_balance_adjustments`
    *   `model.cherry_data_model.stg_loanpro_chargeoffs_aggregation`
    *   `model.cherry_data_model.stg_loanpro_transactions_breakdown`
    *   `model.cherry_data_model.stg_soonest_payments`

---
