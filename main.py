"""
===============================================================================
File Name   : main.py
Project     : Enterprise AI ETL Framework
Purpose     : Framework Entry Point
Author      : Venkata
===============================================================================
"""

from core.logger.logger import logger
from core.monitoring.monitor import FrameworkMonitor
from core.workflows.workflow_manager import WorkflowManager
from integrations.mcp.tool_response import ToolResponse


def main():
    """Starts the Enterprise AI ETL Framework."""

    logger.info("=" * 80)
    logger.info("Enterprise AI ETL Framework Started")
    logger.info("=" * 80)

    monitor = FrameworkMonitor()

    try:

        monitor.start()

        workflow = WorkflowManager()

        # ------------------------------------------------------------
        # User Question
        # ------------------------------------------------------------

        question = "Generate complete ETL testing package for Employee table."

        # Execute Workflow
        context = workflow.execute(question)

        print("\n")
        print("=" * 80)
        print("FINAL RESPONSE")
        print("=" * 80)

        # ------------------------------------------------------------
        # Pretty print SQL result if available
        # ------------------------------------------------------------

        print("\n")
        print("=" * 80)
        print("WORKFLOW CONTEXT")
        print("=" * 80)

        workflow = context.to_dict()

        for key, value in workflow.items():

            print(f"\n{key.upper()}")
            print("-" * 40)

            if key == "query_result" and isinstance(value, ToolResponse):

                value.pretty_print()

            else:

                print(value)

        if context.report_file:
            print("\n")
            print("=" * 80)
            print("DOCUMENTATION REPORT")
            print("=" * 80)
            print(f"Markdown Report : {context.report_file}")

    except Exception as error:

        logger.exception(error)

    finally:

        monitor.stop()
        monitor.save_metrics()
        monitor.display_metrics()

    logger.info("Framework Execution Completed Successfully.")


if __name__ == "__main__":
    main()