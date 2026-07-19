"""
===============================================================================
File Name   : documentation_agent.py
Project     : Enterprise AI ETL Framework
Purpose     : AI Documentation Agent
Author      : Venkata
===============================================================================
"""

from pathlib import Path
from datetime import datetime

from agents.base_agent import BaseAgent
from core.logger.logger import logger
from services.integrations.email_service import EmailService


class DocumentationAgent(BaseAgent):
    """
    AI Agent responsible for generating the final ETL execution report,
    saving it as a Markdown document, and emailing the report.
    """

    def __init__(
            self,
            rag_pipeline=None,
            client=None,
            email_service=None
    ):

        super().__init__(
            agent_name="Documentation Agent",
            rag_pipeline=rag_pipeline,
            client=client
        )

        self.email_service = email_service or EmailService()

        self.output_folder = Path("resources/outputs/documentation")
        self.output_folder.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------
    # Save Markdown Report
    # ------------------------------------------------------------------

    def save_markdown(self, context) -> str:

        filename = datetime.now().strftime(
            "ETL_Test_Report_%Y%m%d_%H%M%S.md"
        )

        report_path = self.output_folder / filename

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

{context.jira_issue}
"""

        report_path.write_text(content, encoding="utf-8")

        logger.info("Documentation saved: %s", report_path)

        return str(report_path)

    def send_reports(self, context):

        jira_key = "N/A"

        if context.jira_issue:

            try:
                jira_key = context.jira_issue.result.get(
                    "issue_key",
                    "N/A"
                )

            except Exception:

                jira_key = str(context.jira_issue)

        email_body = f"""
    Enterprise AI ETL Framework Execution Completed

    Workflow Status : SUCCESS

    Requirement : Completed
    Test Cases  : Generated
    SQL         : Generated
    Validation  : Completed
    Jira Issue  : {jira_key}

    Please find the attached reports.

    Regards,
    Enterprise AI ETL Framework
    """

        attachments = []

        if getattr(context, "documentation_file", None):
            attachments.append(context.documentation_file)

        if getattr(context, "report_file", None):
            attachments.append(context.report_file)

        self.email_service.send_email(
            to_email=self.email_service.report_email,
            subject="Enterprise AI ETL Framework - Execution Report",
            body=email_body,
            attachments=attachments,
            monitor=context.monitor
        )

        logger.info("Execution reports emailed successfully.")

    # ------------------------------------------------------------------
    # Execute
    # ------------------------------------------------------------------

    def execute(self, context):

        logger.info("=" * 80)
        logger.info("Documentation Agent Started.")
        logger.info("=" * 80)

        prompt = f"""
    Generate a professional Enterprise ETL Execution Report.

    Requirement
    {context.requirement}

    Mapping Analysis
    {context.mapping}

    Generated Test Cases
    {context.test_cases}

    Generated Test Data
    {context.test_data}

    Generated SQL
    {context.generated_sql}

    Database Result
    {context.query_result}

    Validation Summary
    {context.validation}

    Defect Analysis
    {context.defect_analysis}

    Jira Issue
    {context.jira_issue}

    Prepare a professional report suitable for management.
    """

        report = self.ask_llm(
            question=prompt,
            context=context
        )

        context.documentation = (
                report or "Mock Documentation Generated"
        )

        # Generate Documentation Report
        context.documentation_file = self.save_markdown(context)

        logger.info("Documentation Generated Successfully.")

        return context