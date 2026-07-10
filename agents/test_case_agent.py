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

    def __init__(self, rag_pipeline=None):

        super().__init__("Test Case Agent", rag_pipeline)

    # ------------------------------------------------------------

    def execute(self, context):

        logger.info("Test Case Agent Started.")

        prompt = f"""
Requirement

{context.requirement}

Mapping

{context.mapping}

Generate comprehensive ETL Test Cases.
"""

        test_cases = self.ask_llm(prompt)
        context.metrics.add_tokens(500)
        context.test_cases = test_cases

        logger.info("Test Case Generation Completed.")

        return context


# ------------------------------------------------------------
# Testing
# ------------------------------------------------------------

if __name__ == "__main__":

    from core.workflows.workflow_context import WorkflowContext

    agent = TestCaseAgent()

    context = WorkflowContext("Generate ETL Test Cases")

    context.requirement = "Validate Employee records."

    context.mapping = "EMPLOYEE -> EMPLOYEE"

    context = agent.execute(context)

    print(context.to_dict())