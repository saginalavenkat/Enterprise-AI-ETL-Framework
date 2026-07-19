"""
===============================================================================
File Name   : jira_agent.py
Project     : Enterprise AI ETL Framework
Purpose     : AI Jira Agent
Author      : Venkata
===============================================================================
"""

from agents.base_agent import BaseAgent
from core.logger.logger import logger

from integrations.mcp.mcp_client import MCPClient
from integrations.mcp.tool_call import ToolCall


class JiraAgent(BaseAgent):
    """
    AI Agent responsible for creating Jira issues
    for ETL validation failures.
    """

    def __init__(
            self,
            rag_pipeline=None,
            client=None,
            mcp_client=None
    ):

        super().__init__(
            agent_name="Jira Agent",
            rag_pipeline=rag_pipeline,
            client=client
        )

        self.mcp_client = mcp_client or MCPClient()

    # ------------------------------------------------------------------
    # Execute
    # ------------------------------------------------------------------

    def execute(self, context):

        logger.info("=" * 80)
        logger.info("Jira Agent Started.")
        logger.info("=" * 80)

        if context.defect_analysis is None:

            logger.info("No defect detected. Skipping Jira creation.")

            return context

        summary = context.defect_analysis.get(
            "summary",
            "Enterprise AI ETL Validation Failure"
        )

        description = context.defect_analysis.get(
            "description",
            "Validation failed."
        )

        severity = context.defect_analysis.get(
            "severity",
            "Medium"
        )

        priority = context.defect_analysis.get(
            "priority",
            "Medium"
        )

        description += f"""

Severity : {severity}

Priority : {priority}

Generated Automatically by Enterprise AI ETL Framework.
"""

        tool_call = ToolCall(
            tool_name="jira",
            arguments={
                "action": "create_issue",
                "project": "SCRUM",
                "summary": summary,
                "description": description,
                "issue_type": "Task", "monitor": context.monitor})

        logger.info("Creating Jira issue using MCP...")

        try:

            response = self.mcp_client.execute(tool_call)

            context.jira_issue = response

            logger.info("Jira Issue Created Successfully.")

        except Exception:

            logger.exception("Failed to create Jira issue.")

            raise

        return context