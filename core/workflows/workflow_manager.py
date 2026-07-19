"""
===============================================================================
File Name   : workflow_manager.py
Project     : Enterprise AI ETL Framework
Purpose     : Enterprise Workflow Manager
Author      : Venkata
===============================================================================
"""
from reporting.report_generator import ReportGenerator
from datetime import time
import time

from core.logger.logger import logger

from agents.planner import Planner
from agents.agent_registry import AgentRegistry

from knowledge.rag.rag_pipeline import RAGPipeline

from core.workflows.workflow_context import WorkflowContext
from core.monitoring.framework_monitor import FrameworkMonitor

from integrations.mcp.mcp_client import MCPClient


class WorkflowManager:

    def __init__(
            self,
            rag_pipeline=None,
            planner=None,
            agent_registry=None,
            monitor=None,
            mcp_client=None
    ):

        logger.info("Workflow Manager Initialized.")

        self.rag_pipeline = rag_pipeline or RAGPipeline()

        self.planner = planner or Planner()

        self.monitor = monitor or FrameworkMonitor()

        self.report_generator = ReportGenerator()

        # ----------------------------------------------------------
        # Shared MCP Client
        # ----------------------------------------------------------

        self.mcp_client = mcp_client or MCPClient()

        self.agent_registry = agent_registry or AgentRegistry(rag_pipeline=self.rag_pipeline, mcp_client=self.mcp_client)

    # ------------------------------------------------------------------

    def execute(self, question):

        logger.info("=" * 80)
        logger.info("Workflow Started.")
        logger.info("=" * 80)

        self.monitor.start()

        context = WorkflowContext(question=question, monitor=self.monitor)

        try:

            # ----------------------------------------------------------
            # Generate Workflow Embedding (Only Once)
            # ----------------------------------------------------------

            try:

                logger.info("Generating Workflow Embedding...")

                context.embedding = self.rag_pipeline.get_embedding(question)

                logger.info("Workflow Embedding Generated Successfully.")

            except Exception:

                logger.exception("Workflow Embedding Generation Failed.")

            # ----------------------------------------------------------
            # Create Execution Plan
            # ----------------------------------------------------------

            plan = self.planner.create_plan(question)

            context.execution_plan = plan

            logger.info("=" * 80)
            logger.info("Execution Plan : %s", plan)
            logger.info("=" * 80)

            print("\nExecution Plan:", plan)

            # ----------------------------------------------------------
            # Execute Agents
            # ----------------------------------------------------------

            for step in plan:

                context.current_agent = step

                agent = self.agent_registry.get_agent(step)

                if agent is None:
                    logger.warning("Unknown Agent : %s", step)

                    context.errors.append(f"Unknown Agent : {step}")

                    continue

                logger.info("Executing Agent : %s", step)

                print(f"Executing Agent -> {step}")

                try:

                    # ----------------------------------------------
                    # Start Agent Timer
                    # ----------------------------------------------

                    start_time = time.time()

                    context = agent.execute(context)

                    # ----------------------------------------------
                    # Stop Agent Timer
                    # ----------------------------------------------

                    end_time = time.time()

                    execution_time = round(end_time - start_time, 2)

                    context.monitor.record_agent_time(step, execution_time)

                    context.monitor.service_success()

                except Exception as ex:

                    # ----------------------------------------------
                    # Record Time Even If Agent Fails
                    # ----------------------------------------------

                    start_time = time.time()
                    end_time = time.time()

                    execution_time = round(end_time - start_time, 2)

                    context.monitor.record_agent_time(step, execution_time)

                    logger.exception("Error while executing %s Agent", step)

                    context.errors.append(str(ex))

                    context.monitor.service_failed()

                    raise

            logger.info("Workflow Completed Successfully.")

            # ----------------------------------------------------------
            # Generate Execution Report
            # ----------------------------------------------------------

            context.report_file = self.report_generator.generate(context)

            # ----------------------------------------------------------
            # Email reports AFTER execution report is created
            # ----------------------------------------------------------

            documentation_agent = self.agent_registry.get_agent("documentation")

            documentation_agent.send_reports(context)

            return context

        finally:

            self.monitor.stop()

            self.monitor.save_metrics()

            self.monitor.display_metrics()

            logger.info("=" * 80)
            logger.info("Workflow Finished.")
            logger.info("=" * 80)