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
from agents.sql_agent import SQLAgent
from agents.validation_agent import ValidationAgent
from agents.documentation_agent import DocumentationAgent
from agents.test_case_agent import TestCaseAgent
from agents.mapping_analysis_agent import MappingAnalysisAgent
from agents.test_data_agent import TestDataAgent
from agents.root_cause_agent import RootCauseAgent
from agents.defect_analysis_agent import DefectAnalysisAgent
from agents.jira_agent import JiraAgent

class AgentRegistry:

    def __init__(self, rag_pipeline):

        logger.info("Initializing Agent Registry...")

        # Save RAG pipeline
        self.rag_pipeline = rag_pipeline

        self.agents = {

            "requirement": RequirementAgent(self.rag_pipeline),

            "mapping_analysis": MappingAnalysisAgent(self.rag_pipeline),

            "test_case": TestCaseAgent(self.rag_pipeline),

            "test_data": TestDataAgent(self.rag_pipeline),

            "sql": SQLAgent(self.rag_pipeline),

            "validation": ValidationAgent(self.rag_pipeline),

            "defect_analysis": DefectAnalysisAgent(self.rag_pipeline),

            "jira": JiraAgent(self.rag_pipeline),

            "documentation": DocumentationAgent(self.rag_pipeline),

            "root_cause": RootCauseAgent(self.rag_pipeline)

        }

        logger.info(
            "Registered Agents : %s",
            ", ".join(self.agents.keys())
        )
    # ------------------------------------------------------------

    def get_agent(self, agent_name):

        return self.agents.get(agent_name)