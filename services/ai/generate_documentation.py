from core.config.paths import PROMPTS_DIR
from core.config.paths import OUTPUTS_DIR

from services.ai.openai_service import execute_prompt


def generate_documentation():
    return execute_prompt(
        prompt_file=PROMPTS_DIR / "documentation_prompt.txt",
        output_file=OUTPUTS_DIR / "documentation.md"
    )


if __name__ == "__main__":
    output = generate_documentation()
    print(output)