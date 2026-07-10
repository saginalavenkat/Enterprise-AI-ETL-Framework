"""
===============================================================================
File Name   : defect_analysis_agent.py
Project     : Enterprise AI ETL Framework
Purpose     : AI Defect Analysis Agent
Author      : Venkata
===============================================================================
"""

from agents.base_agent import BaseAgent
from core.logger.logger import logger


class DefectAnalysisAgent(BaseAgent):

    """
    AI Agent for ETL Defect Analysis.
    """

    def __init__(self, rag_pipeline=None):

        super().__init__("Defect Analysis Agent", rag_pipeline)

        logger.info("Defect Analysis Agent Initialized.")

    # -----------------------------------------------------------------

    def execute(self, context):

        logger.info("Defect Analysis Agent Started.")

        # ------------------------------------------------------------
        # If validation passed, no defect is created
        # ------------------------------------------------------------

        if context.validation:

            validation_text = str(context.validation).lower()

            if "pass" in validation_text:

                logger.info("Validation Passed. No defect found.")

                context.defect_analysis = None

                return context

        # ------------------------------------------------------------
        # Build Prompt
        # ------------------------------------------------------------

        prompt = f"""
You are an ETL QA Lead.

Requirement:
{context.requirement}

Generated SQL:
{context.generated_sql}

Validation Result:
{context.validation}

Database Result:
{context.query_result}

Generate:

1. Defect Summary

2. Root Cause

3. Severity

4. Priority

5. Recommendation

Return concise enterprise output.
"""

        analysis = self.ask_llm(prompt)
        context.metrics.add_tokens(500)
        # ------------------------------------------------------------
        # Store structured result
        # ------------------------------------------------------------

        context.defect_analysis = {

            "summary": "ETL Validation Failed",

            "description": analysis,

            "severity": "High",

            "priority": "High"

        }

        logger.info("Defect Analysis Completed.")

        return context


# --------------------------------------------------------------------
# Testing
# --------------------------------------------------------------------

if __name__ == "__main__":

    from core.workflows.workflow_context import WorkflowContext

    context = WorkflowContext("Employee Validation")

    context.requirement = "Validate Employee Salary"

    context.generated_sql = (
        "SELECT * FROM EMPLOYEE WHERE SALARY > 90000"
    )

    context.query_result = "2 Records Returned"

    context.validation = "Validation Failed"

    agent = DefectAnalysisAgent()

    context = agent.execute(context)

    print()

    print("=" * 80)

    print("DEFECT ANALYSIS")

    print("=" * 80)

    print(context.to_dict())