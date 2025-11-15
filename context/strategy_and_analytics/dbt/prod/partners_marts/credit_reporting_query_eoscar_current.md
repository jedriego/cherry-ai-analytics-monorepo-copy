## Model: `credit_reporting_query_eoscar_current`

`credit_reporting_query_eoscar_current`

*   **Unique ID:** `model.cherry_data_model.credit_reporting_query_eoscar_current`
*   **FQN:** `prod.partners_marts.credit_reporting_query_eoscar_current`
*   **Description:** **Comprehensive Credit Bureau Reporting for Bloom Credit/EOSCAR Partnership**
This sophisticated model generates credit bureau reporting data for Cherry's partnership with Bloom Credit/EOSCAR,  implementing comprehensive credit reporting standards and regulatory compliance requirements. The model serves as  Cherry's primary credit reporting engine, producing detailed borrower credit history records that comply with  industry-standard credit reporting formats and regulations.
**Core Business Functions:** - **Credit Bureau Data Generation**: Creates standardized credit reporting records for submission to major credit bureaus - **Regulatory Compliance**: Ensures compliance with FCRA, ECOA, and other credit reporting regulations - **Account Status Management**: Implements sophisticated logic for determining account status codes (11, 13, 64, 71, 78, 80, 82, 97) - **Payment History Tracking**: Maintains detailed payment rating codes (0, 1, 2, 3, L) for closed accounts - **Bankruptcy Integration**: Manages complex bankruptcy status codes and consumer information indicators - **Data Quality Assurance**: Includes extensive data validation and address correction logic
**Sophisticated Model Architecture:**
**1. Loan Schedule Recreation Engine:** - **Funding Date Synthetic Schedules**: Creates synthetic due dates based on original funding patterns - **Due Date Change Management**: Tracks and applies due date modifications with dynamic day pattern adjustments - **Calendar Spine Integration**: Ensures complete date coverage using calendar table scaffolding - **Schedule Deduplication**: Prioritizes actual schedule data over synthetic, with month-level deduplication
**2. Advanced Payment and Transaction Tracking:** - **Multi-Source Payment Integration**: Combines LoanPro payments with transaction breakdowns - **Charge-off Recovery Detection**: Sophisticated logic for identifying and flagging recovery payments - **Payment Application Waterfall**: Tracks how payments are applied to principal, interest, and fees - **Most Recent Payment Calculation**: Determines last payment dates with complex charge-off considerations
**3. Comprehensive Charge-off Management:** - **Charge-off Transaction Processing**: Tracks charge-off events with balance and recovery calculations - **Active Charge-off Calculation**: Determines net charge-off amounts after recoveries - **Charge-off Date Tracking**: Maintains first charge-off dates for credit reporting timeline requirements - **Recovery Payment Integration**: Links recovery payments to original charge-off transactions
**4. Bankruptcy Status Processing:** - **IDICore Integration**: Combines automated bankruptcy detection with manual bankruptcy data scrubs - **Chapter-Specific Status Codes**: Maps bankruptcy chapters (7, 11, 12, 13) to specific credit reporting codes - **Case Status Management**: Tracks Active, Discharged, Dismissed, and Closed bankruptcy cases - **Timeline Validation**: Ensures bankruptcy dates align with loan funding and reporting periods
**5. Credit Reporting Business Logic:** - **Account Status Determination**: Complex cascading logic for status codes:
  - DA: Do not report (fraud/request)
  - DF: Fraud accounts  
  - 11: Current accounts with balance
  - 13: Closed/paid accounts
  - 64: Charged-off accounts paid in full
  - 71: 30+ days past due
  - 78: 60+ days past due  
  - 80: 90+ days past due
  - 82: 120+ days past due
  - 97: Active charge-offs
