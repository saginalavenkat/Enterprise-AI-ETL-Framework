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
from core.monitoring.monitor import FrameworkMonitor

class WorkflowManager:

    def __init__(self):

        logger.info("Workflow Manager Initialized.")

        self.rag_pipeline = RAGPipeline()

        self.planner = Planner()

        self.agent_registry = AgentRegistry(self.rag_pipeline)

        self.monitor = FrameworkMonitor()
        self.monitor.start()
    # ------------------------------------------------------------

    def execute(self, question):

        logger.info("Workflow Started.")

        from core.workflows.workflow_context import WorkflowContext

        context = WorkflowContext(question)

        plan = self.planner.create_plan(question)

        logger.info("=" * 80)
        logger.info("Execution Plan: %s", plan)
        logger.info("=" * 80)

        print("\nExecution Plan:", plan)

        logger.info("Execution Plan : %s", plan)

        for step in plan:

            agent = self.agent_registry.get_agent(step)

            if agent is None:
                logger.warning("Unknown Agent : %s", step)

                continue

            logger.info("Executing %s Agent", step)
            print(f"Executing Agent -> {step}")

            try:

                context = agent.execute(context)
                self.monitor.service_success()
                self.monitor.update_tokens(500)
                self.monitor.update_cost(0.001)
                #context.metrics.service_success()

            except Exception:

                self.monitor.service_failed()

                raise

        logger.info("Workflow Completed.")

        context.monitor = self.monitor

        return context
# ------------------------------------------------------------
# Testing
# ------------------------------------------------------------

if __name__ == "__main__":

    workflow = WorkflowManager()

    response = workflow.execute("Generate complete ETL Testing package for Employee table.")

    print(response)