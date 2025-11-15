## Model: `support_and_collections_agent_statuses_xf`

`support_and_collections_agent_statuses_xf`

*   **Unique ID:** `model.cherry_data_model.support_and_collections_agent_statuses_xf`
*   **FQN:** `prod.servicing_marts.support_and_collections_agent_statuses_xf`
*   **Description:** **Comprehensive Agent Status and Occupancy Analytics (Servicing & Collections)**
This model combines agent status data from multiple sources to provide a unified view of agent  availability, productivity, and workload. It serves as the single source of truth for workforce  management, capacity planning, and agent performance analytics across Cherry's support and  collections operations.
**Key Business Logic:** - **Multi-Source Integration**: Merges Zendesk schedules (governing base), TCN agent statuses, 
  and real-time occupancy calculations from tickets and dials
- **Weighted Sustainability Scoring**: Implements complex scoring based on concurrent calls, 
  chats, and SMS to identify agent burnout risk and optimize workload distribution
- **On-Queue Classification**: Standardizes agent availability across systems with TCN states 
  (paused/preparingAfterPause = Off Queue, all others = On Queue)

**Critical Data Sources:** - `stg_zendesk_schedules_and_on_queue_statuses`: Governing schedule data for all agents - `stg_tcn_agent_statuses`: Real-time TCN dialer agent status transitions - `zendesk_collections_team_tickets_xf`: Collections ticket activity - `zendesk_support_team_tickets_xf`: Support ticket activity - `stg_tcn_dials`: Outbound dial activity for occupancy calculation - `nice_collections_contacts_xf_archive`: NICE collections interactions, deprecated May 2025
**Primary Use Cases:** - Real-time agent capacity and availability monitoring - Workforce optimization and scheduling efficiency analysis - Agent productivity and utilization reporting - Workload sustainability and burnout prevention - Cross-platform contact center performance tracking
**Grain:** One record per agent per minute during business hours (9am-9pm ET, reduced hours weekends)

