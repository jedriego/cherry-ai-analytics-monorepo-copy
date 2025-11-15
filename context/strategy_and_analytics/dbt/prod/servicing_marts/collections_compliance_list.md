## Model: `collections_compliance_list`

`collections_compliance_list`

*   **Unique ID:** `model.cherry_data_model.collections_compliance_list`
*   **FQN:** `prod.servicing_marts.collections_compliance_list`
*   **Description:** **Comprehensive Collections Contact Eligibility Engine**
This sophisticated model serves as Cherry's primary contact eligibility determination system for collections  operations, implementing multi-layered business rules, regulatory compliance requirements, and operational  constraints to determine which borrowers can be contacted via different communication channels. The model  combines complex state-specific regulations, TCPA compliance rules, contact volume limits, and exclusion  logic to ensure lawful and effective collections communications.
**Multi-Layer Architecture:** - **Status Restrictions**: Borrower flags (do not call, bankruptcy, deceased, etc.), debt sale status, 
  fraud/void/refund exclusions, and consent management
- **Engagement Restrictions**: Pending payments, active forbearances, unfulfilled commitments, future 
  follow-up dates, and recent right party contact (RPC) rules
- **Business Rules**: Valid loan status, minimum balance thresholds, appropriate DPD ranges for 
  voice vs digital contact
- **Compliance Rules**: TCPA timezone restrictions, state-specific contact limits, natural disaster 
  exclusions, and multi-jurisdictional regulatory requirements

**State-Specific Regulations Implemented:** - **California/Maryland/Minnesota/South Dakota**: 7-in-7 rule (max 7 calls per 7 days) - **West Virginia**: 30 calls/10 SMS per 7 days limits - **South Carolina**: 7 contacts per channel + 21 total per 7 days + daily limits - **Washington DC**: 2 contacts per channel + 5 total per 7 days - **Massachusetts**: 1 contact per channel per day + 2 daily call/SMS limit - **New York City**: 1 contact per channel + 2 daily call/SMS limit (by zipcode)
**Critical Staging Model Integration:** - **omnichannel_collections_outbounds_xf**: Multi-channel contact history for volume calculations - **unsubscribed_borrowers_xf**: SMS/email consent and opt-out status tracking - **stg_forbearances**: Active forbearance periods requiring contact suspension - **src_commitments**: Unfulfilled payment arrangements affecting contact eligibility - **daily_loan_xf**: Current loan status and delinquency information
**Primary Use Cases:** - Real-time contact eligibility determination for dialer systems - Regulatory compliance monitoring and audit trails - Collections workflow automation and decisioning - State law adherence verification and documentation - Operational efficiency optimization through intelligent contact routing
**Grain:** One record per loan per day (current date focus with loan-level deduplication logic)

