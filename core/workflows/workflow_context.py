"""
===============================================================================
File Name   : workflow_context.py
Project     : Enterprise AI ETL Framework
Purpose     : Shared Workflow Context
Author      : Venkata
===============================================================================
"""
from core.metrics.framework_metrics import FrameworkMetrics

class WorkflowContext:

    """
    Shared context that flows through all AI Agents.
    Each agent reads the existing context,
    performs its task,
    and updates the context for the next agent.
    """

    def __init__(self, question: str):

        self.metrics = FrameworkMetrics()

        self.question = question

        # ------------------------------------------------------------
        # AI Outputs
        # ------------------------------------------------------------

        self.requirement = None
        self.mapping = None
        self.test_cases = None
        self.test_data = None
        self.generated_sql = None
        self.query_result = None
        self.validation = None
        self.documentation = None
        self.defect_analysis = None
        self.jira_issue = None
        self.report_file = None

    # ------------------------------------------------------------

    def to_dict(self):
        return {

            "question": self.question,
            "requirement": self.requirement,
            "mapping": self.mapping,
            "test_cases": self.test_cases,
            "test_data": self.test_data,
            "generated_sql": self.generated_sql,
            "query_result": self.query_result,
            "validation": self.validation,
            "documentation": self.documentation,
            "report_file": self.report_file,
            "defect_analysis": self.defect_analysis,
            "jira_issue": self.jira_issue,
        }