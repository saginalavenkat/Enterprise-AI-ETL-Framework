"""
===============================================================================
File Name   : agent_registry.py
Project     : Enterprise AI ETL Framework
Purpose     : AI Agent Registry
Author      : Venkata
===============================================================================
"""

from core.logger.logger import logger

from agents.requirement_agent import RequirementAgent
from agents.mapping_analysis_agent import MappingAnalysisAgent
from agents.test_case_agent import TestCaseAgent
from agents.test_data_agent import TestDataAgent
from agents.sql_agent import SQLAgent
from agents.validation_agent import ValidationAgent
from agents.documentation_agent import DocumentationAgent
from agents.defect_analysis_agent import DefectAnalysisAgent
from agents.root_cause_agent import RootCauseAgent
from agents.jira_agent import JiraAgent


class AgentRegistry:
    """
    Enterprise AI Agent Registry

    Responsible for

    - Registering AI Agents
    - Returning Agents
    - Future Dynamic Registration
    """

    def __init__(
            self,
            rag_pipeline,
            mcp_client
    ):

        logger.info("Initializing Agent Registry...")

        self.rag_pipeline = rag_pipeline

        self.mcp_client = mcp_client

        self.agents = {

            "requirement": RequirementAgent(
                self.rag_pipeline
            ),

            "mapping_analysis": MappingAnalysisAgent(
                self.rag_pipeline
            ),

            "test_case": TestCaseAgent(
                self.rag_pipeline
            ),

            "test_data": TestDataAgent(
                self.rag_pipeline
            ),

            "sql": SQLAgent(
                rag_pipeline=self.rag_pipeline,
                mcp_client=self.mcp_client
            ),

            "validation": ValidationAgent(
                self.rag_pipeline
            ),

            "defect_analysis": DefectAnalysisAgent(
                self.rag_pipeline
            ),

            "jira": JiraAgent(
                rag_pipeline=self.rag_pipeline,
                mcp_client=self.mcp_client
            ),

            "documentation": DocumentationAgent(
                self.rag_pipeline
            ),

            "root_cause": RootCauseAgent(
                self.rag_pipeline
            )

        }

        logger.info(
            "Registered Agents : %s",
            ", ".join(self.agents.keys())
        )

    # ------------------------------------------------------------------

    def get_agent(self, agent_name: str):

        agent = self.agents.get(agent_name.lower())

        if agent is None:

            logger.warning(
                "Agent '%s' is not registered.",
                agent_name
            )

        return agent

    # ------------------------------------------------------------------

    def register_agent(self, agent_name: str, agent):

        logger.info(
            "Registering Agent : %s",
            agent_name
        )

        self.agents[agent_name.lower()] = agent

    # ------------------------------------------------------------------

    def get_registered_agents(self):

        return list(self.agents.keys())