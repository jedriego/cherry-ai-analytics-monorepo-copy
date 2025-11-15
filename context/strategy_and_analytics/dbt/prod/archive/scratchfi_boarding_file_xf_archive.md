## Model: `scratchfi_boarding_file_xf_archive`

`scratchfi_boarding_file_xf_archive`

*   **Unique ID:** `model.cherry_data_model.scratchfi_boarding_file_xf_archive`
*   **FQN:** `prod.archive.scratchfi_boarding_file_xf_archive`
*   **Description:** This model serves as the boarding file for our backup servicer Scratchfi. The boarding file provides them with the information they need for each contract and borrower to take over servicing duties for the loan if there is an event which means that Cherry is no longer capable of servicing the loans on its book.
The model is exported as a `.csv` file each day and sent to their SFTP server so that they have up to date information on the borrowers and contracts within Cherry's book.

*   **Tags:** `['archive', 'partners', 'servicing']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `CONTRACT_ID` | 1 | `TEXT` | The auto-generated *"friendly"* name for a borrower's Cherry loan. It has been generated in
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
    | `FIRST_NAME` | 3 | `TEXT` |  |  | `[]` | `{}` |
    | `LAST_NAME` | 4 | `TEXT` |  |  | `[]` | `{}` |
    | `DATE_OF_BIRTH` | 5 | `DATE` |  |  | `[]` | `{}` |
    | `BORROWER_SSN` | 6 | `TEXT` |  |  | `[]` | `{}` |
    | `BORROWER_CREDIT_SCORE` | 7 | `FLOAT` |  |  | `[]` | `{}` |
    | `EMAIL` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `MOBILE_PHONE_NUMBER` | 9 | `TEXT` |  |  | `[]` | `{}` |
    | `BORROWER_MAILING_ADDRESS` | 10 | `TEXT` |  |  | `[]` | `{}` |
    | `BORROWER_CITY` | 11 | `TEXT` |  |  | `[]` | `{}` |
    | `BORROWER_STATE` | 12 | `TEXT` |  |  | `[]` | `{}` |
    | `BORROWER_COUNTRY` | 13 | `TEXT` |  |  | `[]` | `{}` |
    | `BORROWER_POSTAL_CODE` | 14 | `TEXT` |  |  | `[]` | `{}` |
    | `ACH_ACCOUNT_HOLDER` | 15 | `TEXT` |  |  | `[]` | `{}` |
    | `ACH_ACCOUNT_NUMBER` | 16 | `TEXT` |  |  | `[]` | `{}` |
    | `ACH_ROUTING_NUMBER` | 17 | `TEXT` |  |  | `[]` | `{}` |
    | `ACH_ACCOUNT_TYPE` | 18 | `TEXT` |  |  | `[]` | `{}` |
    | `ORIGINAL_PRINCIPAL_AMOUNT` | 19 | `FLOAT` |  |  | `[]` | `{}` |
    | `AUTOPAY_STATUS` | 20 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `LOAN_START_DATE` | 21 | `DATE` |  |  | `[]` | `{}` |
    | `MERCHANT_NAME` | 22 | `TEXT` |  |  | `[]` | `{}` |
    | `ORIGINATION_DATE` | 23 | `DATE` |  |  | `[]` | `{}` |
    | `DISBURSEMENT_DATE` | 24 | `DATE` |  |  | `[]` | `{}` |
    | `APR` | 25 | `NUMBER` | The APR on the loan | The APR on the loan | `[]` | `{}` |
    | `FIRST_REPAYMENT_DATE` | 26 | `DATE` | The first payment date for the loan under the **current** loan setup/modification schema | The first payment date for the loan under the **current** loan setup/modification schema | `[]` | `{}` |
    | `NUMBER_OF_LOAN_TERMS` | 27 | `NUMBER` | The number of scheduled payments/terms for the loan | The number of scheduled payments/terms for the loan | `[]` | `{}` |
    | `MATURITY_DATE` | 28 | `DATE` | The original final payment date for the loan | The original final payment date for the loan | `[]` | `{}` |
    | `CURR_INTEREST_RATE` | 29 | `NUMBER` |  |  | `[]` | `{}` |
    | `LOAN_INTEREST_RATE_TYPE` | 30 | `TEXT` |  |  | `[]` | `{}` |
    | `CURRENT_MONTHLY_INSTALLMENT_AMOUNT` | 31 | `NUMBER` |  |  | `[]` | `{}` |
    | `REPAYMENT_STATUS` | 32 | `TEXT` |  |  | `[]` | `{}` |
    | `CREDITOR_NAME` | 33 | `TEXT` |  |  | `[]` | `{}` |
    | `OUTSTANDING_PRINCIPAL_AMOUNT` | 34 | `NUMBER` | The outstanding principal balance on the loan. Because of the way we forgive small balances to borrowers it is set to be greater than 0
 | The outstanding principal balance on the loan. Because of the way we forgive small balances to borrowers it is set to be greater than 0
 | `[]` | `{}` |
    | `REMAINING_TERMS` | 35 | `NUMBER` |  |  | `[]` | `{}` |
    | `NEXT_PAYMENT_DATE` | 36 | `DATE` |  |  | `[]` | `{}` |
    | `PAYMENT_FREQUENCY` | 37 | `NUMBER` |  |  | `[]` | `{}` |
    | `TCPA_CONSENT` | 38 | `BOOLEAN` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.borrowers_merged_emails_xf`
    *   `model.cherry_data_model.int_funded_information_pt`
    *   `model.cherry_data_model.loan_statuses_today_xf`
    *   `model.cherry_data_model.src_loan_tx`
    *   `model.cherry_data_model.src_loanpro_loans`
    *   `model.cherry_data_model.stg_active_forbearances`
    *   `model.cherry_data_model.stg_active_loan_setups`
    *   `model.cherry_data_model.stg_borrower_addresses_with_tz`
    *   `model.cherry_data_model.stg_current_installment_payment_methods`
    *   `model.cherry_data_model.stg_soonest_payments`
    *   `model.cherry_data_model.unsubscribed_borrowers_xf`

---
