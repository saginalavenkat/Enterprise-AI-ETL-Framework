"""
===============================================================================
File Name   : tool_response.py
Project     : Enterprise AI ETL Framework
Purpose     : MCP Tool Response
Author      : Venkata
===============================================================================
"""


class ToolResponse:

    """Standard response object returned by every Enterprise Tool. Used by: - Database Tool - Jira Tool - Email Tool - File Tool; Provides: - Status - Result - JSON Conversion - Pretty Printing"""

    def __init__(self, status, result):

        self.status = status

        self.result = result

    # ----------------------------------------------------------------

    def is_success(self):

        return self.status.upper() == "SUCCESS"

    # ----------------------------------------------------------------

    def is_failed(self):

        return self.status.upper() == "FAILED"

    # ----------------------------------------------------------------

    def to_dict(self):

        return {"status": self.status, "result": self.result}

    # ----------------------------------------------------------------

    def pretty_print(self):

        print("\n")
        print("=" * 80)
        print("TOOL RESPONSE")
        print("=" * 80)

        print(f"Status : {self.status}")

        if isinstance(self.result, dict):

            for key, value in self.result.items():

                print(f"{key} : {value}")

        else:

            print(self.result)

        print("=" * 80)

    # ----------------------------------------------------------------

    def __str__(self):

        return f"ToolResponse(status={self.status}, result={self.result})"

    # ----------------------------------------------------------------

    def __repr__(self):

        return self.__str__()