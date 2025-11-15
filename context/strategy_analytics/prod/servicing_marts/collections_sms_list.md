## Model: `collections_sms_list`

`collections_sms_list`

*   **Unique ID:** `model.cherry_data_model.collections_sms_list`
*   **FQN:** `prod.servicing_marts.collections_sms_list`
*   **Description:** This model generates an SMS list for the collections and recovery teams to follow. It attaches both a pre-written message and important metadata about the borrower/loan.
*   **Tags:** `['servicing_and_collections', 'daily']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `SEND_DATE` | 1 | `DATE` | Date when the communication or message is scheduled to be sent to the borrower
 | Date when the communication or message is scheduled to be sent to the borrower
 | `[]` | `{}` |
    | `ASSOCIATED_TEAM` | 2 | `TEXT` | Internal team responsible for the outreach, such as Collections or Recoveries
 | Internal team responsible for the outreach, such as Collections or Recoveries
 | `[]` | `{}` |
    | `HOUR_START` | 3 | `NUMBER` | Hour (ET) before which messages should not be sent; sourced from borrower timezone rules
 | Hour (ET) before which messages should not be sent; sourced from borrower timezone rules
 | `[]` | `{}` |
    | `TIMEZONE` | 4 | `TEXT` | Borrower’s local timezone used to determine permissible contact hours
 | Borrower’s local timezone used to determine permissible contact hours
 | `[]` | `{}` |
    | `STATE_CODE` | 5 | `TEXT` | Two-letter state abbreviation for borrower’s residence or loan origination
 | Two-letter state abbreviation for borrower’s residence or loan origination
 | `[]` | `{}` |
    | `LOAN_ID` | 6 | `NUMBER` | Unique identifier for the borrower’s loan record
 | Unique identifier for the borrower’s loan record
 | `[]` | `{}` |
    | `CONTRACT_ID` | 7 | `TEXT` | Contract identifier tied to the loan agreement
 | Contract identifier tied to the loan agreement
 | `[]` | `{}` |
    | `FIRST_NAME` | 8 | `TEXT` | Borrower’s first name used for personalization in communications
 | Borrower’s first name used for personalization in communications
 | `[]` | `{}` |
    | `PHONE` | 9 | `TEXT` | Primary phone number to contact the borrower
 | Primary phone number to contact the borrower
 | `[]` | `{}` |
    | `TEXT` | 10 | `TEXT` | Body content of the SMS or message prepared for borrower outreach
 | Body content of the SMS or message prepared for borrower outreach
 | `[]` | `{}` |
    | `TEXT_BUCKET` | 11 | `TEXT` | Categorical label grouping messages by content (Recoveries only)
 | Categorical label grouping messages by content (Recoveries only)
 | `[]` | `{}` |
    | `DPD` | 12 | `NUMBER` | Days past due on the borrower’s most recent scheduled payment (Collections only)
 | Days past due on the borrower’s most recent scheduled payment (Collections only)
 | `[]` | `{}` |
    | `PRINCIPAL_BALANCE` | 13 | `NUMBER` | Outstanding principal balance currently owed on the loan (Collections only)
 | Outstanding principal balance currently owed on the loan (Collections only)
 | `[]` | `{}` |
    | `AMOUNT_DUE` | 14 | `NUMBER` | Amount currently due for payment including any past-due portion (Collections only)
 | Amount currently due for payment including any past-due portion (Collections only)
 | `[]` | `{}` |
    | `INSTALL_AMOUNT` | 15 | `FLOAT` | Scheduled installment payment amount due from borrower (Collections only)
 | Scheduled installment payment amount due from borrower (Collections only)
 | `[]` | `{}` |
    | `NEXT_PAYMENT_DATE` | 16 | `DATE` | Date of the borrower’s next scheduled payment (Collections only)
 | Date of the borrower’s next scheduled payment (Collections only)
 | `[]` | `{}` |
    | `FINAL_INSTALL_DUE_DATE` | 17 | `DATE` | Due date of the final remaining installment in the repayment plan (Collections only)
 | Due date of the final remaining installment in the repayment plan (Collections only)
 | `[]` | `{}` |
    | `REMAINING_INSTALLMENTS` | 18 | `NUMBER` | Number of remaining scheduled installments until the loan is fully repaid (Collections only)
 | Number of remaining scheduled installments until the loan is fully repaid (Collections only)
 | `[]` | `{}` |
    | `MONTHS_SINCE_CO` | 19 | `NUMBER` | Number of months elapsed since the loan’s charge-off date (Recoveries only)
 | Number of months elapsed since the loan’s charge-off date (Recoveries only)
 | `[]` | `{}` |
    | `PAYOFF_REMAINING` | 20 | `NUMBER` | Remaining total payoff amount required to close the loan (Recoveries only)
 | Remaining total payoff amount required to close the loan (Recoveries only)
 | `[]` | `{}` |
    | `CHARGE_OFF_DATE` | 21 | `DATE` | Date on which the loan was charged off for accounting purposes (Recoveries only)
 | Date on which the loan was charged off for accounting purposes (Recoveries only)
 | `[]` | `{}` |
    | `DAYS_SINCE_CO` | 22 | `NUMBER` | Number of days elapsed since the charge-off event occurred (Recoveries only)
 | Number of days elapsed since the charge-off event occurred (Recoveries only)
 | `[]` | `{}` |
    | `EQUABLI_SCORE` | 23 | `NUMBER` | External borrower engagement or recovery score sourced from Equabli (Recoveries only)
 | External borrower engagement or recovery score sourced from Equabli (Recoveries only)
 | `[]` | `{}` |
    | `PAYOFF_BUCKET` | 24 | `NUMBER` | Grouping of borrowers based on remaining payoff amount bands (Recoveries only)
 | Grouping of borrowers based on remaining payoff amount bands (Recoveries only)
 | `[]` | `{}` |
    | `DAYS_CO_WINDOW` | 25 | `NUMBER` | Categorized time window representing the number of days since charge-off (Recoveries only)
 | Categorized time window representing the number of days since charge-off (Recoveries only)
 | `[]` | `{}` |
    | `DAYS_CO_GROUP` | 26 | `NUMBER` | Group label assigned based on days since charge-off used for segmentation or offer strategy (Recoveries only) | Group label assigned based on days since charge-off used for segmentation or offer strategy (Recoveries only) | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.collections_compliance_list`
    *   `model.cherry_data_model.int_collections_sms_metadata_joined`
    *   `seed.cherry_data_model.state_codes_and_tz`

---
