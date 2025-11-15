## Model: `lp_period_xf`

`lp_period_xf`

*   **Unique ID:** `model.cherry_data_model.lp_period_xf`
*   **FQN:** `prod.risk_marts.lp_period_xf`
*   **Description:** **Enhanced LoanPro Period Analytics with Cumulative Performance Metrics**
This model extends the staging `stg_lp_period` table by adding cumulative calculations across loan  lifecycles using window functions. It serves as Cherry's comprehensive loan period performance  tracking table for vintage analysis, loss rate calculations, and longitudinal loan performance  measurement at the individual loan level.
**Key Business Logic:** - **Cumulative Calculations**: Adds running totals for finance charges, principal payments, fees, 
  charge-offs, and recoveries using window functions partitioned by loan_id and ordered by periods_on_book
- **Period Structure**: Each loan gets one record per period (typically monthly) from funding through 
  current period, enabling vintage-level performance analysis
- **Risk Performance Metrics**: Tracks cumulative charge-offs by category (fraud, bankruptcy, deceased, 
  early vs. total) and recoveries for comprehensive loss analysis
- **Payment Tracking**: Captures both period-specific and cumulative payment activity including 
  pre-payments, minimum payments, and principal collections

**Critical Data Sources:** - `stg_lp_period`: Base period structure with all non-cumulative metrics from LoanPro period data, 
  daily loan snapshots, payments, fees, charge-offs, and recoveries
- `int_adjusted_lp_periods`: Period skeleton providing loan lifecycle structure and period boundaries - Multiple intermediate models for payments, fees, adjustments, and charge-off data aggregation
**Primary Use Cases:** - Vintage (origination month) level loss rate and performance analysis - Longitudinal tracking of loan performance across loan lifecycles   - Cumulative loss analysis and charge-off rate calculations by loan and vintage - Pre-payment rate analysis and payment behavior measurement - Credit risk assessment and portfolio performance monitoring

