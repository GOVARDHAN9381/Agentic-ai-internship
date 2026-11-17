import pytest
from pathlib import Path
from src.crew import build_crew, run_research_pipeline

def test_build_crew():
    topic = "AI Safety in Agentic Systems"
    crew, agents, tasks = build_crew(topic=topic, output_path="outputs/test_report.md")
    assert crew is not None
    assert len(agents) == 3
    assert len(tasks) == 3

def test_run_simulation_pipeline(tmp_path):
    topic = "Multi-Agent System Orchestration"
    out_file = tmp_path / "test_report.md"
    result = run_research_pipeline(topic=topic, output_path=str(out_file), force_demo=True)
    assert result is not None
    assert topic in result
    assert "Editorial QA & Compliance Sign-Off" in result
    assert out_file.exists()
    assert len(out_file.read_text(encoding="utf-8")) > 500
