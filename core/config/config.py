import os
from openai import OpenAI

_client = None

def get_openai_client():
    global _client

    if _client is None:
        _client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    return _client






 # creates: Connection To ChatGPT - api_key: As a QA Lead, you may never actually see the raw key.
                                                     # You simply use: api_key = os.getenv("OPENAI_API_KEY") and the DevOps team Creates OpenAI Subscription
                                                     # Stores Key in Secrets Manager QA / Dev Team Uses It.





