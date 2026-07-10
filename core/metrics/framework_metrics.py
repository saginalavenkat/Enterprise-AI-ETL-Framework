"""
===============================================================================
Framework Metrics
===============================================================================
"""

import time


class FrameworkMetrics:

    def __init__(self):

        self.start_time = time.time()

        self.services_executed = 0
        self.successful_services = 0
        self.failed_services = 0

        self.tokens_used = 0
        self.estimated_cost = 0.0

    # -------------------------------------------------------

    def service_success(self):

        self.services_executed += 1
        self.successful_services += 1

    # -------------------------------------------------------

    def service_failed(self):

        self.services_executed += 1
        self.failed_services += 1

    # -------------------------------------------------------

    def add_tokens(self, tokens):

        self.tokens_used += tokens

    # -------------------------------------------------------

    def execution_time(self):

        return round(time.time() - self.start_time, 2)