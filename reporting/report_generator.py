"""
===============================================================================
File Name   : report_generator.py
Project     : Enterprise AI ETL Framework
Purpose     : Generate Enterprise Execution Report
Author      : Venkata
===============================================================================
"""

from pathlib import Path
from datetime import datetime


class ReportGenerator:

    def generate(self, context):

        base_dir = Path(__file__).resolve().parent.parent

        report_folder = (
            base_dir /
            "reports" /
            "execution_reports"
        )

        report_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        report_file = (
            report_folder /
            f"Execution_Report_{timestamp}.md"
        )

        with open(
                report_file,
                "w",
                encoding="utf-8"
        ) as file:

            file.write("# Enterprise AI ETL Framework\n\n")

            file.write("## Execution Summary\n\n")

            file.write(
                f"- **Question:** {context.question}\n"
            )

            file.write(
                f"- **Execution Time:** "
                f"{context.monitor.metrics['execution_time']} sec\n"
            )

            file.write(
                f"- **Workflow Status:** SUCCESS\n\n"
            )

            # --------------------------------------------------

            file.write("## Execution Plan\n\n")

            for index, agent in enumerate(
                    context.execution_plan,
                    start=1
            ):
                file.write(
                    f"{index}. {agent}\n"
                )

            file.write("\n")

            # --------------------------------------------------

            file.write("## Agent Execution Time\n\n")

            for agent, timing in (
                    context.monitor.agent_timings.items()
            ):
                file.write(
                    f"- {agent} : {timing:.2f} sec\n"
                )

            file.write("\n")

            # --------------------------------------------------

            file.write("## Generated SQL\n\n")

            file.write("```sql\n")

            file.write(
                f"{context.generated_sql}\n"
            )

            file.write("```\n\n")

            # --------------------------------------------------

            file.write("## Query Result\n\n")

            if context.query_result:
                result = context.query_result.result

                file.write(
                    f"Database : {result['database']}\n"
                )

                file.write(
                    f"Rows Returned : {result['row_count']}\n"
                )

                file.write(
                    f"Execution Time : {result['execution_time']}\n\n"
                )

                file.write("Sample Rows\n\n")

                file.write("```text\n")

                file.write(
                    str(result["sample_rows"])
                )

                file.write("\n```\n")

            file.write(
                f"{context.validation}\n\n"
            )

            # --------------------------------------------------

            file.write("## Defect Analysis\n\n")

            file.write(
                f"{context.defect_analysis}\n\n"
            )

            # --------------------------------------------------

            file.write("## Jira Issue\n\n")

            file.write(
                f"{context.jira_issue}\n\n"
            )

            # --------------------------------------------------

            file.write("## Documentation\n\n")

            file.write(
                f"{context.documentation}\n\n"
            )

            # --------------------------------------------------

            file.write("## Framework Metrics\n\n")

            metrics = context.monitor.metrics

            for key, value in metrics.items():

                file.write(
                    f"- {key} : {value}\n"
                )

            file.write("\n")

            # --------------------------------------------------
            # --------------------------------------------------

            file.write("## Query Result\n\n")

            if context.query_result:

                result = context.query_result.result

                file.write(
                    f"Database : {result.get('database')}\n"
                )

                file.write(
                    f"Rows Returned : {result.get('row_count')}\n"
                )

                file.write(
                    f"Execution Time : {result.get('execution_time')}\n\n"
                )

                file.write("Sample Rows\n\n")

                file.write("```text\n")

                file.write(
                    str(result.get("sample_rows"))
                )

                file.write("\n```\n\n")

            else:

                file.write(
                    "No Query Result\n\n"
                )

            # --------------------------------------------------

            file.write("## Errors\n\n")

            if context.errors:

                for error in context.errors:

                    file.write(
                        f"- {error}\n"
                    )

            else:

                file.write(
                    "No Errors.\n"
                )

        context.report_file = str(report_file)

        print("\nExecution Report Generated")

        print(report_file)

        return report_file