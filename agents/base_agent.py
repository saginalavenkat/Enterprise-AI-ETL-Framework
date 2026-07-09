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
from knowledge.rag.rag_pipeline import RAGPipeline
from core.config.config import client


class BaseAgent(ABC):
    """
    Base class for all AI Agents.
    Every AI Agent inherits from this class.
    """

    def __init__(self, agent_name, rag_pipeline=None):

        self.agent_name = agent_name

        if rag_pipeline is None:
            self.rag_pipeline = RAGPipeline()
        else:
            self.rag_pipeline = rag_pipeline

        logger.info(f"{self.agent_name} Initialized.")

    # -----------------------------------------------------------------

    def retrieve_context(self, question: str) -> str:
        """
        Retrieves project context using RAG.
        """

        logger.info(f"{self.agent_name} : Retrieving Context")

        return self.rag_pipeline.retrieve_context(question)

    # -----------------------------------------------------------------

    def build_prompt(self, question: str) -> str:
        """
        Builds final prompt using RAG.
        """

        logger.info(f"{self.agent_name} : Building Prompt")

        return self.rag_pipeline.execute(question)

    # -----------------------------------------------------------------

    def ask_llm(self, question: str) -> str:
        """
        Sends the RAG prompt to GPT.
        """

        logger.info(f"{self.agent_name} : Calling GPT")

        final_prompt = self.build_prompt(question)

        try:

            response = client.chat.completions.create(model = "gpt-4o", temperature = 0, messages = [{"role": "user", "content": final_prompt}])

            return response.choices[0].message.content

        except Exception as error:

            logger.warning(f"GPT Call Failed : {error}")
            logger.warning("Using Mock GPT Response")

            return self.get_mock_response()

    # -----------------------------------------------------------------

    def get_mock_response(self):
        """
        Default mock response.
        Child agents should override this method if needed.
        """

        return "Mock Response"

    # -----------------------------------------------------------------

    @abstractmethod
    def execute(self, question: str):
        """
        Every child Agent MUST implement execute().
        """
        pass