## Model: `sf_user_info_xf`

`sf_user_info_xf`

*   **Unique ID:** `model.cherry_data_model.sf_user_info_xf`
*   **FQN:** `prod.salesforce_marts.sf_user_info_xf`
*   **Description:** **Salesforce User ROE (Rules of Engagement) Workload Tracking**
This model calculates the current workload for each Salesforce user by counting their assigned  leads and opportunities, serving as a critical component for Cherry's Rules of Engagement (ROE)  system that manages lead distribution and capacity limits. The model tracks active workloads to  ensure proper lead routing and prevents users from being assigned more leads/opportunities than  they can effectively manage.
**Key Business Logic:** - **Lead Filtering**: Only counts active leads (non-deleted, non-converted) to focus on current workload - **Opportunity Filtering**: Excludes opportunities in advanced/closed stages that no longer require 
  active sales management (Turned Live through Customer Success stages and Closed Lost)
- **Workload Aggregation**: Combines lead and opportunity counts to provide total active assignments 
  per user for capacity management
- **Watermark Tracking**: Captures most recent modification timestamp across all assigned records 
  for staleness detection and workload prioritization

**Primary Use Cases:** - ROE system capacity management and lead distribution decisions - Sales manager workload monitoring and team balancing - Automated lead routing based on current user capacity - Performance analytics and productivity tracking
**Grain:** One record per Salesforce user (owner_id) with active leads or opportunities

*   **Tags:** `['salesforce']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `OWNER_ID` | 1 | `TEXT` | **Salesforce User Identifier**
The unique Salesforce user ID who owns the leads and opportunities. This serves as the primary  key and links to Salesforce users table for additional user information (name, team, role, etc.).  Used by ROE system to identify capacity limits and routing rules for each user.
 | **Salesforce User Identifier**
The unique Salesforce user ID who owns the leads and opportunities. This serves as the primary  key and links to Salesforce users table for additional user information (name, team, role, etc.).  Used by ROE system to identify capacity limits and routing rules for each user.
 | `[]` | `{}` |
    | `LEAD_COUNT` | 2 | `NUMBER` | **Active Lead Count**
Total number of active leads currently assigned to this user, calculated from `src_sf_leads`  with filters for `is_deleted = false` and `is_converted = false`. Represents current prospecting  workload that requires active sales development efforts. Used by ROE system to determine if  user has capacity for additional lead assignments.
 | **Active Lead Count**
Total number of active leads currently assigned to this user, calculated from `src_sf_leads`  with filters for `is_deleted = false` and `is_converted = false`. Represents current prospecting  workload that requires active sales development efforts. Used by ROE system to determine if  user has capacity for additional lead assignments.
 | `[]` | `{}` |
    | `OPPORTUNITY_COUNT` | 3 | `NUMBER` | **Active Opportunity Count**
Total number of active opportunities currently assigned to this user, calculated from  `src_sf_opportunities` excluding deleted records and advanced/closed stages. Excludes  opportunities in stages: 'Turned Live, No Applications', 'Applications, No Approvals',  'Approvals, No Transactions', '1 Transaction/Activated', 'Sales Handoff Tasks',  'Handoff to Customer Success', 'Customer Success (holding)', and 'Closed Lost'.  Represents current sales pipeline requiring active management.
 | **Active Opportunity Count**
Total number of active opportunities currently assigned to this user, calculated from  `src_sf_opportunities` excluding deleted records and advanced/closed stages. Excludes  opportunities in stages: 'Turned Live, No Applications', 'Applications, No Approvals',  'Approvals, No Transactions', '1 Transaction/Activated', 'Sales Handoff Tasks',  'Handoff to Customer Success', 'Customer Success (holding)', and 'Closed Lost'.  Represents current sales pipeline requiring active management.
 | `[]` | `{}` |
    | `MAX_TIMESTAMP` | 4 | `TIMESTAMP_TZ` | **Most Recent Activity Watermark**
The most recent `last_modified_date` across all leads and opportunities assigned to this user,  providing a watermark for when their workload was last updated. Used for staleness detection,  priority scoring, and identifying accounts that may need immediate attention. Helps sales  managers identify users with aging assignments that require follow-up action. | **Most Recent Activity Watermark**
The most recent `last_modified_date` across all leads and opportunities assigned to this user,  providing a watermark for when their workload was last updated. Used for staleness detection,  priority scoring, and identifying accounts that may need immediate attention. Helps sales  managers identify users with aging assignments that require follow-up action. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.src_sf_leads`
    *   `model.cherry_data_model.src_sf_opportunities`

---
