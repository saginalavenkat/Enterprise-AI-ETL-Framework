"""
class FrameworkMonitor:

    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.metrics = {"execution_time": 0, "services_executed": 0, "successful_services": 0, "failed_services": 0, "tokens_used": 0, "estimated_cost": 0}

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()
        self.metrics["execution_time"] = round(self.end_time - self.start_time, 2)

    def service_success(self):
        self.metrics["services_executed"] += 1
        self.metrics["successful_services"] += 1

    def service_failed(self):
        self.metrics["services_executed"] += 1
        self.metrics["failed_services"] += 1

    def update_tokens(self, tokens):
        self.metrics["tokens_used"] += tokens

    def update_cost(self, cost):
        self.metrics["estimated_cost"] += cost

    def save_metrics(self):
        BASE_DIR = Path(__file__).resolve().parent.parent
        report_folder = BASE_DIR / "reports"
        report_folder.mkdir(exist_ok=True)
        report_file = report_folder / "metrics.json"
        with open(report_file, "w", encoding="utf-8") as file:
            json.dump(self.metrics, file, indent=4)

    def display_metrics(self):
        print("\n")
        print("=" * 80)
        print("FRAMEWORK METRICS")
        print("=" * 80)

        for key, value in self.metrics.items():
            print(f"{key:25} : {value}")
"""


"""
===============================================================================
File Name   : monitor.py
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

        self.metrics = {
            "execution_time": 0,
            "services_executed": 0,
            "successful_services": 0,
            "failed_services": 0,
            "tokens_used": 0,
            "estimated_cost": 0
        }

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
    # Success
    # ------------------------------------------------------------

    def service_success(self):

        self.metrics["services_executed"] += 1

        self.metrics["successful_services"] += 1

    # ------------------------------------------------------------
    # Failure
    # ------------------------------------------------------------

    def service_failed(self):

        self.metrics["services_executed"] += 1

        self.metrics["failed_services"] += 1

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

        BASE_DIR = Path(__file__).resolve().parent.parent

        report_folder = BASE_DIR / "reports"

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
        print("FRAMEWORK METRICS")
        print("=" * 80)

        for key, value in self.metrics.items():

            print(f"{key:25} : {value}")