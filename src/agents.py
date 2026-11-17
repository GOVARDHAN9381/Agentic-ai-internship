from crewai import Agent
from src.tools import research_search_tool, metric_synthesizer_tool

def create_research_agent(llm=None) -> Agent:
    """
    Creates the Senior Research Analyst Agent responsible for gathering,
    filtering, and synthesizing deep technical data and insights.
    """
    kwargs = {
        "role": "Senior Research Analyst",
        "goal": "Uncover cutting-edge developments, gather empirical data, and synthesize in-depth insights on {topic}",
        "backstory": (
            "You are a world-class investigative research analyst specializing in emerging technologies. "
            "Known for your analytical rigor and ability to spot high-impact patterns, you dissect complex topics "
            "into structured knowledge, verify facts, and produce thorough research briefs that serve as the foundation "
            "for executive decision-making."
        ),
        "verbose": True,
        "allow_delegation": False,
        "tools": [research_search_tool, metric_synthesizer_tool],
    }
    if llm:
        kwargs["llm"] = llm
    return Agent(**kwargs)

def create_writer_agent(llm=None) -> Agent:
    """
    Creates the Lead Technical Writer Agent responsible for crafting an engaging,
    authoritative, and structured comprehensive report.
    """
    kwargs = {
        "role": "Lead Technical Content Writer",
        "goal": "Transform raw research findings and data into an engaging, structured, and publication-ready report on {topic}",
        "backstory": (
            "You are an acclaimed technical writer and author renowned for translating dense, complicated "
            "research into captivating, lucid, and high-impact prose. You structure documents with clear headings, "
            "bullet points, executive summaries, and actionable takeaways, making technical depth accessible "
            "to both technical experts and executive leadership."
        ),
        "verbose": True,
        "allow_delegation": False,
    }
    if llm:
        kwargs["llm"] = llm
    return Agent(**kwargs)

def create_reviewer_agent(llm=None) -> Agent:
    """
    Creates the Quality Assurance & Chief Editor Agent responsible for reviewing,
    fact-checking, formatting, and refining the final report.
    """
    kwargs = {
        "role": "Chief Editor & QA Specialist",
        "goal": "Critically review, polish, and ensure maximum clarity, accuracy, and structural excellence of the report on {topic}",
        "backstory": (
            "You are a meticulous chief editor with a zero-tolerance policy for ambiguity, grammatical slips, "
            "and unverified claims. You refine reports for tone, cohesion, logical flow, formatting standards, "
            "and executive presentation before final sign-off."
        ),
        "verbose": True,
        "allow_delegation": False,
    }
    if llm:
        kwargs["llm"] = llm
    return Agent(**kwargs)