*   **Tags:** `['risk', 'performance_data', 'lp_period']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `ROW_KEY` | 1 | `TEXT` | **Unique Row Identifier**
Surrogate key generated using dbt_utils to provide unique identification for each loan-period  combination. Originally created in int_adjusted_lp_periods using loan_id and periods_on_book  values, then carried forward for row identification and testing uniqueness across the lp_period  model tree.
 | **Unique Row Identifier**
Surrogate key generated using dbt_utils to provide unique identification for each loan-period  combination. Originally created in int_adjusted_lp_periods using loan_id and periods_on_book  values, then carried forward for row identification and testing uniqueness across the lp_period  model tree.
 | `[]` | `{}` |
    | `LOAN_ID` | 2 | `NUMBER` | **Cherry Loan Identifier**
Cherry's internal unique identifier for the loan contract. Used as the primary partitioning  key for cumulative calculations and the main dimension for loan-level analysis. Links to  other Cherry loan tables and serves as the primary key for loan tracking.
 | **Cherry Loan Identifier**
Cherry's internal unique identifier for the loan contract. Used as the primary partitioning  key for cumulative calculations and the main dimension for loan-level analysis. Links to  other Cherry loan tables and serves as the primary key for loan tracking.
 | `[]` | `{}` |
    | `LOANPRO_LOAN_ID` | 3 | `NUMBER` | **LoanPro System Identifier**
External identifier from the LoanPro loan management system. Used for joining to LoanPro  source data including payments, fees, and account adjustments. Critical for linking period  data back to operational loan management activities.
 | **LoanPro System Identifier**
External identifier from the LoanPro loan management system. Used for joining to LoanPro  source data including payments, fees, and account adjustments. Critical for linking period  data back to operational loan management activities.
 | `[]` | `{}` |
    | `CONTRACT_ID` | 4 | `TEXT` | **Contract Identifier**
Unique identifier for the loan contract document. Links the period performance data to the  original contract terms and serves as an additional identifier for contract-level analysis  and reporting.
 | **Contract Identifier**
Unique identifier for the loan contract document. Links the period performance data to the  original contract terms and serves as an additional identifier for contract-level analysis  and reporting.
 | `[]` | `{}` |
    | `FUNDED_DATE` | 5 | `DATE` | **Loan Funding Date**
The date when the loan was originally funded and disbursed to the borrower. Used as the  start point for period calculations and vintage analysis. Critical for determining loan  age and performance timing analysis.
 | **Loan Funding Date**
The date when the loan was originally funded and disbursed to the borrower. Used as the  start point for period calculations and vintage analysis. Critical for determining loan  age and performance timing analysis.
 | `[]` | `{}` |
    | `PERIODS_ON_BOOK` | 6 | `NUMBER` | **Period Number (Loan Age)**
Sequential period number indicating how many periods the loan has been active since funding.  Typically represents months on book. Used as the ordering dimension for cumulative calculations  and for vintage performance analysis at specific loan ages.
 | **Period Number (Loan Age)**
Sequential period number indicating how many periods the loan has been active since funding.  Typically represents months on book. Used as the ordering dimension for cumulative calculations  and for vintage performance analysis at specific loan ages.
 | `[]` | `{}` |
    | `SCHEDULED_PAYMENT_DATE` | 7 | `DATE` | **Scheduled Payment Due Date**
The date when a payment was originally scheduled to be due for this period. May be null  for periods beyond the original loan term when loans are extended or in special arrangements.  Used for delinquency calculations and payment timing analysis.
 | **Scheduled Payment Due Date**
The date when a payment was originally scheduled to be due for this period. May be null  for periods beyond the original loan term when loans are extended or in special arrangements.  Used for delinquency calculations and payment timing analysis.
 | `[]` | `{}` |
    | `SCHEDULED_PAYMENT_AMOUNT` | 8 | `NUMBER` | **Scheduled Payment Amount**
The dollar amount that was originally scheduled to be paid during this period according  to the loan terms. Used for payment variance analysis and understanding planned vs. actual  payment performance. In USD.
 | **Scheduled Payment Amount**
The dollar amount that was originally scheduled to be paid during this period according  to the loan terms. Used for payment variance analysis and understanding planned vs. actual  payment performance. In USD.
 | `[]` | `{}` |
    | `START_PERIOD` | 9 | `DATE` | **Period Start Date**
The first day of this loan period, typically one day after the previous period ended.  For the first period, this is set to the loan funding date. Used for determining which  transactions and events fall within each period.
 | **Period Start Date**
The first day of this loan period, typically one day after the previous period ended.  For the first period, this is set to the loan funding date. Used for determining which  transactions and events fall within each period.
 | `[]` | `{}` |
    | `END_PERIOD` | 10 | `DATE` | **Period End Date**
The last day of this loan period, typically aligned with monthly boundaries. Used for  determining which transactions and events fall within each period and for period-based  aggregations and reporting.
 | **Period End Date**
The last day of this loan period, typically aligned with monthly boundaries. Used for  determining which transactions and events fall within each period and for period-based  aggregations and reporting.
 | `[]` | `{}` |
    | `CO_DATE` | 11 | `DATE` |  |  | `[]` | `{}` |
    | `DPD_BOP` | 12 | `NUMBER` | **Days Past Due - Beginning of Period**
Number of days the loan was delinquent at the start of this period. For the first period,  uses data from the first loan record. Set to 0 if the loan was charged off before this  period started. Used for delinquency trend analysis and payment behavior measurement.
 | **Days Past Due - Beginning of Period**
Number of days the loan was delinquent at the start of this period. For the first period,  uses data from the first loan record. Set to 0 if the loan was charged off before this  period started. Used for delinquency trend analysis and payment behavior measurement.
 | `[]` | `{}` |
    | `PRINCIPAL_BALANCE_BOP` | 13 | `NUMBER` | **Principal Balance - Beginning of Period**
Outstanding principal balance on the loan at the start of this period. For the first period,  uses the original loan amount. Set to 0 if charged off before this period. Used for calculating  principal reduction and payment application analysis. In USD.
 | **Principal Balance - Beginning of Period**
Outstanding principal balance on the loan at the start of this period. For the first period,  uses the original loan amount. Set to 0 if charged off before this period. Used for calculating  principal reduction and payment application analysis. In USD.
 | `[]` | `{}` |
    | `INTEREST_DUE_BOP` | 14 | `NUMBER` | **Interest Due - Beginning of Period**
Amount of interest that was due/accrued at the start of this period. Set to 0 if charged  off before this period. Used for interest collection analysis and payment application  calculations. In USD.
 | **Interest Due - Beginning of Period**
Amount of interest that was due/accrued at the start of this period. Set to 0 if charged  off before this period. Used for interest collection analysis and payment application  calculations. In USD.
 | `[]` | `{}` |
    | `FEES_BALANCE_BOP` | 15 | `NUMBER` | **Fees Balance - Beginning of Period**
Outstanding fees balance (late fees, processing fees, etc.) at the start of this period.  Set to 0 if charged off before this period. Used for fee collection analysis and payment  application tracking. In USD.
 | **Fees Balance - Beginning of Period**
Outstanding fees balance (late fees, processing fees, etc.) at the start of this period.  Set to 0 if charged off before this period. Used for fee collection analysis and payment  application tracking. In USD.
 | `[]` | `{}` |
    | `NEXT_PAYMENT_AMOUNT_BOP` | 16 | `NUMBER` | **Next Payment Amount - Beginning of Period**
The amount that was due for the next payment at the start of this period. Set to 0 if  charged off before this period. Used for payment adequacy analysis and comparing scheduled  vs. actual payments. In USD.
 | **Next Payment Amount - Beginning of Period**
The amount that was due for the next payment at the start of this period. Set to 0 if  charged off before this period. Used for payment adequacy analysis and comparing scheduled  vs. actual payments. In USD.
 | `[]` | `{}` |
    | `PI_DUE_BOP` | 17 | `NUMBER` | **Principal and Interest Due - Beginning of Period**
Combined principal and interest amount that was due at the start of this period, excluding  fees. Set to 0 if charged off before this period. Used for core payment obligation analysis.  In USD.
 | **Principal and Interest Due - Beginning of Period**
Combined principal and interest amount that was due at the start of this period, excluding  fees. Set to 0 if charged off before this period. Used for core payment obligation analysis.  In USD.
 | `[]` | `{}` |
    | `DPD_EOP` | 18 | `NUMBER` | **Days Past Due - End of Period**
Number of days the loan was delinquent at the end of this period. Set to 0 if the loan  was charged off during or before this period. Used for delinquency progression analysis  and determining payment effectiveness within the period.
 | **Days Past Due - End of Period**
Number of days the loan was delinquent at the end of this period. Set to 0 if the loan  was charged off during or before this period. Used for delinquency progression analysis  and determining payment effectiveness within the period.
 | `[]` | `{}` |
    | `PRINCIPAL_BALANCE_EOP` | 19 | `NUMBER` | **Principal Balance - End of Period**
Outstanding principal balance on the loan at the end of this period after all payments  and adjustments. Set to 0 if charged off during or before this period. Used for period-end  position analysis and principal reduction tracking. In USD.
 | **Principal Balance - End of Period**
Outstanding principal balance on the loan at the end of this period after all payments  and adjustments. Set to 0 if charged off during or before this period. Used for period-end  position analysis and principal reduction tracking. In USD.
 | `[]` | `{}` |
    | `INTEREST_DUE_EOP` | 20 | `NUMBER` | **Interest Due - End of Period**
Amount of interest that was due/accrued at the end of this period. Set to 0 if charged  off during or before this period. Used for interest accrual and collection analysis. In USD.
 | **Interest Due - End of Period**
Amount of interest that was due/accrued at the end of this period. Set to 0 if charged  off during or before this period. Used for interest accrual and collection analysis. In USD.
 | `[]` | `{}` |
    | `FEES_BALANCE_EOP` | 21 | `NUMBER` | **Fees Balance - End of Period**
Outstanding fees balance at the end of this period after any fees assessed, waived, or  collected. Set to 0 if charged off during or before this period. Used for fee management  and collection effectiveness analysis. In USD.
 | **Fees Balance - End of Period**
Outstanding fees balance at the end of this period after any fees assessed, waived, or  collected. Set to 0 if charged off during or before this period. Used for fee management  and collection effectiveness analysis. In USD.
 | `[]` | `{}` |
    | `NEXT_PAYMENT_AMOUNT_EOP` | 22 | `NUMBER` | **Next Payment Amount - End of Period**
The amount that was due for the next payment at the end of this period. Set to 0 if  charged off during or before this period. Used for forward-looking payment analysis  and loan servicing requirements. In USD.
 | **Next Payment Amount - End of Period**
The amount that was due for the next payment at the end of this period. Set to 0 if  charged off during or before this period. Used for forward-looking payment analysis  and loan servicing requirements. In USD.
 | `[]` | `{}` |
    | `PI_DUE_EOP` | 23 | `NUMBER` | **Principal and Interest Due - End of Period**
Combined principal and interest amount that was due at the end of this period. Set to 0  if charged off during or before this period. Used for core payment obligation tracking  and payment adequacy analysis. In USD.
 | **Principal and Interest Due - End of Period**
Combined principal and interest amount that was due at the end of this period. Set to 0  if charged off during or before this period. Used for core payment obligation tracking  and payment adequacy analysis. In USD.
 | `[]` | `{}` |
    | `DQ_BUCKET` | 24 | `NUMBER` | **Delinquency Bucket**
Delinquency category at the end of the period (0=Current, 1=30-59 days, 2=60-89 days,  3=90-119 days, 4=120+ days). Set to 0 if charged off during or before this period.  Used for delinquency distribution analysis and risk categorization.
 | **Delinquency Bucket**
Delinquency category at the end of the period (0=Current, 1=30-59 days, 2=60-89 days,  3=90-119 days, 4=120+ days). Set to 0 if charged off during or before this period.  Used for delinquency distribution analysis and risk categorization.
 | `[]` | `{}` |
    | `C1CDQ` | 25 | `NUMBER` | **Current Delinquent 1 (30-59 days)**
Principal balance if the loan was in the 30-59 day delinquency bucket at period end,  0 otherwise. Only counts if not charged off during this period. Used for delinquency  aging analysis and calculating vintage delinquency rates by bucket. In USD.
 | **Current Delinquent 1 (30-59 days)**
Principal balance if the loan was in the 30-59 day delinquency bucket at period end,  0 otherwise. Only counts if not charged off during this period. Used for delinquency  aging analysis and calculating vintage delinquency rates by bucket. In USD.
 | `[]` | `{}` |
    | `C2CDQ` | 26 | `NUMBER` | **Current Delinquent 2 (60-89 days)**
Principal balance if the loan was in the 60-89 day delinquency bucket at period end,  0 otherwise. Only counts if not charged off during this period. Used for tracking  progression into deeper delinquency stages. In USD.
 | **Current Delinquent 2 (60-89 days)**
Principal balance if the loan was in the 60-89 day delinquency bucket at period end,  0 otherwise. Only counts if not charged off during this period. Used for tracking  progression into deeper delinquency stages. In USD.
 | `[]` | `{}` |
    | `C3CDQ` | 27 | `NUMBER` | **Current Delinquent 3 (90-119 days)**
Principal balance if the loan was in the 90-119 day delinquency bucket at period end,  0 otherwise. Only counts if not charged off during this period. Used for pre-charge-off  delinquency analysis and collection effectiveness measurement. In USD.
 | **Current Delinquent 3 (90-119 days)**
Principal balance if the loan was in the 90-119 day delinquency bucket at period end,  0 otherwise. Only counts if not charged off during this period. Used for pre-charge-off  delinquency analysis and collection effectiveness measurement. In USD.
 | `[]` | `{}` |
    | `C4CDQ` | 28 | `NUMBER` | **Current Delinquent 4 (120+ days)**
Principal balance if the loan was in the 120+ day delinquency bucket at period end,  0 otherwise. Only counts if not charged off during this period. Used for severe delinquency  tracking and charge-off timing analysis. In USD.
 | **Current Delinquent 4 (120+ days)**
Principal balance if the loan was in the 120+ day delinquency bucket at period end,  0 otherwise. Only counts if not charged off during this period. Used for severe delinquency  tracking and charge-off timing analysis. In USD.
 | `[]` | `{}` |
    | `FC_ASSESSED` | 29 | `NUMBER` | **Finance Charges Assessed**
Total finance charges (interest) assessed during this period based on the loan's APR  and outstanding balance. Sourced from cumulative daily loan calculations aggregated  by period. Used for revenue recognition and interest income analysis. In USD.
 | **Finance Charges Assessed**
Total finance charges (interest) assessed during this period based on the loan's APR  and outstanding balance. Sourced from cumulative daily loan calculations aggregated  by period. Used for revenue recognition and interest income analysis. In USD.
 | `[]` | `{}` |
    | `FC_COLLECTED` | 30 | `NUMBER` | **Finance Charges Collected**
Total finance charges (interest) actually collected from borrower payments during this  period. Sourced from payment data aggregated by period. Used for interest collection  rate analysis and payment application tracking. In USD.
 | **Finance Charges Collected**
Total finance charges (interest) actually collected from borrower payments during this  period. Sourced from payment data aggregated by period. Used for interest collection  rate analysis and payment application tracking. In USD.
 | `[]` | `{}` |
    | `FEES_ASSESSED` | 31 | `NUMBER` | **Fees Assessed**
Total fees (late fees, processing fees, etc.) assessed during this period. Sourced from  LoanPro fee data aggregated by period. Used for fee revenue analysis and fee assessment  pattern tracking. In USD.
 | **Fees Assessed**
Total fees (late fees, processing fees, etc.) assessed during this period. Sourced from  LoanPro fee data aggregated by period. Used for fee revenue analysis and fee assessment  pattern tracking. In USD.
 | `[]` | `{}` |
    | `FEES_WAIVED` | 32 | `NUMBER` | **Fees Waived**
Total fees that were waived during this period as part of customer service or collection  strategies. Sourced from LoanPro fee waiver data. Used for fee waiver analysis and  customer service cost measurement. In USD.
 | **Fees Waived**
Total fees that were waived during this period as part of customer service or collection  strategies. Sourced from LoanPro fee waiver data. Used for fee waiver analysis and  customer service cost measurement. In USD.
 | `[]` | `{}` |
    | `FEES_COLLECTED` | 33 | `NUMBER` | **Fees Collected**
Total fees actually collected from borrower payments during this period. Sourced from  payment data showing fee portions of payments. Used for fee collection effectiveness  analysis and payment application tracking. In USD.
 | **Fees Collected**
Total fees actually collected from borrower payments during this period. Sourced from  payment data showing fee portions of payments. Used for fee collection effectiveness  analysis and payment application tracking. In USD.
 | `[]` | `{}` |
    | `PRINCIPAL_COLLECTED` | 34 | `NUMBER` | **Principal Collected**
Total principal amount collected from borrower payments during this period. Sourced from  payment data showing principal portions of payments. Used for principal paydown analysis  and payment application tracking. In USD.
 | **Principal Collected**
Total principal amount collected from borrower payments during this period. Sourced from  payment data showing principal portions of payments. Used for principal paydown analysis  and payment application tracking. In USD.
 | `[]` | `{}` |
    | `TOTAL_PMT_DUE` | 35 | `NUMBER` | **Total Payment Due**
Total amount that was due to be paid during this period, calculated as the greater of  next_payment_amount or pi_due from the beginning of period data. Set to 0 if no amount  was due. Used for payment adequacy analysis and comparing scheduled vs. actual payments. In USD.
 | **Total Payment Due**
Total amount that was due to be paid during this period, calculated as the greater of  next_payment_amount or pi_due from the beginning of period data. Set to 0 if no amount  was due. Used for payment adequacy analysis and comparing scheduled vs. actual payments. In USD.
 | `[]` | `{}` |
    | `PRE_PMT` | 36 | `NUMBER` | **Pre-Payment Amount**
Amount paid above the required minimum payment during this period, excluding processing  fees. Set to 0 if pre-payment equals processing fees charged. Used for pre-payment behavior  analysis and borrower payment pattern assessment. In USD.
 | **Pre-Payment Amount**
Amount paid above the required minimum payment during this period, excluding processing  fees. Set to 0 if pre-payment equals processing fees charged. Used for pre-payment behavior  analysis and borrower payment pattern assessment. In USD.
 | `[]` | `{}` |
    | `MIN_PMT` | 37 | `NUMBER` | **Minimum Payment**
Minimum required payment amount for this period. Used for payment adequacy analysis  and determining if borrowers are meeting minimum payment obligations. In USD.
 | **Minimum Payment**
Minimum required payment amount for this period. Used for payment adequacy analysis  and determining if borrowers are meeting minimum payment obligations. In USD.
 | `[]` | `{}` |
    | `TOTAL_BALANCE_ADJ` | 38 | `NUMBER` | **Total Balance Adjustments**
Total balance adjustments (positive or negative) applied to the loan during this period.  Sourced from LoanPro adjustment data aggregated by period. Used for tracking manual  adjustments and account maintenance activities. In USD.
 | **Total Balance Adjustments**
Total balance adjustments (positive or negative) applied to the loan during this period.  Sourced from LoanPro adjustment data aggregated by period. Used for tracking manual  adjustments and account maintenance activities. In USD.
 | `[]` | `{}` |
    | `PRINCIPAL_BALANCE_ADJ` | 39 | `NUMBER` | **Principal Balance Adjustments**
Principal-specific balance adjustments applied to the loan during this period. Subset  of total_balance_adj focusing only on principal adjustments. Used for principal adjustment  analysis and tracking principal write-offs or corrections. In USD.
 | **Principal Balance Adjustments**
Principal-specific balance adjustments applied to the loan during this period. Subset  of total_balance_adj focusing only on principal adjustments. Used for principal adjustment  analysis and tracking principal write-offs or corrections. In USD.
 | `[]` | `{}` |
    | `CHARGE_OFF_DATE` | 40 | `DATE` | **Charge-Off Date for Period**
The charge-off date if the loan was charged off during this specific period, null otherwise.  Used for identifying the exact period when charge-off occurred and for charge-off timing  analysis. Only populated in the period when charge-off actually happened.
 | **Charge-Off Date for Period**
The charge-off date if the loan was charged off during this specific period, null otherwise.  Used for identifying the exact period when charge-off occurred and for charge-off timing  analysis. Only populated in the period when charge-off actually happened.
 | `[]` | `{}` |
    | `GUCO_FRAUD` | 41 | `NUMBER` | **Gross Charge-Off - Fraud**
Gross charge-off amount attributable to fraud if the loan was charged off during this  period, 0 otherwise. Used for fraud loss analysis and charge-off reason categorization.  Part of the total GUCO amount. In USD.
 | **Gross Charge-Off - Fraud**
Gross charge-off amount attributable to fraud if the loan was charged off during this  period, 0 otherwise. Used for fraud loss analysis and charge-off reason categorization.  Part of the total GUCO amount. In USD.
 | `[]` | `{}` |
    | `GUCO_BK` | 42 | `NUMBER` | **Gross Charge-Off - Bankruptcy**
Gross charge-off amount attributable to bankruptcy if the loan was charged off during  this period, 0 otherwise. Used for bankruptcy loss analysis and understanding legal  collection limitations. Part of the total GUCO amount. In USD.
 | **Gross Charge-Off - Bankruptcy**
Gross charge-off amount attributable to bankruptcy if the loan was charged off during  this period, 0 otherwise. Used for bankruptcy loss analysis and understanding legal  collection limitations. Part of the total GUCO amount. In USD.
 | `[]` | `{}` |
    | `GUCO_DECEASED` | 43 | `NUMBER` | **Gross Charge-Off - Deceased**
Gross charge-off amount attributable to borrower death if the loan was charged off during  this period, 0 otherwise. Used for deceased borrower loss analysis and estate collection  tracking. Part of the total GUCO amount. In USD.
 | **Gross Charge-Off - Deceased**
Gross charge-off amount attributable to borrower death if the loan was charged off during  this period, 0 otherwise. Used for deceased borrower loss analysis and estate collection  tracking. Part of the total GUCO amount. In USD.
 | `[]` | `{}` |
    | `GUCO_E` | 44 | `NUMBER` | **Gross Charge-Off - Early**
Early gross charge-off amount if the loan was charged off during this period, 0 otherwise.  Represents charge-offs that occurred before the standard charge-off timeline. Used for  early charge-off analysis and policy evaluation. In USD.
 | **Gross Charge-Off - Early**
Early gross charge-off amount if the loan was charged off during this period, 0 otherwise.  Represents charge-offs that occurred before the standard charge-off timeline. Used for  early charge-off analysis and policy evaluation. In USD.
 | `[]` | `{}` |
    | `GUCO_T` | 45 | `NUMBER` | **Gross Charge-Off - Total Timeline**
Total timeline gross charge-off amount if the loan was charged off during this period,  0 otherwise. Represents charge-offs that occurred according to standard charge-off timeline.  Used for standard charge-off analysis. In USD.
 | **Gross Charge-Off - Total Timeline**
Total timeline gross charge-off amount if the loan was charged off during this period,  0 otherwise. Represents charge-offs that occurred according to standard charge-off timeline.  Used for standard charge-off analysis. In USD.
 | `[]` | `{}` |
    | `GUCO` | 46 | `NUMBER` | **Gross Charge-Off - Total**
Total gross charge-off amount if the loan was charged off during this period, 0 otherwise.  Represents the full outstanding balance at charge-off before any recoveries. Used for  gross loss analysis and charge-off reporting. In USD.
 | **Gross Charge-Off - Total**
Total gross charge-off amount if the loan was charged off during this period, 0 otherwise.  Represents the full outstanding balance at charge-off before any recoveries. Used for  gross loss analysis and charge-off reporting. In USD.
 | `[]` | `{}` |
    | `GACO_FRAUD` | 47 | `NUMBER` | **Gross Amount Charged Off - Fraud**
GACO fraud amount if the loan was charged off during this period, 0 otherwise. Similar  to GUCO but may use different calculation methodology. Used for fraud-specific GACO  analysis and regulatory reporting. In USD.
 | **Gross Amount Charged Off - Fraud**
GACO fraud amount if the loan was charged off during this period, 0 otherwise. Similar  to GUCO but may use different calculation methodology. Used for fraud-specific GACO  analysis and regulatory reporting. In USD.
 | `[]` | `{}` |
    | `GACO_BK` | 48 | `NUMBER` | **Gross Amount Charged Off - Bankruptcy**
GACO bankruptcy amount if the loan was charged off during this period, 0 otherwise.  Used for bankruptcy-specific GACO analysis and understanding legal recovery limitations.  In USD.
 | **Gross Amount Charged Off - Bankruptcy**
GACO bankruptcy amount if the loan was charged off during this period, 0 otherwise.  Used for bankruptcy-specific GACO analysis and understanding legal recovery limitations.  In USD.
 | `[]` | `{}` |
    | `GACO_DECEASED` | 49 | `NUMBER` | **Gross Amount Charged Off - Deceased**
GACO deceased amount if the loan was charged off during this period, 0 otherwise. Used  for deceased borrower GACO analysis and estate collection strategy evaluation. In USD.
 | **Gross Amount Charged Off - Deceased**
GACO deceased amount if the loan was charged off during this period, 0 otherwise. Used  for deceased borrower GACO analysis and estate collection strategy evaluation. In USD.
 | `[]` | `{}` |
    | `GACO_E` | 50 | `NUMBER` | **Gross Amount Charged Off - Early**
Early GACO amount if the loan was charged off during this period, 0 otherwise. Used  for early GACO analysis and comparing early vs. standard timeline charge-off patterns.  In USD.
 | **Gross Amount Charged Off - Early**
Early GACO amount if the loan was charged off during this period, 0 otherwise. Used  for early GACO analysis and comparing early vs. standard timeline charge-off patterns.  In USD.
 | `[]` | `{}` |
    | `GACO_T` | 51 | `NUMBER` | **Gross Amount Charged Off - Total Timeline**
Total timeline GACO amount if the loan was charged off during this period, 0 otherwise.  Used for standard timeline GACO analysis and regulatory reporting requirements. In USD.
 | **Gross Amount Charged Off - Total Timeline**
Total timeline GACO amount if the loan was charged off during this period, 0 otherwise.  Used for standard timeline GACO analysis and regulatory reporting requirements. In USD.
 | `[]` | `{}` |
    | `GACO` | 52 | `NUMBER` | **Gross Amount Charged Off - Total**
Total GACO amount if the loan was charged off during this period, 0 otherwise. Represents  the total gross amount charged off according to GACO methodology. Used for GACO reporting  and loss analysis. In USD.
 | **Gross Amount Charged Off - Total**
Total GACO amount if the loan was charged off during this period, 0 otherwise. Represents  the total gross amount charged off according to GACO methodology. Used for GACO reporting  and loss analysis. In USD.
 | `[]` | `{}` |
    | `RECOVERIES` | 53 | `NUMBER` | **Recoveries**
Total amount recovered during this period from collections activities on this loan.  Sourced from recovery data aggregated by period. Used for recovery rate analysis and  post-charge-off collection effectiveness measurement. In USD.
 | **Recoveries**
Total amount recovered during this period from collections activities on this loan.  Sourced from recovery data aggregated by period. Used for recovery rate analysis and  post-charge-off collection effectiveness measurement. In USD.
 | `[]` | `{}` |
    | `NACO` | 54 | `NUMBER` | **Net Amount Charged Off**
Net charge-off amount for this period, calculated as GACO minus recoveries if the loan  was charged off during this period. Represents the net loss after accounting for recoveries.  Used for net loss analysis and final loss rate calculations. In USD.
 | **Net Amount Charged Off**
Net charge-off amount for this period, calculated as GACO minus recoveries if the loan  was charged off during this period. Represents the net loss after accounting for recoveries.  Used for net loss analysis and final loss rate calculations. In USD.
 | `[]` | `{}` |
    | `AVG_PRINCIPAL_BALANCE` | 55 | `NUMBER` | **Average Principal Balance**
Average principal balance during this period, calculated from daily balance data aggregated  over the period. Used for yield calculations, average balance analysis, and interest  computation validation. In USD.
 | **Average Principal Balance**
Average principal balance during this period, calculated from daily balance data aggregated  over the period. Used for yield calculations, average balance analysis, and interest  computation validation. In USD.
 | `[]` | `{}` |
    | `CUM_FC_ASSESSED` | 56 | `NUMBER` | **Cumulative Finance Charges Assessed**
Running total of finance charges assessed from loan inception through this period.  Calculated using window function SUM() OVER (PARTITION BY loan_id ORDER BY periods_on_book).  Used for lifetime interest income analysis and loan profitability assessment. In USD.
 | **Cumulative Finance Charges Assessed**
Running total of finance charges assessed from loan inception through this period.  Calculated using window function SUM() OVER (PARTITION BY loan_id ORDER BY periods_on_book).  Used for lifetime interest income analysis and loan profitability assessment. In USD.
 | `[]` | `{}` |
    | `CUM_FC_COLLECTED` | 57 | `NUMBER` | **Cumulative Finance Charges Collected**
Running total of finance charges collected from loan inception through this period.  Used for cumulative interest collection analysis and comparing assessed vs. collected  interest over the loan lifecycle. In USD.
 | **Cumulative Finance Charges Collected**
Running total of finance charges collected from loan inception through this period.  Used for cumulative interest collection analysis and comparing assessed vs. collected  interest over the loan lifecycle. In USD.
 | `[]` | `{}` |
    | `CUM_PRINCIPAL_COLLECTED` | 58 | `NUMBER` | **Cumulative Principal Collected**
Running total of principal collected from loan inception through this period. Used for  principal paydown analysis, loan balance tracking, and calculating remaining principal  outstanding. In USD.
 | **Cumulative Principal Collected**
Running total of principal collected from loan inception through this period. Used for  principal paydown analysis, loan balance tracking, and calculating remaining principal  outstanding. In USD.
 | `[]` | `{}` |
    | `CUM_PRE_PMT` | 59 | `NUMBER` | **Cumulative Pre-Payments**
Running total of pre-payments made from loan inception through this period. Used for  cumulative pre-payment behavior analysis and understanding borrower payment patterns  over time. In USD.
 | **Cumulative Pre-Payments**
Running total of pre-payments made from loan inception through this period. Used for  cumulative pre-payment behavior analysis and understanding borrower payment patterns  over time. In USD.
 | `[]` | `{}` |
    | `CUM_MIN_PMT` | 60 | `NUMBER` | **Cumulative Minimum Payments**
Running total of minimum payments from loan inception through this period. Used for  tracking cumulative minimum payment obligations and payment compliance analysis. In USD.
 | **Cumulative Minimum Payments**
Running total of minimum payments from loan inception through this period. Used for  tracking cumulative minimum payment obligations and payment compliance analysis. In USD.
 | `[]` | `{}` |
    | `CUM_PRINCIPAL_BALANCE_ADJ` | 61 | `NUMBER` | **Cumulative Principal Balance Adjustments**
Running total of principal balance adjustments from loan inception through this period.  Used for tracking cumulative principal adjustments and their impact on loan balances  over time. In USD.
 | **Cumulative Principal Balance Adjustments**
Running total of principal balance adjustments from loan inception through this period.  Used for tracking cumulative principal adjustments and their impact on loan balances  over time. In USD.
 | `[]` | `{}` |
    | `CUM_TOTAL_BALANCE_ADJ` | 62 | `NUMBER` | **Cumulative Total Balance Adjustments**
Running total of all balance adjustments from loan inception through this period. Used  for comprehensive adjustment tracking and understanding total adjustment impact on loan  performance. In USD.
 | **Cumulative Total Balance Adjustments**
Running total of all balance adjustments from loan inception through this period. Used  for comprehensive adjustment tracking and understanding total adjustment impact on loan  performance. In USD.
 | `[]` | `{}` |
    | `CUM_FEES_ASSESSED` | 63 | `NUMBER` | **Cumulative Fees Assessed**
Running total of fees assessed from loan inception through this period. Used for cumulative  fee revenue analysis and tracking total fee burden on borrowers over loan lifecycle. In USD.
 | **Cumulative Fees Assessed**
Running total of fees assessed from loan inception through this period. Used for cumulative  fee revenue analysis and tracking total fee burden on borrowers over loan lifecycle. In USD.
 | `[]` | `{}` |
    | `CUM_FEES_WAIVED` | 64 | `NUMBER` | **Cumulative Fees Waived**
Running total of fees waived from loan inception through this period. Used for cumulative  fee waiver analysis and measuring customer service costs over loan lifecycle. In USD.
 | **Cumulative Fees Waived**
Running total of fees waived from loan inception through this period. Used for cumulative  fee waiver analysis and measuring customer service costs over loan lifecycle. In USD.
 | `[]` | `{}` |
    | `CUM_FEES_COLLECTED` | 65 | `NUMBER` | **Cumulative Fees Collected**
Running total of fees collected from loan inception through this period. Used for cumulative  fee collection analysis and measuring fee collection effectiveness over time. In USD.
 | **Cumulative Fees Collected**
Running total of fees collected from loan inception through this period. Used for cumulative  fee collection analysis and measuring fee collection effectiveness over time. In USD.
 | `[]` | `{}` |
    | `CUM_GUCO_T` | 66 | `NUMBER` | **Cumulative GUCO Total Timeline**
Running total of GUCO total timeline amounts from loan inception through this period.  Used for cumulative charge-off analysis and vintage loss tracking. Typically only non-zero  in the period when charge-off occurs. In USD.
 | **Cumulative GUCO Total Timeline**
Running total of GUCO total timeline amounts from loan inception through this period.  Used for cumulative charge-off analysis and vintage loss tracking. Typically only non-zero  in the period when charge-off occurs. In USD.
 | `[]` | `{}` |
    | `CUM_GUCO_E` | 67 | `NUMBER` | **Cumulative GUCO Early**
Running total of GUCO early amounts from loan inception through this period. Used for  cumulative early charge-off analysis and tracking early charge-off patterns over vintage.  In USD.
 | **Cumulative GUCO Early**
Running total of GUCO early amounts from loan inception through this period. Used for  cumulative early charge-off analysis and tracking early charge-off patterns over vintage.  In USD.
 | `[]` | `{}` |
    | `CUM_GUCO` | 68 | `NUMBER` | **Cumulative GUCO Total**
Running total of total GUCO amounts from loan inception through this period. Used for  comprehensive cumulative gross charge-off analysis and lifetime loss tracking. In USD.
 | **Cumulative GUCO Total**
Running total of total GUCO amounts from loan inception through this period. Used for  comprehensive cumulative gross charge-off analysis and lifetime loss tracking. In USD.
 | `[]` | `{}` |
    | `CUM_GACO_T` | 69 | `NUMBER` | **Cumulative GACO Total Timeline**
Running total of GACO total timeline amounts from loan inception through this period.  Used for cumulative GACO analysis and regulatory reporting over loan lifecycle. In USD.
 | **Cumulative GACO Total Timeline**
Running total of GACO total timeline amounts from loan inception through this period.  Used for cumulative GACO analysis and regulatory reporting over loan lifecycle. In USD.
 | `[]` | `{}` |
    | `CUM_GACO_BK` | 70 | `NUMBER` | **Cumulative GACO Bankruptcy**
Running total of GACO bankruptcy amounts from loan inception through this period. Used  for cumulative bankruptcy-related GACO analysis and tracking bankruptcy loss patterns.  In USD.
 | **Cumulative GACO Bankruptcy**
Running total of GACO bankruptcy amounts from loan inception through this period. Used  for cumulative bankruptcy-related GACO analysis and tracking bankruptcy loss patterns.  In USD.
 | `[]` | `{}` |
    | `CUM_GACO_DECEASED` | 71 | `NUMBER` | **Cumulative GACO Deceased**
Running total of GACO deceased amounts from loan inception through this period. Used  for cumulative deceased borrower GACO analysis and estate collection performance tracking.  In USD.
 | **Cumulative GACO Deceased**
Running total of GACO deceased amounts from loan inception through this period. Used  for cumulative deceased borrower GACO analysis and estate collection performance tracking.  In USD.
 | `[]` | `{}` |
    | `CUM_GACO_FRAUD` | 72 | `NUMBER` | **Cumulative GACO Fraud**
Running total of GACO fraud amounts from loan inception through this period. Used for  cumulative fraud-related GACO analysis and fraud loss pattern assessment over vintage.  In USD.
 | **Cumulative GACO Fraud**
Running total of GACO fraud amounts from loan inception through this period. Used for  cumulative fraud-related GACO analysis and fraud loss pattern assessment over vintage.  In USD.
 | `[]` | `{}` |
    | `CUM_GACO_E` | 73 | `NUMBER` | **Cumulative GACO Early**
Running total of GACO early amounts from loan inception through this period. Used for  cumulative early GACO analysis and early charge-off pattern tracking over loan lifecycle.  In USD.
 | **Cumulative GACO Early**
Running total of GACO early amounts from loan inception through this period. Used for  cumulative early GACO analysis and early charge-off pattern tracking over loan lifecycle.  In USD.
 | `[]` | `{}` |
    | `CUM_GACO` | 74 | `NUMBER` | **Cumulative GACO Total**
Running total of total GACO amounts from loan inception through this period. Used for  comprehensive cumulative GACO analysis and lifetime GACO tracking for regulatory and  internal reporting. In USD.
 | **Cumulative GACO Total**
Running total of total GACO amounts from loan inception through this period. Used for  comprehensive cumulative GACO analysis and lifetime GACO tracking for regulatory and  internal reporting. In USD.
 | `[]` | `{}` |
    | `CUM_RECOVERIES` | 75 | `NUMBER` | **Cumulative Recoveries**
Running total of recoveries from loan inception through this period. Used for cumulative  recovery analysis and measuring total collection effectiveness over the loan lifecycle  including post-charge-off collections. In USD.
 | **Cumulative Recoveries**
Running total of recoveries from loan inception through this period. Used for cumulative  recovery analysis and measuring total collection effectiveness over the loan lifecycle  including post-charge-off collections. In USD.
 | `[]` | `{}` |
    | `CUM_NACO` | 76 | `NUMBER` | **Cumulative Net Amount Charged Off**
Running total of net charge-off amounts (GACO minus recoveries) from loan inception  through this period. Used for cumulative net loss analysis and final loss rate calculations  over vintage performance. In USD.
 | **Cumulative Net Amount Charged Off**
Running total of net charge-off amounts (GACO minus recoveries) from loan inception  through this period. Used for cumulative net loss analysis and final loss rate calculations  over vintage performance. In USD.
 | `[]` | `{}` |
    | `RUNNING_PRINCIPAL_BALANCE` | 77 | `NUMBER` | **Running Principal Balance**
Cumulative sum of average principal balances from loan inception through this period.  Used for weighted average balance calculations and comprehensive balance tracking across  the loan lifecycle. Not the same as outstanding balance. In USD. | **Running Principal Balance**
Cumulative sum of average principal balances from loan inception through this period.  Used for weighted average balance calculations and comprehensive balance tracking across  the loan lifecycle. Not the same as outstanding balance. In USD. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.stg_lp_period`

---
