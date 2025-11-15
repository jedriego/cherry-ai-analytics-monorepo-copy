## Model: `support_conversion_rate_xf_archive`

`support_conversion_rate_xf_archive`

*   **Unique ID:** `model.cherry_data_model.support_conversion_rate_xf_archive`
*   **FQN:** `prod.archive.support_conversion_rate_xf_archive`
*   **Description:** This table marries inbound, borrower, and merchant information with application information to demonstrate the effects of customer support interactions on the progression of a patient's application. With this information, we can calculate a support conversion rate: of patients who call in with a specific set of wrap up codes, what percentage of them reach a final application decision within 7 days as a direct result of a support interaction? This can then be broken out by any time period of interest, as well as by Genesys user. For more information on the details of this calculation, check out the Guru card here: 
https://app.getguru.com/boards/iLx9MBMT/Operations-Analytics/?activeCard=7c7c9a40-4a89-4908-b975-09a8b9e51688&boardSectionId=b0c3df56-71fb-4678-bd01-dd76eb93fd52

*   **Tags:** `['archive', 'customer_support', 'genesys']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `CONVERSATION_ID` | 1 | `TEXT` |  | The UUID of the conversation from Genesys.
 | `[]` | `{}` |
    | `CONVERSATION_START` | 2 | `TIMESTAMP_NTZ` |  | The timestamp of when the conversation began, in PST | `[]` | `{}` |
    | `CONVERSATION_END` | 3 | `TIMESTAMP_NTZ` |  | The timestamp of when the conversation ended, in PST | `[]` | `{}` |
    | `CONVERSATION_LENGTH` | 4 | `NUMBER` |  | The difference between the conversation start and the conversation end, in seconds | `[]` | `{}` |
    | `ORIGINATING_DIRECTION` | 5 | `TEXT` |  | The direction that the interaction originated from as logged by Genesys | `[]` | `{}` |
    | `QUEUE_NAME` | 6 | `TEXT` |  | The name of the queue that the interaction took place on | `[]` | `{}` |
    | `MEDIA_TYPE` | 7 | `TEXT` |  | The media type of the interaction. All the Genesys interactions have a single media type | `[]` | `{}` |
    | `GENESYS_USER_NAME` | 8 | `TEXT` |  | The name for the user within Genesys. This is derived from the Genesys user information seed which is manually updated
 | `[]` | `{}` |
    | `GENESYS_USER_TEAM` | 9 | `TEXT` |  | The team that the Genesys user belongs to. Derived from the Genesys user information seed | `[]` | `{}` |
    | `INTERACTION_WRAP_UP_CODE_NAME` | 10 | `TEXT` |  | A higher level grouping of wrap-up codes than merely by name. It is provided by the wrap-up code seed file and defined by Irina on the customer support team.
 | `[]` | `{}` |
    | `INTERACTION_WRAP_UP_CODE_GROUP` | 11 | `TEXT` |  |  | `[]` | `{}` |
    | `INTERACTION_EXTERNAL_PHONE` | 12 | `TEXT` |  | The external phone number for the interaction if it is a voice or message interaction | `[]` | `{}` |
    | `INTERACTION_EXTERNAL_EMAIL` | 13 | `TEXT` |  | The external email that the interaction occurred with. The only change versus the table which is is based on is setting the external email to `NULL` if it is from a SMS interaction with a consumer.
 | `[]` | `{}` |
    | `INTERACTION_CUSTOMER_ID` | 14 | `TEXT` |  | The customer ID that an interaction occurred with in Genesys. Depending on what type of customer was reaching out this can be either the:
* Borrower ID
* Merchant ID
* User ID
 | `[]` | `{}` |
    | `INTERACTION_MERCHANT_ID` | 15 | `NUMBER` |  | The associated merchant ID for an interaction. *Mainly provided for testing purposes.* Allows for validation that the `interaction_customer_id` column is behaving as expected for merchant interactions
 | `[]` | `{}` |
    | `INTERACTION_BORROWER_ID` | 16 | `NUMBER` |  | The associated borrower ID for an interaction. *Mainly provided for testing purposes.* Allows for validation that the `interaction_customer_id` column is behaving as expected for borrower/applicant interactions
 | `[]` | `{}` |
    | `IS_INTERACTION_IN_OPERATING_HOURS` | 17 | `BOOLEAN` |  | Whether or not the interaction began within the operating hours. Operating hours can change over time which is why we use an operating hours seed.
Only considers the **support** operating hours for this project
 | `[]` | `{}` |
    | `TIME_AGO` | 18 | `NUMBER` |  | The number of days ago that an interaction occurred | `[]` | `{}` |
    | `INTERACTION_PARTITION_KEY` | 19 | `TEXT` |  | ## Interaction Partition Key

This column is designed to give us a key for partitioning over the set of conversations which are
considered for one touch resolution. It is manufactured by prefixing the customer id for the
interaction with `b-` if the interaction can be attributed to a borrower or `m-` if the interaction
can be attributed to a merchant or organization user. Within the Cherry system there is no *unified*
`person` table which means that borrowers, merchants, users, organizations, etc. may all share the
same auto-incremement key value. This prefix allows us to discriminate between interactions with different
types of consumers that may share the same auto-increment ID.

It is also intended to allow us to determine if the same consumer contacts cherry through **different**
channels within a set period of time by unifying the information we have saved for them together into
a single key.

It makes use of a waterfalling schema of attribution based on the queue. The waterfall is set-up to
run in the following way:

1. Emails

  i. First attributed to merchants with the email address

  ii. Then borrowers with the email address

  iii. Lastly to the email address itself

2. Merchant Queue

  i. If there is a `merchant_id` associated with the interaction it will append `m-` to the `merchant_id`

  ii. If there is no `merchant_id` associated and the wrap up code name contains `Borrower` it will append `b-` to the `borrower_id`

  iii. Then if there is a phone number it will be set to the phone number

  iv. Finally it will be set `m-` the `interaction_customer_id` if none of the conditions above match

3. Borrower Queue

  i. If there is a `borrower_id` associated with the interaction it will append `b-` to the `borrower_id`

  ii. If there is a phone number it will use the phone number

  iii. Finally it will be set to `b-` the `interaction_customer_id` if none of the conditions above match | `[]` | `{}` |
    | `IS_ONE_TOUCH_FOUR_ELIGIBLE` | 20 | `BOOLEAN` |  | A boolean that indicates whether an interaction is eligible to be considered a **base** interaction for 4 day one touch resolution rate. It checks to see if the conversation_start as a date is more than 4 days before the current date.
 | `[]` | `{}` |
    | `IS_ONE_TOUCH_SEVEN_ELIGIBLE` | 21 | `BOOLEAN` |  | A boolean that indicates whether an interaction is eligible to be considered a **base** interaction for 7 day one touch resolution rate. It checks to see if the conversation_start as a date is more than 7 days before the current date.
 | `[]` | `{}` |
    | `CONVERSATION_ID_UNIQUE_KEY` | 22 | `TEXT` |  | A surrogate key generated via dbt_utils from the `conversation_id` and the `conversation_start`. This allows us to apply a `QUALIFY` statement to ensure that we have only one row in the table for each unique pair of these two. **This is useful for removing duplicate rows in the case where multiple merchants share the same phone number within the Cherry database.**
 | `[]` | `{}` |
    | `INTERACTION_NUMBER` | 23 | `NUMBER` |  | The result of applying the `ROW_NUMBER()` function to the `interaction_partition_key`. It allows us to join interactions to one another to determine when, or if, a re-contact occurred for the person who reached out to customer support.
 | `[]` | `{}` |
    | `CONTACT_TYPE` | 24 | `TEXT` |  |  | `[]` | `{}` |
    | `BORROWER_KYC_STATUS` | 25 | `TEXT` |  |  | `[]` | `{}` |
    | `BORROWER_KYC_REASON` | 26 | `TEXT` |  |  | `[]` | `{}` |
    | `PHONE_NUMBER` | 27 | `TEXT` |  |  | `[]` | `{}` |
    | `EMAIL` | 28 | `TEXT` |  |  | `[]` | `{}` |
    | `MERCHANT_NAME` | 29 | `TEXT` |  |  | `[]` | `{}` |
    | `MERCHANT_SIZE` | 30 | `TEXT` |  |  | `[]` | `{}` |
    | `CHERRY_DB_INDUSTRY` | 31 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE` | 32 | `TEXT` |  |  | `[]` | `{}` |
    | `ONBOARDING_SPECIALIST` | 33 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER` | 34 | `TEXT` |  |  | `[]` | `{}` |
    | `GO_LIVE_DATE` | 35 | `DATE` |  |  | `[]` | `{}` |
    | `DAYS_SINCE_GO_LIVE` | 36 | `NUMBER` |  |  | `[]` | `{}` |
    | `RESPONSIBLE_DEPARTMENT` | 37 | `TEXT` |  |  | `[]` | `{}` |
    | `RESPONSIBLE_CONTACT` | 38 | `TEXT` |  |  | `[]` | `{}` |
    | `PRACTICE_LIFECYCLE_STAGE` | 39 | `TEXT` |  |  | `[]` | `{}` |
    | `TOTAL_BORROWERS` | 40 | `NUMBER` |  |  | `[]` | `{}` |
    | `TOTAL_LOANS` | 41 | `NUMBER` |  |  | `[]` | `{}` |
    | `APPLICATION_ID` | 42 | `NUMBER` |  |  | `[]` | `{}` |
    | `INITIAL_STATUS` | 43 | `TEXT` |  | The first recorded application status change for this application_id | `[]` | `{}` |
    | `INITIAL_STATUS_PT` | 44 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `STATUS_TWO` | 45 | `TEXT` |  |  | `[]` | `{}` |
    | `STATUS_TWO_PT` | 46 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `STATUS_THREE` | 47 | `TEXT` |  |  | `[]` | `{}` |
    | `STATUS_THREE_PT` | 48 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `STATUS_FOUR` | 49 | `TEXT` |  |  | `[]` | `{}` |
    | `STATUS_FOUR_PT` | 50 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `FINAL_STATUS` | 51 | `TEXT` |  | The final recorded application status change for this application_id, or 'HAS NOT APPLIED' if an inbound patient has not applied yet. | `[]` | `{}` |
    | `FINAL_STATUS_PT` | 52 | `TIMESTAMP_NTZ` |  | The timestamp in Pacific Time associated with the final recorded application status change for this application_id. | `[]` | `{}` |
    | `TIME_TO_COMPLETION_MINS` | 53 | `NUMBER` |  |  | `[]` | `{}` |
    | `TIME_TO_COMPLETION_DAYS` | 54 | `NUMBER` |  |  | `[]` | `{}` |
    | `ATTRIBUTION_WINDOW` | 55 | `NUMBER` |  |  | `[]` | `{}` |
    | `IS_VALID_WRAP_UP_CODE` | 56 | `NUMBER` |  |  | `[]` | `{}` |
    | `CONVERSION_ELIGIBLE` | 57 | `NUMBER` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.int_inbound_borrower_merchant_info_joined`
    *   `model.cherry_data_model.src_cherry_applications`
    *   `model.cherry_data_model.stg_cherry_application_status_timeline`

---
