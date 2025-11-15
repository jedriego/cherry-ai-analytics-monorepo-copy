## Model: `collections_inventory_by_bucket_xf`

`collections_inventory_by_bucket_xf`

*   **Unique ID:** `model.cherry_data_model.collections_inventory_by_bucket_xf`
*   **FQN:** `prod.servicing_marts.collections_inventory_by_bucket_xf`
*   **Description:** **Collections Inventory Analytics by Delinquency Bucket**
This comprehensive collections operations analytics model aggregates borrower inventory across  delinquency buckets, tracking contact eligibility, exclusion reasons, and penetration rates for  collections activities. The model serves as the primary dashboard for collections management by  combining complex business rules, regulatory compliance requirements, and state-specific contact  limitations to provide actionable insights for collections strategy and performance monitoring.
**Key Business Logic:** - **Delinquency Bucketing**: Groups borrowers into DPD ranges using sophisticated logic that accounts 
  for day-over-day changes and cured accounts (1-5, 6-29, 30-59, 60-89, 90-120 DPD)
- **Multi-Layer Exclusions**: Applies hierarchical exclusion logic covering status restrictions 
  (fraud, bankruptcy, deceased), engagement restrictions (pending payments, forbearance), and 
  compliance restrictions (RPC cooling periods, state-specific limits)
- **Contact Method Eligibility**: Determines eligibility for calls, SMS, and email based on consent, 
  unsubscribe status, and state-specific regulations (CA, MD, MN, SC, SD, DC, MA, NYC rules)
- **Penetration Analysis**: Calculates dial penetration rates and saturation metrics by state 
  contact limit categories (restricted vs unrestricted states)
- **Natural Disaster Protection**: Includes geographic exclusions for borrowers in declared 
  natural disaster areas (specific NC ZIP codes)

**Data Sources:** - **daily_loan_xf**: Core delinquency and loan status data for bucketing and filtering - **borrower_flags**: Status restrictions (do not call, bankruptcy, deceased, fraud flags) - **unsubscribed_borrowers_xf**: SMS/email consent and unsubscribe status tracking - **nice_collections_contacts_xf**: Historical collections contact data for compliance calculations - **omnichannel_collections_outbounds_xf**: Multi-channel contact history for volume limits - **stg_forbearances**: Active forbearance periods requiring contact suspension - **src_commitments**: Unfulfilled payment commitments affecting contact eligibility
**Primary Use Cases:** - Daily collections inventory management and capacity planning - Regulatory compliance monitoring and state-specific rule enforcement - Collections strategy optimization through penetration and saturation analysis - Exclusion reason tracking for operational efficiency improvements - Performance benchmarking across different delinquency stages
**Grain:** One record per record_date and dpd_bucket combination (daily aggregated metrics)