*   **Tags:** `['servicing_and_collections', 'collections_hourly']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `RECORD_DATE` | 1 | `DATE` | Date of the loan record snapshot from daily_loan_xf, filtered to current_date() to ensure  only the most recent loan status information is used for contact eligibility decisions.
 | Date of the loan record snapshot from daily_loan_xf, filtered to current_date() to ensure  only the most recent loan status information is used for contact eligibility decisions.
 | `[]` | `{}` |
    | `BORROWER_ID` | 2 | `NUMBER` | Unique borrower identifier from Cherry's system, serving as the primary key for contact  eligibility determination. Used to aggregate contact history, apply borrower-specific  restrictions, and enforce state compliance rules across all borrower loans.
 | Unique borrower identifier from Cherry's system, serving as the primary key for contact  eligibility determination. Used to aggregate contact history, apply borrower-specific  restrictions, and enforce state compliance rules across all borrower loans.
 | `[]` | `{}` |
    | `LOAN_ID` | 3 | `NUMBER` | Unique loan identifier from Cherry's system. Multiple loans per borrower are deduplicated  using qualify clause with row_number() logic that prioritizes non-callable loans to ensure  conservative contact decisions when borrowers have mixed loan eligibility statuses.
 | Unique loan identifier from Cherry's system. Multiple loans per borrower are deduplicated  using qualify clause with row_number() logic that prioritizes non-callable loans to ensure  conservative contact decisions when borrowers have mixed loan eligibility statuses.
 | `[]` | `{}` |
    | `LOAN_STATUS` | 4 | `TEXT` | Current loan status from daily_loan_xf (e.g., 'Late', 'Charged Off', 'Open'). Used in  business rules validation to determine if the loan qualifies for collections contact based  on valid statuses that indicate active collection efforts are appropriate.
 | Current loan status from daily_loan_xf (e.g., 'Late', 'Charged Off', 'Open'). Used in  business rules validation to determine if the loan qualifies for collections contact based  on valid statuses that indicate active collection efforts are appropriate.
 | `[]` | `{}` |
    | `LOAN_SUBSTATUS` | 5 | `TEXT` | Detailed loan substatus from daily_loan_xf providing granular loan state information  (e.g., 'Performing', 'Charged Off', 'Bankruptcy'). Used in conjunction with loan_status  to make precise contact eligibility determinations.
 | Detailed loan substatus from daily_loan_xf providing granular loan state information  (e.g., 'Performing', 'Charged Off', 'Bankruptcy'). Used in conjunction with loan_status  to make precise contact eligibility determinations.
 | `[]` | `{}` |
    | `ANY_CONTACT_ELIGIBLE` | 6 | `BOOLEAN` | Master contact eligibility flag that determines if the borrower can be contacted through  ANY communication channel. This hierarchical flag evaluates all major restriction categories  including status restrictions (do not call, bankruptcy, deceased, etc.), business rules  (valid balance, loan status, DPD), compliance rules (TCPA hours, state hours), and  state-specific contact limits. Returns FALSE if any fundamental restriction applies,  serving as the base requirement for all channel-specific eligibility.
 | Master contact eligibility flag that determines if the borrower can be contacted through  ANY communication channel. This hierarchical flag evaluates all major restriction categories  including status restrictions (do not call, bankruptcy, deceased, etc.), business rules  (valid balance, loan status, DPD), compliance rules (TCPA hours, state hours), and  state-specific contact limits. Returns FALSE if any fundamental restriction applies,  serving as the base requirement for all channel-specific eligibility.
 | `[]` | `{}` |
    | `CALL_ELIGIBLE` | 7 | `BOOLEAN` | Determines voice call eligibility by applying call-specific business rules and restrictions  on top of any_contact_eligible requirements. Additional restrictions include: future follow-up  dates, recent RPC within 7 days, valid DPD for phone contact (6-120 days or charged off),  daily call volume limits, and state-specific calling regulations. Only borrowers passing  all voice contact requirements can receive collections calls.
 | Determines voice call eligibility by applying call-specific business rules and restrictions  on top of any_contact_eligible requirements. Additional restrictions include: future follow-up  dates, recent RPC within 7 days, valid DPD for phone contact (6-120 days or charged off),  daily call volume limits, and state-specific calling regulations. Only borrowers passing  all voice contact requirements can receive collections calls.
 | `[]` | `{}` |
    | `VOICEMAIL_ELIGIBLE` | 8 | `BOOLEAN` | Determines voicemail eligibility using the same restriction logic as call_eligible but  with separate volume tracking for voicemail-specific limits. Voicemails are treated as  voice contacts for regulatory purposes but tracked separately for operational contact  frequency management and compliance monitoring.
 | Determines voicemail eligibility using the same restriction logic as call_eligible but  with separate volume tracking for voicemail-specific limits. Voicemails are treated as  voice contacts for regulatory purposes but tracked separately for operational contact  frequency management and compliance monitoring.
 | `[]` | `{}` |
    | `SMS_ELIGIBLE` | 9 | `BOOLEAN` | Determines SMS text message eligibility by enforcing SMS consent requirements and digital  contact business rules. Key restrictions include: SMS consent verification, valid DPD for  digital contact (1-120 days or charged off), daily SMS volume limits, and state-specific  text messaging regulations. Only borrowers with verified SMS consent and appropriate  delinquency status can receive collections text messages.
 | Determines SMS text message eligibility by enforcing SMS consent requirements and digital  contact business rules. Key restrictions include: SMS consent verification, valid DPD for  digital contact (1-120 days or charged off), daily SMS volume limits, and state-specific  text messaging regulations. Only borrowers with verified SMS consent and appropriate  delinquency status can receive collections text messages.
 | `[]` | `{}` |
    | `EMAIL_ELIGIBLE` | 10 | `BOOLEAN` | Determines email contact eligibility by enforcing email consent requirements and digital  contact business rules. Restrictions include: email consent verification, valid DPD for  digital contact (1-120 days or charged off), daily email volume limits, and state-specific  email regulations. Email eligibility is independent of SMS eligibility but follows similar  consent and business rule validation patterns.
 | Determines email contact eligibility by enforcing email consent requirements and digital  contact business rules. Restrictions include: email consent verification, valid DPD for  digital contact (1-120 days or charged off), daily email volume limits, and state-specific  email regulations. Email eligibility is independent of SMS eligibility but follows similar  consent and business rule validation patterns.
 | `[]` | `{}` |
    | `DO_NOT_CALL` | 11 | `BOOLEAN` | Borrower flag indicating explicit request to not be called. When TRUE, borrower is excluded  from all contact attempts regardless of other eligibility factors. Sourced from Cherry's  borrower_flags table and represents legally binding contact restriction requiring complete  communication cessation.
 | Borrower flag indicating explicit request to not be called. When TRUE, borrower is excluded  from all contact attempts regardless of other eligibility factors. Sourced from Cherry's  borrower_flags table and represents legally binding contact restriction requiring complete  communication cessation.
 | `[]` | `{}` |
    | `BANKRUPTCY` | 12 | `BOOLEAN` | Borrower flag indicating active bankruptcy status. When TRUE, borrower is excluded from  collections contact due to automatic stay provisions under bankruptcy law. Collections  activities must cease until bankruptcy proceedings are resolved or court permission is obtained.
 | Borrower flag indicating active bankruptcy status. When TRUE, borrower is excluded from  collections contact due to automatic stay provisions under bankruptcy law. Collections  activities must cease until bankruptcy proceedings are resolved or court permission is obtained.
 | `[]` | `{}` |
    | `DECEASED` | 13 | `BOOLEAN` | Borrower flag indicating deceased status. When TRUE, borrower is excluded from all contact  attempts as collections contact with deceased individuals is inappropriate and potentially  unlawful. Contact restrictions remain in effect until estate proceedings are established.
 | Borrower flag indicating deceased status. When TRUE, borrower is excluded from all contact  attempts as collections contact with deceased individuals is inappropriate and potentially  unlawful. Contact restrictions remain in effect until estate proceedings are established.
 | `[]` | `{}` |
    | `CEASE_AND_DESIST` | 14 | `BOOLEAN` | Borrower flag indicating formal cease and desist request under FDCPA. When TRUE, borrower  is excluded from all contact attempts except for specific legally permitted communications.  Represents legal notice requiring cessation of collection communications.
 | Borrower flag indicating formal cease and desist request under FDCPA. When TRUE, borrower  is excluded from all contact attempts except for specific legally permitted communications.  Represents legal notice requiring cessation of collection communications.
 | `[]` | `{}` |
    | `WRONG_NUMBER` | 15 | `BOOLEAN` | Borrower flag indicating confirmed wrong number status. When TRUE, borrower is excluded  from contact attempts to prevent TCPA violations and ensure operational efficiency by  avoiding continued contact attempts to incorrect phone numbers.
 | Borrower flag indicating confirmed wrong number status. When TRUE, borrower is excluded  from contact attempts to prevent TCPA violations and ensure operational efficiency by  avoiding continued contact attempts to incorrect phone numbers.
 | `[]` | `{}` |
    | `LEGAL_ACTION` | 16 | `BOOLEAN` | Borrower flag indicating active legal proceedings. When TRUE, borrower is excluded from  standard collections contact as legal action supersedes normal collection activities.  Contact restrictions prevent interference with legal proceedings.
 | Borrower flag indicating active legal proceedings. When TRUE, borrower is excluded from  standard collections contact as legal action supersedes normal collection activities.  Contact restrictions prevent interference with legal proceedings.
 | `[]` | `{}` |
    | `IS_DEBT_SALE` | 17 | `BOOLEAN` | Loan-level flag indicating debt sale status from src_debt_sale_transactions. When TRUE,  loan is excluded from contact as debt has been sold to third party and Cherry no longer  has collection responsibility. Contact must cease upon debt sale completion.
 | Loan-level flag indicating debt sale status from src_debt_sale_transactions. When TRUE,  loan is excluded from contact as debt has been sold to third party and Cherry no longer  has collection responsibility. Contact must cease upon debt sale completion.
 | `[]` | `{}` |
    | `IS_OUTSOURCED` | 18 | `BOOLEAN` | Loan-level flag from src_cherry_loans indicating outsourced collections status. When TRUE,  loan is excluded from internal collections contact as external collection agency has  assumed responsibility. Prevents duplicate collection efforts.
 | Loan-level flag from src_cherry_loans indicating outsourced collections status. When TRUE,  loan is excluded from internal collections contact as external collection agency has  assumed responsibility. Prevents duplicate collection efforts.
 | `[]` | `{}` |
    | `IS_FRAUD` | 19 | `BOOLEAN` | Loan-level flag from src_cherry_loans indicating fraud status. When TRUE, loan is excluded  from standard collections contact as fraud cases require specialized handling and different  communication protocols outside normal collections processes.
 | Loan-level flag from src_cherry_loans indicating fraud status. When TRUE, loan is excluded  from standard collections contact as fraud cases require specialized handling and different  communication protocols outside normal collections processes.
 | `[]` | `{}` |
    | `IS_VOIDED` | 20 | `BOOLEAN` | Loan-level flag indicating voided loan status derived from loan_status = 'VOIDED' in  src_cherry_loans. When TRUE, loan is excluded from contact as voided loans are invalid  and should not be subject to collections activities.
 | Loan-level flag indicating voided loan status derived from loan_status = 'VOIDED' in  src_cherry_loans. When TRUE, loan is excluded from contact as voided loans are invalid  and should not be subject to collections activities.
 | `[]` | `{}` |
    | `IS_REFUNDED` | 21 | `BOOLEAN` | Loan-level flag indicating refunded loan status derived from loan_status = 'REFUNDED'  in src_cherry_loans. When TRUE, loan is excluded from contact as refunded loans have  been settled and collections activities are inappropriate.
 | Loan-level flag indicating refunded loan status derived from loan_status = 'REFUNDED'  in src_cherry_loans. When TRUE, loan is excluded from contact as refunded loans have  been settled and collections activities are inappropriate.
 | `[]` | `{}` |
    | `IS_DISPUTE` | 22 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `HAS_SMS_CONSENT` | 23 | `BOOLEAN` | Borrower consent flag for SMS communications from unsubscribed_borrowers_xf model. When  FALSE, borrower is excluded from SMS contact to ensure TCPA compliance. Derived from  Twilio unsubscribe data and Genesys SMS acceptance preferences. Required TRUE for SMS eligibility.
 | Borrower consent flag for SMS communications from unsubscribed_borrowers_xf model. When  FALSE, borrower is excluded from SMS contact to ensure TCPA compliance. Derived from  Twilio unsubscribe data and Genesys SMS acceptance preferences. Required TRUE for SMS eligibility.
 | `[]` | `{}` |
    | `HAS_EMAIL_CONSENT` | 24 | `BOOLEAN` | Borrower consent flag for email communications from unsubscribed_borrowers_xf model. When  FALSE, borrower is excluded from email contact. Derived from SendGrid unsubscribe data  to ensure CAN-SPAM compliance. Required TRUE for email eligibility.
 | Borrower consent flag for email communications from unsubscribed_borrowers_xf model. When  FALSE, borrower is excluded from email contact. Derived from SendGrid unsubscribe data  to ensure CAN-SPAM compliance. Required TRUE for email eligibility.
 | `[]` | `{}` |
    | `OLD_RISC_LOAN` | 25 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `INTERACTION_DISPOSITION_EXCLUSION` | 26 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_PEND_PAY` | 27 | `BOOLEAN` | Payment restriction flag indicating pending payment status from src_cherry_payments. When  TRUE, borrower is excluded from contact to avoid interrupting pending payment processing.  Only includes payments updated within last 3 days to avoid stale payment status interference.
 | Payment restriction flag indicating pending payment status from src_cherry_payments. When  TRUE, borrower is excluded from contact to avoid interrupting pending payment processing.  Only includes payments updated within last 3 days to avoid stale payment status interference.
 | `[]` | `{}` |
    | `IS_ACTIVE_FORBEARANCE` | 28 | `BOOLEAN` | Forbearance restriction flag from stg_forbearances indicating active forbearance period.  When TRUE, borrower is excluded from contact as forbearance agreements require suspension  of collections activities during the forbearance period. Derived from forbearance start/end dates.
 | Forbearance restriction flag from stg_forbearances indicating active forbearance period.  When TRUE, borrower is excluded from contact as forbearance agreements require suspension  of collections activities during the forbearance period. Derived from forbearance start/end dates.
 | `[]` | `{}` |
    | `IS_UNFULFILLED_COMMITMENT` | 29 | `BOOLEAN` | Commitment restriction flag from src_commitments indicating unfulfilled payment commitments.  When TRUE, borrower is excluded from contact during active commitment periods to honor  payment arrangement agreements. Based on commitment_progress = 'UNFULFILLED' status.
 | Commitment restriction flag from src_commitments indicating unfulfilled payment commitments.  When TRUE, borrower is excluded from contact during active commitment periods to honor  payment arrangement agreements. Based on commitment_progress = 'UNFULFILLED' status.
 | `[]` | `{}` |
    | `IS_TOP_PRIORITY_LOAN` | 30 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `NEXT_FOLLOW_UP_DATE` | 31 | `DATE` | Future follow-up date from LOAN_FOLLOW_UP_DATE_NOTES source indicating scheduled future  contact. When not null and in the future, borrower is excluded from current contact  attempts to respect scheduled follow-up timing and avoid premature contact.
 | Future follow-up date from LOAN_FOLLOW_UP_DATE_NOTES source indicating scheduled future  contact. When not null and in the future, borrower is excluded from current contact  attempts to respect scheduled follow-up timing and avoid premature contact.
 | `[]` | `{}` |
    | `FLEX_PAY_DATE` | 32 | `DATE` |  |  | `[]` | `{}` |
    | `RPC_LAST_CONTACT_PT` | 33 | `TIMESTAMP_NTZ` | Timestamp of most recent right party contact (RPC) from nice_collections_contacts_xf within  the last 7 days. When not null, borrower is excluded from contact to comply with 7-day  RPC restriction rules preventing excessive contact frequency.
 | Timestamp of most recent right party contact (RPC) from nice_collections_contacts_xf within  the last 7 days. When not null, borrower is excluded from contact to comply with 7-day  RPC restriction rules preventing excessive contact frequency.
 | `[]` | `{}` |
    | `IS_REAL_BALANCE` | 34 | `BOOLEAN` | Business rule flag validating meaningful loan balance from daily_loan_xf. Returns TRUE  when principal_balance > 5 OR charge_off > 5, ensuring collections contact only occurs  for loans with sufficient outstanding balance to justify collection efforts.
 | Business rule flag validating meaningful loan balance from daily_loan_xf. Returns TRUE  when principal_balance > 5 OR charge_off > 5, ensuring collections contact only occurs  for loans with sufficient outstanding balance to justify collection efforts.
 | `[]` | `{}` |
    | `IS_VALID_DPD_PHONE` | 35 | `BOOLEAN` | Business rule flag validating appropriate days past due (DPD) for voice contact. Returns  TRUE when DPD between 6-120 days OR loan_substatus = 'Charged Off'. Ensures voice contact  aligns with collection strategy timing and excludes very early delinquency from phone calls.
 | Business rule flag validating appropriate days past due (DPD) for voice contact. Returns  TRUE when DPD between 6-120 days OR loan_substatus = 'Charged Off'. Ensures voice contact  aligns with collection strategy timing and excludes very early delinquency from phone calls.
 | `[]` | `{}` |
    | `IS_VALID_DPD_DIGITAL` | 36 | `BOOLEAN` | Business rule flag validating appropriate DPD for digital contact (SMS/email). Returns  TRUE when DPD between 1-120 days OR loan_substatus = 'Charged Off'. Allows earlier  digital outreach compared to voice contact while maintaining appropriate timing boundaries.
 | Business rule flag validating appropriate DPD for digital contact (SMS/email). Returns  TRUE when DPD between 1-120 days OR loan_substatus = 'Charged Off'. Allows earlier  digital outreach compared to voice contact while maintaining appropriate timing boundaries.
 | `[]` | `{}` |
    | `IS_VALID_LOAN_STATUS` | 37 | `BOOLEAN` | Business rule flag validating acceptable loan status and substatus for collections contact.  Returns FALSE when loan_status or loan_substatus indicates states inappropriate for  collections (e.g., 'Settled', 'Void', 'Fraud'). Ensures contact attempts align with  collectible loan states.
 | Business rule flag validating acceptable loan status and substatus for collections contact.  Returns FALSE when loan_status or loan_substatus indicates states inappropriate for  collections (e.g., 'Settled', 'Void', 'Fraud'). Ensures contact attempts align with  collectible loan states.
 | `[]` | `{}` |
    | `IS_VALID_DPD_CONTACT` | 38 | `BOOLEAN` | Alias for is_valid_dpd_digital used in general contact eligibility validation. Provides  consistent DPD validation across different contact eligibility logic paths while  maintaining digital contact timing rules.
 | Alias for is_valid_dpd_digital used in general contact eligibility validation. Provides  consistent DPD validation across different contact eligibility logic paths while  maintaining digital contact timing rules.
 | `[]` | `{}` |
    | `IS_OFFER_ACTIVE` | 39 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_VOICEMAIL_ELIGIBLE` | 40 | `BOOLEAN` | Volume-based eligibility flag for voicemail contacts from contact_limit logic. Returns  FALSE when daily dial count (call + voicemail) >= 4, preventing excessive voice contact  attempts and ensuring operational efficiency while respecting borrower contact preferences.
 | Volume-based eligibility flag for voicemail contacts from contact_limit logic. Returns  FALSE when daily dial count (call + voicemail) >= 4, preventing excessive voice contact  attempts and ensuring operational efficiency while respecting borrower contact preferences.
 | `[]` | `{}` |
    | `IS_CALL_ELIGIBLE` | 41 | `BOOLEAN` | Volume-based eligibility flag for call contacts from contact_limit logic. Returns FALSE  when daily dial count >= 4, implementing internal contact frequency limits that supplement  regulatory requirements and optimize collections effectiveness.
 | Volume-based eligibility flag for call contacts from contact_limit logic. Returns FALSE  when daily dial count >= 4, implementing internal contact frequency limits that supplement  regulatory requirements and optimize collections effectiveness.
 | `[]` | `{}` |
    | `IS_SMS_ELIGIBLE` | 42 | `BOOLEAN` | Volume-based eligibility flag for SMS contacts from contact_limit logic. Returns FALSE  when daily SMS count >= 1 * delinquent_loan_count, scaling SMS frequency limits based  on borrower's delinquent loan count to balance communication needs with respect for borrower.
 | Volume-based eligibility flag for SMS contacts from contact_limit logic. Returns FALSE  when daily SMS count >= 1 * delinquent_loan_count, scaling SMS frequency limits based  on borrower's delinquent loan count to balance communication needs with respect for borrower.
 | `[]` | `{}` |
    | `IS_EMAIL_ELIGIBLE` | 43 | `BOOLEAN` | Volume-based eligibility flag for email contacts from contact_limit logic. Returns FALSE  when daily email count >= 1 * delinquent_loan_count, implementing same scaled approach  as SMS for email frequency management based on borrower's portfolio complexity.
 | Volume-based eligibility flag for email contacts from contact_limit logic. Returns FALSE  when daily email count >= 1 * delinquent_loan_count, implementing same scaled approach  as SMS for email frequency management based on borrower's portfolio complexity.
 | `[]` | `{}` |
    | `IS_NAT_DISASTER_AREA` | 44 | `TEXT` | Emergency restriction flag indicating borrower location in declared natural disaster area.  When TRUE, borrower is excluded from contact during disaster recovery periods. Currently  implements North Carolina Hurricane exclusion zones through 11/28/24 based on specific  zipcode ranges affected by natural disasters.
 | Emergency restriction flag indicating borrower location in declared natural disaster area.  When TRUE, borrower is excluded from contact during disaster recovery periods. Currently  implements North Carolina Hurricane exclusion zones through 11/28/24 based on specific  zipcode ranges affected by natural disasters.
 | `[]` | `{}` |
    | `IS_TCPA_HOURS_ELIGIBLE` | 45 | `BOOLEAN` | TCPA compliance flag validating contact timing based on borrower timezone. Returns TRUE  when current time falls within federally permissible calling hours (8am-9pm borrower local time)  for each timezone. Essential for TCPA compliance and avoiding federal calling time violations.
 | TCPA compliance flag validating contact timing based on borrower timezone. Returns TRUE  when current time falls within federally permissible calling hours (8am-9pm borrower local time)  for each timezone. Essential for TCPA compliance and avoiding federal calling time violations.
 | `[]` | `{}` |
    | `IS_STATE_HOURS_ELIGIBLE` | 46 | `BOOLEAN` | State-specific calling hours compliance flag implementing stricter state requirements beyond  federal TCPA rules. Includes Indiana (6am-5pm EST/7am-6pm CST), South Carolina (5am-4pm),  Oklahoma (7am-7pm), and California (9am-9pm) specific hours. Returns FALSE outside permitted hours.
 | State-specific calling hours compliance flag implementing stricter state requirements beyond  federal TCPA rules. Includes Indiana (6am-5pm EST/7am-6pm CST), South Carolina (5am-4pm),  Oklahoma (7am-7pm), and California (9am-9pm) specific hours. Returns FALSE outside permitted hours.
 | `[]` | `{}` |
    | `IS_SUNDAY_ELIGIBLE` | 47 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_HOLIDAY_ELIGIBLE` | 48 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `TEST` | 49 | `NUMBER` |  |  | `[]` | `{}` |
    | `IS_CALLABLE_7IN7` | 50 | `BOOLEAN` | Multi-state regulatory compliance flag implementing "7-in-7" rule for California, Maryland,  Minnesota, and South Dakota. Returns FALSE when 7+ calls made within rolling 7-day period,  preventing violation of state laws limiting call frequency to protect consumers.
 | Multi-state regulatory compliance flag implementing "7-in-7" rule for California, Maryland,  Minnesota, and South Dakota. Returns FALSE when 7+ calls made within rolling 7-day period,  preventing violation of state laws limiting call frequency to protect consumers.
 | `[]` | `{}` |
    | `IS_CALLABLE_WV` | 51 | `BOOLEAN` | West Virginia-specific calling compliance flag limiting calls to 30 per rolling 7-day period.  Returns FALSE when limit exceeded, ensuring compliance with WV's more permissive but still  regulated calling frequency requirements for debt collection activities.
 | West Virginia-specific calling compliance flag limiting calls to 30 per rolling 7-day period.  Returns FALSE when limit exceeded, ensuring compliance with WV's more permissive but still  regulated calling frequency requirements for debt collection activities.
 | `[]` | `{}` |
    | `IS_TEXTABLE_WV` | 52 | `BOOLEAN` | West Virginia-specific SMS compliance flag limiting text messages to 10 per rolling 7-day  period. Returns FALSE when limit exceeded, implementing WV's specific digital communication  restrictions that differ from voice contact regulations.
 | West Virginia-specific SMS compliance flag limiting text messages to 10 per rolling 7-day  period. Returns FALSE when limit exceeded, implementing WV's specific digital communication  restrictions that differ from voice contact regulations.
 | `[]` | `{}` |
    | `IS_CALLABLE_SC` | 53 | `BOOLEAN` | South Carolina calling compliance flag limiting calls to 7 per rolling 7-day period.  Part of SC's comprehensive contact regulation system that includes per-channel and total  contact limits designed to prevent harassment while allowing reasonable collection efforts.
 | South Carolina calling compliance flag limiting calls to 7 per rolling 7-day period.  Part of SC's comprehensive contact regulation system that includes per-channel and total  contact limits designed to prevent harassment while allowing reasonable collection efforts.
 | `[]` | `{}` |
    | `IS_TEXTABLE_SC` | 54 | `BOOLEAN` | South Carolina SMS compliance flag limiting text messages to 7 per rolling 7-day period.  Implements SC's channel-specific digital communication limits as part of their multi-faceted  approach to regulating debt collection contact frequency.
 | South Carolina SMS compliance flag limiting text messages to 7 per rolling 7-day period.  Implements SC's channel-specific digital communication limits as part of their multi-faceted  approach to regulating debt collection contact frequency.
 | `[]` | `{}` |
    | `IS_EMAILABLE_SC` | 55 | `BOOLEAN` | South Carolina email compliance flag limiting emails to 7 per rolling 7-day period.  Completes SC's comprehensive per-channel contact regulation system ensuring balanced  communication opportunities while preventing excessive contact across all channels.
 | South Carolina email compliance flag limiting emails to 7 per rolling 7-day period.  Completes SC's comprehensive per-channel contact regulation system ensuring balanced  communication opportunities while preventing excessive contact across all channels.
 | `[]` | `{}` |
    | `IS_CONTACTABLE_SC` | 56 | `BOOLEAN` | South Carolina total contact compliance flag limiting all contact types to 21 per rolling  7-day period. Implements SC's overall contact volume cap that works in conjunction with  per-channel limits to provide comprehensive consumer protection.
 | South Carolina total contact compliance flag limiting all contact types to 21 per rolling  7-day period. Implements SC's overall contact volume cap that works in conjunction with  per-channel limits to provide comprehensive consumer protection.
 | `[]` | `{}` |
    | `IS_CALLABLE_DC` | 57 | `BOOLEAN` | Washington DC calling compliance flag limiting calls to 2 per rolling 7-day period.  Implements DC's restrictive calling regulations designed to provide strong consumer  protection in the federal district while allowing minimal collection contact.
 | Washington DC calling compliance flag limiting calls to 2 per rolling 7-day period.  Implements DC's restrictive calling regulations designed to provide strong consumer  protection in the federal district while allowing minimal collection contact.
 | `[]` | `{}` |
    | `IS_TEXTABLE_DC` | 58 | `BOOLEAN` | Washington DC SMS compliance flag limiting text messages to 2 per rolling 7-day period.  Mirrors DC's restrictive approach for digital communications, maintaining consistency  across communication channels in their consumer protection framework.
 | Washington DC SMS compliance flag limiting text messages to 2 per rolling 7-day period.  Mirrors DC's restrictive approach for digital communications, maintaining consistency  across communication channels in their consumer protection framework.
 | `[]` | `{}` |
    | `IS_EMAILABLE_DC` | 59 | `BOOLEAN` | Washington DC email compliance flag limiting emails to 2 per rolling 7-day period.  Completes DC's restrictive per-channel contact limits ensuring uniform low-volume  contact approach across all communication methods for debt collection.
 | Washington DC email compliance flag limiting emails to 2 per rolling 7-day period.  Completes DC's restrictive per-channel contact limits ensuring uniform low-volume  contact approach across all communication methods for debt collection.
 | `[]` | `{}` |
    | `IS_CONTACTABLE_DC` | 60 | `BOOLEAN` | Washington DC total contact compliance flag limiting all contact types to 5 per rolling  7-day period. Implements DC's overall contact volume cap that provides additional  protection beyond per-channel limits with very restrictive total contact allowance.
 | Washington DC total contact compliance flag limiting all contact types to 5 per rolling  7-day period. Implements DC's overall contact volume cap that provides additional  protection beyond per-channel limits with very restrictive total contact allowance.
 | `[]` | `{}` |
    | `IS_CALLABLE_MA` | 61 | `BOOLEAN` | Massachusetts calling compliance flag limiting calls to 1 per day. Implements MA's  daily-based restriction system that differs from weekly rolling periods used by other  states, providing stricter day-over-day contact limitations.
 | Massachusetts calling compliance flag limiting calls to 1 per day. Implements MA's  daily-based restriction system that differs from weekly rolling periods used by other  states, providing stricter day-over-day contact limitations.
 | `[]` | `{}` |
    | `IS_TEXTABLE_MA` | 62 | `BOOLEAN` | Massachusetts SMS compliance flag limiting text messages to 1 per day. Maintains  consistency with MA's daily-based approach while ensuring digital communications  follow the same restrictive timing as voice communications.
 | Massachusetts SMS compliance flag limiting text messages to 1 per day. Maintains  consistency with MA's daily-based approach while ensuring digital communications  follow the same restrictive timing as voice communications.
 | `[]` | `{}` |
    | `IS_CONTACTABLE_MA` | 63 | `BOOLEAN` | Massachusetts daily total contact compliance flag limiting calls and SMS combined to  2 per day. Implements MA's unique daily aggregate limit that focuses on immediate  contact pressure rather than weekly accumulation patterns.
 | Massachusetts daily total contact compliance flag limiting calls and SMS combined to  2 per day. Implements MA's unique daily aggregate limit that focuses on immediate  contact pressure rather than weekly accumulation patterns.
 | `[]` | `{}` |
    | `IS_CALLABLE_NYC` | 64 | `BOOLEAN` | New York City calling compliance flag limiting calls to 1 per rolling 7-day period  for borrowers in NYC zipcodes. Implements NYC's municipal-level restrictions that  are more stringent than state requirements, determined by specific zipcode ranges.
 | New York City calling compliance flag limiting calls to 1 per rolling 7-day period  for borrowers in NYC zipcodes. Implements NYC's municipal-level restrictions that  are more stringent than state requirements, determined by specific zipcode ranges.
 | `[]` | `{}` |
    | `IS_TEXTABLE_NYC` | 65 | `BOOLEAN` | New York City SMS compliance flag limiting text messages to 1 per rolling 7-day period  for borrowers in NYC zipcodes. Maintains NYC's restrictive approach across all  communication channels with geographic-specific application.
 | New York City SMS compliance flag limiting text messages to 1 per rolling 7-day period  for borrowers in NYC zipcodes. Maintains NYC's restrictive approach across all  communication channels with geographic-specific application.
 | `[]` | `{}` |
    | `IS_EMAILABLE_NYC` | 66 | `BOOLEAN` | New York City email compliance flag limiting emails to 1 per rolling 7-day period  for borrowers in NYC zipcodes. Completes NYC's comprehensive single-contact approach  across all communication channels for municipal-level consumer protection.
 | New York City email compliance flag limiting emails to 1 per rolling 7-day period  for borrowers in NYC zipcodes. Completes NYC's comprehensive single-contact approach  across all communication channels for municipal-level consumer protection.
 | `[]` | `{}` |
    | `IS_CONTACTABLE_NYC` | 67 | `BOOLEAN` | New York City daily total contact compliance flag limiting calls and SMS combined to  2 per day for borrowers in NYC zipcodes. Implements NYC's unique combination of daily  aggregate limits with weekly per-channel limits for comprehensive contact management. | New York City daily total contact compliance flag limiting calls and SMS combined to  2 per day for borrowers in NYC zipcodes. Implements NYC's unique combination of daily  aggregate limits with weekly per-channel limits for comprehensive contact management. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.calendar_table_xf`
    *   `model.cherry_data_model.daily_loan_xf`
    *   `model.cherry_data_model.int_borrower_timezones`
    *   `model.cherry_data_model.omnichannel_collections_outbounds_xf`
    *   `model.cherry_data_model.src_borrower_flags`
    *   `model.cherry_data_model.src_borrower_old_risc_features`
    *   `model.cherry_data_model.src_borrowers`
    *   `model.cherry_data_model.src_cherry_loans`
    *   `model.cherry_data_model.src_cherry_payments`
    *   `model.cherry_data_model.src_commitments`
    *   `model.cherry_data_model.src_debt_sale_transactions`
    *   `model.cherry_data_model.src_flexible_payments`
    *   `model.cherry_data_model.src_loan_offers_audit`
    *   `model.cherry_data_model.src_loan_schedule`
    *   `model.cherry_data_model.stg_forbearances`
    *   `model.cherry_data_model.stg_zendesk_tickets`
    *   `model.cherry_data_model.unsubscribed_borrowers_xf`
    *   `model.cherry_data_model.zendesk_collections_and_recoveries_eligible_tickets_xf`
    *   `source.cherry_data_model.mongo_notes.LOAN_FOLLOW_UP_DATE_NOTES`

---
