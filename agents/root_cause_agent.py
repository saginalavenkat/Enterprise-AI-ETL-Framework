"""
===============================================================================
File Name   : root_cause_agent.py
Project     : Enterprise AI ETL Framework
Purpose     : AI Root Cause Analysis Agent
Author      : Venkata
===============================================================================
"""

from agents.base_agent import BaseAgent


class RootCauseAgent(BaseAgent):
    """
    AI Agent for Root Cause Analysis.
    """

    def __init__(self, rag_pipeline=None):

        super().__init__("Root Cause Agent", rag_pipeline)

    def get_mock_response(self):

        return """ Root Cause Analysis: Source contained duplicate records. ETL job loaded duplicate rows. Deduplication rule missing. """

    def execute(self, question: str):
        return self.ask_llm(question)