- **Payment Rating Calculation**: For closed accounts, determines payment history quality (0-3, L) - **Delinquency Date Logic**: Sophisticated calculation of first delinquency dates across multiple scenarios
**6. Address and Data Quality Management:** - **Address Correction Logic**: Implements hotfix logic for borrower address data quality - **Phone Number Standardization**: Cleans and validates phone number formats - **Name Cleaning**: Removes initials and standardizes borrower names for credit reporting - **SSN and DOB Validation**: Ensures critical identity fields meet credit bureau standards
**7. Refunded Loan Processing:** - **30-Day Refund Rule**: Identifies loans refunded more than 30 days after funding - **Credit Deletion Logic**: Marks refunded loans for deletion from credit bureau records - **Separate Processing**: Handles refunded loans with distinct business logic from active loans
**Critical Staging Model Integration:** - **stg_active_loanpro_payments**: Active, non-reversed payment records with detailed payment application data - **stg_loanpro_chargeoffs_aggregation**: Comprehensive charge-off calculations with recovery tracking - **stg_idicore_bankruptcies**: Combined automated and manual bankruptcy data with chapter and status details - **int_funded_information_pt**: Core loan funding data with Cherry loan ID mappings - **daily_loan_xf**: Daily loan status snapshots for historical performance tracking - **borrowers_merged_emails_xf**: Borrower information with intelligently merged contact data - **stg_borrower_addresses_with_tz**: Geographic data with timezone information for regulatory compliance
**Regulatory and Compliance Framework:** - **FCRA Compliance**: Ensures fair credit reporting act compliance with accurate dispute handling - **ECOA Requirements**: Maintains equal credit opportunity act compliance for all protected classes - **Credit Bureau Standards**: Adheres to Experian, Equifax, and TransUnion data format requirements - **Data Retention**: Implements proper data retention policies for credit reporting data - **Privacy Protection**: Ensures borrower privacy while maintaining reporting accuracy
**Data Quality and Validation:** - **Deduplication Logic**: Ensures one record per account per reporting period - **Cross-Reference Validation**: Validates consistency across multiple data sources - **Timeline Integrity**: Ensures logical sequence of dates and events - **Balance Reconciliation**: Validates current balances against payment and charge-off history
**Partner Integration:** This model specifically serves Cherry's partnership with Bloom Credit/EOSCAR, providing the data feed  necessary for credit bureau submissions. The output format aligns with industry-standard credit reporting  schemas and enables Cherry to participate in the broader credit ecosystem while maintaining data accuracy  and regulatory compliance.
**Primary Use Cases:** - Monthly credit bureau data submissions to major credit bureaus - Regulatory compliance reporting and auditing - Credit portfolio performance analysis and monitoring - Dispute resolution and data correction workflows - Partnership reporting and reconciliation with Bloom Credit/EOSCAR
**Grain:** One record per reportable loan account with complete credit reporting data for the current reporting period

*   **Tags:** `['external_partners', 'external', 'credit_reporting']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `ASSOCIATION_CODE` | 1 | `TEXT` | **Credit bureau association code indicating account relationship.** Returns 'X' for deceased borrowers  (loan_substatus = 'Deceased'), otherwise '1' for primary account holder. This code informs credit  bureaus about the account relationship and ensures proper handling of deceased borrower accounts  in accordance with credit reporting regulations.
 | **Credit bureau association code indicating account relationship.** Returns 'X' for deceased borrowers  (loan_substatus = 'Deceased'), otherwise '1' for primary account holder. This code informs credit  bureaus about the account relationship and ensures proper handling of deceased borrower accounts  in accordance with credit reporting regulations.
 | `[]` | `{}` |
    | `FIRST_NAME` | 2 | `TEXT` | **Cleaned borrower first name for credit reporting.** Uses cleaned_first_name from borrower_information  which removes initials and standardizes format. Name cleaning logic removes trailing initials (single  character words after periods) to ensure consistent credit bureau data format and avoid duplicate  credit files due to name variations.
 | **Cleaned borrower first name for credit reporting.** Uses cleaned_first_name from borrower_information  which removes initials and standardizes format. Name cleaning logic removes trailing initials (single  character words after periods) to ensure consistent credit bureau data format and avoid duplicate  credit files due to name variations.
 | `[]` | `{}` |
    | `MIDDLE_NAME` | 3 | `TEXT` | **Middle name field (always empty in current implementation).** Set to empty string as Cherry's current  data model does not capture middle names. This field is included to maintain compatibility with  standard credit reporting formats that expect this field.
 | **Middle name field (always empty in current implementation).** Set to empty string as Cherry's current  data model does not capture middle names. This field is included to maintain compatibility with  standard credit reporting formats that expect this field.
 | `[]` | `{}` |
    | `LAST_NAME` | 4 | `TEXT` | **Cleaned borrower last name for credit reporting.** Uses cleaned_last_name from borrower_information  which removes initials and standardizes format. Applies same cleaning logic as first name to ensure  consistent credit bureau submissions and prevent credit file fragmentation.
 | **Cleaned borrower last name for credit reporting.** Uses cleaned_last_name from borrower_information  which removes initials and standardizes format. Applies same cleaning logic as first name to ensure  consistent credit bureau submissions and prevent credit file fragmentation.
 | `[]` | `{}` |
    | `ADDRESS_LINE_ONE` | 5 | `TEXT` | **Primary address line with data quality corrections.** Uses borrower address data with fallback to  hotfix_final_addresses for data quality improvements. Hotfix logic addresses cases where primary  address data is missing or incomplete, using historical address records or most recent address  information to ensure complete credit reporting data.
 | **Primary address line with data quality corrections.** Uses borrower address data with fallback to  hotfix_final_addresses for data quality improvements. Hotfix logic addresses cases where primary  address data is missing or incomplete, using historical address records or most recent address  information to ensure complete credit reporting data.
 | `[]` | `{}` |
    | `ADDRESS_LINE_TWO` | 6 | `TEXT` | **Secondary address line (apartment, suite, etc.).** Pulled directly from borrower_addresses without  modification. Used for complete address information in credit reporting to ensure proper borrower  identification and address verification by credit bureaus.
 | **Secondary address line (apartment, suite, etc.).** Pulled directly from borrower_addresses without  modification. Used for complete address information in credit reporting to ensure proper borrower  identification and address verification by credit bureaus.
 | `[]` | `{}` |
    | `CITY` | 7 | `TEXT` | **City name from borrower address record.** Mapped from city_name field in borrower_addresses.  Essential for geographic identification and credit bureau address verification processes.
 | **City name from borrower address record.** Mapped from city_name field in borrower_addresses.  Essential for geographic identification and credit bureau address verification processes.
 | `[]` | `{}` |
    | `STATE` | 8 | `TEXT` | **State abbreviation from borrower address record.** Uses state_abbreviation from borrower_addresses  to provide standardized state codes for credit bureau submission and geographic classification.
 | **State abbreviation from borrower address record.** Uses state_abbreviation from borrower_addresses  to provide standardized state codes for credit bureau submission and geographic classification.
 | `[]` | `{}` |
    | `ZIPCODE` | 9 | `TEXT` | **ZIP code with 9-digit formatting for credit bureaus.** If borrower ZIP is 5 digits, appends '0000'  to create 9-digit format (ZIP+4). This formatting ensures compatibility with credit bureau systems  that expect extended ZIP code format for precise geographic identification.
 | **ZIP code with 9-digit formatting for credit bureaus.** If borrower ZIP is 5 digits, appends '0000'  to create 9-digit format (ZIP+4). This formatting ensures compatibility with credit bureau systems  that expect extended ZIP code format for precise geographic identification.
 | `[]` | `{}` |
    | `SSN` | 10 | `TEXT` | **Social Security Number for borrower identification.** Critical field for credit bureau matching  and ensuring accurate credit file association. Used by credit bureaus as primary identifier for  linking credit accounts to the correct borrower credit profile.
 | **Social Security Number for borrower identification.** Critical field for credit bureau matching  and ensuring accurate credit file association. Used by credit bureaus as primary identifier for  linking credit accounts to the correct borrower credit profile.
 | `[]` | `{}` |
    | `PHONE_NUMBER` | 11 | `TEXT` | **Primary contact phone number from borrower record.** Used for contact information and additional  verification by credit bureaus. Important for borrower communication and account verification  processes by credit monitoring services.
 | **Primary contact phone number from borrower record.** Used for contact information and additional  verification by credit bureaus. Important for borrower communication and account verification  processes by credit monitoring services.
 | `[]` | `{}` |
    | `DATE_OF_BIRTH` | 12 | `DATE` | **Borrower date of birth for identity verification.** Essential for credit bureau matching algorithms  and preventing identity mix-ups. Used in combination with SSN and name for precise borrower  identification in credit reporting systems.
 | **Borrower date of birth for identity verification.** Essential for credit bureau matching algorithms  and preventing identity mix-ups. Used in combination with SSN and name for precise borrower  identification in credit reporting systems.
 | `[]` | `{}` |
    | `END_OF_MONTH_LOAN_STATUS` | 13 | `TEXT` | **Loan status as of the effective reporting date.** Reflects the loan status from daily_loan_xf  on the reporting cutoff date. Critical for determining account status codes and payment ratings.  Key statuses include Open, Late, Closed, Charged Off, Bankruptcy, Settled, and Debt Sale.
 | **Loan status as of the effective reporting date.** Reflects the loan status from daily_loan_xf  on the reporting cutoff date. Critical for determining account status codes and payment ratings.  Key statuses include Open, Late, Closed, Charged Off, Bankruptcy, Settled, and Debt Sale.
 | `[]` | `{}` |
    | `CONSUMER_INFORMATION_INDICATOR` | 14 | `TEXT` | **Bankruptcy status code for credit bureau reporting.** Complex mapping of bankruptcy chapters  and case statuses to standard credit reporting codes: - A: Chapter 7 Active/Reopened/Reinstated - B: Chapter 11 Active/Reopened/Reinstated   - C: Chapter 12 Active/Reopened/Reinstated - D: Chapter 13 Active/Reopened/Reinstated - E: Chapter 7 Discharged - F: Chapter 11 Discharged - G: Chapter 12 Discharged - H: Chapter 13 Discharged - I/J/K/L: Dismissed cases (deprecated) - Q: Closed cases - Z: Bankruptcy filed status - Empty: No bankruptcy
 | **Bankruptcy status code for credit bureau reporting.** Complex mapping of bankruptcy chapters  and case statuses to standard credit reporting codes: - A: Chapter 7 Active/Reopened/Reinstated - B: Chapter 11 Active/Reopened/Reinstated   - C: Chapter 12 Active/Reopened/Reinstated - D: Chapter 13 Active/Reopened/Reinstated - E: Chapter 7 Discharged - F: Chapter 11 Discharged - G: Chapter 12 Discharged - H: Chapter 13 Discharged - I/J/K/L: Dismissed cases (deprecated) - Q: Closed cases - Z: Bankruptcy filed status - Empty: No bankruptcy
 | `[]` | `{}` |
    | `ACCOUNT_NUMBER` | 15 | `TEXT` | **Unique account identifier for credit bureau reporting.** Uses cleaned contract_id with hyphens  and spaces removed to create standardized account number format. This serves as the primary  account identifier for credit bureau systems and must remain consistent across all reporting periods.
 | **Unique account identifier for credit bureau reporting.** Uses cleaned contract_id with hyphens  and spaces removed to create standardized account number format. This serves as the primary  account identifier for credit bureau systems and must remain consistent across all reporting periods.
 | `[]` | `{}` |
    | `PORTFOLIO_TYPE` | 16 | `TEXT` | **Portfolio classification code (always 'I' for installment).** Fixed value indicating installment  loan type for credit bureau classification. Cherry's loans are installment loans as opposed to  revolving credit, so this field consistently reports 'I' for proper credit bureau categorization.
 | **Portfolio classification code (always 'I' for installment).** Fixed value indicating installment  loan type for credit bureau classification. Cherry's loans are installment loans as opposed to  revolving credit, so this field consistently reports 'I' for proper credit bureau categorization.
 | `[]` | `{}` |
    | `ACCOUNT_TYPE` | 17 | `TEXT` | **Credit account type code (always '06' for personal installment).** Standard credit bureau code  indicating personal installment loan type. This classification helps credit bureaus properly  categorize the account type for credit scoring and reporting purposes.
 | **Credit account type code (always '06' for personal installment).** Standard credit bureau code  indicating personal installment loan type. This classification helps credit bureaus properly  categorize the account type for credit scoring and reporting purposes.
 | `[]` | `{}` |
    | `DATE_OPEN` | 18 | `DATE` | **Loan origination/funding date.** The date when the loan was originally funded and became active.  This date establishes the beginning of the credit relationship and is used by credit bureaus for  account age calculations in credit scoring models.
 | **Loan origination/funding date.** The date when the loan was originally funded and became active.  This date establishes the beginning of the credit relationship and is used by credit bureaus for  account age calculations in credit scoring models.
 | `[]` | `{}` |
    | `DATE_OF_LAST_PAYMENT` | 19 | `DATE` | **Date of most recent payment received.** Pulled from most_recent_payments based on LoanPro payment  records, excluding debt sale payments. Critical for credit bureaus to understand payment activity  and account management. Null for accounts with no payments.
 | **Date of most recent payment received.** Pulled from most_recent_payments based on LoanPro payment  records, excluding debt sale payments. Critical for credit bureaus to understand payment activity  and account management. Null for accounts with no payments.
 | `[]` | `{}` |
    | `DATE_CLOSED` | 20 | `TIMESTAMP_NTZ` | **Account closure date with complex business logic.** Calculated based on multiple scenarios: - Debt sale date if sold to third party - Zero balance date for naturally paid accounts   - Null for active accounts - Null for do-not-report or certain charge-off scenarios This date informs credit bureaus when the account obligation ended.
 | **Account closure date with complex business logic.** Calculated based on multiple scenarios: - Debt sale date if sold to third party - Zero balance date for naturally paid accounts   - Null for active accounts - Null for do-not-report or certain charge-off scenarios This date informs credit bureaus when the account obligation ended.
 | `[]` | `{}` |
    | `ACCOUNT_STATUS` | 21 | `TEXT` | **Primary credit bureau account status code.** Sophisticated cascading logic determines status: - DA: Do not report (borrower request/fraud) - DF: Fraud accounts - 11: Current with balance - 13: Closed/paid in full   - 64: Charged off, paid in full - 71: 30-59 days past due - 78: 60-89 days past due - 80: 90-119 days past due   - 82: 120+ days past due - 97: Active charge-off This code drives credit bureau interpretation and credit scoring impact.
 | **Primary credit bureau account status code.** Sophisticated cascading logic determines status: - DA: Do not report (borrower request/fraud) - DF: Fraud accounts - 11: Current with balance - 13: Closed/paid in full   - 64: Charged off, paid in full - 71: 30-59 days past due - 78: 60-89 days past due - 80: 90-119 days past due   - 82: 120+ days past due - 97: Active charge-off This code drives credit bureau interpretation and credit scoring impact.
 | `[]` | `{}` |
    | `PAYMENT_RATING` | 22 | `TEXT` | **Payment history quality rating for closed accounts.** Only applicable when account_status is in  ('13','65','88','89','94','95'). Ratings based on maximum DPD during loan lifecycle: - 0: Never late (max DPD < 30) - 1: 30-59 days late maximum - 2: 60-89 days late maximum   - 3: 90+ days late maximum - L: Charged off accounts paid in full Empty for active accounts. Critical for credit scoring of closed accounts.
 | **Payment history quality rating for closed accounts.** Only applicable when account_status is in  ('13','65','88','89','94','95'). Ratings based on maximum DPD during loan lifecycle: - 0: Never late (max DPD < 30) - 1: 30-59 days late maximum - 2: 60-89 days late maximum   - 3: 90+ days late maximum - L: Charged off accounts paid in full Empty for active accounts. Critical for credit scoring of closed accounts.
 | `[]` | `{}` |
    | `DATE_OF_FIRST_DELINQUENCY` | 23 | `TIMESTAMP_NTZ` | **First delinquency date for credit bureau timeline.** Complex calculation determining when account  first became delinquent (30+ DPD). Uses multiple data sources including daily_loan_xf first  delinquency tracking, bankruptcy dates, and charge-off dates. Critical for credit bureau timelines  and regulatory compliance. Null for accounts that never went delinquent.
 | **First delinquency date for credit bureau timeline.** Complex calculation determining when account  first became delinquent (30+ DPD). Uses multiple data sources including daily_loan_xf first  delinquency tracking, bankruptcy dates, and charge-off dates. Critical for credit bureau timelines  and regulatory compliance. Null for accounts that never went delinquent.
 | `[]` | `{}` |
    | `DAYS_PAST_DUE` | 24 | `NUMBER` | **Current days past due as of reporting date.** Shows DPD from daily_loan_xf on the effective  reporting date. Key metric for credit bureaus to understand current account status and risk level.  Zero for current accounts, positive integer for delinquent accounts.
 | **Current days past due as of reporting date.** Shows DPD from daily_loan_xf on the effective  reporting date. Key metric for credit bureaus to understand current account status and risk level.  Zero for current accounts, positive integer for delinquent accounts.
 | `[]` | `{}` |
    | `CREDIT_LIMIT` | 25 | `NUMBER` | **Credit limit (always 0 for installment loans).** Fixed at 0 because Cherry provides installment  loans with fixed amounts rather than revolving credit lines. This distinguishes installment loans  from credit cards and other revolving credit products.
 | **Credit limit (always 0 for installment loans).** Fixed at 0 because Cherry provides installment  loans with fixed amounts rather than revolving credit lines. This distinguishes installment loans  from credit cards and other revolving credit products.
 | `[]` | `{}` |
    | `HIGHEST_CREDIT` | 26 | `FLOAT` | **Original loan amount/highest credit extended.** Reports the original purchase_amount as the maximum  credit extended to the borrower. This amount represents the highest balance the account has ever  carried and is used by credit bureaus for utilization calculations and risk assessment.
 | **Original loan amount/highest credit extended.** Reports the original purchase_amount as the maximum  credit extended to the borrower. This amount represents the highest balance the account has ever  carried and is used by credit bureaus for utilization calculations and risk assessment.
 | `[]` | `{}` |
    | `CURRENT_BALANCE` | 27 | `NUMBER` | **Outstanding balance as of reporting date.** Complex calculation considering: - Zero for debt sale or closed accounts - Active charge-off amount for charged-off accounts   - Current payoff or principal balance for active accounts This balance represents the borrower's current obligation and impacts credit utilization metrics.
 | **Outstanding balance as of reporting date.** Complex calculation considering: - Zero for debt sale or closed accounts - Active charge-off amount for charged-off accounts   - Current payoff or principal balance for active accounts This balance represents the borrower's current obligation and impacts credit utilization metrics.
 | `[]` | `{}` |
    | `AMOUNT_PAST_DUE` | 28 | `NUMBER` | **Past due amount for delinquent accounts.** Calculated for accounts 30+ DPD using amount_past_due_thirty  from daily_loan_xf, with logic to ensure past due amount doesn't exceed current balance. Zero for  current accounts and closed/charged-off accounts. Critical for collections and credit bureau risk assessment.
 | **Past due amount for delinquent accounts.** Calculated for accounts 30+ DPD using amount_past_due_thirty  from daily_loan_xf, with logic to ensure past due amount doesn't exceed current balance. Zero for  current accounts and closed/charged-off accounts. Critical for collections and credit bureau risk assessment.
 | `[]` | `{}` |
    | `MONTHLY_PAYMENT` | 29 | `FLOAT` | **Scheduled monthly payment amount.** Reports the original installment_amount for active accounts.  Set to 0 for closed accounts (status 13) and charge-offs (status 97, 64) since no future payments  are expected. Used by credit bureaus for debt-to-income calculations and payment capacity assessment.
 | **Scheduled monthly payment amount.** Reports the original installment_amount for active accounts.  Set to 0 for closed accounts (status 13) and charge-offs (status 97, 64) since no future payments  are expected. Used by credit bureaus for debt-to-income calculations and payment capacity assessment.
 | `[]` | `{}` |
    | `ACTUAL_PAYMENT` | 30 | `NUMBER` | **Total payments received during reporting period.** Sums all payments from last_periods_payments  between the previous and current reporting dates. Reflects actual borrower payment behavior during  the reporting period. Zero if no payments were made during the period.
 | **Total payments received during reporting period.** Sums all payments from last_periods_payments  between the previous and current reporting dates. Reflects actual borrower payment behavior during  the reporting period. Zero if no payments were made during the period.
 | `[]` | `{}` |
    | `TERMS_FREQUENCY` | 31 | `TEXT` | **Payment frequency code (always 'M' for monthly).** Fixed value indicating monthly payment schedule  for all Cherry loans. This standardized frequency helps credit bureaus understand the payment  obligation schedule and calculate appropriate credit metrics.
 | **Payment frequency code (always 'M' for monthly).** Fixed value indicating monthly payment schedule  for all Cherry loans. This standardized frequency helps credit bureaus understand the payment  obligation schedule and calculate appropriate credit metrics.
 | `[]` | `{}` |
    | `TERMS` | 32 | `NUMBER` | **Loan term in months.** Reports the original loan term from loan_terms model, with preference for  application-based terms over LoanPro defaults. Represents the total number of scheduled monthly  payments when the loan was originated. Critical for credit bureau understanding of loan structure.
 | **Loan term in months.** Reports the original loan term from loan_terms model, with preference for  application-based terms over LoanPro defaults. Represents the total number of scheduled monthly  payments when the loan was originated. Critical for credit bureau understanding of loan structure.
 | `[]` | `{}` |
    | `ORIGINAL_CHARGE_OFF_AMOUNT` | 33 | `NUMBER` | **Total amount charged off.** Reports total_chargeoff from charge_off_totals aggregation, representing  the full amount written off when the account was charged off. This includes principal, interest,  and fees that were deemed uncollectible. Null for accounts never charged off.
 | **Total amount charged off.** Reports total_chargeoff from charge_off_totals aggregation, representing  the full amount written off when the account was charged off. This includes principal, interest,  and fees that were deemed uncollectible. Null for accounts never charged off.
 | `[]` | `{}` |
    | `ORIGINAL_CHARGE_OFF_DATE` | 34 | `DATE` | **Date of first charge-off transaction.** Reports the earliest charge-off date from  first_charge_off_transaction_date. Establishes the timeline for charge-off reporting and recovery  tracking. Critical for credit bureau charge-off timeline compliance.
 | **Date of first charge-off transaction.** Reports the earliest charge-off date from  first_charge_off_transaction_date. Establishes the timeline for charge-off reporting and recovery  tracking. Critical for credit bureau charge-off timeline compliance.
 | `[]` | `{}` |
    | `DATE_OF_ACCOUNT_INFORMATION` | 35 | `TIMESTAMP_NTZ` | **As-of date for all account information.** Complex calculation providing the effective date for  all reported data: - Debt sale date for sold accounts - Latest of closure date or last payment date for closed accounts   - Effective reporting date for active accounts This date tells credit bureaus when the account information was current and accurate. | **As-of date for all account information.** Complex calculation providing the effective date for  all reported data: - Debt sale date for sold accounts - Latest of closure date or last payment date for closed accounts   - Effective reporting date for active accounts This date tells credit bureaus when the account information was current and accurate. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.applications_loans_xf`
    *   `model.cherry_data_model.borrowers_merged_emails_xf`
    *   `model.cherry_data_model.calendar_table_xf`
    *   `model.cherry_data_model.daily_loan_xf`
    *   `model.cherry_data_model.int_funded_information_pt`
    *   `model.cherry_data_model.int_servicing_bankruptcies`
    *   `model.cherry_data_model.loan_info_xf`
    *   `model.cherry_data_model.src_borrower_addresses`
    *   `model.cherry_data_model.src_borrowers`
    *   `model.cherry_data_model.src_cherry_loans`
    *   `model.cherry_data_model.src_debt_sale_transactions`
    *   `model.cherry_data_model.src_due_date_changes`
    *   `model.cherry_data_model.src_loan_plans`
    *   `model.cherry_data_model.src_loan_schedule`
    *   `model.cherry_data_model.src_loanpro_chargeoff_transactions`
    *   `model.cherry_data_model.stg_active_loanpro_payments`
    *   `model.cherry_data_model.stg_borrower_addresses_with_tz`
    *   `model.cherry_data_model.stg_loanpro_chargeoffs_aggregation`
    *   `source.cherry_data_model.cherry_data.loan_status_history`

---
