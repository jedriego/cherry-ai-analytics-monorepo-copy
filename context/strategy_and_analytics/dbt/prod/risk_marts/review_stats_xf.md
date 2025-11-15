## Model: `review_stats_xf`

`review_stats_xf`

*   **Unique ID:** `model.cherry_data_model.review_stats_xf`
*   **FQN:** `prod.risk_marts.review_stats_xf`
*   **Description:** **Merchant Review Performance Analytics**
This comprehensive model provides detailed statistics and performance metrics for merchants currently  undergoing review processes as part of Cherry's risk management and recovery program. It combines  merchant profile data, health assessments, transaction volumes, credit score analysis, and competitive  positioning to create a 360-degree view of merchant performance during review periods.
**Key Business Logic:** - **Review Context**: Focuses exclusively on merchants with active review periods from the reviews model - **Multi-Faceted Analysis**: Combines financial performance, health scores, competitive analysis, 
  and borrower risk profiles for comprehensive merchant assessment
- **Risk Segmentation**: Categorizes loans as Prime vs Subprime based on risk scores and pricing menu tiers - **Competitive Intelligence**: Includes estimated CareCredit volumes and Cherry market share calculations - **Dashboard Integration**: Provides direct links to operational dashboards and Salesforce records
**Data Sources:** - **reviews**: Active review periods and decisions for merchants under review - **merchant_health_score_daily**: Partnership health scores, web review scores, and risk assessments - **practice_info_xf**: Comprehensive merchant and practice information - **transactions_historical**: Historical transaction volume data across multiple time periods - **mystery_shopping_valids**: Look position assessments and mystery shopping evaluations - **applications_loans_xf**: Application and loan data for credit score analysis
**Primary Use Cases:** - Risk management and merchant recovery program analytics - Performance benchmarking during review periods - Competitive analysis and market share assessment - Credit quality analysis and subprime exposure evaluation - Recovery strategy development and intervention planning
**Grain:** One record per merchant under review (filtered by active review periods)

