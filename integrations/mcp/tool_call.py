"""
===============================================================================
File Name   : tool_call.py
Project     : Enterprise AI ETL Framework
Purpose     : MCP Tool Call
Author      : Venkata
===============================================================================
"""


class ToolCall:

    def __init__(self, tool_name, arguments):

        self.tool_name = tool_name

        self.arguments = arguments

    def __repr__(self):

        return f"ToolCall(tool={self.tool_name}, arguments={self.arguments})"