"""
===============================================================================
File Name   : mapping_analysis_agent.py
Project     : Enterprise AI ETL Framework
Purpose     : AI Mapping Analysis Agent
Author      : Venkata
===============================================================================
"""

from agents.base_agent import BaseAgent
from core.logger.logger import logger


class MappingAnalysisAgent(BaseAgent):

    def __init__(self, rag_pipeline=None):

        super().__init__("Mapping Analysis Agent", rag_pipeline)

    # ------------------------------------------------------------

    def execute(self, context):

        logger.info("Mapping Analysis Agent Started.")

        prompt = f"""
Business Requirement

{context.requirement}

Analyze the mapping document and identify:

- Source Tables
- Target Tables
- Column Mapping
- Business Rules
"""

        mapping = self.ask_llm(prompt)
        context.metrics.add_tokens(500)
        context.mapping = mapping

        logger.info("Mapping Analysis Completed.")

        return context


# ------------------------------------------------------------
# Testing
# ------------------------------------------------------------

if __name__ == "__main__":

    from core.workflows.workflow_context import WorkflowContext

    agent = MappingAnalysisAgent()

    context = WorkflowContext("Generate Mapping")

    context.requirement = "Employee data should be validated."

    context = agent.execute(context)

    print(context.to_dict())