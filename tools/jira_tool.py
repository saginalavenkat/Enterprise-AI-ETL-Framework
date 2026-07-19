"""
===============================================================================
File Name   : jira_tool.py
Project     : Enterprise AI ETL Framework
Purpose     : Jira Tool
Author      : Venkata
===============================================================================
"""

from core.logger.logger import logger

from services.integrations.jira_service import JiraService

from tools.base_tool import BaseTool

from integrations.mcp.tool_response import ToolResponse


class JiraTool(BaseTool):

    def __init__(self):

        super().__init__("Jira Tool")

        logger.info("Jira Tool Initialized.")

        self.service = JiraService()

    # ------------------------------------------------------------------

    def execute(
            self,
            action,
            project=None,
            summary=None,
            description=None,
            issue_type="Task",
            jql=None,
            issue_key=None,
            comment=None, monitor=None):

        if action == "create_issue":

            result = self.service.create_issue(
                project=project,
                summary=summary,
                description=description,
                issue_type=issue_type, monitor=monitor)

            return ToolResponse(
                status="SUCCESS",
                result=result
            )

        elif action == "search_issue":

            result = self.service.search_issue(jql)

            return ToolResponse(
                status="SUCCESS",
                result=result
            )

        elif action == "add_comment":

            result = self.service.add_comment(
                issue_key,
                comment
            )

            return ToolResponse(
                status="SUCCESS",
                result=result
            )

        return ToolResponse(
            status="FAILED",
            result=f"Unknown Jira action : {action}"
        )


