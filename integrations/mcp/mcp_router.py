"""
===============================================================================
File Name   : mcp_router.py
Project     : Enterprise AI ETL Framework
Purpose     : MCP Router
Author      : Venkata
===============================================================================
"""

from core.logger.logger import logger


class MCPRouter:

    def __init__(self, tool_registry):

        self.tool_registry = tool_registry

    # ------------------------------------------------------------

    def route(self, tool_call):

        logger.info(f"Routing Tool : {tool_call.tool_name}")

        tool = self.tool_registry.get_tool(tool_call.tool_name)

        if tool is None:

            raise Exception(f"Tool '{tool_call.tool_name}' not found.")

        return tool.execute(**tool_call.arguments)