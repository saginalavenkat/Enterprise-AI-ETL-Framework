"""
===============================================================================
File Name   : tool_registry.py
Project     : Enterprise AI ETL Framework
Purpose     : MCP Tool Registry
Author      : Venkata
===============================================================================
"""

from core.logger.logger import logger

from tools.database_tool import DatabaseTool
from tools.jira_tool import JiraTool
from tools.file_tool import FileTool
from tools.email_tool import EmailTool


class ToolRegistry:

    def __init__(self):

        logger.info("Initializing Tool Registry...")

        self.tools = {

            "database": {

                "description": "Execute SQL queries on enterprise databases",

                "tool": DatabaseTool()

            },

            "jira": {

                "description": "Create, search and update Jira issues",

                "tool": JiraTool()

            },

            "file": {

                "description": "Enterprise file operations",

                "tool": FileTool()

            },

            "email": {

                "description": "Enterprise email notifications",

                "tool": EmailTool()

            }

        }

        logger.info("Registered Tools: %s", ", ".join(self.tools.keys()))

    # ------------------------------------------------------------------

    def get_tool(self, tool_name):

        """Returns the requested tool object. Parameters: tool_name (str): Name of the tool, Returns: BaseTool | None """

        tool = self.tools.get(tool_name.lower())

        if tool:
            logger.info("Tool '%s' selected.", tool_name)
            return tool["tool"]

        logger.error("Tool '%s' not found.", tool_name)
        return None

    # ------------------------------------------------------------------

    def list_tools(self):
        """
        Returns all registered tool names.
        """

        return list(self.tools.keys())

    # ------------------------------------------------------------------

    def get_tool_description(self, tool_name):

        """Returns the description of the specified tool. Parameters: tool_name (str): Name of the tool, Returns: str | None"""

        tool = self.tools.get(tool_name.lower())

        if tool:
            return tool["description"]

        return None

    # ------------------------------------------------------------------

    def list_tool_details(self):

        """Returns all registered tools with descriptions. Returns: dict"""

        return {name: details["description"] for name, details in self.tools.items()}