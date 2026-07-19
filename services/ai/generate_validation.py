from core.config.paths import PROMPTS_DIR
from core.config.paths import OUTPUTS_DIR

from services.ai.openai_service import execute_prompt


def generate_validation():
    return execute_prompt(prompt_file=PROMPTS_DIR / "validation_prompt.txt", output_file=OUTPUTS_DIR / "validation_report.txt")

