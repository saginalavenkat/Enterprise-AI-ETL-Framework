"""
===============================================================================
File Name   : base_tool.py
Project     : Enterprise AI ETL Framework
Purpose     : Base Tool
Author      : Venkata
===============================================================================
"""

from abc import ABC, abstractmethod


class BaseTool(ABC):

    def __init__(self, tool_name):

        self.tool_name = tool_name

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass