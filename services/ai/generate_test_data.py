from core.config.paths import PROMPTS_DIR
from core.config.paths import OUTPUTS_DIR

from services.ai.openai_service import execute_prompt


def generate_test_data():
    return execute_prompt(
        prompt_file=PROMPTS_DIR / "test_data_prompt.txt",
        output_file=OUTPUTS_DIR / "test_data.sql"
    )


if __name__ == "__main__":
    output = generate_test_data()
    print(output)