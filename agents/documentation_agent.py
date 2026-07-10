"""
===============================================================================
File Name   : documentation_agent.py
Project     : Enterprise AI ETL Framework
Purpose     : AI Documentation Agent
Author      : Venkata
===============================================================================
"""

from agents.base_agent import BaseAgent
from core.logger.logger import logger
from pathlib import Path
from services.integrations.email_service import EmailService

class DocumentationAgent(BaseAgent):

    def __init__(self, rag_pipeline=None):

        super().__init__("Documentation Agent", rag_pipeline)
        self.output_folder = Path("resources/outputs/documentation")
        self.output_folder.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------
    def save_markdown(self, context):

        report_path = self.output_folder / "ETL_Test_Report.md"

        content = f"""
    # Enterprise AI ETL Execution Report

    ## Requirement

    {context.requirement}

    ## Mapping

    {context.mapping}

    ## Test Cases

    {context.test_cases}

    ## Test Data

    {context.test_data}

    ## SQL

    {context.generated_sql}

    ## Validation

    {context.validation}

    ## Documentation

    {context.documentation}
    
    ## Defect Analysis

    {context.defect_analysis}

    ## Jira Issue

    {context.jira_issue}"""

        report_path.write_text(content, encoding="utf-8")

        logger.info("Documentation saved : %s", report_path)

        return str(report_path)

    def execute(self, context):
        print("=" * 80)
        print("Documentation Agent Started")
        print("=" * 80)

        logger.info("Documentation Agent Started.")

        prompt = f"""
        Generate a professional ETL Execution Report.

        Include the following sections.

        ------------------------------------------------

        Requirement

        {context.requirement}

        ------------------------------------------------

        Mapping Analysis

        {context.mapping}

        ------------------------------------------------

        Generated Test Cases

        {context.test_cases}

        ------------------------------------------------

        Generated Test Data

        {context.test_data}

        ------------------------------------------------

        Generated SQL

        {context.generated_sql}

        ------------------------------------------------

        Database Result

        {context.query_result}

        ------------------------------------------------

        Validation Summary

        {context.validation}

        ------------------------------------------------

        Defect Analysis

        {context.defect_analysis}

        ------------------------------------------------

        Jira Issue

        {context.jira_issue}

        ------------------------------------------------

        Prepare a professional report suitable for management.
        """
        report = self.ask_llm(prompt)
        context.metrics.add_tokens(500)
        print("LLM Report:", report)

        # Save report in workflow context
        context.documentation = report or "Mock Documentation Generated"
        print("Documentation Stored:", context.documentation)

        # Save Markdown report and store the file path
        context.report_file = self.save_markdown(context)
        email_service = EmailService()

        email_body = f"""
        Enterprise AI ETL Framework Execution Completed

        Requirement      : Completed
        Test Cases       : Generated
        SQL              : Generated
        Validation       : Completed
        Jira Issue       : {context.jira_issue}

        Please find the attached execution report.

        Regards,
        Enterprise AI ETL Framework
        """

        email_service.send_email(to_email=email_service.report_email, subject="Enterprise AI ETL Execution Report", body=email_body, attachments=[context.report_file])

        logger.info("Documentation Generated Successfully.")
        print("Documentation Agent Completed")

        return context
# ------------------------------------------------------------

if __name__ == "__main__":

    from core.workflows.workflow_context import WorkflowContext

    agent = DocumentationAgent()

    context = WorkflowContext("Generate Report")

    context.requirement = "Employee Validation"

    context.mapping = "EMPLOYEE Mapping"

    context.test_cases = "Salary Validation"

    context.test_data = "10 Sample Records"

    context.generated_sql = "SELECT * FROM EMPLOYEE"

    context.query_result = "10 Rows"

    context.validation = "Validation Passed"

    context = agent.execute(context)

    print(context.to_dict())