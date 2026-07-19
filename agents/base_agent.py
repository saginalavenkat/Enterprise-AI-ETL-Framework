"""
===============================================================================
File Name   : base_agent.py
Project     : Enterprise AI ETL Framework
Purpose     : Parent Class for all AI Agents
Author      : Venkata
===============================================================================
"""

from abc import ABC, abstractmethod

from core.logger.logger import logger
from core.config.config import get_openai_client

from knowledge.rag.rag_pipeline import RAGPipeline


class BaseAgent(ABC):
    """
    Base class for all Enterprise AI Agents.

    Responsibilities
    ----------------
    - Retrieve project context using RAG
    - Build final prompt
    - Call GPT
    - Handle GPT failures
    - Return mock response when GPT is unavailable

    Child classes only need to implement execute().
    """

    def __init__(self, agent_name: str, rag_pipeline=None, client=None):

        self.agent_name = agent_name

        self.rag_pipeline = rag_pipeline or RAGPipeline()

        self.client = client or get_openai_client()

        logger.info("%s Initialized.", self.agent_name)

    # ------------------------------------------------------------------
    # Retrieve Context
    # ------------------------------------------------------------------

    def retrieve_context(self, question: str) -> str:

        logger.info("%s : Retrieving Context", self.agent_name)

        return self.rag_pipeline.retrieve_context(question)

    # ------------------------------------------------------------------
    # Build Prompt
    # ------------------------------------------------------------------

    def build_prompt(self, question: str, context) -> str:

        logger.info("Embedding Present: %s", context is not None and context.embedding is not None)

        logger.info("%s : Building Prompt", self.agent_name)

        return self.rag_pipeline.execute(question, embedding=context.embedding, monitor=context.monitor)

    # ------------------------------------------------------------------
    # Ask LLM
    # ------------------------------------------------------------------

    def ask_llm(self, question, context=None):

        logger.info("%s : Calling GPT", self.agent_name)

        # ---------------------------------------------------------
        # Reuse Cached RAG Prompt
        # ---------------------------------------------------------
        if context:

            if context.rag_context is None:

                logger.info("%s : Building Prompt", self.agent_name)

                context.rag_context = self.build_prompt(
                    question,
                    context
                )

            else:

                logger.info(
                    "%s : Using Cached Prompt",
                    self.agent_name
                )

            final_prompt = context.rag_context

        else:

            final_prompt = self.build_prompt(
                question,
                context
            )

        try:

            response = self.client.chat.completions.create(
                model="gpt-4.1",
                messages=[
                    {
                        "role": "user",
                        "content": final_prompt
                    }
                ]
            )

            usage = response.usage

            if context and context.monitor:

                context.monitor.llm_call()

                if usage:
                    context.monitor.update_tokens(
                        usage.total_tokens
                    )

            return response.choices[0].message.content

        except Exception:

            logger.exception(
                "%s : GPT Call Failed.",
                self.agent_name
            )

            logger.warning(
                "%s : Using Mock GPT Response.",
                self.agent_name
            )

            if context and context.monitor:
                context.monitor.llm_call()

            return "Mock Response"

    # ------------------------------------------------------------------
    # Mock Response
    # ------------------------------------------------------------------

    def get_mock_response(self):

        return "Mock Response"

    # ------------------------------------------------------------------
    # Execute
    # ------------------------------------------------------------------

    @abstractmethod
    def execute(self, context):
        """
        Every Business Agent must implement execute().
        """
        pass