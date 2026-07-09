"""
===============================================================================
File Name   : openai_service.py
Project     : Enterprise AI ETL Framework
Purpose     : Centralized OpenAI Service with RAG Integration
Author      : Venkata
===============================================================================
"""
from core.config.config import get_openai_client

client = get_openai_client()
from core.logger.logger import logger
from knowledge.rag.rag_pipeline import RAGPipeline


def execute_prompt(prompt_file, output_file):
    """
    Executes Prompt using Enterprise RAG Pipeline.
    """

    try:

        logger.info(f"Reading Prompt : {prompt_file.name}")

        # ------------------------------------------------------------
        # Read Prompt Template
        # ------------------------------------------------------------

        with open(prompt_file, "r", encoding="utf-8") as file:
            prompt_template = file.read()

        # ------------------------------------------------------------
        # RAG Pipeline
        # ------------------------------------------------------------

        logger.info("Retrieving Project Knowledge...")

        rag = RAGPipeline()

        final_prompt = rag.execute(prompt_template)

        # ------------------------------------------------------------
        # OpenAI Call
        # ------------------------------------------------------------

        logger.info("Calling OpenAI...")

        response = client.chat.completions.create(model = "gpt-4o", temperature = 0, messages = [{"role": "user", "content": final_prompt}])

        output = response.choices[0].message.content

        # ------------------------------------------------------------
        # Save Output
        # ------------------------------------------------------------

        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(output)

        logger.info("Output Saved Successfully.")

        return output

    except Exception as error:

        logger.error(f"OpenAI Service Error : {error}")

        raise