*   **Tags:** `['servicing_and_collections']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `RECORD_DATE` | 1 | `DATE` | **Report Date**
Date for which the collections inventory analysis is calculated, set to yesterday's date  (current_date - 1) to ensure complete data availability. Used as the primary date dimension  for time series analysis and daily collections planning.
 | **Report Date**
Date for which the collections inventory analysis is calculated, set to yesterday's date  (current_date - 1) to ensure complete data availability. Used as the primary date dimension  for time series analysis and daily collections planning.
 | `[]` | `{}` |
    | `DPD_BUCKET` | 2 | `TEXT` | **Delinquency Bucket**
Standardized delinquency ranges calculated using sophisticated day-over-day logic that  accounts for DPD changes and cured accounts. Buckets include: '1-5 dpd', '6-29 dpd',  '30-59 dpd', '60-89 dpd', '90-120 dpd'. The logic considers both current and previous day  DPD to properly classify borrowers who have cured or progressed in delinquency.
 | **Delinquency Bucket**
Standardized delinquency ranges calculated using sophisticated day-over-day logic that  accounts for DPD changes and cured accounts. Buckets include: '1-5 dpd', '6-29 dpd',  '30-59 dpd', '60-89 dpd', '90-120 dpd'. The logic considers both current and previous day  DPD to properly classify borrowers who have cured or progressed in delinquency.
 | `[]` | `{}` |
    | `BORROWER_COUNT` | 3 | `NUMBER` | **Total Borrower Inventory**
Total count of distinct borrowers in the delinquency bucket, representing the universe  of borrowers requiring collections attention. Calculated from borrowers with loans in  'Late' or 'Charged Off' status, excluding loans in 'Closed', 'Debt Sale', 'Settled',  or 'Bankruptcy' status.
 | **Total Borrower Inventory**
Total count of distinct borrowers in the delinquency bucket, representing the universe  of borrowers requiring collections attention. Calculated from borrowers with loans in  'Late' or 'Charged Off' status, excluding loans in 'Closed', 'Debt Sale', 'Settled',  or 'Bankruptcy' status.
 | `[]` | `{}` |
    | `DIALED_BORROWERS` | 4 | `NUMBER` | **Contacted Borrower Count**
Count of distinct borrowers who received dial attempts on the report date, derived from  actual contact activity across Nice collections dials and SafeSelect automated campaigns.  Used to calculate penetration rates and assess collections team productivity.
 | **Contacted Borrower Count**
Count of distinct borrowers who received dial attempts on the report date, derived from  actual contact activity across Nice collections dials and SafeSelect automated campaigns.  Used to calculate penetration rates and assess collections team productivity.
 | `[]` | `{}` |
    | `DIAL_COUNT` | 5 | `NUMBER` | **Total Dial Volume**
Total number of dial attempts made across all borrowers in the bucket, including multiple  attempts per borrower up to state-specific limits. Represents actual collections activity  volume and is used for capacity planning and performance measurement.
 | **Total Dial Volume**
Total number of dial attempts made across all borrowers in the bucket, including multiple  attempts per borrower up to state-specific limits. Represents actual collections activity  volume and is used for capacity planning and performance measurement.
 | `[]` | `{}` |
    | `EXCLUDED_BORROWER_COUNT` | 6 | `NUMBER` | **Excluded Borrower Count**
Count of borrowers excluded from collections contact due to any contact eligibility or  call eligibility restrictions. Includes all exclusions from status restrictions, compliance  violations, or state-specific contact limits.
 | **Excluded Borrower Count**
Count of borrowers excluded from collections contact due to any contact eligibility or  call eligibility restrictions. Includes all exclusions from status restrictions, compliance  violations, or state-specific contact limits.
 | `[]` | `{}` |
    | `VARIANCE_COUNT` | 7 | `NUMBER` | **Available Borrower Inventory**
Net available borrowers for collections contact, calculated as borrower_count minus  excluded_borrower_count. Represents the actionable inventory available for collections  efforts after all exclusions are applied.
 | **Available Borrower Inventory**
Net available borrowers for collections contact, calculated as borrower_count minus  excluded_borrower_count. Represents the actionable inventory available for collections  efforts after all exclusions are applied.
 | `[]` | `{}` |
    | `PENETRATION` | 8 | `NUMBER` | **Collections Penetration Rate**
Percentage of available borrowers who were contacted, calculated as dialed_borrowers  divided by variance_count. Key performance metric indicating how effectively the  collections team is reaching the available borrower population.
 | **Collections Penetration Rate**
Percentage of available borrowers who were contacted, calculated as dialed_borrowers  divided by variance_count. Key performance metric indicating how effectively the  collections team is reaching the available borrower population.
 | `[]` | `{}` |
    | `RESTRICTED_STATE_SATURATION` | 9 | `NUMBER` | **Restricted State Contact Saturation**
Average dial saturation for borrowers in states with 1-call-per-day limits (CA, MD, MN,  SC, SD), calculated as total dials divided by borrower count in restricted states.  Used to monitor compliance with state-specific contact frequency restrictions.
 | **Restricted State Contact Saturation**
Average dial saturation for borrowers in states with 1-call-per-day limits (CA, MD, MN,  SC, SD), calculated as total dials divided by borrower count in restricted states.  Used to monitor compliance with state-specific contact frequency restrictions.
 | `[]` | `{}` |
    | `UNRESTRICTED_STATE_SATURATION` | 10 | `NUMBER` | **Unrestricted State Contact Saturation**
Average dial saturation for borrowers in states allowing up to 4 calls per day, calculated  as total dials divided by borrower count in unrestricted states. Used to assess contact  efficiency in states with more permissive regulations.
 | **Unrestricted State Contact Saturation**
Average dial saturation for borrowers in states allowing up to 4 calls per day, calculated  as total dials divided by borrower count in unrestricted states. Used to assess contact  efficiency in states with more permissive regulations.
 | `[]` | `{}` |
    | `DNC_COUNT` | 11 | `NUMBER` | **Do Not Call Exclusions**
Count of borrowers excluded due to do_not_call flag being TRUE. Represents borrowers who  have explicitly requested not to be contacted by phone, requiring compliance for regulatory  and customer satisfaction reasons.
 | **Do Not Call Exclusions**
Count of borrowers excluded due to do_not_call flag being TRUE. Represents borrowers who  have explicitly requested not to be contacted by phone, requiring compliance for regulatory  and customer satisfaction reasons.
 | `[]` | `{}` |
    | `BANKRUPTCY_COUNT` | 12 | `NUMBER` | **Bankruptcy Exclusions**
Count of borrowers excluded due to bankruptcy flag being TRUE. Represents borrowers in  active bankruptcy proceedings who cannot be contacted for collections purposes due to  automatic stay provisions.
 | **Bankruptcy Exclusions**
Count of borrowers excluded due to bankruptcy flag being TRUE. Represents borrowers in  active bankruptcy proceedings who cannot be contacted for collections purposes due to  automatic stay provisions.
 | `[]` | `{}` |
    | `DECEASED_COUNT` | 13 | `NUMBER` | **Deceased Borrower Exclusions**
Count of borrowers excluded due to deceased flag being TRUE. Represents borrowers who  have been reported as deceased and require special estate handling procedures rather  than standard collections contact.
 | **Deceased Borrower Exclusions**
Count of borrowers excluded due to deceased flag being TRUE. Represents borrowers who  have been reported as deceased and require special estate handling procedures rather  than standard collections contact.
 | `[]` | `{}` |
    | `C_D_COUNT` | 14 | `NUMBER` | **Cease and Desist Exclusions**
Count of borrowers excluded due to cease_and_desist flag being TRUE. Represents borrowers  who have issued formal cease and desist requests requiring immediate cessation of all  collections communications for legal compliance.
 | **Cease and Desist Exclusions**
Count of borrowers excluded due to cease_and_desist flag being TRUE. Represents borrowers  who have issued formal cease and desist requests requiring immediate cessation of all  collections communications for legal compliance.
 | `[]` | `{}` |
    | `WRONG_NUM_COUNT` | 15 | `NUMBER` | **Wrong Number Exclusions**
Count of borrowers excluded due to wrong_number flag being TRUE. Represents borrowers  whose phone numbers have been identified as incorrect or disconnected, making contact  attempts ineffective.
 | **Wrong Number Exclusions**
Count of borrowers excluded due to wrong_number flag being TRUE. Represents borrowers  whose phone numbers have been identified as incorrect or disconnected, making contact  attempts ineffective.
 | `[]` | `{}` |
    | `LEGAL_ACTION_COUNT` | 16 | `NUMBER` | **Legal Action Exclusions**
Count of borrowers excluded due to legal_action flag being TRUE. Represents borrowers  involved in legal proceedings that require suspension of standard collections activities  pending legal resolution.
 | **Legal Action Exclusions**
Count of borrowers excluded due to legal_action flag being TRUE. Represents borrowers  involved in legal proceedings that require suspension of standard collections activities  pending legal resolution.
 | `[]` | `{}` |
    | `DEBT_SALE_COUNT` | 17 | `NUMBER` | **Debt Sale Exclusions**
Count of borrowers excluded because their debt has been sold to third-party collectors.  These accounts are no longer managed by internal collections and should not receive  Cherry collections contact.
 | **Debt Sale Exclusions**
Count of borrowers excluded because their debt has been sold to third-party collectors.  These accounts are no longer managed by internal collections and should not receive  Cherry collections contact.
 | `[]` | `{}` |
    | `OUTSOURCED_COUNT` | 18 | `NUMBER` | **Outsourced Account Exclusions**
Count of borrowers excluded because their accounts have been outsourced to external  collections agencies. Prevents duplicate collections efforts between internal and  external agencies.
 | **Outsourced Account Exclusions**
Count of borrowers excluded because their accounts have been outsourced to external  collections agencies. Prevents duplicate collections efforts between internal and  external agencies.
 | `[]` | `{}` |
    | `FRAUD_COUNT` | 19 | `NUMBER` | **Fraud Flag Exclusions**
Count of borrowers excluded due to fraud flags being TRUE. Represents accounts flagged  for fraudulent activity that require special handling procedures rather than standard  collections contact.
 | **Fraud Flag Exclusions**
Count of borrowers excluded due to fraud flags being TRUE. Represents accounts flagged  for fraudulent activity that require special handling procedures rather than standard  collections contact.
 | `[]` | `{}` |
    | `VOIDED_COUNT` | 20 | `NUMBER` | **Voided Loan Exclusions**
Count of borrowers excluded because their loans have been voided. Voided loans should  not receive collections contact as they are no longer valid financial obligations.
 | **Voided Loan Exclusions**
Count of borrowers excluded because their loans have been voided. Voided loans should  not receive collections contact as they are no longer valid financial obligations.
 | `[]` | `{}` |
    | `REFUNDED_COUNT` | 21 | `NUMBER` | **Refunded Loan Exclusions**
Count of borrowers excluded because their loans have been refunded. Refunded loans  should not receive collections contact as the financial obligation has been satisfied.
 | **Refunded Loan Exclusions**
Count of borrowers excluded because their loans have been refunded. Refunded loans  should not receive collections contact as the financial obligation has been satisfied.
 | `[]` | `{}` |
    | `PEND_PAY_COUNT` | 22 | `NUMBER` | **Pending Payment Exclusions**
Count of borrowers excluded due to payments in 'PENDING' status within the last 1-3 days.  Prevents collections contact while payments are processing to avoid customer confusion  and unnecessary contact.
 | **Pending Payment Exclusions**
Count of borrowers excluded due to payments in 'PENDING' status within the last 1-3 days.  Prevents collections contact while payments are processing to avoid customer confusion  and unnecessary contact.
 | `[]` | `{}` |
    | `FORBEARANCE_COUNT` | 23 | `NUMBER` | **Active Forbearance Exclusions**
Count of borrowers excluded due to active forbearance agreements. Borrowers in forbearance  have approved payment deferrals and should not receive collections contact during the  forbearance period.
 | **Active Forbearance Exclusions**
Count of borrowers excluded due to active forbearance agreements. Borrowers in forbearance  have approved payment deferrals and should not receive collections contact during the  forbearance period.
 | `[]` | `{}` |
    | `COMMIT_COUNT` | 24 | `NUMBER` | **Unfulfilled Commitment Exclusions**
Count of borrowers excluded due to unfulfilled payment commitments. Borrowers with active  but unfulfilled commitments may require different handling than standard collections contact.
 | **Unfulfilled Commitment Exclusions**
Count of borrowers excluded due to unfulfilled payment commitments. Borrowers with active  but unfulfilled commitments may require different handling than standard collections contact.
 | `[]` | `{}` |
    | `FOLLOW_UP_COUNT` | 25 | `NUMBER` | **Future Follow-Up Date Exclusions**
Count of borrowers excluded because they have future follow-up dates scheduled in the  loan notes system. Respects agent-scheduled follow-up timing to avoid premature contact.
 | **Future Follow-Up Date Exclusions**
Count of borrowers excluded because they have future follow-up dates scheduled in the  loan notes system. Respects agent-scheduled follow-up timing to avoid premature contact.
 | `[]` | `{}` |
    | `RPC_7DAYS_COUNT` | 26 | `NUMBER` | **Right Party Contact Cooling Period Exclusions**
Count of borrowers excluded due to Right Party Contact (RPC) within the last 7 days.  Implements cooling period after successful borrower contact to comply with best practices  and avoid over-contacting.
 | **Right Party Contact Cooling Period Exclusions**
Count of borrowers excluded due to Right Party Contact (RPC) within the last 7 days.  Implements cooling period after successful borrower contact to comply with best practices  and avoid over-contacting.
 | `[]` | `{}` |
    | `NAT_DISASTER_COUNT` | 27 | `NUMBER` | **Natural Disaster Area Exclusions**
Count of borrowers excluded because they reside in declared natural disaster areas  (specific North Carolina ZIP codes). Provides humanitarian relief by suspending  collections during disaster recovery periods.
 | **Natural Disaster Area Exclusions**
Count of borrowers excluded because they reside in declared natural disaster areas  (specific North Carolina ZIP codes). Provides humanitarian relief by suspending  collections during disaster recovery periods.
 | `[]` | `{}` |
    | `SEVEN_IN_SEVEN_COUNT` | 28 | `NUMBER` | **7-in-7 Day Limit Exclusions (CA/MD/MN/SD)**
Count of borrowers excluded due to reaching the 7-call limit within 7 days in states  with this restriction (California, Maryland, Minnesota, South Dakota). Ensures compliance  with state-specific collections regulations.
 | **7-in-7 Day Limit Exclusions (CA/MD/MN/SD)**
Count of borrowers excluded due to reaching the 7-call limit within 7 days in states  with this restriction (California, Maryland, Minnesota, South Dakota). Ensures compliance  with state-specific collections regulations.
 | `[]` | `{}` |
    | `WV_COUNT` | 29 | `NUMBER` | **West Virginia Contact Limit Exclusions**
Count of borrowers excluded due to West Virginia's specific contact limits (30 calls  in 7 days). Ensures compliance with WV state collections regulations.
 | **West Virginia Contact Limit Exclusions**
Count of borrowers excluded due to West Virginia's specific contact limits (30 calls  in 7 days). Ensures compliance with WV state collections regulations.
 | `[]` | `{}` |
    | `SC_COUNT` | 30 | `NUMBER` | **South Carolina Contact Limit Exclusions**
Count of borrowers excluded due to South Carolina's contact limits (7 calls, 7 SMS,  7 emails in 7 days, or 21 total contacts). Ensures compliance with SC comprehensive  contact restrictions.
 | **South Carolina Contact Limit Exclusions**
Count of borrowers excluded due to South Carolina's contact limits (7 calls, 7 SMS,  7 emails in 7 days, or 21 total contacts). Ensures compliance with SC comprehensive  contact restrictions.
 | `[]` | `{}` |
    | `DC_COUNT` | 31 | `NUMBER` | **District of Columbia Contact Limit Exclusions**
Count of borrowers excluded due to DC's restrictive contact limits (2 calls, 2 SMS,  2 emails in 7 days, or 5 total contacts). Ensures compliance with DC's strict  collections regulations.
 | **District of Columbia Contact Limit Exclusions**
Count of borrowers excluded due to DC's restrictive contact limits (2 calls, 2 SMS,  2 emails in 7 days, or 5 total contacts). Ensures compliance with DC's strict  collections regulations.
 | `[]` | `{}` |
    | `MA_COUNT` | 32 | `NUMBER` | **Massachusetts Contact Limit Exclusions**
Count of borrowers excluded due to Massachusetts contact limits (1 call, 1 SMS per day,  2 total contacts per day). Ensures compliance with MA's restrictive collections laws.
 | **Massachusetts Contact Limit Exclusions**
Count of borrowers excluded due to Massachusetts contact limits (1 call, 1 SMS per day,  2 total contacts per day). Ensures compliance with MA's restrictive collections laws.
 | `[]` | `{}` |
    | `NYC_COUNT` | 33 | `NUMBER` | **New York City Contact Limit Exclusions**
Count of borrowers excluded due to NYC-specific contact limits (1 call, 1 SMS, 1 email  in 7 days, 2 total contacts per day) based on NYC ZIP code identification. Ensures  compliance with NYC's municipal collections regulations.
 | **New York City Contact Limit Exclusions**
Count of borrowers excluded due to NYC-specific contact limits (1 call, 1 SMS, 1 email  in 7 days, 2 total contacts per day) based on NYC ZIP code identification. Ensures  compliance with NYC's municipal collections regulations.
 | `[]` | `{}` |
    | `PROCESS_TS` | 34 | `TIMESTAMP_LTZ` | **Processing Timestamp**
Timestamp when the collections inventory analysis was processed and aggregated. Used  for data lineage tracking and ensuring data freshness for operational dashboards. | **Processing Timestamp**
Timestamp when the collections inventory analysis was processed and aggregated. Used  for data lineage tracking and ensuring data freshness for operational dashboards. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.cherry_data_model.is_nyc_zipcode`
    *   `model.cherry_data_model.borrowers_merged_emails_xf`
    *   `model.cherry_data_model.collections_safe_select_dials_archive`
    *   `model.cherry_data_model.daily_loan_xf`
    *   `model.cherry_data_model.int_active_commitments`
    *   `model.cherry_data_model.nice_collections_contacts_xf_archive`
    *   `model.cherry_data_model.nice_collections_dials_xf_archive`
    *   `model.cherry_data_model.omnichannel_collections_outbounds_xf`
    *   `model.cherry_data_model.src_cherry_loans`
    *   `model.cherry_data_model.src_commitments`
    *   `model.cherry_data_model.src_debt_sale_transactions`
    *   `model.cherry_data_model.stg_forbearances`
    *   `model.cherry_data_model.unsubscribed_borrowers_xf`
    *   `source.cherry_data_model.cherry_data.borrower_addresses`
    *   `source.cherry_data_model.cherry_data.borrower_flags`
    *   `source.cherry_data_model.cherry_data.payments`
    *   `source.cherry_data_model.mongo_notes.LOAN_FOLLOW_UP_DATE_NOTES`

---
