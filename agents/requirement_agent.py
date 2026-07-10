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
    AI Agent for Requirement Analysis.
    """

    def __init__(self, rag_pipeline=None):

        super().__init__("Requirement Agent", rag_pipeline)

    # ------------------------------------------------------------

    def execute(self, context):

        logger.info("Requirement Agent Started.")

        requirement = self.ask_llm(context.question)
        context.metrics.add_tokens(500)
        context.requirement = requirement

        logger.info("Requirement Analysis Completed.")

        return context


# ------------------------------------------------------------
# Testing
# ------------------------------------------------------------

if __name__ == "__main__":

    from core.workflows.workflow_context import WorkflowContext

    agent = RequirementAgent()

    context = WorkflowContext(
        "Show employees working in IT department earning above 90000."
    )

    context = agent.execute(context)

    print(context.to_dict())