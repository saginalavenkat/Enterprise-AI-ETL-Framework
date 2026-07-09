"""
===============================================================================
File Name   : multi_agent_orchestrator.py
Project     : Enterprise AI ETL Framework
Purpose     : Enterprise Multi-Agent Orchestrator
Author      : Venkata
===============================================================================
"""

from core.logger.logger import logger

from knowledge.rag import RAGPipeline

from agents.requirement_agent import RequirementAgent
from agents.test_case_agent import TestCaseAgent
from agents.sql_agent import SQLAgent
from agents.validation_agent import ValidationAgent
from agents.documentation_agent import DocumentationAgent

from agents.planner import Planner

from legacy.tool_manager import ToolManager
from legacy.tool_selector import ToolSelector

class MultiAgentOrchestrator:

    def __init__(self):

        logger.info("=" * 80)
        logger.info("Initializing Multi-Agent Orchestrator")
        logger.info("=" * 80)

        self.rag_pipeline = RAGPipeline()

        self.planner = Planner()                                                  # to connect planner

        self.tool_manager = ToolManager()

        self.tool_selector = ToolSelector()

        self.requirement_agent = RequirementAgent(self.rag_pipeline)

        self.test_case_agent = TestCaseAgent(self.rag_pipeline)

        self.sql_agent = SQLAgent(self.rag_pipeline)

        self.validation_agent = ValidationAgent(self.rag_pipeline)

        self.documentation_agent = DocumentationAgent(self.rag_pipeline)

    # ------------------------------------------------------------

    def execute(self, question: str):

        logger.info("Starting Multi-Agent Workflow...")

        plan = self.planner.create_plan(question)

        logger.info("=" * 80)
        logger.info("Execution Plan")
        logger.info(plan)
        logger.info("=" * 80)

        results = {}

        # Initialize shared variables

        requirements = ""
        test_cases = ""
        sql = ""
        validation = ""
        documentation = ""

        for step in plan:

            # -----------------------------------------------------------------
            # Step 1 : Requirement Agent
            # -----------------------------------------------------------------

            if step == "requirement":

                logger.info("Executing Requirement Agent...")

                requirements = self.requirement_agent.execute("Explain all business requirements from project documents.")

                results["requirements"] = requirements

            # -----------------------------------------------------------------
            # Step 2 : Test Case Agent
            # -----------------------------------------------------------------

            elif step == "test_case":

                logger.info("Executing Test Case Agent...")

                test_case_question = f"""Business Requirements {requirements} Generate comprehensive ETL Test Cases."""

                test_cases = self.test_case_agent.execute(test_case_question)

                results["test_cases"] = test_cases

            # -----------------------------------------------------------------
            # Step 3 : SQL Agent
            # -----------------------------------------------------------------

            elif step == "sql":

                logger.info("Executing SQL Agent...")

                sql_question = f"""Business Requirements {requirements} ETL Test Cases {test_cases} Generate SQL Validation Queries."""

                sql = self.sql_agent.execute(sql_question)

                results["sql"] = sql

            # -----------------------------------------------------------------
            # Step 4 : Validation Agent
            # -----------------------------------------------------------------

            elif step == "validation":

                logger.info("Executing Validation Agent...")

                validation_question = f"""Business Requirements {requirements} ETL Test Cases {test_cases} SQL Validation {sql} Generate Validation Checklist."""

                validation = self.validation_agent.execute(validation_question)

                results["validation"] = validation

            # -----------------------------------------------------------------
            # Step 5 : Documentation Agent
            # -----------------------------------------------------------------

            elif step == "documentation":

                logger.info("Executing Documentation Agent...")

                documentation_question = f"""Business Requirements  {requirements} ETL Test Cases {test_cases} SQL Validation {sql} Validation Checklist {validation} Generate Final ETL Testing Documentation."""

                documentation = self.documentation_agent.execute(documentation_question)

                results["documentation"] = documentation

        logger.info("Multi-Agent Workflow Completed.")
        logger.info(f"Total Agents Executed : {len(results)}")

        return results

# ------------------------------------------------------------
# Testing
# ------------------------------------------------------------

if __name__ == "__main__":

    orchestrator = MultiAgentOrchestrator()

    output = orchestrator.execute("Generate Complete ETL Testing Package")

    print("\n")

    for section, response in output.items():

        print("=" * 80)

        print(section.upper())

        print("=" * 80)

        print(response)