## Model: `charged_off_view_xf`

`charged_off_view_xf`

*   **Unique ID:** `model.cherry_data_model.charged_off_view_xf`
*   **FQN:** `prod.risk_marts.charged_off_view_xf`
*   **Description:** **Comprehensive Loan Charge-Off Analysis**
This model provides a unified view of all loan charge-offs across Cherry's portfolio, capturing both event-driven charge-offs (fraud, bankruptcy, deceased) and time-based charge-offs (120+ days past due). The model serves as the single source of truth for charge-off reporting, loss calculations, and portfolio risk analysis by combining transaction-based charge-off events with systematic time-based charge-offs.
**Key Business Logic:** - **Event-Based Charge-offs**: Identified through specific transaction titles containing 'fraud', 'bankr', or 'deceased' - **Time-Based Charge-offs**: Loans reaching 120+ days past due (excluding those already in bankruptcy or other terminal statuses) - **Deduplication**: Ensures only one charge-off record per loan using the most recent charge-off date - **Exclusions**: Filters out invalid contracts and handles edge cases for proper charge-off attribution
**Primary Use Cases:** - Loss provisioning and charge-off reserve calculations - Portfolio risk analysis and vintage performance tracking - Regulatory reporting and capital market analytics - Collections strategy and recovery planning
**Data Sources:** - `daily_loan_xf`: Daily loan status and balance information with days past due tracking - `src_loan_tx`: LoanPro transaction data for event-based charge-off identification - `int_funded_information_pt`: Cherry-LoanPro loan ID mapping and basic loan information
**Grain:** One record per charged-off loan, with the most recent charge-off date if multiple charge-off events occur

