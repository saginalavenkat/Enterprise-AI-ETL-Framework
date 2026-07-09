"""
===============================================================================
File Name   : retriever.py
Project     : Enterprise AI ETL Framework
Purpose     : Retrieve Relevant Chunks from ChromaDB
Author      : Venkata
===============================================================================
"""

from core.logger.logger import logger


class Retriever:
    """
    Retrieves the most relevant chunks
    from ChromaDB.
    """

    def __init__(self, vector_db):

        self.vector_db = vector_db

    # ------------------------------------------------------------

    def retrieve(self, query_embedding, top_k = 3):

        logger.info("Searching ChromaDB...")

        results = self.vector_db.collection.query(query_embeddings = [query_embedding], n_results = top_k)

        logger.info("Relevant Chunks Retrieved.")

        return results

# Testing - For now, we'll use a mock embedding because your OpenAI billing is still pending.

if __name__ == "__main__":

    from integrations.vectordb.chroma_db import ChromaVectorDB

    vector_db = ChromaVectorDB()

    mock_embedding = [0.1] * 1536

    retriever = Retriever(vector_db)

    results = retriever.retrieve(mock_embedding)

    print(results)