*   **Tags:** `['servicing_and_collections', 'servicing_marts', 'agent_data']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `AGENT_NAME` | 1 | `TEXT` | **Agent Name**
Full name of the agent. Primary key component. Standardized across all systems with  Michael Conner → Michael Conner II mapping applied. Sourced from Zendesk schedules as base.
 | **Agent Name**
Full name of the agent. Primary key component. Standardized across all systems with  Michael Conner → Michael Conner II mapping applied. Sourced from Zendesk schedules as base.
 | `[]` | `{}` |
    | `TIMESTAMP_MINUTE` | 2 | `TIMESTAMP_NTZ` | **Activity Timestamp (Minute Granularity)**
Timestamp of the agent activity rounded to the minute. Primary key component.  Used for minute-level capacity and occupancy analysis. In PT timezone.
 | **Activity Timestamp (Minute Granularity)**
Timestamp of the agent activity rounded to the minute. Primary key component.  Used for minute-level capacity and occupancy analysis. In PT timezone.
 | `[]` | `{}` |
    | `WORK_DATE` | 3 | `DATE` | **Work Date**
Date of the agent activity. Used for daily aggregations and reporting.  Derived from timestamp_minute.
 | **Work Date**
Date of the agent activity. Used for daily aggregations and reporting.  Derived from timestamp_minute.
 | `[]` | `{}` |
    | `TEAM` | 4 | `TEXT` | **Team Assignment**
Team the agent belongs to (Support, Collections, or Unknown). Sourced from  ops_user_teams with date-based validity. Drives team-level performance metrics.
 | **Team Assignment**
Team the agent belongs to (Support, Collections, or Unknown). Sourced from  ops_user_teams with date-based validity. Drives team-level performance metrics.
 | `[]` | `{}` |
    | `TCN_STATE` | 5 | `TEXT` | **TCN Agent State**
Current state from TCN dialer system. Includes: ready, idle, paused, peered, wrapup,  preparingafterpause, preparingafteridle, preparingafterwrapup, transfer states, dial states.  NULL when agent not logged into TCN.
 | **TCN Agent State**
Current state from TCN dialer system. Includes: ready, idle, paused, peered, wrapup,  preparingafterpause, preparingafteridle, preparingafterwrapup, transfer states, dial states.  NULL when agent not logged into TCN.
 | `[]` | `{}` |
    | `TCN_ON_QUEUE_STATUS` | 6 | `TEXT` | **TCN Queue Status**
Binary classification of TCN state. 'On Queue' for all states except paused and  preparingAfterPause. 'Off Queue' for paused and preparingAfterPause. NULL when not in TCN.
 | **TCN Queue Status**
Binary classification of TCN state. 'On Queue' for all states except paused and  preparingAfterPause. 'Off Queue' for paused and preparingAfterPause. NULL when not in TCN.
 | `[]` | `{}` |
    | `TCN_ACTIVITY_CATEGORY` | 7 | `TEXT` | **TCN Activity Category**
Categorization of TCN state into business activities. Categories include: Call Handling,  Available, Idle Time, Break/Paused, Transfer, Manual Dial, Other. Used for productivity analysis.
 | **TCN Activity Category**
Categorization of TCN state into business activities. Categories include: Call Handling,  Available, Idle Time, Break/Paused, Transfer, Manual Dial, Other. Used for productivity analysis.
 | `[]` | `{}` |
    | `TCN_IS_PRODUCTIVE` | 8 | `BOOLEAN` | Boolean flag indicating productive time in TCN. When TRUE, agent is in On Queue status.  When FALSE, agent is Off Queue. Used for TCN-specific utilization calculations.
 | Boolean flag indicating productive time in TCN. When TRUE, agent is in On Queue status.  When FALSE, agent is Off Queue. Used for TCN-specific utilization calculations.
 | `[]` | `{}` |
    | `TCN_CALL_ID` | 9 | `TEXT` | **TCN Call Identifier**
Unique identifier for active TCN call. Links to dial records. NULL when agent not on call.
 | **TCN Call Identifier**
Unique identifier for active TCN call. Links to dial records. NULL when agent not on call.
 | `[]` | `{}` |
    | `ZENDESK_STATUS` | 10 | `TEXT` | **Zendesk Agent Status**
Current status from Zendesk system. Includes: Available, Unavailable (with reason),  Away, Offline, Unified online. Represents actual agent state in Zendesk.
 | **Zendesk Agent Status**
Current status from Zendesk system. Includes: Available, Unavailable (with reason),  Away, Offline, Unified online. Represents actual agent state in Zendesk.
 | `[]` | `{}` |
    | `ZENDESK_ON_QUEUE_STATUS` | 11 | `TEXT` | **Zendesk Actual Queue Status**
Actual on-queue status in Zendesk based on agent activity. 'On Queue' when available  and working. 'Off Queue' when unavailable or away.
 | **Zendesk Actual Queue Status**
Actual on-queue status in Zendesk based on agent activity. 'On Queue' when available  and working. 'Off Queue' when unavailable or away.
 | `[]` | `{}` |
    | `ZENDESK_SCHEDULED_STATUS` | 12 | `TEXT` | **Zendesk Scheduled Queue Status**
Scheduled on-queue status from workforce management. 'On Queue' when scheduled to work.  'Off Queue' when scheduled for breaks or offline. Used for adherence calculations.
 | **Zendesk Scheduled Queue Status**
Scheduled on-queue status from workforce management. 'On Queue' when scheduled to work.  'Off Queue' when scheduled for breaks or offline. Used for adherence calculations.
 | `[]` | `{}` |
    | `QUEUE_ALIGNMENT_STATUS` | 13 | `TEXT` | **Schedule Adherence Status**
Comparison between actual and scheduled status. Values: 'Aligned On Queue', 'Aligned Off Queue',  'Actual On Queue, Scheduled Off Queue', 'Actual Off Queue, Scheduled On Queue'.  Critical for workforce management.
 | **Schedule Adherence Status**
Comparison between actual and scheduled status. Values: 'Aligned On Queue', 'Aligned Off Queue',  'Actual On Queue, Scheduled Off Queue', 'Actual Off Queue, Scheduled On Queue'.  Critical for workforce management.
 | `[]` | `{}` |
    | `SCHEDULED_TASK` | 14 | `TEXT` | **Scheduled Task**
Workforce management scheduled activity. Includes: On Queue, Break, Lunch, Meeting,  Training, Offline. Sourced from Zendesk WFM schedules.
 | **Scheduled Task**
Workforce management scheduled activity. Includes: On Queue, Break, Lunch, Meeting,  Training, Offline. Sourced from Zendesk WFM schedules.
 | `[]` | `{}` |
    | `COMBINED_ON_QUEUE_STATUS` | 15 | `TEXT` | **Combined Queue Status**
Unified on-queue status across all systems. Takes TCN status if available, otherwise  Zendesk status. Primary field for cross-platform availability analysis.
 | **Combined Queue Status**
Unified on-queue status across all systems. Takes TCN status if available, otherwise  Zendesk status. Primary field for cross-platform availability analysis.
 | `[]` | `{}` |
    | `DATA_SOURCE` | 16 | `TEXT` | **Data Source Indicator**
Indicates which systems have data for this agent-minute. 'Both' when TCN and Zendesk data present. 'TCN Only' when only TCN data. 'Zendesk Only' when only Zendesk data. 'Unknown' when source unclear. Used for data completeness analysis.
 | **Data Source Indicator**
Indicates which systems have data for this agent-minute. 'Both' when TCN and Zendesk data present. 'TCN Only' when only TCN data. 'Zendesk Only' when only Zendesk data. 'Unknown' when source unclear. Used for data completeness analysis.
 | `[]` | `{}` |
    | `ACTIVE_CALLS` | 17 | `NUMBER` | **Active Call Count**
Number of active voice calls at this minute. Includes Zendesk voice, TCN dials,  and NICE calls. Used for voice channel utilization. Count of unique tickets.
 | **Active Call Count**
Number of active voice calls at this minute. Includes Zendesk voice, TCN dials,  and NICE calls. Used for voice channel utilization. Count of unique tickets.
 | `[]` | `{}` |
    | `ACTIVE_CHATS` | 18 | `NUMBER` | **Active Chat Count**
Number of active chat conversations at this minute. Sourced from Zendesk tickets  with media_type='Chat'. Used for digital channel utilization. Count of unique tickets.
 | **Active Chat Count**
Number of active chat conversations at this minute. Sourced from Zendesk tickets  with media_type='Chat'. Used for digital channel utilization. Count of unique tickets.
 | `[]` | `{}` |
    | `ACTIVE_SMS` | 19 | `NUMBER` | **Active SMS Count**
Number of active SMS conversations at this minute. Sourced from Zendesk tickets  with media_type='SMS'. Used for asynchronous channel utilization. Count of unique tickets.
 | **Active SMS Count**
Number of active SMS conversations at this minute. Sourced from Zendesk tickets  with media_type='SMS'. Used for asynchronous channel utilization. Count of unique tickets.
 | `[]` | `{}` |
    | `TOTAL_ACTIVE_CONTACTS` | 20 | `NUMBER` | **Total Active Contacts**
Sum of all active contacts across channels (calls + chats + SMS). Primary metric  for agent occupancy. Used for capacity planning. Count of unique tickets.
 | **Total Active Contacts**
Sum of all active contacts across channels (calls + chats + SMS). Primary metric  for agent occupancy. Used for capacity planning. Count of unique tickets.
 | `[]` | `{}` |
    | `WEIGHTED_SUSTAINABILITY_SCORE` | 21 | `NUMBER` | **Weighted Sustainability Score**
Score from 0-2 indicating workload sustainability. 0=Inactive, 0.5=Low sustainable load,  1.0=Medium sustainable load, 2.0=High risk of burnout. Based on concurrent channel mix. In points.
 | **Weighted Sustainability Score**
Score from 0-2 indicating workload sustainability. 0=Inactive, 0.5=Low sustainable load,  1.0=Medium sustainable load, 2.0=High risk of burnout. Based on concurrent channel mix. In points.
 | `[]` | `{}` |
    | `OCCUPANCY_CATEGORY` | 22 | `TEXT` | **Occupancy Category**
Simplified categorization of agent workload. Categories: Inactive (no contacts),  Low, Medium, High. Drives real-time monitoring dashboards.
 | **Occupancy Category**
Simplified categorization of agent workload. Categories: Inactive (no contacts),  Low, Medium, High. Drives real-time monitoring dashboards.
 | `[]` | `{}` |
    | `IS_PRODUCTIVE_MINUTE` | 23 | `NUMBER` | Flag indicating productive time. When TRUE, agent is On Queue AND actively handling contacts.  When FALSE, agent is either Off Queue or On Queue but idle. Used for true productivity calculations.
 | Flag indicating productive time. When TRUE, agent is On Queue AND actively handling contacts.  When FALSE, agent is either Off Queue or On Queue but idle. Used for true productivity calculations.
 | `[]` | `{}` |
    | `IS_AVAILABLE_MINUTE` | 24 | `NUMBER` | Flag indicating availability. When TRUE, agent is On Queue regardless of contact activity.  When FALSE, agent is Off Queue. Used for availability and utilization metrics.
 | Flag indicating availability. When TRUE, agent is On Queue regardless of contact activity.  When FALSE, agent is Off Queue. Used for availability and utilization metrics.
 | `[]` | `{}` |
    | `UPDATED_AT` | 25 | `TIMESTAMP_LTZ` | **Model Refresh Timestamp**
Timestamp when this record was last updated. Used for data freshness monitoring  and incremental processing. In UTC timezone.
 | **Model Refresh Timestamp**
Timestamp when this record was last updated. Used for data freshness monitoring  and incremental processing. In UTC timezone.
 | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.nice_collections_contacts_xf_archive`
    *   `model.cherry_data_model.stg_nice_contacts`
    *   `model.cherry_data_model.stg_tcn_agent_statuses`
    *   `model.cherry_data_model.stg_tcn_dials`
    *   `model.cherry_data_model.stg_zendesk_schedules_and_on_queue_statuses`
    *   `model.cherry_data_model.zendesk_collections_team_tickets_xf`
    *   `model.cherry_data_model.zendesk_support_team_tickets_xf`

---
