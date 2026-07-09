from core.config.paths import PROMPTS_DIR
from core.config.paths import OUTPUTS_DIR
from services.ai.openai_service import execute_prompt


def generate_sql():
    return execute_prompt(prompt_file = PROMPTS_DIR / "sql_prompt.txt", output_file = OUTPUTS_DIR / "validation.sql")