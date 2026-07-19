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
from resources.vector_db.chroma_db import ChromaVectorDB


class RAGPipeline:

    """Enterprise Retrieval Augmented Generation (RAG) Pipeline - Flow -

        User Question --> Embedding Generator --> Vector Database --> Retriever --> Retrieved Context --> Prompt Builder --> Final Prompt"""

    MOCK_EMBEDDING_DIMENSION = 1536

    def __init__(self, embedding_generator=None, vector_db=None, retriever=None):

        logger.info("Initializing RAG Pipeline...")

        self.embedding_generator = embedding_generator or EmbeddingGenerator()

        self.vector_db = vector_db or ChromaVectorDB()

        self.retriever = retriever or Retriever(self.vector_db)

    def get_embedding(self, question):

        try:
            return self.embedding_generator.generate_embedding(question)

        except Exception:

            logger.exception("Embedding Generation Failed.")

            logger.warning("Using Mock Workflow Embedding.")

            return [0.0] * self.MOCK_EMBEDDING_DIMENSION

    # ------------------------------------------------------------------
    # Retrieve Context
    # ------------------------------------------------------------------

    def retrieve_context(self, question: str, embedding=None) -> str:

        logger.info("Retrieving Context...")

        try:

            if embedding is None:
                logger.info("Generating Embedding...")
                embedding = self.embedding_generator.generate_embedding(question)
            else:
                logger.info("Using Cached Embedding.")

            logger.info("Query Embedding Generated Successfully.")

        except Exception:

            logger.exception("Embedding Generation Failed.")

            logger.warning("Using Mock Query Embedding.")

            embedding = [0.1] * self.MOCK_EMBEDDING_DIMENSION

        logger.info("Searching ChromaDB...")

        results = self.retriever.retrieve(embedding)

        documents = results.get("documents", [[]])[0]

        context = "\n\n".join(documents)

        logger.info("Retrieved %s document(s).", len(documents))

        logger.info("Context Retrieved Successfully.")

        return context

    # ------------------------------------------------------------------
    # Build Final Prompt
    # ------------------------------------------------------------------

    def build_prompt(self, question: str, context: str) -> str:

        logger.info("Building Final Prompt...")

        prompt = f"""
You are an Enterprise ETL Testing Expert.

===============================================================================
PROJECT CONTEXT
===============================================================================

{context}

===============================================================================
USER REQUEST
===============================================================================

{question}

===============================================================================
INSTRUCTIONS
===============================================================================

Provide a detailed enterprise-grade response. Use the project context whenever applicable. If the context does not contain enough information,
answer using ETL Testing best practices. Do not fabricate project-specific information."""

        logger.info("Final Prompt Built Successfully.")

        return prompt

    # ------------------------------------------------------------------
    # Execute RAG Pipeline
    # ------------------------------------------------------------------

    def execute(self, question: str, embedding=None, monitor=None) -> str:

        logger.info("=" * 80)
        logger.info("Starting RAG Pipeline")
        logger.info("=" * 80)

        if monitor:
            monitor.rag_search()

        context = self.retrieve_context(question, embedding=embedding)

        final_prompt = self.build_prompt(question, context)

        logger.info("RAG Pipeline Completed Successfully.")

        return final_prompt