"""
===============================================================================
File Name   : framework_monitor.py
Project     : Enterprise AI ETL Framework
Purpose     : Monitor Framework Execution
Author      : Venkata
===============================================================================
"""

import json
import time
from pathlib import Path


class FrameworkMonitor:

    def __init__(self):

        self.start_time = None
        self.end_time = None
        self.agent_timings = {}

        self.metrics = {

            # Overall
            "execution_time": 0,

            # Agents
            "agents_executed": 0,
            "successful_agents": 0,
            "failed_agents": 0,

            # AI
            "llm_calls": 0,
            "rag_searches": 0,

            # Integrations
            "database_queries": 0,
            "jira_issues_created": 0,
            "emails_sent": 0,

            # Cost
            "tokens_used": 0,
            "estimated_cost": 0
        }

    def record_agent_time(self, agent_name, execution_time):
        self.agent_timings[agent_name] = execution_time

    # ------------------------------------------------------------
    # Start Monitoring
    # ------------------------------------------------------------

    def start(self):

        self.start_time = time.time()

    # ------------------------------------------------------------
    # Stop Monitoring
    # ------------------------------------------------------------

    def stop(self):

        self.end_time = time.time()

        self.metrics["execution_time"] = round(self.end_time - self.start_time, 2)

    # ------------------------------------------------------------
    # Agent Success
    # ------------------------------------------------------------

    def service_success(self):

        self.metrics["agents_executed"] += 1
        self.metrics["successful_agents"] += 1

    # ------------------------------------------------------------
    # Agent Failure
    # ------------------------------------------------------------

    def service_failed(self):

        self.metrics["agents_executed"] += 1
        self.metrics["failed_agents"] += 1

    # ------------------------------------------------------------
    # LLM Call
    # ------------------------------------------------------------

    def llm_call(self):

        self.metrics["llm_calls"] += 1

    # ------------------------------------------------------------
    # RAG Search
    # ------------------------------------------------------------

    def rag_search(self):

        self.metrics["rag_searches"] += 1

    # ------------------------------------------------------------
    # Database Query
    # ------------------------------------------------------------

    def database_query(self):

        self.metrics["database_queries"] += 1

    # ------------------------------------------------------------
    # Jira Issue
    # ------------------------------------------------------------

    def jira_issue_created(self):

        self.metrics["jira_issues_created"] += 1

    # ------------------------------------------------------------
    # Email Sent
    # ------------------------------------------------------------

    def email_sent(self):

        self.metrics["emails_sent"] += 1

    # ------------------------------------------------------------
    # Token Usage
    # ------------------------------------------------------------

    def update_tokens(self, tokens):

        self.metrics["tokens_used"] += tokens

    # ------------------------------------------------------------
    # Cost
    # ------------------------------------------------------------

    def update_cost(self, cost):

        self.metrics["estimated_cost"] += cost

    # ------------------------------------------------------------
    # Save Metrics
    # ------------------------------------------------------------

    def save_metrics(self):

        base_dir = Path(__file__).resolve().parent.parent

        report_folder = base_dir / "reports"

        report_folder.mkdir(exist_ok=True)

        report_file = report_folder / "metrics.json"

        with open(report_file, "w", encoding="utf-8") as file:

            json.dump(self.metrics, file, indent=4)

    # ------------------------------------------------------------
    # Display Metrics
    # ------------------------------------------------------------

    def display_metrics(self):

        print("\n")
        print("=" * 80)
        print("ENTERPRISE AI ETL FRAMEWORK METRICS")
        print("=" * 80)

        print(f"{'Execution Time':30}: {self.metrics['execution_time']} sec")
        print()

        print("Agent Execution Time")
        print("-" * 80)

        for agent, execution_time in self.agent_timings.items():
            print(f"{agent:<30}: {execution_time:.2f} sec")

        print()

        print(f"{'Agents Executed':30}: {self.metrics['agents_executed']}")
        print(f"{'Successful Agents':30}: {self.metrics['successful_agents']}")
        print(f"{'Failed Agents':30}: {self.metrics['failed_agents']}")
        print()

        print(f"{'LLM Calls':30}: {self.metrics['llm_calls']}")
        print(f"{'RAG Searches':30}: {self.metrics['rag_searches']}")
        print()

        print(f"{'Database Queries':30}: {self.metrics['database_queries']}")
        print(f"{'Jira Issues Created':30}: {self.metrics['jira_issues_created']}")
        print(f"{'Emails Sent':30}: {self.metrics['emails_sent']}")
        print()

        print(f"{'Tokens Used':30}: {self.metrics['tokens_used']}")
        print(f"{'Estimated Cost ($)':30}: {round(self.metrics['estimated_cost'], 6)}")

        print("=" * 80)