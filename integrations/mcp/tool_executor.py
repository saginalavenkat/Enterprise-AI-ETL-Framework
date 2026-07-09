"""
===============================================================================
File Name   : tool_executor.py
Project     : Enterprise AI ETL Framework
Purpose     : Tool Execution Engine
Author      : Venkata
===============================================================================
"""

from core.logger.logger import logger


class ToolExecutor:

    def __init__(self):

        logger.info("Tool Executor Initialized.")

    # ------------------------------------------------------------

    def execute(self, tool, *args, **kwargs):

        logger.info(f"Executing Tool : {tool.tool_name}")

        return tool.execute(*args, **kwargs)


# ------------------------------------------------------------
# Testing
# ------------------------------------------------------------

if __name__ == "__main__":

    from legacy.sql_tool import SQLTool

    executor = ToolExecutor()

    sql_tool = SQLTool()

    result = executor.execute(sql_tool, "SELECT COUNT(*) FROM CUSTOMER")

    print(result)