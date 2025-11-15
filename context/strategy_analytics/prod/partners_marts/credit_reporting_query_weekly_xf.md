## Model: `credit_reporting_query_weekly_xf`

`credit_reporting_query_weekly_xf`

*   **Unique ID:** `model.cherry_data_model.credit_reporting_query_weekly_xf`
*   **FQN:** `prod.partners_marts.credit_reporting_query_weekly_xf`
*   **Description:** **Weekly Credit Bureau Reporting for Standard Installment Loans**
This model generates weekly credit bureau reporting files for Datalinx processing, specifically for  standard installment loans (excluding Pay-in-Four products). It implements a cohort-based reporting  system that divides loans into 4 groups based on their payment due dates to enable more frequent  reporting while managing processing load.
**Cohort Structure:** - Cohort 1: Loans with due dates 1st-7th (reports on 7th) - Cohort 2: Loans with due dates 8th-14th (reports on 14th)   - Cohort 3: Loans with due dates 15th-21st (reports on 21st) - Cohort 4: Loans with due dates 22nd-31st (reports on last day of month)
**Key Features:** - Weekly reporting cycle instead of monthly - Excludes Pay-in-Four loans (1.5 month term) - Includes loans with status changes since last reporting period - Implements cohort filtering to process relevant loans only - Uses effective reporting date logic to determine current cohort
**Data Processing:** - Determines effective reporting date based on current date - Identifies active cohort and previous reporting period - Processes both reportable and refunded loans - Applies same credit bureau formatting as monthly model
**Use Cases:** - More frequent credit bureau updates for better accuracy - Reduced processing load through cohort-based batching - Improved cash flow through faster reporting cycles - Better borrower credit profile maintenance

