## Model: `debt_sale_contracts_pii_hashed_xf_archive`

`debt_sale_contracts_pii_hashed_xf_archive`

*   **Unique ID:** `model.cherry_data_model.debt_sale_contracts_pii_hashed_xf_archive`
*   **FQN:** `prod.archive.debt_sale_contracts_pii_hashed_xf_archive`
*   **Description:** This model takes the results of the model `int_debt_sale_charged_off_contracts` and hashes PII columns using the [SHA-2 function](https://docs.snowflake.com/en/sql-reference/functions/sha2.html) provided by Snowflake to keep borrower information secure for external inspection.

*   **Tags:** `['archive', 'debt_sale']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `LOAN_PRODUCT_TYPE` | 1 | `TEXT` |  | The type of the loan product | `[]` | `{}` |
    | `FIRST_NAME` | 2 | `TEXT` |  | The first name of the borrower | `[]` | `{}` |
    | `LAST_NAME` | 3 | `TEXT` |  | The last name of the borrower hashed via Snowflake | `[]` | `{}` |
    | `IS_CEASE_AND_DESIST` | 4 | `BOOLEAN` |  | Indicates whether the borrower has requested that Cherry cease and desist collections activities | `[]` | `{}` |
    | `BORROWER_SSN` | 5 | `TEXT` |  | The **hashed** SSN of the borrower. It is stored hashed within the Cherry database and double hashed via Snowflake
 | `[]` | `{}` |
    | `ADDRESS` | 6 | `TEXT` |  | The first line for the address of the borrower hashed via Snowflake | `[]` | `{}` |
    | `ADDRESS2` | 7 | `TEXT` |  | The second line for the address of the borrower. Cherry does not currently separate the *different* lines of the address for borrowers or merchants hashed via Snowflake
 | `[]` | `{}` |
    | `CITY` | 8 | `TEXT` |  | The name of the city for the borrower's address | `[]` | `{}` |
    | `ST` | 9 | `TEXT` |  | The name of the city for the borrower's address | `[]` | `{}` |
    | `ZIP` | 10 | `TEXT` |  | The zipcode for the borrower's address | `[]` | `{}` |
    | `HOME_PHONE` | 11 | `TEXT` |  | The home phone number for the borrower. Cherry does not currently collect home phone numbers. Hashed via Snowflake
 | `[]` | `{}` |
    | `WORK_PHONE` | 12 | `TEXT` |  | The work phone number for the borrower. Cherry does not currently collect work phone numbers. Hashed via Snowflake
 | `[]` | `{}` |
    | `MOBILE_PHONE` | 13 | `TEXT` |  | The borrower's mobile phone number hashed via Snowflake | `[]` | `{}` |
    | `LOAN_AMOUNT` | 14 | `FLOAT` |  | The original amount lent to the borrower | `[]` | `{}` |
    | `CHARGE_OFF_AMOUNT` | 15 | `NUMBER` |  | The amount that the loan was originally charged off for | `[]` | `{}` |
    | `CURRENT_BALANCE` | 16 | `NUMBER` |  | The current balance of the contract including all principal and interest and fees accrued | `[]` | `{}` |
    | `PRINCIPAL_OUTSTANDING` | 17 | `NUMBER` |  | The current principal balance outstanding on the contract | `[]` | `{}` |
    | `INTEREST_OUTSTANDING` | 18 | `NUMBER` |  | The current outstanding interest on the contract | `[]` | `{}` |
    | `FEES_OUTSTANDING` | 19 | `NUMBER` |  | The current outstanding fees on the contract | `[]` | `{}` |
    | `CUSTOMER_ID` | 20 | `TEXT` |  | The loan id of the contract which the customer is familiar with. Equivalent to **contract_id** within the Cherry data model | `[]` | `{}` |
    | `LOAN_OPEN_DATE` | 21 | `DATE` |  | The date that the contract was opened with the borrower | `[]` | `{}` |
    | `ORIGINAL_DUE_DATE` | 22 | `DATE` |  | The due date of the customer's last contractual payment | `[]` | `{}` |
    | `CHARGE_OFF_DATE` | 23 | `DATE` |  | The date when the contract was originally charged off | `[]` | `{}` |
    | `ORIGINAL_PRINCIPAL_BALANCE` | 24 | `FLOAT` |  | The original amount lent to the borrower | `[]` | `{}` |
    | `AMOUNT_PAID` | 25 | `NUMBER` |  | The total amount paid on the contract by the borrower before charge off | `[]` | `{}` |
    | `PRINCIPAL_PAID` | 26 | `NUMBER` |  | The total amount paid to principal on the contract by the borrower before charge off | `[]` | `{}` |
    | `INTEREST_PAID` | 27 | `NUMBER` |  | The total amount paid to interest on the contract by the borrower before charge off | `[]` | `{}` |
    | `FEES_PAID` | 28 | `NUMBER` |  | The total amount paid to fees on the contract by the borrower before charge off | `[]` | `{}` |
    | `LAST_PAYMENT_DATE` | 29 | `DATE` |  | The date on which a payment that was **not** the down payment was last received on the account | `[]` | `{}` |
    | `LAST_PAYMENT_AMOUNT` | 30 | `FLOAT` |  | The amount of the last payment that was **not** the down payment | `[]` | `{}` |
    | `AMOUNT_PAID_POST_CHARGE_OFF` | 31 | `NUMBER` |  | The total amount paid by the borrower following the charge off | `[]` | `{}` |
    | `POST_CHARGE_OFF_INTEREST` | 32 | `NUMBER` |  | The interest accrued on the account post charge off. Because Cherry stops interest accrual at charge off this is hard coded to zero
 | `[]` | `{}` |
    | `POST_CHARGE_OFF_FEES` | 33 | `NUMBER` |  | The fees assessed on the account post charge charge off. Because Cherry stops attempting to draft payment this is hard coded to zero.
 | `[]` | `{}` |
    | `FIRST_DEFAULT_DATE` | 34 | `DATE` |  | The final date when the contract went 30+ days past due before the charge off date | `[]` | `{}` |
    | `LAST_RETURN_REASON` | 35 | `TEXT` |  | The last reason which was returned for an ACH payment attempted on the customer's account before charge off | `[]` | `{}` |
    | `LAST_RETURN_DATE` | 36 | `DATE` |  | The last date when an ACH payment was attempted and returned | `[]` | `{}` |
    | `ACCOUNT_ROUTING_NUMBER` | 37 | `TEXT` |  | The routing number of the account which was last attempted for an ACH payment hashed via Snowflake
 | `[]` | `{}` |
    | `CHECKING_ACCOUNT_NUMBER` | 38 | `TEXT` |  | The account number which was last attempted to be debited via ACH for a payment hashed via Snowflake
 | `[]` | `{}` |
    | `BANK_NAME` | 39 | `TEXT` |  | The name of the bank which was last attempted for an ACH debit | `[]` | `{}` |
    | `DRIVERS_LICENSE` | 40 | `TEXT` |  | The driver's license number of the borrower. Cherry does not currently collect this information | `[]` | `{}` |
    | `DRIVERS_LICENSE_STATE` | 41 | `TEXT` |  | The state the borrower's drivers license was issued by. Cherry does not currently collect this information | `[]` | `{}` |
    | `EMPLOYER_COMPANY_NAME` | 42 | `TEXT` |  | The name of the company the borrower is employeed by. Cherry does not currently collect this information | `[]` | `{}` |
    | `EMPLOYMENT_POSITION_DESCRIPTION` | 43 | `TEXT` |  | The name of the borrower's position at their employer. Cherry does not currently collect this information | `[]` | `{}` |
    | `EMPLOYER_PHONE_NUMBER` | 44 | `TEXT` |  | The phone number of the borrower's employer. Cherry does not currently collect this information | `[]` | `{}` |
    | `EMAIL` | 45 | `TEXT` |  | The email that Cherry has on file for the borrower. This is not currently collected for all borrowers. However, some borrowers **choose** to provide it and it is inferred for others by getting the **top matching** email address from their bank account linked via Plaid. Hashed via Snowflake
 | `[]` | `{}` |
    | `DEBTOR_DATEOFBIRTH` | 46 | `DATE` |  | The borrower's date of birth | `[]` | `{}` |
    | `MONTHLY_GROSS_SALARY` | 47 | `TEXT` |  | The borrower's monthly gross salary. Cherry does not currently collect this information | `[]` | `{}` |
    | `MONTHLY_NET_SALARY` | 48 | `TEXT` |  | The borrower's monthly net salary. Cherry does not currently collect this information | `[]` | `{}` |
    | `SALARY_FREQ` | 49 | `TEXT` |  | The borrower's pay frequency. Cherry does not currently collect this information | `[]` | `{}` |
    | `BAD_HOME_ADDRESS_YES_NO` | 50 | `TEXT` |  | Whether the borrower can be reached at the address they provided. Cherry does not currently collect this information | `[]` | `{}` |
    | `OWN_OR_RENT` | 51 | `TEXT` |  | Whether the borrower owns or rents the address they provided. Cherry does not currently collect this information | `[]` | `{}` |
    | `PAID_OFF_LOANS` | 52 | `NUMBER` |  | The number of contracts that the borrower has paid off with Cherry | `[]` | `{}` |
    | `DEBT_AGE` | 53 | `NUMBER` |  | The number of days since the first default date for the contract | `[]` | `{}` |
    | `TERM_IN_MONTHS` | 54 | `NUMBER` |  | The length of the contract in months | `[]` | `{}` |
    | `NSF_CHECK_AMOUNT` | 55 | `FLOAT` |  | The amount of the last **non-down payment** which had an NSF return | `[]` | `{}` |
    | `NSF_LATE_FEES` | 56 | `NUMBER` |  | The amount of fees charged to the borrower due to NSF returns on payments. Cherry **only** charges NSF fees for the first installment payment of a unique delinquency.
 | `[]` | `{}` |
    | `APR` | 57 | `FLOAT` |  | The APR associated with the contract | `[]` | `{}` |
    | `ORIGINATION_TYPE` | 58 | `TEXT` |  | The type of checkout the borrower went through | `[]` | `{}` |
    | `LICENSED_LENDER_NAME` | 59 | `TEXT` |  | The lender which originated the contract | `[]` | `{}` |
    | `ORIGINATION_STORE` | 60 | `NUMBER` |  | The **internal** Cherry id for the merchant that originated the contract | `[]` | `{}` |
    | `ORIGINATION_STATE` | 61 | `TEXT` |  | The state that the merchant that originated the contract is located in | `[]` | `{}` |
    | `STORE_ADDRESS` | 62 | `TEXT` |  | The address of the store that originated the contract | `[]` | `{}` |
    | `VANTAGE_FOUR_SCORE` | 63 | `FLOAT` |  | The credit score (Vantage 4) of the borrower at origination. If the score does not exist the borrower was underwritten solely using cashflow data.
 | `[]` | `{}` |
    | `ORIGINATION_STORE_INDUSTRY` | 64 | `TEXT` |  | The industry which Cherry has the originating store marked in | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.int_debt_sale_charged_off_contracts`

---
