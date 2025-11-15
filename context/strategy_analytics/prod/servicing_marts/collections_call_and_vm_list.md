## Model: `collections_call_and_vm_list`

`collections_call_and_vm_list`

*   **Unique ID:** `model.cherry_data_model.collections_call_and_vm_list`
*   **FQN:** `prod.servicing_marts.collections_call_and_vm_list`
*   **Description:** This model generates a prioritized call list for the Collections and Recoveries team. It uses time zones and propensity to pay to determine the highest priority borrowers to call, and then ranks them within each of our business hours.
*   **Tags:** `['servicing_and_collections', 'daily']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `CALLING_ORDER` | 1 | `NUMBER` | Numeric priority order for calling based on borrower timezone to optimize agent productivity and ensure TCPA compliance. Values: EST=1, CST=2, MST=3, PST=4, HST/AKST=5, Unknown=-1. Lower numbers indicate higher priority for earlier calling windows.
 | Numeric priority order for calling based on borrower timezone to optimize agent productivity and ensure TCPA compliance. Values: EST=1, CST=2, MST=3, PST=4, HST/AKST=5, Unknown=-1. Lower numbers indicate higher priority for earlier calling windows.
 | `[]` | `{}` |
    | `BORROWER_ID` | 2 | `NUMBER` | Unique identifier for the borrower
 | Unique identifier for the borrower
 | `[]` | `{}` |
    | `CALL_HOUR` | 3 | `NUMBER` | Hour of day (EST) when the call is scheduled
 | Hour of day (EST) when the call is scheduled
 | `[]` | `{}` |
    | `CALL_RANK` | 4 | `NUMBER` | Rank used to prioritize borrowers within the call list
 | Rank used to prioritize borrowers within the call list
 | `[]` | `{}` |
    | `CONTRACT_ID` | 5 | `TEXT` | Identifier for the loan contract associated with the borrower
 | Identifier for the loan contract associated with the borrower
 | `[]` | `{}` |
    | `FIRST_NAME` | 6 | `TEXT` | Borrower’s first name
 | Borrower’s first name
 | `[]` | `{}` |
    | `LAST_NAME` | 7 | `TEXT` | Borrower’s last name
 | Borrower’s last name
 | `[]` | `{}` |
    | `FULL_NAME` | 8 | `TEXT` | Concatenated borrower full name (FIRST_NAME + LAST_NAME)
 | Concatenated borrower full name (FIRST_NAME + LAST_NAME)
 | `[]` | `{}` |
    | `PAYOFF` | 9 | `NUMBER` | Total payoff amount required to close the loan (collections only, recoveries will be 0)
 | Total payoff amount required to close the loan (collections only, recoveries will be 0)
 | `[]` | `{}` |
    | `AMOUNT_DUE` | 10 | `NUMBER` | Amount currently due for payment
 | Amount currently due for payment
 | `[]` | `{}` |
    | `TOTAL_AMOUNT_DUE` | 11 | `NUMBER` | Sum of all outstanding amounts including past due balances
 | Sum of all outstanding amounts including past due balances
 | `[]` | `{}` |
    | `DAYS_PAST_DUE` | 12 | `NUMBER` | Number of days since the most recent missed payment
 | Number of days since the most recent missed payment
 | `[]` | `{}` |
    | `REMAINING_BALANCE` | 13 | `NUMBER` | Remaining principal balance on the loan
 | Remaining principal balance on the loan
 | `[]` | `{}` |
    | `SKIP_TRACE` | 14 | `TEXT` | Flag indicating whether borrower requires skip tracing
 | Flag indicating whether borrower requires skip tracing
 | `[]` | `{}` |
    | `PHONE_NUMBER` | 15 | `TEXT` | Primary borrower phone number
 | Primary borrower phone number
 | `[]` | `{}` |
    | `THIRD_PARTY_PHONE_NUMBER_1` | 16 | `TEXT` | Alternate or third-party contact number 1
 | Alternate or third-party contact number 1
 | `[]` | `{}` |
    | `THIRD_PARTY_PHONE_NUMBER_2` | 17 | `TEXT` | Alternate or third-party contact number 2
 | Alternate or third-party contact number 2
 | `[]` | `{}` |
    | `THIRD_PARTY_PHONE_NUMBER_3` | 18 | `TEXT` | Alternate or third-party contact number 3
 | Alternate or third-party contact number 3
 | `[]` | `{}` |
    | `THIRD_PARTY_PHONE_NUMBER_4` | 19 | `TEXT` | Alternate or third-party contact number 4
 | Alternate or third-party contact number 4
 | `[]` | `{}` |
    | `THIRD_PARTY_PHONE_NUMBER_5` | 20 | `TEXT` | Alternate or third-party contact number 5
 | Alternate or third-party contact number 5
 | `[]` | `{}` |
    | `THIRD_PARTY_PHONE_NUMBER_6` | 21 | `TEXT` | Alternate or third-party contact number 6
 | Alternate or third-party contact number 6
 | `[]` | `{}` |
    | `THIRD_PARTY_PHONE_NUMBER_7` | 22 | `TEXT` | Alternate or third-party contact number 7
 | Alternate or third-party contact number 7
 | `[]` | `{}` |
    | `THIRD_PARTY_PHONE_NUMBER_8` | 23 | `TEXT` | Alternate or third-party contact number 8
 | Alternate or third-party contact number 8
 | `[]` | `{}` |
    | `THIRD_PARTY_PHONE_NUMBER_9` | 24 | `TEXT` | Alternate or third-party contact number 9
 | Alternate or third-party contact number 9
 | `[]` | `{}` |
    | `THIRD_PARTY_PHONE_NUMBER_10` | 25 | `TEXT` | Alternate or third-party contact number 10
 | Alternate or third-party contact number 10
 | `[]` | `{}` |
    | `SMS_OPT_OUT` | 26 | `BOOLEAN` | Flag indicating whether borrower opted out of SMS communications
 | Flag indicating whether borrower opted out of SMS communications
 | `[]` | `{}` |
    | `EMAIL` | 27 | `TEXT` | Borrower’s email address
 | Borrower’s email address
 | `[]` | `{}` |
    | `STATE_ABBREVIATION` | 28 | `TEXT` | Two-letter abbreviation of borrower’s state
 | Two-letter abbreviation of borrower’s state
 | `[]` | `{}` |
    | `ZIP` | 29 | `TEXT` | Borrower’s ZIP code
 | Borrower’s ZIP code
 | `[]` | `{}` |
    | `IS_NEW_YORK_CITY_ZIPCODE` | 30 | `BOOLEAN` | Boolean flag identifying if ZIP code is within New York City
 | Boolean flag identifying if ZIP code is within New York City
 | `[]` | `{}` |
    | `TIME_ZONE` | 31 | `TEXT` | Borrower’s local time zone used for contact timing
 | Borrower’s local time zone used for contact timing
 | `[]` | `{}` |
    | `LOAN_ID` | 32 | `NUMBER` | Unique identifier of the loan within servicing systems
 | Unique identifier of the loan within servicing systems
 | `[]` | `{}` |
    | `SERVICING_URL` | 33 | `TEXT` | Direct link to the loan in the Cherry dashboard
 | Direct link to the loan in the Cherry dashboard
 | `[]` | `{}` |
    | `PROPENSITY_TO_PAY_RISK_SCORE` | 34 | `FLOAT` | Score predicting likelihood of payment
 | Score predicting likelihood of payment
 | `[]` | `{}` |
    | `PROPENSITY_TO_PAY_BUCKET` | 35 | `TEXT` | Categorical bucket derived from propensity-to-pay score
 | Categorical bucket derived from propensity-to-pay score
 | `[]` | `{}` |
    | `RISK_SCORE` | 36 | `NUMBER` | Overall loan or borrower risk score
 | Overall loan or borrower risk score
 | `[]` | `{}` |
    | `CHARGE_OFF_DATE` | 37 | `DATE` | Date the loan was charged off
 | Date the loan was charged off
 | `[]` | `{}` |
    | `MONTHS_SINCE_CHARGE_OFF` | 38 | `NUMBER` | Number of months since charge-off event
 | Number of months since charge-off event
 | `[]` | `{}` |
    | `BANK_ACCOUNT_LAST_4_DIGIT` | 39 | `TEXT` | Last four digits of borrower’s linked bank account
 | Last four digits of borrower’s linked bank account
 | `[]` | `{}` |
    | `BANK_ACCOUNT_BALANCE` | 40 | `FLOAT` | Latest known balance of borrower’s linked bank account
 | Latest known balance of borrower’s linked bank account
 | `[]` | `{}` |
    | `DID_FIRST_PAYMENT_DEFAULT` | 41 | `BOOLEAN` | Indicates whether the borrower missed their first scheduled payment
 | Indicates whether the borrower missed their first scheduled payment
 | `[]` | `{}` |
    | `ORIGINAL_MATURITY_DATE` | 42 | `DATE` | Original scheduled maturity date of the loan
 | Original scheduled maturity date of the loan
 | `[]` | `{}` |
    | `NEXT_FOLLOW_UP_DATE` | 43 | `DATE` | Next scheduled follow-up or contact date for collections
 | Next scheduled follow-up or contact date for collections
 | `[]` | `{}` |
    | `BORROWER_LANGUAGE` | 44 | `TEXT` | Preferred language of borrower for communication
 | Preferred language of borrower for communication
 | `[]` | `{}` |
    | `ANY_CONTACT_ELIGIBLE` | 45 | `NUMBER` | Flag indicating borrower is eligible for any contact channel
 | Flag indicating borrower is eligible for any contact channel
 | `[]` | `{}` |
    | `CALL_ELIGIBLE` | 46 | `NUMBER` | Flag indicating borrower is eligible for phone call outreach
 | Flag indicating borrower is eligible for phone call outreach
 | `[]` | `{}` |
    | `VOICEMAIL_ELIGIBLE` | 47 | `NUMBER` | Flag indicating borrower is eligible for voicemail drop
 | Flag indicating borrower is eligible for voicemail drop
 | `[]` | `{}` |
    | `NO_DIAL_GROUP` | 48 | `NUMBER` | Indicates borrower belongs to a no-dial control group
 | Indicates borrower belongs to a no-dial control group
 | `[]` | `{}` |
    | `CONTROL_GROUP` | 49 | `NUMBER` | Flag for experimental or control group segmentation
 | Flag for experimental or control group segmentation
 | `[]` | `{}` |
    | `EQUABLI_SCORE` | 50 | `NUMBER` | Indicator if this borrower was scored by Equabli
 | Indicator if this borrower was scored by Equabli
 | `[]` | `{}` |
    | `PRODIGAL_HOUR` | 51 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRODIGAL_SCORE` | 52 | `NUMBER` | Indicator if this borrower was scored by Prodigal
 | Indicator if this borrower was scored by Prodigal
 | `[]` | `{}` |
    | `IS_PAST_DUE` | 53 | `TEXT` | Flag indicating whether borrower account is currently past due
 | Flag indicating whether borrower account is currently past due
 | `[]` | `{}` |
    | `IS_CHARGED_OFF` | 54 | `TEXT` | Flag indicating whether loan has been charged off
 | Flag indicating whether loan has been charged off
 | `[]` | `{}` |
    | `MAXDPD` | 55 | `NUMBER` | Maximum historical days past due on the loan
 | Maximum historical days past due on the loan
 | `[]` | `{}` |
    | `DAY_OF_WEEK` | 56 | `NUMBER` | Numeric representation of day of week
 | Numeric representation of day of week
 | `[]` | `{}` |
    | `WEEKEND_FLAG` | 57 | `NUMBER` | Indicates if call date falls on a weekend
 | Indicates if call date falls on a weekend
 | `[]` | `{}` |
    | `AI_VOICE_ELIGIBLE` | 58 | `BOOLEAN` | Flag indicating borrower is eligible for AI voice
 | Flag indicating borrower is eligible for AI voice
 | `[]` | `{}` |
    | `LOAN_ID_EXTRACTED` | 59 | `TEXT` | Loan ID parsed from the SERVICING_URL field using split_part | Loan ID parsed from the SERVICING_URL field using split_part | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.applications_loans_xf`
    *   `model.cherry_data_model.collections_call_list_today_exclusions_xf`
    *   `model.cherry_data_model.collections_compliance_list`
    *   `model.cherry_data_model.daily_loan_xf`
    *   `model.cherry_data_model.int_call_list_hours`
    *   `model.cherry_data_model.int_eligible_call_list`
    *   `model.cherry_data_model.src_borrower_segmentation`
    *   `model.cherry_data_model.src_segments`
    *   `model.cherry_data_model.stg_joined_cherry_payments_and_transactions`
    *   `model.cherry_data_model.stg_unsubscribed_mobile_phones`

---
