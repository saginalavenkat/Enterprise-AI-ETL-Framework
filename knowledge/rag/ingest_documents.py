"""
===============================================================================
File Name   : ingest_documents.py
Project     : Enterprise AI ETL Framework
Purpose     : Load Documents and Store into ChromaDB
Author      : Venkata
===============================================================================
"""

from pathlib import Path

from core.logger.logger import logger

from knowledge.rag.document_loader import DocumentLoader
from knowledge.rag.chunking import TextChunker
from knowledge.rag.embeddings import EmbeddingGenerator
from integrations.vectordb.chroma_db import ChromaVectorDB


class DocumentIngestion:

    def __init__(self):

        self.loader = DocumentLoader()      # Document Loader Object

        self.chunker = TextChunker()        # Chunker Object

        self.embedding_generator = EmbeddingGenerator()     # Embedding Object

        self.vector_db = ChromaVectorDB()                   # Vector Database Connection

    # ------------------------------------------------------------

    def ingest_document(self, file_name):

        logger.info("=" * 80)
        logger.info(f"Ingesting : {file_name}")
        logger.info("=" * 80)

        extension = Path(file_name).suffix.lower()

        if extension == ".pdf":

            text = self.loader.load_pdf(file_name)

        elif extension == ".docx":

            text = self.loader.load_docx(file_name)

        elif extension == ".xlsx":

            text = self.loader.load_excel(file_name)

        elif extension == ".txt":

            text = self.loader.load_txt(file_name)

        else:

            logger.error(f"Unsupported File : {file_name}")

            return

        chunks = self.chunker.split_text(text)

        logger.info(f"Chunks Created : {len(chunks)}")

        for index, chunk in enumerate(chunks, start=1):

            document_id = f"{file_name}_Chunk_{index}"

            try:

                embedding = self.embedding_generator.generate_embedding(chunk)

            except Exception:

                logger.warning("Using Mock Embedding")

                embedding = [0.1] * 1536

            self.vector_db.add_document(document_id = document_id, text = chunk, embedding = embedding

            )

            logger.info(f"Stored {document_id}")

        logger.info(f"Completed : {file_name}")

# Testing code

if __name__ == "__main__":

    ingestion = DocumentIngestion()

    ingestion.ingest_document("Business_Rules.docx")