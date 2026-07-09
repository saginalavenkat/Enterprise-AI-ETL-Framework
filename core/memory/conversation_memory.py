"""
===============================================================================
File Name   : conversation_memory.py
Project     : Enterprise AI ETL Framework
Purpose     : Stores Conversation Memory
Author      : Venkata
===============================================================================
"""

from core.logger.logger import logger


class ConversationMemory:

    def __init__(self):

        logger.info("Conversation Memory Initialized.")

        self.memory = {}

    # -----------------------------------------------------------------

    def save(self, key: str, value: str):

        logger.info(f"Saving Memory : {key}")

        self.memory[key] = value

    # -----------------------------------------------------------------

    def load(self, key: str):

        return self.memory.get(key, "")

    # -----------------------------------------------------------------

    def get_all(self):

        return self.memory

    # -----------------------------------------------------------------

    def clear(self):

        logger.info("Clearing Conversation Memory")

        self.memory.clear()


# -----------------------------------------------------------------
# Testing
# -----------------------------------------------------------------

if __name__ == "__main__":

    memory = ConversationMemory()

    memory.save("requirements", "Customer ID must be unique.")

    memory.save("test_cases", "Duplicate Validation")

    print(memory.get_all())