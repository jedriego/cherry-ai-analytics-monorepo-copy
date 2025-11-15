## Model: `tagged_customer_satisfaction_responses_xf`

`tagged_customer_satisfaction_responses_xf`

*   **Unique ID:** `model.cherry_data_model.tagged_customer_satisfaction_responses_xf`
*   **FQN:** `prod.customer_support_marts.tagged_customer_satisfaction_responses_xf`
*   **Description:** **Tagged Customer Satisfaction Response Processing for Support Team**
This model processes Delighted customer satisfaction survey responses with intelligent tag-based  corrections and specialist reassignments. It serves as the definitive source for support team  CSAT analysis by applying business rules to handle common data quality issues and attribution  corrections through Delighted's tagging system.
**Key Business Logic:** - **Score Correction**: Automatically updates survey scores based on specialist-applied tags 
  ('Update to 1', 'Update to 2', etc.) to correct accidental misscoring by customers
- **Agent Reassignment**: Uses first name matching in tags combined with ops_user_teams tenure 
  data to reassign surveys to the correct specialist when initial attribution is incorrect
- **Response Filtering**: Excludes responses tagged with 'Remove' to handle invalid or duplicate surveys - **Manager Attribution**: Adds operational manager context based on agent assignments and tenure dates
**Data Sources:** - `int_aggregated_support_satisfaction_responses`: Aggregated Delighted survey data with contact integration - `ops_user_teams`: Historical team assignments and management hierarchy for accurate attribution - Delighted tag system: Specialist-applied tags for corrections and reassignments
**Primary Use Cases:** - Support team performance analysis and CSAT tracking by specialist - Corrected customer satisfaction reporting with proper agent attribution - Management reporting with accurate scores after specialist corrections - Quality assurance and survey data validation