*   **Tags:** `['risk', 'daily']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `CHARGEOFF_DATE` | 1 | `TIMESTAMP_NTZ` | Date when the loan was charged off, either through a specific charge-off transaction event or when the loan first reached 120+ days past due. For event-based charge-offs, this is the transaction_date from the charge-off transaction. For time-based charge-offs, this is the record_date when the loan first qualified for charge-off (120+ DPD with eligible status).
 | Date when the loan was charged off, either through a specific charge-off transaction event or when the loan first reached 120+ days past due. For event-based charge-offs, this is the transaction_date from the charge-off transaction. For time-based charge-offs, this is the record_date when the loan first qualified for charge-off (120+ DPD with eligible status).
 | `[]` | `{}` |
    | `LOAN_ID` | 2 | `NUMBER` | Foreign key reference to the Cherry loan identifier. This is the primary loan identifier used throughout Cherry's system for loan tracking, reporting, and analysis.
 | Foreign key reference to the Cherry loan identifier. This is the primary loan identifier used throughout Cherry's system for loan tracking, reporting, and analysis.
 | `[]` | `{}` |
    | `CONTRACT_ID` | 3 | `TEXT` | Foreign key reference to the loan contract identifier. This is the display ID used in customer-facing communications and represents the legal contract between Cherry and the borrower.
 | Foreign key reference to the loan contract identifier. This is the display ID used in customer-facing communications and represents the legal contract between Cherry and the borrower.
 | `[]` | `{}` |
    | `DAYS_PAST_DUE` | 4 | `NUMBER` | Number of days the loan was past due at the time of charge-off. For transaction-based charge-offs, this reflects the DPD status on the charge-off transaction date. For time-based charge-offs, this will be 120 or greater, representing the DPD threshold that triggered the charge-off.
 | Number of days the loan was past due at the time of charge-off. For transaction-based charge-offs, this reflects the DPD status on the charge-off transaction date. For time-based charge-offs, this will be 120 or greater, representing the DPD threshold that triggered the charge-off.
 | `[]` | `{}` |
    | `LOAN_STATUS` | 5 | `TEXT` | Current loan status at the time of charge-off, derived from the daily_loan_xf model. Common values include 'LATE', 'OPEN', 'Bankruptcy', and other loan statuses that indicate the operational state of the loan when the charge-off occurred.
 | Current loan status at the time of charge-off, derived from the daily_loan_xf model. Common values include 'LATE', 'OPEN', 'Bankruptcy', and other loan statuses that indicate the operational state of the loan when the charge-off occurred.
 | `[]` | `{}` |
    | `LOAN_SUBSTATUS` | 6 | `TEXT` | Current loan sub-status providing additional detail about the loan's operational state at charge-off. Examples include 'Settled', 'Deceased', 'Fraud', 'Filed' and other sub-statuses that provide granular context for the loan's condition.
 | Current loan sub-status providing additional detail about the loan's operational state at charge-off. Examples include 'Settled', 'Deceased', 'Fraud', 'Filed' and other sub-statuses that provide granular context for the loan's condition.
 | `[]` | `{}` |
    | `GUCO` | 7 | `NUMBER` | **Gross Unpaid Charge Off (Total)** - Total outstanding balance charged off including principal, interest, and fees. This represents the full amount of loss recognized at charge-off and is the primary metric for loss calculations and provisioning.
 | **Gross Unpaid Charge Off (Total)** - Total outstanding balance charged off including principal, interest, and fees. This represents the full amount of loss recognized at charge-off and is the primary metric for loss calculations and provisioning.
 | `[]` | `{}` |
    | `GUCO_T` | 8 | `NUMBER` | **Gross Unpaid Charge Off (Time-Based)** - Amount charged off due to reaching 120+ days past due. This captures systematic charge-offs based on delinquency timing rather than specific events. Set to the full outstanding balance for time-based charge-offs, 0 for event-based.
 | **Gross Unpaid Charge Off (Time-Based)** - Amount charged off due to reaching 120+ days past due. This captures systematic charge-offs based on delinquency timing rather than specific events. Set to the full outstanding balance for time-based charge-offs, 0 for event-based.
 | `[]` | `{}` |
    | `GUCO_F` | 9 | `NUMBER` | **Gross Unpaid Charge Off (Fraud)** - Amount charged off due to confirmed fraud. Identified through transaction titles containing 'fraud'. This represents losses due to fraudulent applications or borrower behavior.
 | **Gross Unpaid Charge Off (Fraud)** - Amount charged off due to confirmed fraud. Identified through transaction titles containing 'fraud'. This represents losses due to fraudulent applications or borrower behavior.
 | `[]` | `{}` |
    | `GUCO_BK` | 10 | `NUMBER` | **Gross Unpaid Charge Off (Bankruptcy)** - Amount charged off due to borrower bankruptcy. Identified through transaction titles containing 'bankr'. These represent losses where legal bankruptcy proceedings prevent or limit collection efforts.
 | **Gross Unpaid Charge Off (Bankruptcy)** - Amount charged off due to borrower bankruptcy. Identified through transaction titles containing 'bankr'. These represent losses where legal bankruptcy proceedings prevent or limit collection efforts.
 | `[]` | `{}` |
    | `GUCO_D` | 11 | `NUMBER` | **Gross Unpaid Charge Off (Deceased)** - Amount charged off due to borrower death. Identified through transaction titles containing 'deceased'. These losses occur when the borrower has passed away and estate recovery is not viable.
 | **Gross Unpaid Charge Off (Deceased)** - Amount charged off due to borrower death. Identified through transaction titles containing 'deceased'. These losses occur when the borrower has passed away and estate recovery is not viable.
 | `[]` | `{}` |
    | `GUCO_E` | 12 | `NUMBER` | **Gross Unpaid Charge Off (Event-Based)** - Total amount charged off due to specific events (fraud + bankruptcy + deceased). This aggregates all event-driven charge-offs as opposed to time-based charge-offs, useful for analyzing loss causation.
 | **Gross Unpaid Charge Off (Event-Based)** - Total amount charged off due to specific events (fraud + bankruptcy + deceased). This aggregates all event-driven charge-offs as opposed to time-based charge-offs, useful for analyzing loss causation.
 | `[]` | `{}` |
    | `GACO` | 13 | `NUMBER` | **Gross Amount Charge Off (Total)** - Principal balance portion of the total charge-off amount. This represents the original loan amount component of the loss, excluding accrued interest and fees, and is key for principal loss rate calculations.
 | **Gross Amount Charge Off (Total)** - Principal balance portion of the total charge-off amount. This represents the original loan amount component of the loss, excluding accrued interest and fees, and is key for principal loss rate calculations.
 | `[]` | `{}` |
    | `GACO_T` | 14 | `NUMBER` | **Gross Amount Charge Off (Time-Based)** - Principal balance charged off due to reaching 120+ days past due. This is the principal component of time-based charge-offs, useful for analyzing principal loss rates by charge-off type.
 | **Gross Amount Charge Off (Time-Based)** - Principal balance charged off due to reaching 120+ days past due. This is the principal component of time-based charge-offs, useful for analyzing principal loss rates by charge-off type.
 | `[]` | `{}` |
    | `GACO_F` | 15 | `NUMBER` | **Gross Amount Charge Off (Fraud)** - Principal balance charged off due to fraud. This represents the original loan amount lost to fraudulent activity, critical for fraud loss analysis and underwriting model evaluation.
 | **Gross Amount Charge Off (Fraud)** - Principal balance charged off due to fraud. This represents the original loan amount lost to fraudulent activity, critical for fraud loss analysis and underwriting model evaluation.
 | `[]` | `{}` |
    | `GACO_BK` | 16 | `NUMBER` | **Gross Amount Charge Off (Bankruptcy)** - Principal balance charged off due to bankruptcy. This captures the principal loss component when borrowers file for bankruptcy protection, important for legal and recovery strategy analysis.
 | **Gross Amount Charge Off (Bankruptcy)** - Principal balance charged off due to bankruptcy. This captures the principal loss component when borrowers file for bankruptcy protection, important for legal and recovery strategy analysis.
 | `[]` | `{}` |
    | `GACO_D` | 17 | `NUMBER` | **Gross Amount Charge Off (Deceased)** - Principal balance charged off due to borrower death. This represents principal losses when borrowers pass away, relevant for insurance considerations and estate recovery procedures.
 | **Gross Amount Charge Off (Deceased)** - Principal balance charged off due to borrower death. This represents principal losses when borrowers pass away, relevant for insurance considerations and estate recovery procedures.
 | `[]` | `{}` |
    | `GACO_E` | 18 | `NUMBER` | **Gross Amount Charge Off (Event-Based)** - Total principal balance charged off due to specific events (fraud + bankruptcy + deceased). This aggregates principal losses from event-driven charge-offs for comparative analysis against time-based principal losses. | **Gross Amount Charge Off (Event-Based)** - Total principal balance charged off due to specific events (fraud + bankruptcy + deceased). This aggregates principal losses from event-driven charge-offs for comparative analysis against time-based principal losses. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.daily_loan_xf`
    *   `model.cherry_data_model.int_funded_information_pt`
    *   `model.cherry_data_model.src_loan_tx`

---
