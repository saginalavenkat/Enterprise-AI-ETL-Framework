"""
===============================================================================
File Name   : database_tool.py
Project     : Enterprise AI ETL Framework
Purpose     : Generic Database Tool
Author      : Venkata
===============================================================================
"""

import time

from core.logger.logger import logger
from tools.base_tool import BaseTool
from integrations.mcp.tool_response import ToolResponse
from services.integrations.database_service import DatabaseService


class DatabaseTool(BaseTool):

    def __init__(self):

        super().__init__("Database Tool")

        logger.info("Database Tool Initialized.")

        self.database_service = DatabaseService()

    # ----------------------------------------------------------------

    def execute(self, database, query, monitor=None):

        logger.info(f"Executing Query on {database}")

        start_time = time.time()

        try:

            rows = self.database_service.execute_query(database, query, monitor)

            execution_time = round(time.time() - start_time, 2)

            response = ToolResponse(status="SUCCESS", result={"database": database, "query": query, "row_count": len(rows), "execution_time": f"{execution_time} sec", "sample_rows": rows[:5]})

            logger.info("Query Returned %s Row(s) in %s sec", len(rows), execution_time)

            return response

        except Exception as e:

            logger.exception("Database Execution Failed.")

            return ToolResponse(status="FAILED", result={"database": database, "query": query, "error": str(e)})