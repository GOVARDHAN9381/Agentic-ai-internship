from crewai import Task, Agent

def create_research_task(agent: Agent, topic: str) -> Task:
    """
    Task assigned to the Research Analyst to collect comprehensive information and synthesize findings.
    """
    return Task(
        description=(
            f"Conduct comprehensive research on the topic: '{topic}'.\n"
            "Your research must thoroughly cover:\n"
            "1. Introduction, core concepts, and historical background.\n"
            "2. Modern architectural paradigms, frameworks, and key design patterns.\n"
            "3. Multi-agent coordination protocols, communication mechanisms, and role specialization.\n"
            "4. Practical, high-impact enterprise use cases and industry adoption benchmarks.\n"
            "5. Primary technical bottlenecks, security/safety considerations, and future projections.\n"
            "Structure your output as an organized Research Brief with specific bullet points, metrics, and key insights."
        ),
        expected_output=(
            "A structured markdown Research Brief containing detailed notes, categorized findings, "
            "architectural blueprints, adoption metrics, and cited analytical takeaways."
        ),
        agent=agent
    )

def create_writing_task(agent: Agent, topic: str, context_tasks: list = None) -> Task:
    """
    Task assigned to the Technical Writer to draft a publication-quality report based on research.
    """
    task_kwargs = {
        "description": (
            f"Using the findings provided by the Senior Research Analyst, author a comprehensive, publication-grade "
            f"technical report on '{topic}'.\n"
            "The report must include:\n"
            "- An engaging Title and Executive Summary\n"
            "- Table of Contents\n"
            "- Deep-dive analytical sections with clear Markdown formatting (headers, tables, bullet points)\n"
            "- Architecture & Multi-Agent Workflow Breakdown\n"
            "- Comparative Analysis / Benchmarks\n"
            "- Real-world Case Studies & Implementation Roadmap\n"
            "- Strategic Recommendations & Conclusion"
        ),
        "expected_output": (
            "A complete, beautifully formatted Markdown report ready for executive review, "
            "with clear structural flow, rich context, and insightful technical commentary."
        ),
        "agent": agent
    }
    if context_tasks:
        task_kwargs["context"] = context_tasks
    return Task(**task_kwargs)

def create_review_task(agent: Agent, topic: str, context_tasks: list = None, output_filename: str = None) -> Task:
    """
    Task assigned to the Chief Editor to polish, fact-check, format, and finalize the report.
    """
    task_kwargs = {
        "description": (
            f"Critically review and refine the drafted report on '{topic}'.\n"
            "Editorial checklist:\n"
            "1. Verify that all claims and metrics are logically coherent and well-supported.\n"
            "2. Enhance clarity, flow, readability, and professional tone.\n"
            "3. Standardize formatting: headers, code snippets, callouts, tables, and bullet points.\n"
            "4. Add an 'Editorial QA & Compliance Sign-Off' section at the end certifying review completion.\n"
            "Produce the final, polished report."
        ),
        "expected_output": (
            "The definitive, publication-ready executive report in markdown, impeccably styled, "
            "thoroughly verified, and containing the final QA sign-off block."
        ),
        "agent": agent
    }
    if output_filename:
        task_kwargs["output_file"] = output_filename
    if context_tasks:
        task_kwargs["context"] = context_tasks
    return Task(**task_kwargs)
