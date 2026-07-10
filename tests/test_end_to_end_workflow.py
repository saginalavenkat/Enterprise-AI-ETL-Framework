"""
===============================================================================
File Name   : test_end_to_end_workflow.py
Project     : Enterprise AI ETL Framework
Purpose     : End-to-End AI Workflow Test
Author      : Venkata
===============================================================================
"""

from core.workflows.workflow_manager import WorkflowManager


def test_end_to_end_workflow():

    question = """
    Validate Employee ETL Load.

    Compare source and Snowflake target.

    Generate ETL test cases.

    Generate SQL validations.

    Perform validation.

    If validation fails,
    analyze defects,
    create Jira issue,
    and generate documentation.
    """

    manager = WorkflowManager()

    context = manager.execute(question)

    assert context is not None
    assert context.documentation is not None