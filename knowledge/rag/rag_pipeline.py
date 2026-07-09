"""
===============================================================================
File Name   : rag_pipeline.py
Project     : Enterprise AI ETL Framework
Purpose     : Enterprise RAG Pipeline
Author      : Venkata
===============================================================================
"""

from core.logger.logger import logger

from knowledge.rag.embeddings import EmbeddingGenerator
from knowledge.rag.retriever import Retriever
from integrations.vectordb.chroma_db import ChromaVectorDB


class RAGPipeline:
    """
    Enterprise RAG Pipeline

    Flow

    Question
        ↓
    Embedding
        ↓
    Retriever
        ↓
    ChromaDB
        ↓
    Context
        ↓
    Final Prompt
    """

    def __init__(self):

        self.embedding_generator = EmbeddingGenerator()

        self.vector_db = ChromaVectorDB()

        self.retriever = Retriever(self.vector_db)

    # ------------------------------------------------------------

    def retrieve_context(self, question):

        logger.info("Retrieving Context...")

        try:

            embedding = self.embedding_generator.generate_embedding(question)

        except Exception:

            logger.warning("Using Mock Query Embedding")

            embedding = [0.1] * 1536

        results = self.retriever.retrieve(embedding)

        documents = results.get("documents", [[]])[0]

        context = "\n\n".join(documents)

        logger.info("Context Retrieved Successfully.")

        return context

    # ------------------------------------------------------------

    def build_prompt(self, question, context):

        logger.info("Building Final Prompt...")

        prompt = f"""You are an ETL Testing Expert. Project Context {context} ---------------------------------------- User Request {question} Provide a detailed enterprise-level response."""

        return prompt

    # ------------------------------------------------------------

    def execute(self, question):

        context = self.retrieve_context(question)

        final_prompt = self.build_prompt(question, context)

        return final_prompt

# Testing

if __name__ == "__main__":

    rag = RAGPipeline()

    question = "Generate ETL Test Cases for Customer Mapping"

    prompt = rag.execute(question)

    print(prompt)