*   **Tags:** `['risk']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `PRIMARY_ORGANIZATION_ID` | 1 | `NUMBER` | Organization identifier for the primary organization associated with the merchant, enabling  organization-level analysis and health score tracking across multiple merchant locations.
 | Organization identifier for the primary organization associated with the merchant, enabling  organization-level analysis and health score tracking across multiple merchant locations.
 | `[]` | `{}` |
    | `SF_ACCOUNT_ID` | 2 | `TEXT` | Salesforce account identifier linking merchants to CRM data, customer interactions,  and sales process tracking. Used for operational workflow integration.
 | Salesforce account identifier linking merchants to CRM data, customer interactions,  and sales process tracking. Used for operational workflow integration.
 | `[]` | `{}` |
    | `SF_ACCOUNT_NAME` | 3 | `TEXT` | Salesforce account name providing the business name for reporting, communication,  and identification purposes in review management processes.
 | Salesforce account name providing the business name for reporting, communication,  and identification purposes in review management processes.
 | `[]` | `{}` |
    | `PRIMARY_MERCHANT_ID` | 4 | `FLOAT` | Cherry's primary merchant identifier representing the main merchant location for the account,  used for consolidating multi-location merchant data and primary relationship management.
 | Cherry's primary merchant identifier representing the main merchant location for the account,  used for consolidating multi-location merchant data and primary relationship management.
 | `[]` | `{}` |
    | `ACCOUNT_INDUSTRY_SEGMENT` | 5 | `TEXT` | Industry segment classification (e.g., 'MedSpa', 'Dental', 'Veterinary')  used for industry-specific risk assessment, recovery strategies, and benchmarking.
 | Industry segment classification (e.g., 'MedSpa', 'Dental', 'Veterinary')  used for industry-specific risk assessment, recovery strategies, and benchmarking.
 | `[]` | `{}` |
    | `POC_FULL_NAME` | 6 | `TEXT` | Full name of the merchant's primary point of contact, used for relationship management  and communication during review and recovery processes.
 | Full name of the merchant's primary point of contact, used for relationship management  and communication during review and recovery processes.
 | `[]` | `{}` |
    | `POC_EMAIL` | 7 | `TEXT` | Primary contact email address for merchant communication during review periods,  recovery interventions, and ongoing relationship management.
 | Primary contact email address for merchant communication during review periods,  recovery interventions, and ongoing relationship management.
 | `[]` | `{}` |
    | `POC_PHONE` | 8 | `TEXT` | Primary contact phone number for direct merchant communication during review processes  and urgent intervention scenarios.
 | Primary contact phone number for direct merchant communication during review processes  and urgent intervention scenarios.
 | `[]` | `{}` |
    | `ADDRESS_LINE_ONE` | 9 | `TEXT` | Primary street address of the merchant location, used for geographic analysis,  territory assignment, and location-based risk assessment.
 | Primary street address of the merchant location, used for geographic analysis,  territory assignment, and location-based risk assessment.
 | `[]` | `{}` |
    | `CITY_NAME` | 10 | `TEXT` | City name of the merchant location, used for geographic clustering, territory management,  and regional performance analysis.
 | City name of the merchant location, used for geographic clustering, territory management,  and regional performance analysis.
 | `[]` | `{}` |
    | `STATE_ABBREVIATION` | 11 | `TEXT` | State abbreviation of the merchant location, critical for regulatory compliance,  territorial analysis, and state-specific recovery strategies.
 | State abbreviation of the merchant location, critical for regulatory compliance,  territorial analysis, and state-specific recovery strategies.
 | `[]` | `{}` |
    | `ZIPCODE` | 12 | `TEXT` | ZIP code of the merchant location, used for demographic analysis, geographic  clustering, and regional market assessment.
 | ZIP code of the merchant location, used for demographic analysis, geographic  clustering, and regional market assessment.
 | `[]` | `{}` |
    | `PHONE` | 13 | `TEXT` | Merchant business phone number, used for customer contact verification and  business presence validation during review processes.
 | Merchant business phone number, used for customer contact verification and  business presence validation during review processes.
 | `[]` | `{}` |
    | `LOOK_POSITION` | 14 | `TEXT` | Assessment of the merchant's "look" position indicating where Cherry appears in  customer financing options. Derived from latest health assessment or mystery shopping,  critical for competitive positioning analysis.
 | Assessment of the merchant's "look" position indicating where Cherry appears in  customer financing options. Derived from latest health assessment or mystery shopping,  critical for competitive positioning analysis.
 | `[]` | `{}` |
    | `POLICY_TYPE` | 15 | `TEXT` | Pricing policy classification indicating 'Very Competitive Menu' or 'Medium Competitive Menu'  based on pricing menu configuration, affecting approval rates and recovery strategies.
 | Pricing policy classification indicating 'Very Competitive Menu' or 'Medium Competitive Menu'  based on pricing menu configuration, affecting approval rates and recovery strategies.
 | `[]` | `{}` |
    | `ESTIMATED_COMPETITOR_MONTHLY_VOLUME` | 16 | `NUMBER` | Estimated monthly CareCredit transaction volume for competitive analysis, derived from  market sizing data to assess total addressable financing market for the merchant.
 | Estimated monthly CareCredit transaction volume for competitive analysis, derived from  market sizing data to assess total addressable financing market for the merchant.
 | `[]` | `{}` |
    | `CHERRY_MONTHLY_VOLUME` | 17 | `FLOAT` | Cherry's monthly transaction volume (last 30 days), providing current performance  baseline for market share calculations and recovery target setting.
 | Cherry's monthly transaction volume (last 30 days), providing current performance  baseline for market share calculations and recovery target setting.
 | `[]` | `{}` |
    | `ESTIMATED_MONTHLY_FINANCING_VOLUME` | 18 | `FLOAT` | Total estimated monthly financing volume combining Cherry and competitor volumes,  representing the merchant's total addressable financing market size.
 | Total estimated monthly financing volume combining Cherry and competitor volumes,  representing the merchant's total addressable financing market size.
 | `[]` | `{}` |
    | `CHERRY_SHARE` | 19 | `FLOAT` | Cherry's market share percentage calculated as Cherry volume divided by total estimated  financing volume, key metric for competitive positioning and growth potential assessment.
 | Cherry's market share percentage calculated as Cherry volume divided by total estimated  financing volume, key metric for competitive positioning and growth potential assessment.
 | `[]` | `{}` |
    | `RETENTION_OWNER` | 20 | `TEXT` | Name of the retention team member responsible for the merchant relationship,  used for accountability, communication routing, and recovery process management.
 | Name of the retention team member responsible for the merchant relationship,  used for accountability, communication routing, and recovery process management.
 | `[]` | `{}` |
    | `LAST_TRANSACTION_DATE` | 21 | `TIMESTAMP_NTZ` | Date of the merchant's most recent funded transaction, critical for assessing  current activity levels and identifying dormant or declining merchants.
 | Date of the merchant's most recent funded transaction, critical for assessing  current activity levels and identifying dormant or declining merchants.
 | `[]` | `{}` |
    | `PRIME_TRANSACTION_VOLUME` | 22 | `FLOAT` | Total transaction volume from prime borrowers (higher credit scores), used for  credit quality analysis and portfolio composition assessment.
 | Total transaction volume from prime borrowers (higher credit scores), used for  credit quality analysis and portfolio composition assessment.
 | `[]` | `{}` |
    | `SUBPRIME_TRANSACTION_VOLUME` | 23 | `FLOAT` | Total transaction volume from subprime borrowers (lower credit scores), indicating  merchant exposure to higher-risk lending and potential fee sensitivity.
 | Total transaction volume from subprime borrowers (lower credit scores), indicating  merchant exposure to higher-risk lending and potential fee sensitivity.
 | `[]` | `{}` |
    | `PRIME_LOAN_COUNT` | 24 | `NUMBER` | Number of loans from prime borrowers, used for calculating prime borrower mix  and credit quality metrics during review assessment.
 | Number of loans from prime borrowers, used for calculating prime borrower mix  and credit quality metrics during review assessment.
 | `[]` | `{}` |
    | `SUBPRIME_LOAN_COUNT` | 25 | `NUMBER` | Number of loans from subprime borrowers, used for calculating subprime exposure  ratios and assessing merchant tolerance for higher-risk lending.
 | Number of loans from subprime borrowers, used for calculating subprime exposure  ratios and assessing merchant tolerance for higher-risk lending.
 | `[]` | `{}` |
    | `PRIME_MERCHANT_FEE_PERCENTAGE` | 26 | `FLOAT` | Merchant fee percentage for prime borrower transactions, representing the fee rate  charged to merchants for higher credit quality lending.
 | Merchant fee percentage for prime borrower transactions, representing the fee rate  charged to merchants for higher credit quality lending.
 | `[]` | `{}` |
    | `SUBPRIME_MERCHANT_FEE_PERCENTAGE` | 27 | `FLOAT` | Merchant fee percentage for subprime borrower transactions, typically higher due  to increased risk, important for fee sensitivity analysis during reviews.
 | Merchant fee percentage for subprime borrower transactions, typically higher due  to increased risk, important for fee sensitivity analysis during reviews.
 | `[]` | `{}` |
    | `TOTAL_TRANSACTION_VOLUME` | 28 | `FLOAT` | Combined transaction volume across all borrower risk categories, providing total  merchant business volume for performance assessment and recovery target setting.
 | Combined transaction volume across all borrower risk categories, providing total  merchant business volume for performance assessment and recovery target setting.
 | `[]` | `{}` |
    | `BLENDED_MERCHANT_FEE_PERCENTAGE` | 29 | `FLOAT` | Weighted average merchant fee percentage across prime and subprime transactions,  representing the effective fee rate and profitability metric for the merchant relationship.
 | Weighted average merchant fee percentage across prime and subprime transactions,  representing the effective fee rate and profitability metric for the merchant relationship.
 | `[]` | `{}` |
    | `Practice's Average Credit Score` | 30 | `FLOAT` |  |  | `[]` | `{}` |
    | `Similar Practices Average Credit Score` | 31 | `FLOAT` |  |  | `[]` | `{}` |
    | `National Average Credit Score` | 32 | `NUMBER` |  |  | `[]` | `{}` |
    | `MAX_PROMO` | 33 | `NUMBER` | Maximum promotional term length (months) enabled for the merchant's organization,  indicating the longest 0% APR period offered to borrowers.
 | Maximum promotional term length (months) enabled for the merchant's organization,  indicating the longest 0% APR period offered to borrowers.
 | `[]` | `{}` |
    | `HEALTH_SCORE` | 34 | `FLOAT` | Current partnership health score from the daily health score model, primary metric  for assessing merchant relationship strength and performance trends.
 | Current partnership health score from the daily health score model, primary metric  for assessing merchant relationship strength and performance trends.
 | `[]` | `{}` |
    | `WEB_REVIEW_SCORE` | 35 | `NUMBER` | Score reflecting Cherry's positioning and prominence on the merchant's website,  critical factor in health assessments and recovery recommendations.
 | Score reflecting Cherry's positioning and prominence on the merchant's website,  critical factor in health assessments and recovery recommendations.
 | `[]` | `{}` |
    | `ORGANIZATION_WEBSITE` | 36 | `TEXT` | Merchant organization's website URL, used for web presence analysis and  positioning assessment during mystery shopping and health evaluations.
 | Merchant organization's website URL, used for web presence analysis and  positioning assessment during mystery shopping and health evaluations.
 | `[]` | `{}` |
    | `Heads Up Display` | 37 | `TEXT` |  |  | `[]` | `{}` |
    | `Salesforce Account` | 38 | `TEXT` |  |  | `[]` | `{}` |
    | `MedSpa Health Dashboard` | 39 | `TEXT` |  |  | `[]` | `{}` |
    | `APPLICATIONS_LAST_4_MONTHS` | 40 | `NUMBER` | Total number of applications submitted in the last 4 months, indicating recent  application activity levels and merchant engagement with Cherry's platform.
 | Total number of applications submitted in the last 4 months, indicating recent  application activity levels and merchant engagement with Cherry's platform.
 | `[]` | `{}` |
    | `FUNDED_LOANS_LAST_4_MONTHS` | 41 | `NUMBER` | Number of applications that resulted in funded loans in the last 4 months,  used for calculating conversion rates and funding success metrics.
 | Number of applications that resulted in funded loans in the last 4 months,  used for calculating conversion rates and funding success metrics.
 | `[]` | `{}` |
    | `REVIEW_START_DATE` | 42 | `TEXT` | Start date of the current review period for the merchant, marking the beginning  of the formal review and intervention process.
 | Start date of the current review period for the merchant, marking the beginning  of the formal review and intervention process.
 | `[]` | `{}` |
    | `REVIEW_END_DATE` | 43 | `DATE` | End date of the current review period, indicating when review decisions and  outcomes are expected to be finalized.
 | End date of the current review period, indicating when review decisions and  outcomes are expected to be finalized.
 | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.applications_loans_xf`
    *   `model.cherry_data_model.cherry_practices_expected_volume`
    *   `model.cherry_data_model.loan_info_xf`
    *   `model.cherry_data_model.look_assessment`
    *   `model.cherry_data_model.merchant_health_score_daily`
    *   `model.cherry_data_model.mystery_shopping_valids`
    *   `model.cherry_data_model.practice_info_xf`
    *   `model.cherry_data_model.reviews`
    *   `model.cherry_data_model.src_borrower_risk_outcomes`
    *   `model.cherry_data_model.src_organization_transaction_setting`
    *   `model.cherry_data_model.stg_merchants`
    *   `model.cherry_data_model.transactions_historical`

---
