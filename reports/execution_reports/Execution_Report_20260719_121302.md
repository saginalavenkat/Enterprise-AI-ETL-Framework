# Enterprise AI ETL Framework

## Execution Summary

- **Question:** 
    Validate Employee ETL Load.

    Compare source and Snowflake target.

    Generate ETL test cases.

    Generate SQL validations.

    Perform validation.

    If validation fails,
    analyze defects,
    create Jira issue,
    and generate documentation.
    
- **Execution Time:** 0 sec
- **Workflow Status:** SUCCESS

## Execution Plan

1. requirement
2. mapping_analysis
3. test_case
4. test_data
5. sql
6. validation
7. defect_analysis
8. jira
9. documentation

## Agent Execution Time

- requirement : 3.17 sec
- mapping_analysis : 2.33 sec
- test_case : 2.30 sec
- test_data : 2.26 sec
- sql : 6.00 sec
- validation : 2.33 sec
- defect_analysis : 2.26 sec
- jira : 1.52 sec
- documentation : 7.14 sec

## Generated SQL

```sql
SELECT * FROM EMPLOYEE WHERE DEPARTMENT='IT' AND SALARY > 90000;
```

## Query Result

