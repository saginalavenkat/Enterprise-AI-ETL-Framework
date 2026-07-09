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

    def __init__(self, rag_pipeline=None):

        super().__init__("Jira Agent", rag_pipeline)

        self.mcp_client = MCPClient()

        logger.info("Jira Agent Initialized.")

    # -----------------------------------------------------------------

    def execute(self, context):

        logger.info("Jira Agent Started.")

        # No defect found → Skip Jira creation
        if context.defect_analysis is None:

            logger.info("No defect detected. Skipping Jira creation.")

            return context

        # -------------------------------------------------------------
        # Read defect information
        # -------------------------------------------------------------

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

Generated Automatically by Enterprise AI ETL Framework
"""

        # -------------------------------------------------------------
        # Create MCP Tool Call
        # -------------------------------------------------------------

        tool_call = ToolCall(

            tool_name="jira",

            arguments={

                "action": "create_issue",

                "project": "SCRUM",

                "summary": summary,

                "description": description,

                "issue_type": "Task"

            }

        )

        # -------------------------------------------------------------
        # Execute Jira Tool
        # -------------------------------------------------------------

        response = self.mcp_client.execute(tool_call)

        context.jira_issue = response

        logger.info("Jira Issue Created Successfully.")

        return context


# ---------------------------------------------------------------------
# Testing
# ---------------------------------------------------------------------

if __name__ == "__main__":

    from core.workflows.workflow_context import WorkflowContext

    context = WorkflowContext("Validation Failure")

    context.defect_analysis = {

        "summary": "Salary Validation Failed",

        "description": "Employee salary mismatch found.",

        "severity": "High",

        "priority": "High"

    }

    agent = JiraAgent()

    context = agent.execute(context)

    print(context.to_dict())