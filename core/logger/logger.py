"""
===============================================================================
File Name   : logger.py
Project     : Enterprise AI ETL Framework
Purpose     : Centralized Logging Utility
Author      : Venkata
===============================================================================
"""

import logging
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

LOG_DIR = BASE_DIR / "reports" / "logs"

LOG_DIR.mkdir(parents = True, exist_ok = True)

LOG_FILE = LOG_DIR / "framework.log"


logging.basicConfig(level = logging.INFO, format = "%(asctime)s | %(levelname)s | %(message)s", handlers = [logging.FileHandler(LOG_FILE, encoding = "utf-8"), logging.StreamHandler()])

logger = logging.getLogger("Enterprise_AI_ETL_Framework")