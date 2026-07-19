"""
===============================================================================
File Name   : test_data_agent.py
Project     : Enterprise AI ETL Framework
Purpose     : AI Test Data Agent
Author      : Venkata
===============================================================================
"""

from agents.base_agent import BaseAgent
from core.logger.logger import logger


class TestDataAgent(BaseAgent):

    def __init__(self, rag_pipeline=None):

        super().__init__("Test Data Agent", rag_pipeline)

    # ------------------------------------------------------------

    def execute(self, context):

        logger.info("Test Data Agent Started.")

        prompt = f"""
Requirement

{context.requirement}

Mapping

{context.mapping}

Test Cases

{context.test_cases}

Generate ETL Test Data.
"""

        test_data = self.ask_llm(prompt, context)
        context.monitor.update_tokens(500)
        context.test_data = test_data

        logger.info("Test Data Generated Successfully.")

        return context

