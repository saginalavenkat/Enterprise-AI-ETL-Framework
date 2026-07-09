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

    def __init__(self, rag_pipeline=None):

        super().__init__("Validation Agent", rag_pipeline)

    # ------------------------------------------------------------

    def execute(self, context):

        logger.info("Validation Agent Started.")

        prompt = f""" Requirement {context.requirement} Generated SQL {context.generated_sql} Database Result {context.query_result} Generate Validation Summary."""

        validation = self.ask_llm(prompt)

        context.validation = validation

        logger.info("Validation Completed.")

        return context


# ------------------------------------------------------------

if __name__ == "__main__":

    from core.workflows.workflow_context import WorkflowContext

    agent = ValidationAgent()

    context = WorkflowContext("Validation")

    context.generated_sql = "SELECT * FROM EMPLOYEE"

    context.query_result = "10 Rows"

    context = agent.execute(context)

    print(context.to_dict())
