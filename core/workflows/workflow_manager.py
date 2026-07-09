"""
===============================================================================
File Name   : workflow_manager.py
Project     : Enterprise AI ETL Framework
Purpose     : Enterprise Workflow Manager
Author      : Venkata
===============================================================================
"""

from core.logger.logger import logger

from agents.planner import Planner
from knowledge.rag.rag_pipeline import RAGPipeline
from agents.agent_registry import AgentRegistry


class WorkflowManager:

    def __init__(self):

        logger.info("Workflow Manager Initialized.")

        self.rag_pipeline = RAGPipeline()

        self.planner = Planner()

        self.agent_registry = AgentRegistry(self.rag_pipeline)

    # ------------------------------------------------------------

    def execute(self, question):

        logger.info("Workflow Started.")

        from core.workflows.workflow_context import WorkflowContext

        context = WorkflowContext(question)

        plan = self.planner.create_plan(question)

        logger.info("Execution Plan : %s", plan)

        for step in plan:

            agent = self.agent_registry.get_agent(step)

            if agent is None:
                logger.warning("Unknown Agent : %s", step)

                continue

            logger.info("Executing %s Agent", step)

            context = agent.execute(context)

        logger.info("Workflow Completed.")

        return context
# ------------------------------------------------------------
# Testing
# ------------------------------------------------------------

if __name__ == "__main__":

    workflow = WorkflowManager()

    response = workflow.execute("Generate complete ETL Testing package for Employee table.")

    print(response)