"""
===============================================================================
File Name   : database_service.py
Project     : Enterprise AI ETL Framework
Purpose     : Enterprise Database Service
Author      : Venkata
===============================================================================
"""

from core.logger.logger import logger
from integrations.database.snowflake_connection import SnowflakeConnection


class DatabaseService:

    def __init__(self):

        logger.info("Database Service Initialized.")

    # ----------------------------------------------------------------

    def execute_query(self, database, query):

        logger.info("Database : %s", database)
        logger.info("Query    : %s", query)

        connection = None

        try:

            if database.lower() == "snowflake":

                connection = SnowflakeConnection()

            else:

                raise ValueError(f"Database '{database}' is not supported.")

            connection.connect()

            result = connection.execute_query(query)

            return result

        except Exception as ex:

            logger.exception("Database execution failed.")

            raise ex

        finally:

            if connection:

                connection.close()