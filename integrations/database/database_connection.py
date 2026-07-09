"""
===============================================================================
File Name   : database_connection.py
Project     : Enterprise AI ETL Framework
Purpose     : Generic Database Connection Interface
Author      : Venkata
===============================================================================
"""

from abc import ABC, abstractmethod


class DatabaseConnection(ABC):

    @abstractmethod
    def connect(self):
        pass

    # ------------------------------------------------------------

    @abstractmethod
    def execute_query(self, query):
        pass

    # ------------------------------------------------------------

    @abstractmethod
    def close(self):
        pass