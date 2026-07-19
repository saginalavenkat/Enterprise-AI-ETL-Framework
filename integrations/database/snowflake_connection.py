"""
===============================================================================
File Name   : snowflake_connection.py
Project     : Enterprise AI ETL Framework
Purpose     : Snowflake Database Connection
Author      : Venkata
===============================================================================
"""

import snowflake.connector
import os

from dotenv import load_dotenv

load_dotenv()

from core.logger.logger import logger

from integrations.database.database_connection import DatabaseConnection

class SnowflakeConnection(DatabaseConnection):

    def __init__(self):

        self.connection = None

        logger.info("SnowflakeConnection Object Created : %s", id(self))

    # -----------------------------------------------------------------

    def connect(self):

        try:

            logger.info("Connecting to Snowflake...")

            account = os.getenv("SNOWFLAKE_ACCOUNT")
            user = os.getenv("SNOWFLAKE_USER")
            password = os.getenv("SNOWFLAKE_PASSWORD")
            warehouse = os.getenv("SNOWFLAKE_WAREHOUSE")
            database = os.getenv("SNOWFLAKE_DATABASE")
            schema = os.getenv("SNOWFLAKE_SCHEMA")
            role = os.getenv("SNOWFLAKE_ROLE")

            self.connection = snowflake.connector.connect(account=account, user=user, password=password, warehouse=warehouse, database=database, schema=schema, role=role)

            logger.info("Connected to Snowflake Successfully.")
            logger.info("Object ID      : %s", id(self))
            logger.info("Connection Obj : %s", self.connection)
            logger.info("Connection ID  : %s", id(self.connection))

            return self.connection

        except Exception as ex:

            logger.exception("Failed to connect to Snowflake.")

            raise
    # -----------------------------------------------------------------

    def execute_query(self, query):

        logger.info("Object ID       : %s", id(self))
        logger.info("Connection Obj  : %s", self.connection)

        if self.connection is None:
            raise Exception("Connection became None before execute_query().")

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