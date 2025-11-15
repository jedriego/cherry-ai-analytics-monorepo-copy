## Model: `meaningful_interactions_and_on_site_visits_xf`

`meaningful_interactions_and_on_site_visits_xf`

*   **Unique ID:** `model.cherry_data_model.meaningful_interactions_and_on_site_visits_xf`
*   **FQN:** `prod.revenue_marts.meaningful_interactions_and_on_site_visits_xf`
*   **Description:** **High-Value Customer Engagement Activities Tracking**
This model provides a curated view of the most significant customer relationship activities by filtering  field visits to include only meaningful interactions and on-site visits. It serves as the primary data  source for analyzing relationship depth, engagement quality, and face-to-face interaction impact on  practice performance and retention.
**Filtering Logic:** - **Meaningful Interactions**: Only includes interactions with status 'Closed' or 'Completed' to ensure data quality - **On-Site Visits**: Includes all on-site visits regardless of status, recognizing their inherent value - Excludes incomplete or cancelled activities to focus on actual customer touchpoints
**Key Business Applications:** - Tracking relationship investment and engagement intensity with practices - Measuring face-to-face interaction impact on practice performance and retention - Supporting retention team performance analysis and resource allocation - Enabling correlation analysis between engagement activities and business outcomes - Providing data for internal referral attribution and Practice Development Manager effectiveness
**Data Sources:** - `field_visits`: Comprehensive field visit data from Salesforce tasks with enriched practice context - Enhanced with practice information, retention ownership, location data, and recent volume metrics - Built from Salesforce tasks with historical user assignment and practice relationship data
**Use Cases:** - Retention strategy optimization based on engagement effectiveness - Practice Development Manager visit planning and territory management - Customer success interaction tracking and relationship health assessment - Internal referral attribution for practices influenced by field activities - Relationship depth analysis for churn prediction and intervention prioritization
**Quality Considerations:** - Only includes completed meaningful interactions for data reliability - All on-site visits included due to their high-value nature regardless of formal completion status - Provides comprehensive context including practice financials and organizational details

