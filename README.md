# AI Research and Report Generator

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![CrewAI Framework](https://img.shields.io/badge/CrewAI-1.15.20-orange.svg)](https://crewai.com)
[![Streamlit UI](https://img.shields.io/badge/Streamlit-1.55-red.svg)](https://streamlit.io)
[![Test Suite](https://img.shields.io/badge/Tests-Passing%20(6%2F6)-brightgreen.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An enterprise-grade autonomous multi-agent system built using **CrewAI** that coordinates specialized AI agents to autonomously research complex topics, synthesize findings, draft comprehensive publications, and conduct rigorous editorial QA sign-offs.

Developed for **Agentic AI & Multi-Agent Systems — Week 1 Project Guidance**.

---

## 📌 Project Overview & Guidance Compliance

This project fulfills all core project guidance requirements:

| # | Requirement | Implementation Status | Core Artifact |
|---|---|---|---|
| **1** | **Set up Python and CrewAI** | ✅ Complete | Python 3.11+, CrewAI 1.15+, robust Windows & Linux setup |
| **2** | **Create research & writing agents with separate roles** | ✅ Complete | `Senior Research Analyst`, `Lead Technical Writer`, `Chief Editor & QA` (`src/agents.py`) |
| **3** | **Assign tasks for collecting & summarizing information** | ✅ Complete | Sequential task pipeline with context handoffs (`src/tasks.py`) |
| **4** | **Generate and review the final report** | ✅ Complete | Automated editorial fact-checking, styling & QA sign-off (`src/crew.py`) |
| **5** | **Submit source code, sample report, screenshots & docs** | ✅ Complete | Complete repository with full source, tests, 2 sample reports, SVG diagrams |

---

## 🏗️ Multi-Agent Architecture

```
+-------------------------------------------------------------------------------+
|                      MULTI-AGENT ORCHESTRATION PIPELINE                       |
+-------------------------------------------------------------------------------+
                                        |
                             [Input Research Topic]
                                        v
  +---------------------------------------------------------------------------+
  | 🔍 1. SENIOR RESEARCH ANALYST (Agent)                                      |
  | Role: Senior Research Analyst                                             |
  | Goal: Deep-dive data mining, trend discovery, metrics extraction           |
  | Tools: ResearchSearchTool, MetricSynthesizerTool                          |
  +---------------------------------------------------------------------------+
                                        |
                              [Research Brief Handoff]
                                        v
  +---------------------------------------------------------------------------+
  | ✍️ 2. LEAD TECHNICAL CONTENT WRITER (Agent)                                |
  | Role: Lead Technical Content Writer                                       |
  | Goal: Synthesize research findings into a structured, executive report    |
  | Sections: Executive Summary, Architecture, Metrics, Benchmarks, Use Cases |
  +---------------------------------------------------------------------------+
                                        |
                                [Draft Report Handoff]
                                        v
  +---------------------------------------------------------------------------+
  | 📋 3. CHIEF EDITOR & QA SPECIALIST (Agent)                                 |
  | Role: Chief Editor & QA Specialist                                        |
  | Goal: Fact-check, polish prose, assess readability, append QA Sign-Off   |
  +---------------------------------------------------------------------------+
                                        |
                                        v
  +---------------------------------------------------------------------------+
  | 📄 FINAL DELIVERABLE: PUBLICATION-READY EXECUTIVE REPORT                  |
  | Saved to: outputs/sample_report_*.md                                       |
  +---------------------------------------------------------------------------+
```

Architecture diagram visual: see [`screenshots/architecture_flow.svg`](screenshots/architecture_flow.svg).

---

## 🤖 Specialized Agent Profiles

### 1. Senior Research Analyst
* **Role:** Senior Research Analyst
* **Goal:** Uncover cutting-edge developments, gather empirical data, and synthesize in-depth insights on `{topic}`.
* **Backstory:** An investigative research analyst specializing in emerging technologies. Known for analytical rigor and spotting high-impact patterns, dissecting complex topics into structured knowledge briefs.
* **Tools:** `Topic Research and Information Retrieval Tool`, `Data and Metric Synthesizer Tool`.

### 2. Lead Technical Content Writer
* **Role:** Lead Technical Content Writer
* **Goal:** Transform raw research findings and data into an engaging, structured, and publication-ready report on `{topic}`.
* **Backstory:** An acclaimed technical author renowned for translating dense research into captivating, clear, and high-impact prose for executives and engineers alike.

### 3. Chief Editor & QA Specialist
* **Role:** Chief Editor & QA Specialist
* **Goal:** Critically review, polish, and ensure maximum clarity, accuracy, and structural excellence.
* **Backstory:** A meticulous chief editor with a zero-tolerance policy for ambiguity, grammatical errors, and unverified claims.

---

## 📁 Repository Structure

```
.
├── .env.example              # Template for API keys (OpenAI, Gemini, Groq, Anthropic)
├── .gitignore                # Git exclusions (caches, virtualenvs, credentials)
├── README.md                 # Complete project documentation and guide
├── requirements.txt          # Project dependencies (CrewAI, Streamlit, etc.)
├── main.py                   # Command-line interface (CLI) entry point
├── app.py                    # Streamlit interactive Web Dashboard
├── run_project.bat           # 1-Click launcher script for Windows
├── run_project.sh            # 1-Click launcher script for Linux/macOS
├── src/
│   ├── __init__.py           # Package initializer
│   ├── config.py             # Environment setup, LLM provider config, cache handler
│   ├── agents.py             # Specialized agent definitions
│   ├── tasks.py              # Task definitions with sequential context dependencies
│   ├── tools.py              # Custom research and metric extraction tools
│   └── crew.py               # Crew orchestration and fallback simulation logic
├── tests/
│   ├── __init__.py
│   ├── test_agents.py        # Unit tests for agent instantiation and roles
│   ├── test_tasks.py         # Unit tests for task assignments and context handoffs
│   └── test_crew.py          # Integration tests for crew build and pipeline execution
├── outputs/
│   ├── sample_report_agentic_ai.md          # Sample Report 1: Agentic AI Systems
│   └── sample_report_quantum_computing.md   # Sample Report 2: Quantum Computing
└── screenshots/
    ├── architecture_flow.svg                # Vector architecture diagram
    └── execution_workflow.md                # Execution trace and workflow documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites
* **Python 3.10+** (Tested on Python 3.11.9)
* **Git**

### 2. Installation
Clone the repository and install the dependencies:

```bash
git clone https://github.com/GOVARDHAN9381/Agentic-ai-internship.git
cd Agentic-ai-internship

# Optional: Create and activate a virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

### 3. Configuration (Optional)
Copy `.env.example` to `.env` and provide your preferred LLM API key:

```bash
cp .env.example .env
```

Supports:
- **OpenAI:** `OPENAI_API_KEY=sk-...` (default model: `gpt-4o-mini`)
- **Google Gemini:** `GEMINI_API_KEY=AIza...` (`MODEL=gemini/gemini-1.5-flash`)
- **Groq:** `GROQ_API_KEY=gsk_...` (`MODEL=groq/llama-3.1-70b-versatile`)
- **Anthropic:** `ANTHROPIC_API_KEY=sk-ant-...`
- **Demo / Offline Mode:** Runs seamlessly without requiring any API keys!

---

## 💻 How to Run

### Option A: Command-Line Interface (CLI)

Run with the default topic:
```bash
python main.py
```

Run with a custom topic and custom output file:
```bash
python main.py --topic "Autonomous AI Agents in Healthcare & Clinical Diagnostics" --output "outputs/healthcare_report.md"
```

Check configured API keys:
```bash
python main.py --check-env
```

Force demo/simulation mode:
```bash
python main.py --demo
```

### Option B: Interactive Streamlit Web Dashboard

Launch the browser-based graphical user interface:
```bash
streamlit run app.py
```
* Features:
  * Topic input and output file customizer
  * Real-time multi-agent execution pipeline display
  * Live Markdown report preview with rendered tables and headings
  * One-click report download (`.md`)

---

## 🧪 Running the Test Suite

Run unit and integration tests using `pytest`:

```bash
python -m pytest tests -v
```

All 6 test cases verify:
- Correct agent instantiation, roles, goals, and backstories.
- Task context dependencies and output bindings.
- Crew assembly and full pipeline execution.

---

## 📄 Sample Reports Generated

1. [`outputs/sample_report_agentic_ai.md`](outputs/sample_report_agentic_ai.md) — Comprehensive report on **Agentic AI & Multi-Agent Systems in 2026: Architectures, Tools, and Enterprise Deployment**.
2. [`outputs/sample_report_quantum_computing.md`](outputs/sample_report_quantum_computing.md) — Comprehensive report on **Quantum Computing Breakthroughs and Post-Quantum Cryptography**.

---

## 👨‍💻 Author & Submission Details

* **Author:** Govardhan
* **GitHub:** [@GOVARDHAN9381](https://github.com/GOVARDHAN9381)
* **Repository:** [Agentic-ai-internship](https://github.com/GOVARDHAN9381/Agentic-ai-internship)
* **Program:** Agentic AI & Multi-Agent Systems Internship
* **Submission Date:** November 2026
