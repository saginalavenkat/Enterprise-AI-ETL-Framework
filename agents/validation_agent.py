"""
===============================================================================
File Name   : validation_agent.py
Project     : Enterprise AI ETL Framework
Purpose     : AI Validation Agent
Author      : Venkata
===============================================================================
"""

from agents.base_agent import BaseAgent
from core.logger.logger import logger


class ValidationAgent(BaseAgent):
    """
    AI Agent responsible for ETL Validation Summary Generation.
    """

    def __init__(self, rag_pipeline=None, client=None):

        super().__init__(agent_name="Validation Agent", rag_pipeline=rag_pipeline, client=client)

    # ------------------------------------------------------------------
    # Execute
    # ------------------------------------------------------------------

    def execute(self, context):

        logger.info("=" * 80)
        logger.info("Validation Agent Started.")
        logger.info("=" * 80)

        prompt = f"""
Requirement
{context.requirement}

Generated SQL
{context.generated_sql}

Database Result
{context.query_result}

Generate a comprehensive ETL Validation Summary including:

1. Data Validation Results
2. Record Count Validation
3. Schema Validation
4. Business Rule Validation
5. Data Quality Issues
6. Overall Validation Status
"""

        validation = self.ask_llm(question=prompt, context=context)

        context.validation = validation

        logger.info("Validation Completed Successfully.")

        return context