*   **Tags:** `['customer_support', 'customer_satisfaction', 'support', 'core_operating_results', 'zendesk_transcripts']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `PERSON_ID` | 1 | `TEXT` | Unique identifier for the survey respondent in Delighted's system. Links to person profile  data and enables tracking of multiple responses from the same individual. Used for customer  relationship analysis and response history tracking. Sourced from int_aggregated_support_satisfaction_responses.
 | Unique identifier for the survey respondent in Delighted's system. Links to person profile  data and enables tracking of multiple responses from the same individual. Used for customer  relationship analysis and response history tracking. Sourced from int_aggregated_support_satisfaction_responses.
 | `[]` | `{}` |
    | `PERSON_NAME` | 2 | `TEXT` | Full name of the survey respondent as stored in Delighted. Used for customer identification  and personalized follow-up communications. May be NULL if not provided during survey.  Sourced from Delighted person data.
 | Full name of the survey respondent as stored in Delighted. Used for customer identification  and personalized follow-up communications. May be NULL if not provided during survey.  Sourced from Delighted person data.
 | `[]` | `{}` |
    | `PERSON_EMAIL` | 3 | `TEXT` | Email address of the survey respondent. Primary contact method for survey follow-up and  customer service outreach. Used for customer identification and communication. May be NULL  if not provided. Sourced from Delighted person data.
 | Email address of the survey respondent. Primary contact method for survey follow-up and  customer service outreach. Used for customer identification and communication. May be NULL  if not provided. Sourced from Delighted person data.
 | `[]` | `{}` |
    | `PERSON_PHONE_COPY` | 4 | `TEXT` | Phone number of the survey respondent copied from survey properties. Used for alternative  contact method and customer identification. May be NULL if not provided during survey.  Sourced from Delighted response properties.
 | Phone number of the survey respondent copied from survey properties. Used for alternative  contact method and customer identification. May be NULL if not provided during survey.  Sourced from Delighted response properties.
 | `[]` | `{}` |
    | `SURVEY_TYPE` | 5 | `TEXT` | Type of Delighted survey conducted (e.g., 'NPS', 'CSAT', 'CES'). Indicates the survey  methodology and scale used for the response. Used for survey type analysis and appropriate  score interpretation. Sourced from Delighted response data.
 | Type of Delighted survey conducted (e.g., 'NPS', 'CSAT', 'CES'). Indicates the survey  methodology and scale used for the response. Used for survey type analysis and appropriate  score interpretation. Sourced from Delighted response data.
 | `[]` | `{}` |
    | `RESPONSE_ID` | 6 | `TEXT` | Unique identifier for each survey response in Delighted's system. Primary key for tracking  individual survey submissions and linking to response metadata. Used for response analysis  and data integrity. Sourced from int_aggregated_support_satisfaction_responses.
 | Unique identifier for each survey response in Delighted's system. Primary key for tracking  individual survey submissions and linking to response metadata. Used for response analysis  and data integrity. Sourced from int_aggregated_support_satisfaction_responses.
 | `[]` | `{}` |
    | `NICE_CONTACT_ID` | 7 | `NUMBER` | Contact identifier from NICE system linking the survey to the original customer service interaction.  Enables tracing satisfaction scores back to specific call or interaction records. Used for  interaction-level analysis and quality assurance. May be NULL for non-NICE interactions.
 | Contact identifier from NICE system linking the survey to the original customer service interaction.  Enables tracing satisfaction scores back to specific call or interaction records. Used for  interaction-level analysis and quality assurance. May be NULL for non-NICE interactions.
 | `[]` | `{}` |
    | `ZENDESK_TICKET_ID` | 8 | `NUMBER` | Zendesk ticket identifier linking the survey response to the support ticket that generated it.  Enables correlation between ticket resolution and customer satisfaction. Used for ticket-level  satisfaction analysis and support quality tracking. May be NULL for non-ticket interactions.
 | Zendesk ticket identifier linking the survey response to the support ticket that generated it.  Enables correlation between ticket resolution and customer satisfaction. Used for ticket-level  satisfaction analysis and support quality tracking. May be NULL for non-ticket interactions.
 | `[]` | `{}` |
    | `RESPONSE_SCORE` | 9 | `NUMBER` | **Corrected satisfaction score** after applying tag-based adjustments. Original score is  updated when tags indicate score corrections ('Update to 1' through 'Update to 5').  Scale typically 1-5 for CSAT surveys. This is the corrected score that should be used  for all analysis. Derived from original response_score with tag-based CASE logic.
 | **Corrected satisfaction score** after applying tag-based adjustments. Original score is  updated when tags indicate score corrections ('Update to 1' through 'Update to 5').  Scale typically 1-5 for CSAT surveys. This is the corrected score that should be used  for all analysis. Derived from original response_score with tag-based CASE logic.
 | `[]` | `{}` |
    | `CREATED_AT` | 10 | `TIMESTAMP_TZ` | UTC timestamp when the survey response was submitted in Delighted's system. Used for  temporal analysis, response timing patterns, and data freshness validation. Critical for  time-based reporting and trend analysis. Sourced from int_aggregated_support_satisfaction_responses.
 | UTC timestamp when the survey response was submitted in Delighted's system. Used for  temporal analysis, response timing patterns, and data freshness validation. Critical for  time-based reporting and trend analysis. Sourced from int_aggregated_support_satisfaction_responses.
 | `[]` | `{}` |
    | `CREATED_AT_PT` | 11 | `TIMESTAMP_NTZ` | Pacific Time timestamp of survey response submission, converted from created_at. Used for  business hour analysis, Pacific timezone reporting, and operational timing alignment.  Derived using convert_to_pt macro from created_at.
 | Pacific Time timestamp of survey response submission, converted from created_at. Used for  business hour analysis, Pacific timezone reporting, and operational timing alignment.  Derived using convert_to_pt macro from created_at.
 | `[]` | `{}` |
    | `SURVEY_CHANNEL` | 12 | `TEXT` | Channel through which the survey was delivered to the respondent (e.g., 'email', 'web', 'sms').  Indicates the survey distribution method and helps analyze channel effectiveness and response  patterns. Used for channel performance analysis. Sourced from Delighted response properties.
 | Channel through which the survey was delivered to the respondent (e.g., 'email', 'web', 'sms').  Indicates the survey distribution method and helps analyze channel effectiveness and response  patterns. Used for channel performance analysis. Sourced from Delighted response properties.
 | `[]` | `{}` |
    | `INTERACTION_CHANNEL` | 13 | `TEXT` | Customer service channel where the interaction occurred that triggered the survey (e.g., 'phone',  'email', 'chat'). Links the satisfaction response to the original service interaction type.  Used for channel-specific satisfaction analysis. Sourced from Delighted response properties.
 | Customer service channel where the interaction occurred that triggered the survey (e.g., 'phone',  'email', 'chat'). Links the satisfaction response to the original service interaction type.  Used for channel-specific satisfaction analysis. Sourced from Delighted response properties.
 | `[]` | `{}` |
    | `AGENT_NAME` | 14 | `TEXT` | **Corrected agent name** responsible for the customer interaction. Uses intelligent reassignment  logic that prioritizes tag-based corrections over original attribution. When tags contain a  first name that matches ops_user_teams data within valid tenure dates, that agent is assigned.  Otherwise uses original agent_name from Delighted. Critical for accurate performance attribution.  Derived from CASE logic combining matching_full_names array and original agent data.
 | **Corrected agent name** responsible for the customer interaction. Uses intelligent reassignment  logic that prioritizes tag-based corrections over original attribution. When tags contain a  first name that matches ops_user_teams data within valid tenure dates, that agent is assigned.  Otherwise uses original agent_name from Delighted. Critical for accurate performance attribution.  Derived from CASE logic combining matching_full_names array and original agent data.
 | `[]` | `{}` |
    | `SKILL_NAME` | 15 | `TEXT` | Customer service skill or queue name where the interaction was handled. Represents the specific  service area or specialization (e.g., 'Billing', 'Technical Support'). Used for skill-based  performance analysis and queue optimization. Sourced from Delighted response properties or queue data.
 | Customer service skill or queue name where the interaction was handled. Represents the specific  service area or specialization (e.g., 'Billing', 'Technical Support'). Used for skill-based  performance analysis and queue optimization. Sourced from Delighted response properties or queue data.
 | `[]` | `{}` |
    | `RESPONSE_COMMENT` | 16 | `TEXT` | Free-text feedback provided by the survey respondent. Contains customer comments,  suggestions, or detailed feedback about their experience. Used for qualitative analysis  and customer insight extraction. May be NULL if no comment provided. Sourced from Delighted response.
 | Free-text feedback provided by the survey respondent. Contains customer comments,  suggestions, or detailed feedback about their experience. Used for qualitative analysis  and customer insight extraction. May be NULL if no comment provided. Sourced from Delighted response.
 | `[]` | `{}` |
    | `FULL_TAGS` | 17 | `TEXT` | Complete concatenated string of all Delighted tags applied to this response, separated by commas.  Contains specialist-applied tags for score corrections ('Update to 1-5'), agent reassignments  (first names), and response filtering ('Remove'). Used for quality control, correction tracking,  and data validation. Combines response tags and person tags with response tags taking priority.  Sourced from int_aggregated_support_satisfaction_responses tag aggregation. | Complete concatenated string of all Delighted tags applied to this response, separated by commas.  Contains specialist-applied tags for score corrections ('Update to 1-5'), agent reassignments  (first names), and response filtering ('Remove'). Used for quality control, correction tracking,  and data validation. Combines response tags and person tags with response tags taking priority.  Sourced from int_aggregated_support_satisfaction_responses tag aggregation. | `[]` | `{}` |
    | `OPS_MANAGER` | 18 | `TEXT` | Manager of the assigned agent at the time of the survey response, based on ops_user_teams  hierarchy and valid tenure dates. Used for management reporting, escalation chains, and  team performance analysis. Provides management accountability for customer satisfaction scores.  May be NULL if manager information not available. Sourced from ops_user_teams manager field.
 | Manager of the assigned agent at the time of the survey response, based on ops_user_teams  hierarchy and valid tenure dates. Used for management reporting, escalation chains, and  team performance analysis. Provides management accountability for customer satisfaction scores.  May be NULL if manager information not available. Sourced from ops_user_teams manager field.
 | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.int_aggregated_support_satisfaction_responses`
    *   `seed.cherry_data_model.ops_user_teams`

---
