import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # creates: Connection To ChatGPT - api_key: As a QA Lead, you may never actually see the raw key.
                                                     # You simply use: api_key = os.getenv("OPENAI_API_KEY") and the DevOps team Creates OpenAI Subscription
                                                     # Stores Key in Secrets Manager QA / Dev Team Uses It.





