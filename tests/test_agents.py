import pytest
from src.agents import create_research_agent, create_writer_agent, create_reviewer_agent

def test_research_agent_creation():
    agent = create_research_agent()
    assert agent is not None
    assert agent.role == "Senior Research Analyst"
    assert "investigative research analyst" in agent.backstory.lower()
    assert len(agent.tools) == 2

def test_writer_agent_creation():
    agent = create_writer_agent()
    assert agent is not None
    assert agent.role == "Lead Technical Content Writer"
    assert "technical writer" in agent.backstory.lower()
    assert agent.verbose is True

def test_reviewer_agent_creation():
    agent = create_reviewer_agent()
    assert agent is not None
    assert agent.role == "Chief Editor & QA Specialist"
    assert "chief editor" in agent.backstory.lower()
