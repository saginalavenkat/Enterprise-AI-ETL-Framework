"""
===============================================================================
File Name   : embeddings.py
Project     : Enterprise AI ETL Framework
Purpose     : Generate Embeddings for Document Chunks
Author      : Venkata
===============================================================================
"""

from core.config.config import client
from core.logger.logger import logger


class EmbeddingGenerator:
    """
    Generates embeddings for text chunks.
    """

    def __init__(self, model="text-embedding-3-small"):  # This model doesn't generate answers. It only generates vectors.
                                                         # Example: client.embeddings.create(...) returns [0.251, 0.824, 0.611, 0.121, ... 1536 numbers] Those 1536 numbers represent the meaning of the sentence.
        self.model = model

    # ------------------------------------------------------------

    def generate_embedding(self, text):

        logger.info("Generating Embedding...")

        response = client.embeddings.create(model = self.model, input = text)

        embedding = response.data[0].embedding

        logger.info(f"Embedding Length : {len(embedding)}")

        return embedding

# Testing the above code

if __name__ == "__main__":

    embedding_generator = EmbeddingGenerator()

    vector = embedding_generator.generate_embedding("Customer ID must be unique.") # this line we use when we have billing for OpenAI API if not use - sample_embedding = [0.1] * 1536

    sample_embedding = [0.1] * 1536

    print(vector[:10])