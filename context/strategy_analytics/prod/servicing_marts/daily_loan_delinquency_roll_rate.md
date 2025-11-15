## Model: `daily_loan_delinquency_roll_rate`

`daily_loan_delinquency_roll_rate`

*   **Unique ID:** `model.cherry_data_model.daily_loan_delinquency_roll_rate`
*   **FQN:** `prod.servicing_marts.daily_loan_delinquency_roll_rate`
*   **Description:** Daily loan delinquency roll rate tracking model. Identifies loans at specific  delinquency stages (1, 30, 60, 90 DPD) and tracks whether they roll forward  into worse delinquency buckets 30 days later.
**Key Logic:** - Tracks loans at DPD milestones: 1, 30, 60, 90 - Looks forward 30 days to determine if loan rolled to next bucket - Roll indicators: 1 DPD → 29+ DPD, 30 DPD → 59+ DPD, 60 DPD → 89+ DPD, 
  90 DPD → 119+ DPD or charge-off
- Excludes: fraud loans, refunded/voided loans, pay-in-four, balance ≤ $5 - Historical window: Last 365 days

*   **Tags:** `['servicing_and_collections', 'core_hourly']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `RECORD_DATE` | 1 | `DATE` | The date of the loan snapshot at the initial delinquency stage being tracked. This is the baseline date from which the 30-day forward roll is measured.
 | The date of the loan snapshot at the initial delinquency stage being tracked. This is the baseline date from which the 30-day forward roll is measured.
 | `[]` | `{}` |
    | `CONTRACT_ID` | 2 | `TEXT` | The LoanPro contract identifier for the loan. Used to track individual  loan performance through delinquency stages.
 | The LoanPro contract identifier for the loan. Used to track individual  loan performance through delinquency stages.
 | `[]` | `{}` |
    | `PRINCIPAL_BALANCE` | 3 | `NUMBER` | The outstanding principal balance of the loan on the record_date.  Used for weighted roll rate calculations. Only loans with balance > [$]5 are included.
 | The outstanding principal balance of the loan on the record_date.  Used for weighted roll rate calculations. Only loans with balance > $5 are included.
 | `[]` | `{}` |
    | `CHARGE_OFF` | 4 | `NUMBER` | The charge-off amount 30 days after the record_date. Used to identify  loans that charged off after being in the 90 DPD bucket. Positive value  indicates a charge-off occurred.
 | The charge-off amount 30 days after the record_date. Used to identify  loans that charged off after being in the 90 DPD bucket. Positive value  indicates a charge-off occurred.
 | `[]` | `{}` |
    | `DQ_BUCKET` | 5 | `NUMBER` | Days Past Due (DPD) bucket at the record_date. Limited to milestone  values: 1, 30, 60, or 90 days. Represents the starting delinquency  stage for roll rate tracking.
 | Days Past Due (DPD) bucket at the record_date. Limited to milestone  values: 1, 30, 60, or 90 days. Represents the starting delinquency  stage for roll rate tracking.
 | `[]` | `{}` |
    | `DPD_ROLL_FORWARD` | 6 | `NUMBER` | Binary indicator (0 or 1) for whether the loan rolled forward into a  worse delinquency bucket 30 days later.
**Roll Forward Logic:** - 1 DPD → 1 if reaches 29+ DPD within 30 days - 30 DPD → 1 if reaches 59+ DPD within 30 days   - 60 DPD → 1 if reaches 89+ DPD within 30 days - 90 DPD → 1 if charges off or reaches 119+ DPD within 30 days - 0 if loan improved or stayed in same bucket | Binary indicator (0 or 1) for whether the loan rolled forward into a  worse delinquency bucket 30 days later.
**Roll Forward Logic:** - 1 DPD → 1 if reaches 29+ DPD within 30 days - 30 DPD → 1 if reaches 59+ DPD within 30 days   - 60 DPD → 1 if reaches 89+ DPD within 30 days - 90 DPD → 1 if charges off or reaches 119+ DPD within 30 days - 0 if loan improved or stayed in same bucket | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.applications_loans_xf`
    *   `model.cherry_data_model.daily_loan_xf`
    *   `model.cherry_data_model.int_funded_information_pt`

---
