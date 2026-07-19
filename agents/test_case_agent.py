"""
===============================================================================
File Name   : test_case_agent.py
Project     : Enterprise AI ETL Framework
Purpose     : AI Test Case Generation Agent
Author      : Venkata
===============================================================================
"""

from agents.base_agent import BaseAgent
from core.logger.logger import logger


class TestCaseAgent(BaseAgent):
    """
    AI Agent responsible for ETL Test Case Generation.
    """

    def __init__(self, rag_pipeline=None, client=None):

        super().__init__(
            agent_name="Test Case Agent",
            rag_pipeline=rag_pipeline,
            client=client
        )

    # ------------------------------------------------------------------

    def execute(self, context):

        logger.info("=" * 80)
        logger.info("Test Case Agent Started.")
        logger.info("=" * 80)

        prompt = f"""
Requirement
{context.requirement}

Mapping
{context.mapping}

Generate comprehensive ETL Test Cases.
"""

        test_cases = self.ask_llm(
            question=prompt,
            context=context
        )

        context.test_cases = test_cases

        logger.info("Test Case Generation Completed.")

        return context