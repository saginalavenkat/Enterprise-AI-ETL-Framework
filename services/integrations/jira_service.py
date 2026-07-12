"""
===============================================================================
File Name   : jira_service.py
Project     : Enterprise AI ETL Framework
Purpose     : Jira Service Layer
Author      : Venkata
===============================================================================
"""

import requests
import os

from core.logger.logger import logger

JIRA_URL = os.getenv("JIRA_URL")
JIRA_USERNAME = os.getenv("JIRA_USERNAME")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")

class JiraService:

    def __init__(self):

        logger.info("Jira Service Initialized.")

        self.base_url = JIRA_URL.rstrip("/")

        self.auth = (JIRA_USERNAME, JIRA_API_TOKEN)

        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    # ------------------------------------------------------------------

    def create_issue(
            self,
            project,
            summary,
            description,
            issue_type="Bug"
    ):

        logger.info("Creating Jira Issue...")

        url = f"{self.base_url}/rest/api/3/issue"

        payload = {

            "fields": {

                "project": {

                    "key": project

                },

                "summary": summary,

                "description": {

                    "type": "doc",

                    "version": 1,

                    "content": [

                        {

                            "type": "paragraph",

                            "content": [

                                {

                                    "type": "text",

                                    "text": description

                                }

                            ]

                        }

                    ]

                },

                "issuetype": {

                    "name": issue_type

                }

            }

        }

        response = requests.post(

            url,

            json=payload,

            auth=self.auth,

            headers=self.headers

        )
        print("=" * 80)
        print("URL")
        print(url)

        print("=" * 80)
        print("PAYLOAD")
        print(payload)

        print("=" * 80)
        print("STATUS")
        print(response.status_code)

        print("=" * 80)
        print("RESPONSE")
        print(response.text)
        response.raise_for_status()

        issue = response.json()

        logger.info("Jira Issue Created : %s", issue["key"])

        return {

            "issue_key": issue["key"],

            "issue_id": issue["id"],

            "issue_url": f"{self.base_url}/browse/{issue['key']}"

        }

    # ------------------------------------------------------------------

    def search_issue(self, jql):

        logger.info("Searching Jira Issues...")

        url = f"{self.base_url}/rest/api/3/search"

        response = requests.get(

            url,

            params={"jql": jql},

            auth=self.auth,

            headers=self.headers

        )

        response.raise_for_status()

        logger.info("Search Completed.")

        return response.json()

    # ------------------------------------------------------------------

    def add_comment(self, issue_key, comment):

        logger.info("Adding Comment To %s", issue_key)

        url = f"{self.base_url}/rest/api/3/issue/{issue_key}/comment"

        payload = {

            "body": {

                "type": "doc",

                "version": 1,

                "content": [

                    {

                        "type": "paragraph",

                        "content": [

                            {

                                "type": "text",

                                "text": comment

                            }

                        ]

                    }

                ]

            }

        }

        response = requests.post(

            url,

            json=payload,

            auth=self.auth,

            headers=self.headers

        )

        response.raise_for_status()

        logger.info("Comment Added Successfully.")

        issue = response.json()

        logger.info("Jira Issue Created : %s", issue["key"])

        return {

            "issue_key": issue["key"],

            "issue_id": issue["id"],

            "issue_url": f"{self.base_url}/browse/{issue['key']}"

        }