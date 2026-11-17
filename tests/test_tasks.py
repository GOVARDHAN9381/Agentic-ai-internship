import pytest
from src.agents import create_research_agent, create_writer_agent, create_reviewer_agent
from src.tasks import create_research_task, create_writing_task, create_review_task

def test_tasks_creation_and_dependencies():
    topic = "Autonomous Multi-Agent Architecture"
    
    research_agent = create_research_agent()
    writer_agent = create_writer_agent()
    reviewer_agent = create_reviewer_agent()

    r_task = create_research_task(research_agent, topic)
    w_task = create_writing_task(writer_agent, topic, context_tasks=[r_task])
    rev_task = create_review_task(reviewer_agent, topic, context_tasks=[w_task], output_filename="test_out.md")

    assert topic in r_task.description
    assert r_task.agent == research_agent
    assert w_task.agent == writer_agent
    assert rev_task.agent == reviewer_agent
    assert w_task.context == [r_task]
    assert rev_task.context == [w_task]
    assert rev_task.output_file == "test_out.md"
