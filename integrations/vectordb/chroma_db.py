"""
===============================================================================
File Name   : chroma_db.py
Project     : Enterprise AI ETL Framework
Purpose     : Store and Retrieve Embeddings using ChromaDB
Author      : Venkata
===============================================================================
"""

import chromadb

from core.logger.logger import logger
from pathlib import Path

class ChromaVectorDB:
    """
    Handles Vector Storage using ChromaDB.
    """

    def __init__(self, collection_name = "etl_documents"):

        logger.info("Initializing ChromaDB...")

        # self.client = chromadb.Client()

        BASE_DIR = Path(__file__).resolve().parent.parent

        DB_PATH = BASE_DIR / "vectordb" / "chroma_storage"

        self.client = chromadb.PersistentClient(path=str(DB_PATH))

        self.collection = self.client.get_or_create_collection(name = collection_name)

    # ------------------------------------------------------------

    def add_document(self, document_id, text, embedding):

        logger.info(f"Adding Document : {document_id}")

        self.collection.add(ids = [document_id], documents = [text], embeddings = [embedding])

    # ------------------------------------------------------------

    def count(self):

        return self.collection.count()

# Testing (Temporary) - Create a temporary test:

if __name__ == "__main__":

    vector_db = ChromaVectorDB()

    sample_embedding = [0.1] * 1536

    vector_db.add_document(document_id = "DOC_001", text = "Customer ID must be unique.", embedding = sample_embedding)

    print("Total Documents :")

    print(vector_db.count())
