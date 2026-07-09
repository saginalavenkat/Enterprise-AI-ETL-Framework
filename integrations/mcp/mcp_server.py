"""
===============================================================================
File Name   : mcp_server.py
Project     : Enterprise AI ETL Framework
Purpose     : MCP Server
Author      : Venkata
===============================================================================
"""

from core.logger.logger import logger

from integrations.mcp.mcp_router import MCPRouter
from integrations.mcp.tool_registry import ToolRegistry


class MCPServer:

    def __init__(self):

        logger.info("Initializing MCP Server...")

        self.registry = ToolRegistry()

        self.router = MCPRouter(self.registry)

    # ------------------------------------------------------------

    def execute(self, tool_call):

        logger.info("MCP Server Executing Tool...")

        # Execute ONLY ONCE

        result = self.router.route(tool_call)

        logger.info("MCP Tool Executed Successfully.")

        return result