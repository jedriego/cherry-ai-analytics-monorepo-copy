## Model: `one_touch_resolution_interactions_xf_archive`

`one_touch_resolution_interactions_xf_archive`

*   **Unique ID:** `model.cherry_data_model.one_touch_resolution_interactions_xf_archive`
*   **FQN:** `prod.archive.one_touch_resolution_interactions_xf_archive`
*   **Description:** ## Overview

This model serves as the base for calculating one touch resolution rate for the customer support
team. It is based on the intermediate model
[int_one_touch_contact_information_joined](/#!/model/model.cherry_data_model.int_one_touch_contact_information_joined)
which joins multiple attributes for single interactions such as known email addresses or phone
numbers to allow us to calculate a rate which is more channel agnostic than the current method
which functions solely on phone number matching.

For example, with the current model a borrower who calls once but chats in three days later
would be counted as a one touch resolution. In this model they would not be. The reverse is also
true. If a merchant chats in but does not reach out via chat, voice, or email again for a week
they would count as a one touch resolution when currently they would be ignored.

The base are interactions which are old enough—they are older than 4 days from today—and they
began **during** operating hours. Subsequent interactions **will** count against one touch resolution
rate if they are intiated **outside** of operating hours, but with the current exclusions on inbound
interactions this is about 0.3% of the total considered interaction volume.
*   **Tags:** `['archive', 'customer_support', 'genesys', 'one_touch']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `INITIAL_CONVERSATION_ID` | 1 | `TEXT` |  | The Genesys UUID for the conversation that we are checking to see if the support team handled within a **single** interaction within four days.
 | `[]` | `{}` |
    | `NEXT_CONVERSATION_ID` | 2 | `TEXT` |  | The Genesys UUID for the conversation that was the next one handled from a particular customer. It is joined based on the `interaction_partition_key` and the `interaction_number` for the joined interaction being 1 greater than the base interaction
 | `[]` | `{}` |
    | `INITIAL_QUEUE` | 3 | `TEXT` |  | The queue within Genesys that the initial interaction took place on | `[]` | `{}` |
    | `NEXT_QUEUE` | 4 | `TEXT` |  | The name of the queue within Genesys that the next interaction took place on | `[]` | `{}` |
    | `INITIAL_AGENT_NAME` | 5 | `TEXT` |  | The name of the agent who handled the initial interaction | `[]` | `{}` |
    | `NEXT_AGENT_NAME` | 6 | `TEXT` |  | The name of the agent who handled the next interaction from the customer | `[]` | `{}` |
    | `INITIAL_MEDIA_TYPE` | 7 | `TEXT` |  | The media type of the initial interaction with the customer within Genesys | `[]` | `{}` |
    | `NEXT_MEDIA_TYPE` | 8 | `TEXT` |  | The media type of the next interaction with the customer within Genesys | `[]` | `{}` |
    | `INITIAL_WRAP_UP_CODE_NAME` | 9 | `TEXT` |  | The initial name for the initial wrap-up code for the customer's interactions | `[]` | `{}` |
    | `NEXT_WRAP_UP_CODE_NAME` | 10 | `TEXT` |  | The name for the next wrap-up code for the customer's interactions. Will be `NULL` if there is not a matching interaction | `[]` | `{}` |
    | `INITIAL_WRAP_UP_CODE_GROUP` | 11 | `TEXT` |  | The higher-level wrap-up code grouping for the initial interaction as defined within the Genesys wrap-up code seed | `[]` | `{}` |
    | `NEXT_WRAP_UP_CODE_GROUP` | 12 | `TEXT` |  | The higher-level wrap-up code grouping for the next interaction as defined within the Genesys wrap-up code seed | `[]` | `{}` |
    | `INITIAL_EXTERNAL_PHONE` | 13 | `TEXT` |  | The external phone for the initial interaction with the customer | `[]` | `{}` |
    | `INTIAL_EXTERNAL_EMAIL` | 14 | `TEXT` |  | The external email for the initial interaction with the customer | `[]` | `{}` |
    | `INITIAL_MERCHANT_ID` | 15 | `NUMBER` |  | The merchant ID for the initial interaction. Either provided directly by Genesys if it is a chat or inferred from the phone number or email address associated with the interaction
 | `[]` | `{}` |
    | `INTIAL_BORROWER_ID` | 16 | `NUMBER` |  |  | `[]` | `{}` |
    | `INITIAL_CUSTOMER_ID` | 17 | `TEXT` |  | The ID provided by Genesys for the participant of a chat interaction. Genesys does not split out if it is a borrower or merchant, so we derive the previous two columns based on the queue and data from joins.
 | `[]` | `{}` |
    | `INTERACTION_MATCHING_KEY` | 18 | `TEXT` |  | ## Interaction Partition Key

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
    | `INITIAL_INTERACTION_BEGIN` | 19 | `TIMESTAMP_NTZ` |  | The timestamp from Genesys for when the initial interaction with the customer began | `[]` | `{}` |
    | `NEXT_INTERACTION_BEGIN` | 20 | `TIMESTAMP_NTZ` |  | The timestamp from Genesys for when the next interaction began | `[]` | `{}` |
    | `INITIAL_INTERACTION_NUMBER` | 21 | `NUMBER` |  | The number for the intial interaction. Based on `ROW_NUMBER() ...` function in the predecessor model on the `interaction_matching_key` | `[]` | `{}` |
    | `NEXT_INTERACTION_NUMBER` | 22 | `NUMBER` |  | The number for the next interaction. Based on `ROW_NUMBER() ...` function in the predecessor model on the `interaction_matching_key` | `[]` | `{}` |
    | `IS_ONE_TOUCH_SEVEN_ELIGIBLE` | 23 | `BOOLEAN` |  | If the interaction is eligible to be considered for seven day one touch resolution rate in addition to four | `[]` | `{}` |
    | `TIME_DIFFERENCE` | 24 | `NUMBER` |  | The time difference between the first interaction and the next interaction that was joined to it using the `interaction_matching_key` and the `interaction_number`. It's derived as a number of days from using the difference between the two timestamp differences in seconds
 | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.int_one_touch_contact_information_joined`

---
