"""
===============================================================================
File Name   : chunking.py
Project     : Enterprise AI ETL Framework
Purpose     : Split Documents into Chunks
Author      : Venkata
===============================================================================
"""

from core.logger.logger import logger


class TextChunker:
    """
    Splits document text into smaller chunks for RAG.
    """

    def __init__(self, chunk_size = 100, overlap = 30):

        self.chunk_size = chunk_size
        self.overlap = overlap

    # ----------------------------------------------------------------

    def split_text(self, text):

        logger.info("Chunking Started...")

        chunks = []

        start = 0

        while start < len(text):

            end = start + self.chunk_size

            chunk = text[start:end]

            chunks.append(chunk)

            start += self.chunk_size - self.overlap

        logger.info(f"Total Chunks Created : {len(chunks)}")

        return chunks

if __name__ == "__main__":

    from knowledge.rag.document_loader import DocumentLoader

    loader = DocumentLoader()

    text = loader.load_docx("Business_Rules.docx")

    chunker = TextChunker()

    chunks = chunker.split_text(text)

    for index, chunk in enumerate(chunks, start=1):

        print("=" * 80)

        print(f"Chunk {index}")

        print("=" * 80)

        print(chunk)