*   **Tags:** `['external_partners', 'external', 'credit_reporting', 'servicing', 'collections', 'weekly', 'bloom_credit']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `ASSOCIATION_CODE` | 1 | `TEXT` | The association code as defined by the credit bureaus for the account. Set to '1' for  individual accounts or 'X' if the borrower is deceased.
 | The association code as defined by the credit bureaus for the account. Set to '1' for  individual accounts or 'X' if the borrower is deceased.
 | `[]` | `{}` |
    | `FIRST_NAME` | 2 | `TEXT` | The borrower's first name, cleaned to remove middle initials. Uses cleaned_first_name  logic that removes single-letter suffixes after spaces.
 | The borrower's first name, cleaned to remove middle initials. Uses cleaned_first_name  logic that removes single-letter suffixes after spaces.
 | `[]` | `{}` |
    | `MIDDLE_NAME` | 3 | `TEXT` | The borrower's middle name. Always empty string as Cherry does not collect middle names  separately from first names.
 | The borrower's middle name. Always empty string as Cherry does not collect middle names  separately from first names.
 | `[]` | `{}` |
    | `LAST_NAME` | 4 | `TEXT` | The borrower's last name, cleaned to remove middle initials. Uses cleaned_last_name  logic that removes single-letter suffixes after spaces.
 | The borrower's last name, cleaned to remove middle initials. Uses cleaned_last_name  logic that removes single-letter suffixes after spaces.
 | `[]` | `{}` |
    | `ADDRESS_LINE_ONE` | 5 | `TEXT` | The first line of the borrower's address. Uses corrected address logic that prioritizes  current address, then most recent address, then address at time of loan origination.
 | The first line of the borrower's address. Uses corrected address logic that prioritizes  current address, then most recent address, then address at time of loan origination.
 | `[]` | `{}` |
    | `ADDRESS_LINE_TWO` | 6 | `TEXT` | The second line of the borrower's address. Currently not collected separately by Cherry,  so this field is typically NULL.
 | The second line of the borrower's address. Currently not collected separately by Cherry,  so this field is typically NULL.
 | `[]` | `{}` |
    | `CITY` | 7 | `TEXT` | The city name from the borrower's address record. Retrieved from the borrower_addresses  table using the borrower_address_id relationship.
 | The city name from the borrower's address record. Retrieved from the borrower_addresses  table using the borrower_address_id relationship.
 | `[]` | `{}` |
    | `STATE` | 8 | `TEXT` | The state abbreviation from the borrower's address record. Retrieved from the  borrower_addresses table as state_abbreviation.
 | The state abbreviation from the borrower's address record. Retrieved from the  borrower_addresses table as state_abbreviation.
 | `[]` | `{}` |
    | `ZIPCODE` | 9 | `TEXT` | The zipcode for the borrower's address. Formatted to 9 digits by appending '0000'  if the original zipcode is only 5 digits.
 | The zipcode for the borrower's address. Formatted to 9 digits by appending '0000'  if the original zipcode is only 5 digits.
 | `[]` | `{}` |
    | `SSN` | 10 | `TEXT` | The hashed version of the borrower's Social Security Number. Retrieved from the  borrower_information table as borrower_ssn.
 | The hashed version of the borrower's Social Security Number. Retrieved from the  borrower_information table as borrower_ssn.
 | `[]` | `{}` |
    | `PHONE_NUMBER` | 11 | `TEXT` | The borrower's phone number as provided during the underwriting process. Retrieved  from the borrower_information table.
 | The borrower's phone number as provided during the underwriting process. Retrieved  from the borrower_information table.
 | `[]` | `{}` |
    | `DATE_OF_BIRTH` | 12 | `DATE` | The borrower's date of birth as provided during application. Retrieved from the  borrower_information table in YYYY-MM-DD format.
 | The borrower's date of birth as provided during application. Retrieved from the  borrower_information table in YYYY-MM-DD format.
 | `[]` | `{}` |
    | `END_OF_MONTH_LOAN_STATUS` | 13 | `TEXT` | The loan status as of the effective reporting date. Retrieved from the daily_loan_xf  table for the most recent record up to the reporting date.
 | The loan status as of the effective reporting date. Retrieved from the daily_loan_xf  table for the most recent record up to the reporting date.
 | `[]` | `{}` |
    | `CONSUMER_INFORMATION_INDICATOR` | 14 | `TEXT` | Credit bureau indicator for consumer account status, primarily used for bankruptcy  classifications. Maps bankruptcy chapter and case status to specific codes (A-H, Q, Z).
 | Credit bureau indicator for consumer account status, primarily used for bankruptcy  classifications. Maps bankruptcy chapter and case status to specific codes (A-H, Q, Z).
 | `[]` | `{}` |
    | `ACCOUNT_NUMBER` | 15 | `TEXT` | The account number for credit bureau reporting. Created by removing spaces and dashes  from the contract_id to meet credit bureau formatting requirements.
 | The account number for credit bureau reporting. Created by removing spaces and dashes  from the contract_id to meet credit bureau formatting requirements.
 | `[]` | `{}` |
    | `PORTFOLIO_TYPE` | 16 | `TEXT` | The portfolio type reported to credit bureaus. Hardcoded to 'I' for installment loans  as all Cherry contracts are installment-based.
 | The portfolio type reported to credit bureaus. Hardcoded to 'I' for installment loans  as all Cherry contracts are installment-based.
 | `[]` | `{}` |
    | `ACCOUNT_TYPE` | 17 | `TEXT` | The account type reported to credit bureaus. Hardcoded to '06' for Installment Sales  Contract as used by the retail industry.
 | The account type reported to credit bureaus. Hardcoded to '06' for Installment Sales  Contract as used by the retail industry.
 | `[]` | `{}` |
    | `DATE_OPEN` | 18 | `DATE` | The date the contract was opened (funded). Retrieved from the funded_at_pt field  and converted to date format for credit bureau reporting.
 | The date the contract was opened (funded). Retrieved from the funded_at_pt field  and converted to date format for credit bureau reporting.
 | `[]` | `{}` |
    | `DATE_OF_LAST_PAYMENT` | 19 | `DATE` | The date of the most recent payment applied to the loan as of the reporting date.  Retrieved from the most_recent_payments CTE.
 | The date of the most recent payment applied to the loan as of the reporting date.  Retrieved from the most_recent_payments CTE.
 | `[]` | `{}` |
    | `DATE_CLOSED` | 20 | `DATE` | The date the contract was closed, if applicable. Calculated based on loan status  and when the balance reached zero, with special handling for charged-off accounts.
 | The date the contract was closed, if applicable. Calculated based on loan status  and when the balance reached zero, with special handling for charged-off accounts.
 | `[]` | `{}` |
    | `ACCOUNT_STATUS` | 21 | `TEXT` | The credit bureau account status code. Maps internal loan status and DPD to specific  codes (11=current, 71=30+DPD, 78=60+DPD, 80=90+DPD, 82=120+DPD, 97=charged off, etc.).
 | The credit bureau account status code. Maps internal loan status and DPD to specific  codes (11=current, 71=30+DPD, 78=60+DPD, 80=90+DPD, 82=120+DPD, 97=charged off, etc.).
 | `[]` | `{}` |
    | `PAYMENT_RATING` | 22 | `TEXT` | The payment rating for closed accounts indicating historical payment performance.  Codes 0-3 represent different levels of delinquency history for closed accounts.
 | The payment rating for closed accounts indicating historical payment performance.  Codes 0-3 represent different levels of delinquency history for closed accounts.
 | `[]` | `{}` |
    | `DATE_OF_FIRST_DELINQUENCY` | 23 | `DATE` | The date when the account first became 30 or more days past due. Calculated using  multiple sources including daily_loan_xf and bankruptcy filing dates.
 | The date when the account first became 30 or more days past due. Calculated using  multiple sources including daily_loan_xf and bankruptcy filing dates.
 | `[]` | `{}` |
    | `DAYS_PAST_DUE` | 24 | `NUMBER` | The number of days past due as of the effective reporting date. Retrieved from the  daily_loan_xf table for the reporting date.
 | The number of days past due as of the effective reporting date. Retrieved from the  daily_loan_xf table for the reporting date.
 | `[]` | `{}` |
    | `CREDIT_LIMIT` | 25 | `NUMBER` | The credit limit for the account. Hardcoded to 0 for installment loans as they do  not have revolving credit limits.
 | The credit limit for the account. Hardcoded to 0 for installment loans as they do  not have revolving credit limits.
 | `[]` | `{}` |
    | `HIGHEST_CREDIT` | 26 | `FLOAT` | The highest credit amount (original loan amount) for the installment contract.  Retrieved from the purchase_amount field and rounded.
 | The highest credit amount (original loan amount) for the installment contract.  Retrieved from the purchase_amount field and rounded.
 | `[]` | `{}` |
    | `CURRENT_BALANCE` | 27 | `NUMBER` | The current outstanding balance on the contract as of the reporting date. Set to 0  for closed accounts, uses charge-off amount for charged-off accounts.
 | The current outstanding balance on the contract as of the reporting date. Set to 0  for closed accounts, uses charge-off amount for charged-off accounts.
 | `[]` | `{}` |
    | `AMOUNT_PAST_DUE` | 28 | `NUMBER` | The amount that is 30 or more days past due as of the reporting date. Calculated  from various balance fields and capped at current_balance.
 | The amount that is 30 or more days past due as of the reporting date. Calculated  from various balance fields and capped at current_balance.
 | `[]` | `{}` |
    | `MONTHLY_PAYMENT` | 29 | `FLOAT` | The contractually scheduled monthly payment amount. Set to 0 for closed or charged-off  accounts, otherwise uses the original installment_amount.
 | The contractually scheduled monthly payment amount. Set to 0 for closed or charged-off  accounts, otherwise uses the original installment_amount.
 | `[]` | `{}` |
    | `ACTUAL_PAYMENT` | 30 | `NUMBER` | The actual amount paid during the reporting period. Sum of all payments between the  previous and current reporting dates.
 | The actual amount paid during the reporting period. Sum of all payments between the  previous and current reporting dates.
 | `[]` | `{}` |
    | `TERMS_FREQUENCY` | 31 | `TEXT` | The frequency of payments for the account. Set to 'M' for monthly payments as all  standard installment loans have monthly payment schedules.
 | The frequency of payments for the account. Set to 'M' for monthly payments as all  standard installment loans have monthly payment schedules.
 | `[]` | `{}` |
    | `TERMS` | 32 | `NUMBER` | The term length of the contract in months. Retrieved from the loan_terms table  based on the loan_id.
 | The term length of the contract in months. Retrieved from the loan_terms table  based on the loan_id.
 | `[]` | `{}` |
    | `ORIGINAL_CHARGE_OFF_AMOUNT` | 33 | `NUMBER` | The total amount charged off for the contract, if applicable. Retrieved from the  charge_off_totals CTE for loans that have been charged off.
 | The total amount charged off for the contract, if applicable. Retrieved from the  charge_off_totals CTE for loans that have been charged off.
 | `[]` | `{}` |
    | `ORIGINAL_CHARGE_OFF_DATE` | 34 | `DATE` | The date when the contract was originally charged off. Retrieved from the  first_charge_off_transaction_date CTE.
 | The date when the contract was originally charged off. Retrieved from the  first_charge_off_transaction_date CTE.
 | `[]` | `{}` |
    | `DATE_OF_ACCOUNT_INFORMATION` | 35 | `DATE` | The date of the account information being reported. Either the effective reporting  date for open accounts or the later of date_closed and date_of_last_payment for closed accounts.
 | The date of the account information being reported. Either the effective reporting  date for open accounts or the later of date_closed and date_of_last_payment for closed accounts.
 | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.borrowers_merged_emails_xf`
    *   `model.cherry_data_model.daily_loan_xf`
    *   `model.cherry_data_model.int_funded_information_pt`
    *   `model.cherry_data_model.int_servicing_bankruptcies`
    *   `model.cherry_data_model.loan_info_xf`
    *   `model.cherry_data_model.src_borrower_addresses`
    *   `model.cherry_data_model.src_borrowers`
    *   `model.cherry_data_model.src_cherry_loans`
    *   `model.cherry_data_model.src_debt_sale_transactions`
    *   `model.cherry_data_model.src_loan_plans`
    *   `model.cherry_data_model.src_loan_schedule`
    *   `model.cherry_data_model.src_loanpro_chargeoff_transactions`
    *   `model.cherry_data_model.stg_active_loanpro_payments`
    *   `model.cherry_data_model.stg_borrower_addresses_with_tz`
    *   `model.cherry_data_model.stg_loanpro_chargeoffs_aggregation`
    *   `source.cherry_data_model.cherry_data.loan_status_history`

---
