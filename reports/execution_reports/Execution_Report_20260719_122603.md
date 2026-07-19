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

- requirement : 2.35 sec
- mapping_analysis : 2.56 sec
- test_case : 2.35 sec
- test_data : 2.27 sec
- sql : 6.35 sec
- validation : 2.24 sec
- defect_analysis : 2.35 sec
- jira : 1.13 sec
- documentation : 7.33 sec

## Generated SQL

```sql
SELECT * FROM EMPLOYEE WHERE DEPARTMENT='IT' AND SALARY > 90000;
```

## Query Result

Database : snowflake
Rows Returned : 2
Execution Time : 3.89 sec

Sample Rows

```text
[(104, 'Robert', 'IT', 'Lead', Decimal('98000.00'), 'Pune', datetime.date(2019, 9, 1), True), (110, 'Vijay', 'IT', 'Architect', Decimal('150000.00'), 'Hyderabad', datetime.date(2016, 2, 8), True)]
```
Mock Response

## Defect Analysis

{'summary': 'ETL Validation Failed', 'description': 'Mock Response', 'severity': 'High', 'priority': 'High'}

## Jira Issue

ToolResponse(status=SUCCESS, result={'issue_key': 'SCRUM-65', 'issue_id': '10352', 'issue_url': 'https://saginalavenkat.atlassian.net/browse/SCRUM-65'})

## Documentation

Mock Response

## Framework Metrics

- execution_time : 0
- agents_executed : 9
- successful_agents : 9
- failed_agents : 0
- llm_calls : 8
- rag_searches : 1
- database_queries : 1
- jira_issues_created : 1
- emails_sent : 1
- tokens_used : 1500
- estimated_cost : 0

## Query Result

Database : snowflake
Rows Returned : 2
Execution Time : 3.89 sec

Sample Rows

```text
[(104, 'Robert', 'IT', 'Lead', Decimal('98000.00'), 'Pune', datetime.date(2019, 9, 1), True), (110, 'Vijay', 'IT', 'Architect', Decimal('150000.00'), 'Hyderabad', datetime.date(2016, 2, 8), True)]
```

## Errors

No Errors.
