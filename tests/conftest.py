"""
===============================================================================
File Name   : conftest.py
Project     : Enterprise AI ETL Framework
Purpose     : Common Pytest Fixtures
Author      : Venkata
===============================================================================
"""

import pytest

from agents.planner import Planner
from agents.agent_registry import AgentRegistry

from knowledge.rag.rag_pipeline import RAGPipeline

from core.monitoring.framework_monitor import FrameworkMonitor
from core.workflows.workflow_manager import WorkflowManager
from core.workflows.workflow_context import WorkflowContext


# =============================================================================
# Framework Fixtures
# =============================================================================

@pytest.fixture(scope="session")
def rag_pipeline():
    return RAGPipeline()


@pytest.fixture(scope="session")
def planner():
    return Planner()


@pytest.fixture(scope="session")
def framework_monitor():
    return FrameworkMonitor()


@pytest.fixture(scope="session")
def agent_registry(rag_pipeline):
    return AgentRegistry(rag_pipeline)


@pytest.fixture(scope="session")
def workflow_manager(
    rag_pipeline,
    planner,
    agent_registry,
    framework_monitor
):
    """
    Enterprise Workflow Manager
    """

    return WorkflowManager(
        rag_pipeline=rag_pipeline,
        planner=planner,
        agent_registry=agent_registry,
        monitor=framework_monitor
    )


# =============================================================================
# Workflow Context
# =============================================================================

@pytest.fixture
def workflow_context(framework_monitor):
    """
    Fresh WorkflowContext for every test.
    """

    return WorkflowContext(
        question="Generate complete ETL Testing package.",
        monitor=framework_monitor
    )


# =============================================================================
# Business Agents
# =============================================================================

@pytest.fixture
def requirement_agent(agent_registry):
    return agent_registry.get_agent("requirement")


@pytest.fixture
def mapping_analysis_agent(agent_registry):
    return agent_registry.get_agent("mapping_analysis")


@pytest.fixture
def test_case_agent(agent_registry):
    return agent_registry.get_agent("test_case")


@pytest.fixture
def test_data_agent(agent_registry):
    return agent_registry.get_agent("test_data")


@pytest.fixture
def sql_agent(agent_registry):
    return agent_registry.get_agent("sql")


@pytest.fixture
def validation_agent(agent_registry):
    return agent_registry.get_agent("validation")


@pytest.fixture
def documentation_agent(agent_registry):
    return agent_registry.get_agent("documentation")


@pytest.fixture
def jira_agent(agent_registry):
    return agent_registry.get_agent("jira")


@pytest.fixture
def defect_analysis_agent(agent_registry):
    return agent_registry.get_agent("defect_analysis")


@pytest.fixture
def root_cause_agent(agent_registry):
    return agent_registry.get_agent("root_cause")