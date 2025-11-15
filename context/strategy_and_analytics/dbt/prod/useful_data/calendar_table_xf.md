## Model: `calendar_table_xf`

`calendar_table_xf`

*   **Unique ID:** `model.cherry_data_model.calendar_table_xf`
*   **FQN:** `prod.useful_data.calendar_table_xf`
*   **Description:** **Calendar Dimension Table with Business Context**
This model serves as the primary calendar dimension table for Cherry's analytics, providing  comprehensive date-related information enriched with business-specific context. It combines  standard calendar data with bank holidays and Cherry company holidays to support accurate  business day calculations and time-based analysis.
**Key Features:** - Standard calendar dimensions (year, month, quarter, day, etc.) - Business-specific holiday identification for Cherry operations - Weekend and weekday classification - Fiscal quarter adjustments (Q1 starts in February) - Bank holiday recognition - Company holiday and retreat date tracking
**Primary Use Cases:** - Time-based reporting and analysis - Business day calculations excluding holidays - Fiscal period reporting with Cherry's calendar - Revenue recognition and financial reporting - Employee productivity analysis (excluding company holidays) - Sales target and quota calculations
**Data Sources:** - `src_calendar_table`: Base calendar data with standard date dimensions - `bank_holiday_details`: Federal and bank holiday information - Hardcoded Cherry company holidays and retreat dates
**Grain:** One record per calendar date

