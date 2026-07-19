"""
===============================================================================
File Name   : requirement_agent.py
Project     : Enterprise AI ETL Framework
Purpose     : AI Requirement Agent
Author      : Venkata
===============================================================================
"""

from agents.base_agent import BaseAgent
from core.logger.logger import logger


class RequirementAgent(BaseAgent):
    """
    AI Agent responsible for Requirement Analysis.
    """

    def __init__(self, rag_pipeline=None, client=None):

        super().__init__(agent_name="Requirement Agent", rag_pipeline=rag_pipeline, client=client)

    # ------------------------------------------------------------------

    def execute(self, context):

        logger.info("=" * 80)
        logger.info("Requirement Agent Started.")
        logger.info("=" * 80)

        requirement = self.ask_llm(question=context.question, context=context)

        context.requirement = requirement

        logger.info("Requirement Analysis Completed.")

        return context