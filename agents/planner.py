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


class Planner:
    """Enterprise AI Planner - Creates an execution plan for Workflow Manager. Flow - User Question --> AI Planner --> Execution Plan --> Workflow Manager

    Falls back to rule-based planning if GPT is unavailable."""

    def __init__(self, client=None):

        logger.info("Planner Initialized.")

        self.client = client or get_openai_client()

    # ------------------------------------------------------------------

    def create_plan(self, question: str):

        logger.info("Creating Execution Plan...")

        try:

            plan = self._create_ai_plan(question)

            logger.info("AI Planner Successfully Generated Execution Plan.")

            return plan

        except Exception as ex:

            logger.exception("AI Planner Failed.")

            logger.warning("Using Rule-Based Planner.")

            return self._create_rule_plan(question)

    # ------------------------------------------------------------------

    def _create_ai_plan(self, question: str):

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

Example {{"plan":["sql"]}} User Request {question}"""

        response = self.client.chat.completions.create(
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

        logger.info("Planner Response : %s", content)

        plan = json.loads(content)

        return plan["plan"]

    # ------------------------------------------------------------------

    def _create_rule_plan(self, question: str):

        question = question.lower()

        plan = []

        if any(word in question for word in [
            "requirement",
            "business rule"
        ]):
            plan.append("requirement")

        if any(word in question for word in [
            "mapping",
            "sttm"
        ]):
            plan.append("mapping_analysis")

        if any(word in question for word in [
            "test case",
            "testcase",
            "etl test"
        ]):

            if "requirement" not in plan:
                plan.append("requirement")

            if "mapping_analysis" not in plan:
                plan.append("mapping_analysis")

            if "test_case" not in plan:
                plan.append("test_case")

            if "test_data" not in plan:
                plan.append("test_data")

        if any(word in question for word in [
            "test data",
            "sample data"
        ]):
            plan.append("test_data")

        if any(word in question for word in [
            "sql",
            "query",
            "select",
            "insert",
            "update",
            "delete"
        ]):
            plan.append("sql")

        if any(word in question for word in [
            "validate",
            "validation",
            "verify",
            "check",
            "etl load",
            "snowflake",
            "compare"
        ]):

            if "requirement" not in plan:
                plan.append("requirement")

            if "mapping_analysis" not in plan:
                plan.append("mapping_analysis")

            if "test_case" not in plan:
                plan.append("test_case")

            if "sql" not in plan:
                plan.append("sql")

            plan.append("validation")

        if any(word in question for word in [
            "root cause",
            "rca"
        ]):
            plan.append("root_cause")

        if any(word in question for word in [
            "defect",
            "bug",
            "failure"
        ]):
            plan.append("defect_analysis")

        if "jira" in question:
            plan.append("jira")

        if any(word in question for word in [
            "documentation",
            "document",
            "report"
        ]):
            plan.append("documentation")

        if any(word in question for word in [
            "complete",
            "package",
            "end to end"
        ]):
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

        if not plan:
            plan.append("requirement")

        return list(dict.fromkeys(plan))