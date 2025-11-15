## Model: `onboarding_implementation_details`

`onboarding_implementation_details`

*   **Unique ID:** `model.cherry_data_model.onboarding_implementation_details`
*   **FQN:** `prod.revenue_marts.onboarding_implementation_details`
*   **Description:** **Onboarding Implementation Success Tracking**
This model provides granular tracking of onboarding implementation success by monitoring whether various  digital marketing and operational tools were successfully implemented within the critical first 30 days  after practice go-live. It transforms wide implementation data into a long format to enable comprehensive  analysis of onboarding effectiveness across different implementation types and practice characteristics.
**Key Business Logic:** - **30-Day Implementation Window**: Creates binary success flags (1/0) for implementations completed within 30 days of go-live - **Comprehensive Coverage**: Tracks 14 different implementation types from digital marketing to operational tools - **Long Format Transformation**: Unpivots implementation data to create one row per practice per implementation type - **Implementation Classification**: Standardizes implementation type names for consistent reporting and analysis
**Implementation Types Tracked:** - **Digital Marketing**: Website, Google Business Profile, Yelp, Facebook, Instagram, TikTok - **Operational Tools**: Appointment Reminders, Intake Forms, Billing Notifications - **E-commerce**: E-Shop, Membership programs - **System Integration**: Integration completion, Custom pricing sheets, Custom marketing
**Critical Business Metrics:** - Implementation success rate within the optimal 30-day onboarding window - Onboarding specialist effectiveness across different implementation types - Industry segment variations in implementation success patterns - Correlation between implementation completeness and early practice performance
**Data Sources:** - `practice_info_full_xf`: Comprehensive practice data including all implementation dates and practice context - Implementation dates sourced from various onboarding tracking systems and manual processes - Practice performance metrics for correlation analysis with implementation success
**Use Cases:** - Onboarding process optimization and bottleneck identification - Onboarding specialist performance evaluation and training needs assessment - Industry-specific implementation strategy development - Early performance prediction based on implementation completeness - Resource allocation for onboarding support based on implementation difficulty
**Reporting Applications:** - Implementation success dashboards by specialist and practice type - Onboarding completion rate trending and goal tracking - Practice early performance correlation with implementation thoroughness - Specialist workload analysis and capacity planning for onboarding activities

