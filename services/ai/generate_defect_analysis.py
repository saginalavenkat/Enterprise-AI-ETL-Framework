from core.config.paths import PROMPTS_DIR
from core.config.paths import OUTPUTS_DIR

from services.ai.openai_service import execute_prompt


def generate_defect_analysis():
    return execute_prompt(
        prompt_file=PROMPTS_DIR / "defect_analysis_prompt.txt",
        output_file=OUTPUTS_DIR / "defect_analysis.txt"
    )


if __name__ == "__main__":
    output = generate_defect_analysis()
    print(output)