"""
===============================================================================
File Name   : test_end_to_end_workflow.py
Project     : Enterprise AI ETL Framework
Purpose     : End-to-End AI Workflow Test
===============================================================================
"""

from core.monitoring.monitor import FrameworkMonitor
from core.workflows.workflow_manager import WorkflowManager


def test_end_to_end_workflow():

    monitor = FrameworkMonitor()
    monitor.start()

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

    monitor.stop()
    monitor.save_metrics()
    monitor.display_metrics()

    assert context is not None
    assert context.documentation is not None