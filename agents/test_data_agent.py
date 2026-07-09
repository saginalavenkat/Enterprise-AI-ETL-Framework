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

        test_data = self.ask_llm(prompt)

        context.test_data = test_data

        logger.info("Test Data Generated Successfully.")

        return context


# ------------------------------------------------------------

if __name__ == "__main__":

    from core.workflows.workflow_context import WorkflowContext

    agent = TestDataAgent()

    context = WorkflowContext("Generate Test Data")

    context.requirement = "Employee validation"

    context.mapping = "Employee Mapping"

    context.test_cases = "Validate Salary"

    context = agent.execute(context)

    print(context.to_dict())