*   **Tags:** `['revenue_analytics']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `SF_ACCOUNT_ID` | 1 | `TEXT` | Salesforce account identifier for the practice. Primary key for linking implementation success  data to practice records and enabling comprehensive onboarding performance analysis across  practice characteristics and outcomes.
 | Salesforce account identifier for the practice. Primary key for linking implementation success  data to practice records and enabling comprehensive onboarding performance analysis across  practice characteristics and outcomes.
 | `[]` | `{}` |
    | `IMPLEMENTATION_TYPE` | 2 | `TEXT` | Human-readable name of the specific implementation activity being tracked (e.g., "Website Implementation",  "Google Business Profile Implementation", "Appointment Reminder Implementation"). Standardized naming  convention for consistent reporting and analysis across all onboarding implementation types.
 | Human-readable name of the specific implementation activity being tracked (e.g., "Website Implementation",  "Google Business Profile Implementation", "Appointment Reminder Implementation"). Standardized naming  convention for consistent reporting and analysis across all onboarding implementation types.
 | `[]` | `{}` |
    | `IMPLEMENTATION` | 3 | `NUMBER` | Binary flag (1/0) indicating whether the specific implementation type was successfully completed  within 30 days of practice go-live. Value of 1 indicates successful timely implementation,  0 indicates either no implementation or implementation beyond the optimal 30-day window.
 | Binary flag (1/0) indicating whether the specific implementation type was successfully completed  within 30 days of practice go-live. Value of 1 indicates successful timely implementation,  0 indicates either no implementation or implementation beyond the optimal 30-day window.
 | `[]` | `{}` |
    | `PRACTICE_GO_LIVE_DATE` | 4 | `DATE` | Date when the practice officially went live and began operations with Cherry. Serves as the  baseline date for calculating the 30-day implementation window and measuring onboarding  timeline effectiveness.
 | Date when the practice officially went live and began operations with Cherry. Serves as the  baseline date for calculating the 30-day implementation window and measuring onboarding  timeline effectiveness.
 | `[]` | `{}` |
    | `ACCOUNT_INDUSTRY_SEGMENT` | 5 | `TEXT` | Industry segment classification of the practice (e.g., "Dental", "Veterinary", "Plastic and Cosmetic Surgery",  "MedSpa"). Used for industry-specific analysis of implementation success patterns  and customizing onboarding strategies based on practice type requirements.
 | Industry segment classification of the practice (e.g., "Dental", "Veterinary", "Plastic and Cosmetic Surgery",  "MedSpa"). Used for industry-specific analysis of implementation success patterns  and customizing onboarding strategies based on practice type requirements.
 | `[]` | `{}` |
    | `ALLE_PRACTICE_TYPE` | 6 | `TEXT` | Specific practice type classification for Alle platform practices. Provides additional  segmentation for practices using the Alle platform, enabling specialized onboarding  analysis for this distinct practice category.
 | Specific practice type classification for Alle platform practices. Provides additional  segmentation for practices using the Alle platform, enabling specialized onboarding  analysis for this distinct practice category.
 | `[]` | `{}` |
    | `ONBOARDING_SPECIALIST_DEPARTMENT` | 7 | `TEXT` | Department of the onboarding specialist responsible for guiding the practice through implementation  (e.g., "Onboarding", "Customer Success"). Used for departmental performance analysis and  resource allocation planning across organizational onboarding functions.
 | Department of the onboarding specialist responsible for guiding the practice through implementation  (e.g., "Onboarding", "Customer Success"). Used for departmental performance analysis and  resource allocation planning across organizational onboarding functions.
 | `[]` | `{}` |
    | `ONBOARDING_SPECIALIST_TEAM` | 8 | `TEXT` | Specific team within the onboarding department responsible for the practice's implementation  process. Enables team-level performance tracking and workload distribution analysis for  onboarding effectiveness optimization.
 | Specific team within the onboarding department responsible for the practice's implementation  process. Enables team-level performance tracking and workload distribution analysis for  onboarding effectiveness optimization.
 | `[]` | `{}` |
    | `ONBOARDING_SPECIALIST` | 9 | `TEXT` | Individual onboarding specialist assigned to guide the practice through the implementation  process. Critical for personal accountability tracking, individual performance assessment,  and relationship continuity management during onboarding.
 | Individual onboarding specialist assigned to guide the practice through the implementation  process. Critical for personal accountability tracking, individual performance assessment,  and relationship continuity management during onboarding.
 | `[]` | `{}` |
    | `ONBOARDING_SPECIALIST_TITLE` | 10 | `TEXT` | Job title or role of the onboarding specialist responsible for the practice. Provides  context for specialist level and expertise, enabling analysis of implementation success  rates by specialist seniority and role type.
 | Job title or role of the onboarding specialist responsible for the practice. Provides  context for specialist level and expertise, enabling analysis of implementation success  rates by specialist seniority and role type.
 | `[]` | `{}` |
    | `PRACTICE_ACTIVATION_DATE` | 11 | `DATE` | Date of the practice's first funded contract, marking the beginning of active transaction  processing. Key milestone for measuring time-to-activation and correlating implementation  completeness with speed to first transaction success.
 | Date of the practice's first funded contract, marking the beginning of active transaction  processing. Key milestone for measuring time-to-activation and correlating implementation  completeness with speed to first transaction success.
 | `[]` | `{}` |
    | `PRACTICE_FIRST_30_GROSS_AMOUNT` | 12 | `FLOAT` | Total gross loan volume generated by the practice in the first 30 days after go-live.  Critical metric for correlating implementation completeness with early practice performance  and identifying the business impact of successful onboarding.
 | Total gross loan volume generated by the practice in the first 30 days after go-live.  Critical metric for correlating implementation completeness with early practice performance  and identifying the business impact of successful onboarding.
 | `[]` | `{}` |
    | `PRACTICE_FIRST_60_GROSS_AMOUNT` | 13 | `FLOAT` | Total gross loan volume generated by the practice in the first 60 days after go-live.  Extended performance indicator for measuring the sustained impact of implementation quality  on practice success and long-term relationship development. | Total gross loan volume generated by the practice in the first 60 days after go-live.  Extended performance indicator for measuring the sustained impact of implementation quality  on practice success and long-term relationship development. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.practice_info_full_xf`

---