*   **Tags:** `['useful_data', 'daily']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `FULL_DATE` | 1 | `DATE` | The complete date in YYYY-MM-DD format. This serves as the primary key and grain  for the calendar table, with one record per calendar date.
 | The complete date in YYYY-MM-DD format. This serves as the primary key and grain  for the calendar table, with one record per calendar date.
 | `[]` | `{}` |
    | `YEAR` | 2 | `NUMBER` | Four-digit year extracted from the full_date. Used for annual reporting,  year-over-year comparisons, and filtering data by calendar year.
 | Four-digit year extracted from the full_date. Used for annual reporting,  year-over-year comparisons, and filtering data by calendar year.
 | `[]` | `{}` |
    | `MONTH` | 3 | `NUMBER` | Numeric month (1-12) extracted from the full_date. Used for monthly reporting,  seasonality analysis, and month-over-month comparisons.
 | Numeric month (1-12) extracted from the full_date. Used for monthly reporting,  seasonality analysis, and month-over-month comparisons.
 | `[]` | `{}` |
    | `MONTH_NAME` | 4 | `TEXT` | Full month name (January, February, etc.) extracted from the full_date.  Used for user-friendly reporting and dashboard displays.
 | Full month name (January, February, etc.) extracted from the full_date.  Used for user-friendly reporting and dashboard displays.
 | `[]` | `{}` |
    | `DAY` | 5 | `NUMBER` | Numeric day of the month (1-31) extracted from the full_date. Used for  daily reporting and day-of-month analysis.
 | Numeric day of the month (1-31) extracted from the full_date. Used for  daily reporting and day-of-month analysis.
 | `[]` | `{}` |
    | `DAY_OF_WEEK` | 6 | `TEXT` | Numeric day of the week extracted from the full_date. Used for day-of-week  analysis, weekly patterns, and business day calculations.
 | Numeric day of the week extracted from the full_date. Used for day-of-week  analysis, weekly patterns, and business day calculations.
 | `[]` | `{}` |
    | `WEEK_OF_YEAR` | 7 | `NUMBER` | Numeric week of the year (1-53) extracted from the full_date. Used for  weekly reporting, seasonal analysis, and week-over-week comparisons.
 | Numeric week of the year (1-53) extracted from the full_date. Used for  weekly reporting, seasonal analysis, and week-over-week comparisons.
 | `[]` | `{}` |
    | `DAY_OF_YEAR` | 8 | `NUMBER` | Numeric day of the year (1-366) extracted from the full_date. Used for  day-of-year analysis, seasonal patterns, and cumulative calculations.
 | Numeric day of the year (1-366) extracted from the full_date. Used for  day-of-year analysis, seasonal patterns, and cumulative calculations.
 | `[]` | `{}` |
    | `QUARTER` | 9 | `NUMBER` | Numeric quarter (1-4) extracted from the full_date. Used for quarterly  reporting, seasonal analysis, and quarter-over-quarter comparisons.
 | Numeric quarter (1-4) extracted from the full_date. Used for quarterly  reporting, seasonal analysis, and quarter-over-quarter comparisons.
 | `[]` | `{}` |
    | `QUARTER_YEAR` | 10 | `TEXT` | Fiscal quarter representation adjusted for Cherry's fiscal calendar.  For January dates, the quarter is attributed to the previous year  (e.g., "2024 Q1" for January 2025), reflecting Cherry's fiscal year structure.
 | Fiscal quarter representation adjusted for Cherry's fiscal calendar.  For January dates, the quarter is attributed to the previous year  (e.g., "2024 Q1" for January 2025), reflecting Cherry's fiscal year structure.
 | `[]` | `{}` |
    | `DAYS_IN_MONTH` | 11 | `NUMBER` | Total number of days in the month for the given date. Calculated using  a window function to count days per year-month combination. Used for  monthly average calculations and month-end reporting.
 | Total number of days in the month for the given date. Calculated using  a window function to count days per year-month combination. Used for  monthly average calculations and month-end reporting.
 | `[]` | `{}` |
    | `CALENDAR_QUARTER` | 12 | `NUMBER` | Standard calendar quarter (1-4) calculated using the QUARTER function.  Represents the traditional calendar quarter without fiscal adjustments.
 | Standard calendar quarter (1-4) calculated using the QUARTER function.  Represents the traditional calendar quarter without fiscal adjustments.
 | `[]` | `{}` |
    | `CALENDAR_QUARTER_YEAR` | 13 | `TEXT` | Standard calendar quarter combined with year (e.g., "2025 Q1").  Uses traditional calendar quarters without fiscal year adjustments.
 | Standard calendar quarter combined with year (e.g., "2025 Q1").  Uses traditional calendar quarters without fiscal year adjustments.
 | `[]` | `{}` |
    | `DAY_NAME` | 14 | `TEXT` | Three-letter day name (Mon, Tue, Wed, Thu, Fri, Sat, Sun) calculated  using the DAYNAME function. Used for day-of-week analysis and  user-friendly reporting.
 | Three-letter day name (Mon, Tue, Wed, Thu, Fri, Sat, Sun) calculated  using the DAYNAME function. Used for day-of-week analysis and  user-friendly reporting.
 | `[]` | `{}` |
    | `IS_WEEKEND` | 15 | `BOOLEAN` | Boolean flag indicating whether the date falls on a weekend (Saturday or Sunday).  TRUE for weekend days, FALSE for weekdays. Used for business day calculations  and filtering out non-business days.
 | Boolean flag indicating whether the date falls on a weekend (Saturday or Sunday).  TRUE for weekend days, FALSE for weekdays. Used for business day calculations  and filtering out non-business days.
 | `[]` | `{}` |
    | `IS_WEEKDAY` | 16 | `BOOLEAN` | Boolean flag indicating whether the date falls on a weekday (Monday through Friday).  TRUE for weekdays, FALSE for weekends. Used for business day calculations  and operational reporting.
 | Boolean flag indicating whether the date falls on a weekday (Monday through Friday).  TRUE for weekdays, FALSE for weekends. Used for business day calculations  and operational reporting.
 | `[]` | `{}` |
    | `IS_BANK_HOLIDAY` | 17 | `BOOLEAN` | Boolean flag indicating whether the date is a recognized bank holiday.  TRUE when the date matches a record in the bank_holiday_details table,  FALSE otherwise. Used for business day calculations and financial reporting.
 | Boolean flag indicating whether the date is a recognized bank holiday.  TRUE when the date matches a record in the bank_holiday_details table,  FALSE otherwise. Used for business day calculations and financial reporting.
 | `[]` | `{}` |
    | `IS_COMPANY_HOLIDAY` | 18 | `BOOLEAN` | Boolean flag indicating whether the date is a Cherry company holiday.  TRUE when the date matches a hardcoded company holiday or retreat date,  FALSE otherwise. Used for employee productivity analysis and operational planning.
 | Boolean flag indicating whether the date is a Cherry company holiday.  TRUE when the date matches a hardcoded company holiday or retreat date,  FALSE otherwise. Used for employee productivity analysis and operational planning.
 | `[]` | `{}` |
    | `COMPANY_HOLIDAY_NAME` | 19 | `TEXT` | Name of the Cherry company holiday if the date is a company holiday.  Includes standard holidays (Christmas, New Year's, etc.), federal holidays  (MLK Day, Presidents' Day, etc.), and company-specific dates (retreats,  Black Friday). NULL for non-company holidays. | Name of the Cherry company holiday if the date is a company holiday.  Includes standard holidays (Christmas, New Year's, etc.), federal holidays  (MLK Day, Presidents' Day, etc.), and company-specific dates (retreats,  Black Friday). NULL for non-company holidays. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.src_calendar_table`
    *   `seed.cherry_data_model.bank_holiday_details`

---
