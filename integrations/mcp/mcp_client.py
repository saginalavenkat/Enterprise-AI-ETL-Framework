"""
===============================================================================
File Name   : mcp_client.py
Project     : Enterprise AI ETL Framework
Purpose     : MCP Client
Author      : Venkata
===============================================================================
"""

from core.logger.logger import logger

from integrations.mcp.mcp_server import MCPServer


class MCPClient:

    def __init__(self):

        logger.info("Initializing MCP Client...")

        self.server = MCPServer()

    # ------------------------------------------------------------

    def execute(self, tool_call):

        logger.info("Sending Request To MCP Server...")

        response = self.server.execute(tool_call)

        logger.info("Response Received From MCP Server.")

        return response