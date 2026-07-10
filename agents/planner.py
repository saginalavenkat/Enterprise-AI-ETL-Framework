"""
===============================================================================
File Name   : planner.py
Project     : Enterprise AI ETL Framework
Purpose     : AI Planner
Author      : Venkata
===============================================================================
"""

import json

from core.logger.logger import logger
from core.config import get_openai_client

client = get_openai_client()


class Planner:
    """
    Creates an execution plan for the Workflow Manager.

    Execution Flow

    User Question
          │
          ▼
      AI Planner
          │
          ▼
    Execution Plan (JSON)
          │
          ▼
    Workflow Manager

    If GPT is unavailable, falls back to rule-based planning.
    """

    def __init__(self):

        logger.info("Planner Initialized.")

    # -----------------------------------------------------------------

    def create_plan(self, question: str):

        logger.info("Creating Execution Plan...")

        try:

            return self._create_ai_plan(question)

        except Exception as ex:

            logger.warning(f"Planner GPT Failed : {ex}")
            logger.warning("Using Rule Based Planner")

            return self._create_rule_plan(question)

    # -----------------------------------------------------------------

    def _create_ai_plan(self, question):

        prompt = f"""
You are an Enterprise ETL Workflow Planner.

Available Agents

- requirement
- mapping_analysis
- test_case
- test_data
- sql
- validation
- documentation
- root_cause
- defect_analysis
- jira

Return ONLY JSON.

Example

Question:
Generate SQL for Employee table

Output

{{"plan":["sql"]}}

Question

{question}
"""

        response = client.chat.completions.create(
            model="gpt-4o",
            temperature=0,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        content = response.choices[0].message.content.strip()

        logger.info(f"Planner Response : {content}")

        plan = json.loads(content)

        return plan["plan"]

    # -----------------------------------------------------------------

    def _create_rule_plan(self, question):

        question = question.lower()

        plan = []

        # ---------------------------------------------------------
        # Requirement
        # ---------------------------------------------------------

        if any(word in question for word in [
            "requirement",
            "business rule"
        ]):
            plan.append("requirement")

        # ---------------------------------------------------------
        # Mapping
        # ---------------------------------------------------------

        if any(word in question for word in [
            "mapping",
            "sttm"
        ]):
            plan.append("mapping_analysis")

        # ---------------------------------------------------------
        # Test Cases
        # ---------------------------------------------------------

        if any(word in question for word in [
            "test case",
            "testcase",
            "etl test"
        ]):
            if "requirement" not in plan:
                plan.append("requirement")

            plan.append("test_case")

        # ---------------------------------------------------------
        # Test Data
        # ---------------------------------------------------------

        if any(word in question for word in [
            "test data",
            "sample data"
        ]):
            plan.append("test_data")

        # ---------------------------------------------------------
        # SQL
        # ---------------------------------------------------------

        if any(word in question for word in [
            "sql",
            "query",
            "select",
            "insert",
            "update",
            "delete"
        ]):
            plan.append("sql")

        # ---------------------------------------------------------
        # Validation
        # ---------------------------------------------------------

        if any(word in question for word in [
            "validate",
            "validation",
            "verify",
            "check",
            "etl load",
            "snowflake",
            "compare"
        ]):

            if "sql" not in plan:
                plan.append("sql")

            plan.append("validation")

        # ---------------------------------------------------------
        # Root Cause
        # ---------------------------------------------------------

        if any(word in question for word in [
            "root cause",
            "rca"
        ]):
            plan.append("root_cause")

        # ---------------------------------------------------------
        # Defect Analysis
        # ---------------------------------------------------------

        if any(word in question for word in [
            "defect",
            "bug",
            "failure"
        ]):
            plan.append("defect_analysis")

        # ---------------------------------------------------------
        # Jira
        # ---------------------------------------------------------

        if "jira" in question:
            plan.append("jira")

        # ---------------------------------------------------------
        # Documentation
        # ---------------------------------------------------------

        if any(word in question for word in [
            "documentation",
            "document",
            "report"
        ]):
            plan.append("documentation")

        # ---------------------------------------------------------
        # Complete Workflow Detection
        # ---------------------------------------------------------

        if "complete" in question or "package" in question or "end to end" in question:
            return [
                "requirement",
                "mapping_analysis",
                "test_case",
                "test_data",
                "sql",
                "validation",
                "defect_analysis",
                "jira",
                "documentation"
            ]

        # ---------------------------------------------------------
        # Intelligent Default
        # ---------------------------------------------------------

        if not plan:
            plan.append("requirement")

        # Remove duplicates while preserving order
        return list(dict.fromkeys(plan))


# -----------------------------------------------------------------
# Testing
# -----------------------------------------------------------------

if __name__ == "__main__":

    planner = Planner()

    questions = [

        "Generate SQL for Employee table",

        "Show employees working in IT department earning above 90000",

        "Generate ETL Test Cases",

        "Validate Employee Data",

        "Analyze Mapping Document",

        "Perform Root Cause Analysis",

        "Create Defect Analysis",

        "Generate Complete ETL Testing Package"
    ]

    for question in questions:

        print("\nQuestion :", question)

        print("Plan     :", planner.create_plan(question))