*   **Tags:** `['revenue_analytics']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `TASK_ID` | 1 | `TEXT` | Unique identifier for each field visit or interaction task from Salesforce. Primary key for  tracking individual engagement activities and linking to detailed task information in source systems.
 | Unique identifier for each field visit or interaction task from Salesforce. Primary key for  tracking individual engagement activities and linking to detailed task information in source systems.
 | `[]` | `{}` |
    | `TASK_OWNER_DEPARTMENT` | 2 | `TEXT` | Department of the employee who conducted the visit or interaction (e.g., "Practice Development",  "Customer Success"). Used for departmental performance analysis and resource allocation planning  across different customer engagement functions.
 | Department of the employee who conducted the visit or interaction (e.g., "Practice Development",  "Customer Success"). Used for departmental performance analysis and resource allocation planning  across different customer engagement functions.
 | `[]` | `{}` |
    | `TASK_OWNER_TEAM` | 3 | `TEXT` | Specific team within the department responsible for the engagement activity. Enables team-level  performance tracking and workload distribution analysis for retention and development activities.
 | Specific team within the department responsible for the engagement activity. Enables team-level  performance tracking and workload distribution analysis for retention and development activities.
 | `[]` | `{}` |
    | `TASK_OWNER` | 4 | `TEXT` | Individual employee who conducted the visit or meaningful interaction. Critical for personal  accountability tracking, individual performance assessment, and relationship continuity management.
 | Individual employee who conducted the visit or meaningful interaction. Critical for personal  accountability tracking, individual performance assessment, and relationship continuity management.
 | `[]` | `{}` |
    | `SUBJECT` | 5 | `TEXT` | Brief description or title of the visit/interaction from the Salesforce task subject line.  Provides quick context about the purpose and nature of the engagement activity for reporting  and categorization purposes.
 | Brief description or title of the visit/interaction from the Salesforce task subject line.  Provides quick context about the purpose and nature of the engagement activity for reporting  and categorization purposes.
 | `[]` | `{}` |
    | `VISIT_DATE` | 6 | `DATE` | Date when the visit or meaningful interaction took place. Primary time dimension for analyzing  engagement frequency, timing effectiveness, and correlation with practice performance outcomes.
 | Date when the visit or meaningful interaction took place. Primary time dimension for analyzing  engagement frequency, timing effectiveness, and correlation with practice performance outcomes.
 | `[]` | `{}` |
    | `ACCOUNT_ID` | 7 | `TEXT` | Salesforce account identifier for the practice that was visited. Primary key for linking  engagement activities to practice records and enabling practice-level relationship analysis.
 | Salesforce account identifier for the practice that was visited. Primary key for linking  engagement activities to practice records and enabling practice-level relationship analysis.
 | `[]` | `{}` |
    | `ACCOUNT_NAME` | 8 | `TEXT` | Human-readable name of the practice account from Salesforce. Used for reporting and identification  purposes in dashboards and engagement activity summaries.
 | Human-readable name of the practice account from Salesforce. Used for reporting and identification  purposes in dashboards and engagement activity summaries.
 | `[]` | `{}` |
    | `LEAD_ID` | 9 | `TEXT` | Salesforce lead identifier if the interaction was with a prospective practice rather than  an existing account. May be null for interactions with established practices. Used for  lead conversion tracking and pre-go-live engagement analysis.
 | Salesforce lead identifier if the interaction was with a prospective practice rather than  an existing account. May be null for interactions with established practices. Used for  lead conversion tracking and pre-go-live engagement analysis.
 | `[]` | `{}` |
    | `LEAD_NAME` | 10 | `TEXT` | Name of the lead contact if the interaction involved a prospective practice. Provides context  for pre-conversion engagement activities and lead nurturing effectiveness analysis.
 | Name of the lead contact if the interaction involved a prospective practice. Provides context  for pre-conversion engagement activities and lead nurturing effectiveness analysis.
 | `[]` | `{}` |
    | `PRIMARY_MERCHANT_ID` | 11 | `FLOAT` | Primary merchant identifier for the practice in Cherry's system. Links engagement activities  to transaction data and enables analysis of interaction impact on practice volume and performance.
 | Primary merchant identifier for the practice in Cherry's system. Links engagement activities  to transaction data and enables analysis of interaction impact on practice volume and performance.
 | `[]` | `{}` |
    | `PRIMARY_ORGANIZATION_ID` | 12 | `NUMBER` | Primary organization identifier for grouping multiple merchant locations under a single  organizational entity. Enables organization-level engagement analysis and multi-location  practice relationship management.
 | Primary organization identifier for grouping multiple merchant locations under a single  organizational entity. Enables organization-level engagement analysis and multi-location  practice relationship management.
 | `[]` | `{}` |
    | `PRIMARY_ORGANIZATION_NAME` | 13 | `TEXT` | Name of the primary organization from Cherry's dashboard. Provides business context for  multi-location practices and enables organization-level relationship tracking and reporting.
 | Name of the primary organization from Cherry's dashboard. Provides business context for  multi-location practices and enables organization-level relationship tracking and reporting.
 | `[]` | `{}` |
    | `ADDRESS` | 14 | `TEXT` | Street address of the practice location that was visited. Critical for on-site visit  planning, territory management, and ensuring accurate location-based engagement tracking.
 | Street address of the practice location that was visited. Critical for on-site visit  planning, territory management, and ensuring accurate location-based engagement tracking.
 | `[]` | `{}` |
    | `CITY` | 15 | `TEXT` | City where the practice is located. Used for geographic analysis of engagement activities,  territory planning, and regional relationship management strategies.
 | City where the practice is located. Used for geographic analysis of engagement activities,  territory planning, and regional relationship management strategies.
 | `[]` | `{}` |
    | `STATE` | 16 | `TEXT` | State abbreviation for the practice location. Enables state-level analysis of engagement  effectiveness and regional performance tracking for field activities.
 | State abbreviation for the practice location. Enables state-level analysis of engagement  effectiveness and regional performance tracking for field activities.
 | `[]` | `{}` |
    | `ZIP` | 17 | `TEXT` | ZIP code of the practice location. Provides precise geographic data for territory optimization,  travel planning, and micro-geographic analysis of engagement patterns.
 | ZIP code of the practice location. Provides precise geographic data for territory optimization,  travel planning, and micro-geographic analysis of engagement patterns.
 | `[]` | `{}` |
    | `LAST_30_VOLUME` | 18 | `FLOAT` | Total gross loan volume generated by the practice in the 30 days prior to the visit.  Provides immediate performance context for evaluating engagement effectiveness and  correlation between visit activities and subsequent volume changes.
 | Total gross loan volume generated by the practice in the 30 days prior to the visit.  Provides immediate performance context for evaluating engagement effectiveness and  correlation between visit activities and subsequent volume changes.
 | `[]` | `{}` |
    | `PRIMARY_PURPOSE` | 19 | `TEXT` | Primary reason or objective for the visit as categorized in Salesforce (e.g., "Relationship Building",  "Training", "Demo"). Used for analyzing visit effectiveness by purpose type and optimizing  engagement strategies based on objective outcomes.
 | Primary reason or objective for the visit as categorized in Salesforce (e.g., "Relationship Building",  "Training", "Demo"). Used for analyzing visit effectiveness by purpose type and optimizing  engagement strategies based on objective outcomes.
 | `[]` | `{}` |
    | `TYPE` | 20 | `TEXT` | Type classification of the engagement activity ("Meaningful Interaction" or "On-Site Visit").  Critical dimension for analyzing different engagement modalities and their relative impact  on practice relationships and performance.
 | Type classification of the engagement activity ("Meaningful Interaction" or "On-Site Visit").  Critical dimension for analyzing different engagement modalities and their relative impact  on practice relationships and performance.
 | `[]` | `{}` |
    | `OUTCOME` | 21 | `TEXT` | Recorded outcome or result of the visit/interaction. Provides qualitative assessment of  engagement effectiveness and enables analysis of successful interaction patterns for  replication and strategy optimization.
 | Recorded outcome or result of the visit/interaction. Provides qualitative assessment of  engagement effectiveness and enables analysis of successful interaction patterns for  replication and strategy optimization.
 | `[]` | `{}` |
    | `DURATION` | 22 | `TEXT` | Length of time spent on the visit or interaction. Used for resource planning, cost analysis,  and understanding the relationship between engagement time investment and outcome effectiveness.
 | Length of time spent on the visit or interaction. Used for resource planning, cost analysis,  and understanding the relationship between engagement time investment and outcome effectiveness.
 | `[]` | `{}` |
    | `ESTIMATED_GIFT_EXPENSES` | 23 | `NUMBER` | Estimated cost of gifts or entertainment expenses associated with the visit. Used for  engagement cost tracking, budget planning, and ROI analysis of relationship-building investments.
 | Estimated cost of gifts or entertainment expenses associated with the visit. Used for  engagement cost tracking, budget planning, and ROI analysis of relationship-building investments.
 | `[]` | `{}` |
    | `NOTES` | 24 | `TEXT` | Detailed notes and observations from the visit or interaction. Provides qualitative context,  relationship insights, and actionable information for follow-up activities and relationship  management strategies.
 | Detailed notes and observations from the visit or interaction. Provides qualitative context,  relationship insights, and actionable information for follow-up activities and relationship  management strategies.
 | `[]` | `{}` |
    | `STATUS` | 25 | `TEXT` | Current status of the task/visit in Salesforce (e.g., "Closed", "Completed"). Used for  tracking task completion, ensuring data quality, and managing follow-up activities for  ongoing engagement initiatives. | Current status of the task/visit in Salesforce (e.g., "Closed", "Completed"). Used for  tracking task completion, ensuring data quality, and managing follow-up activities for  ongoing engagement initiatives. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.field_visits`

---
