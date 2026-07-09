"""
===============================================================================
File Name   : snowflake_connection.py
Project     : Enterprise AI ETL Framework
Purpose     : Snowflake Database Connection
Author      : Venkata
===============================================================================
"""

import snowflake.connector

from core.logger.logger import logger

from integrations.database.database_connection import DatabaseConnection

from core.config.secrets import (SNOWFLAKE_ACCOUNT, SNOWFLAKE_USER, SNOWFLAKE_PASSWORD, SNOWFLAKE_DATABASE, SNOWFLAKE_SCHEMA, SNOWFLAKE_WAREHOUSE, SNOWFLAKE_ROLE)


class SnowflakeConnection(DatabaseConnection):

    def __init__(self):

        self.connection = None

    # -----------------------------------------------------------------

    def connect(self):

        try:

            logger.info("Connecting to Snowflake...")

            self.connection = snowflake.connector.connect(account = SNOWFLAKE_ACCOUNT, user = SNOWFLAKE_USER, password = SNOWFLAKE_PASSWORD, warehouse = SNOWFLAKE_WAREHOUSE, database = SNOWFLAKE_DATABASE, schema = SNOWFLAKE_SCHEMA, role = SNOWFLAKE_ROLE)

            logger.info("Connected to Snowflake Successfully.")

            return self.connection

        except Exception as ex:

            logger.exception("Failed to connect to Snowflake.")

            raise ex

    # -----------------------------------------------------------------

    def execute_query(self, query):

        cursor = self.connection.cursor()

        try:

            logger.info(f"Executing Query : {query}")

            cursor.execute(query)

            result = cursor.fetchall()

            logger.info("Query Executed Successfully.")

            return result

        finally:

            cursor.close()

    # -----------------------------------------------------------------

    def close(self):

        if self.connection:

            self.connection.close()

            logger.info("Snowflake Connection Closed.")