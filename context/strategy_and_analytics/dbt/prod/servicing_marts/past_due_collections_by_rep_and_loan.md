## Model: `past_due_collections_by_rep_and_loan`

`past_due_collections_by_rep_and_loan`

*   **Unique ID:** `model.cherry_data_model.past_due_collections_by_rep_and_loan`
*   **FQN:** `prod.servicing_marts.past_due_collections_by_rep_and_loan`
*   **Description:** An aggregation of all of the past due loans incentives by collections rep and loan

*   **Tags:** `['servicing_and_collections']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `FULL_NAME` | 1 | `TEXT` | Full name of the agent who created the commitment and is eligible for incentives | Full name of the agent who created the commitment and is eligible for incentives | `[]` | `{}` |
    | `PMT_APPLY_DATE` | 2 | `DATE` | Date when the payment was applied in LoanPro | Date when the payment was applied in LoanPro | `[]` | `{}` |
    | `LOAN_ID` | 3 | `NUMBER` | Unique identifier for the loan | Unique identifier for the loan | `[]` | `{}` |
    | `PMT_CREATED_TIMESTAMP` | 4 | `TIMESTAMP_NTZ` | When the payment was created in timestamp, Pacific time | When the payment was created in timestamp, Pacific time | `[]` | `{}` |
    | `PAST_DUE_COLLECTIONS_1` | 5 | `NUMBER` | Sum of past due amount paid when days past due is between 1 and 29 | Sum of past due amount paid when days past due is between 1 and 29 | `[]` | `{}` |
    | `PAST_DUE_COLLECTIONS_30` | 6 | `NUMBER` | Sum of past due amount paid when days past due is between 30 and 59 | Sum of past due amount paid when days past due is between 30 and 59 | `[]` | `{}` |
    | `PAST_DUE_COLLECTIONS_60` | 7 | `NUMBER` | Sum of past due amount paid when days past due is between 60 and 89 | Sum of past due amount paid when days past due is between 60 and 89 | `[]` | `{}` |
    | `PAST_DUE_COLLECTIONS_90` | 8 | `NUMBER` | Sum of past due amount paid when days past due is between 90 and 120 | Sum of past due amount paid when days past due is between 90 and 120 | `[]` | `{}` |
    | `PAST_DUE_RECOVERIES` | 9 | `NUMBER` | Sum of the payment amount of past due recoveries, where
  loan status is either charged off or settled, or is a late payoff,
  or loan substatus is settled
 | Sum of the payment amount of past due recoveries, where
  loan status is either charged off or settled, or is a late payoff,
  or loan substatus is settled
 | `[]` | `{}` |
    | `PAST_DUE_NEW_MONEY_RECOVERIES` | 10 | `NUMBER` | Sum of the payment amount of past due recoveries *this month*, where
  loan status is either charged off or settled, or is a late payoff,
  or loan substatus is settled
 | Sum of the payment amount of past due recoveries *this month*, where
  loan status is either charged off or settled, or is a late payoff,
  or loan substatus is settled
 | `[]` | `{}` |
    | `PAST_DUE_RECOVERIES_NO_SETTLED_SUBSTATUS` | 11 | `NUMBER` | Sum of the payment amount of past due recoveries, where
  loan status is either charged off or settled, or is a late payoff
 | Sum of the payment amount of past due recoveries, where
  loan status is either charged off or settled, or is a late payoff
 | `[]` | `{}` |
    | `PAST_DUE_COLLECTIONS` | 12 | `NUMBER` | Sum of past_due_collections_1, past_due_collections_30, past_due_collections_60, and past_due_collections_90
 | Sum of past_due_collections_1, past_due_collections_30, past_due_collections_60, and past_due_collections_90
 | `[]` | `{}` |
    | `NEW_MONEY_ALL_COLLECTIONS` | 13 | `NUMBER` | Sum of past_due_new_money_recoveries and all days past due recoveries amount between 0 to 120 where the commitment was created this month
 | Sum of past_due_new_money_recoveries and all days past due recoveries amount between 0 to 120 where the commitment was created this month
 | `[]` | `{}` |
    | `NUM_PAST_DUE_COLLECTIONS` | 14 | `NUMBER` | The number of all new past due collections per rep | The number of all new past due collections per rep | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.daily_loan_xf`
    *   `model.cherry_data_model.servicing_rep_incentive_xf`

---
