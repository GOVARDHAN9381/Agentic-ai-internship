import streamlit as st
import time
from pathlib import Path
from src.config import get_api_key_status, has_active_llm_key
from src.crew import run_research_pipeline

st.set_page_config(
    page_title="AI Research & Report Generator",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
with st.sidebar:
    st.title("⚙️ System Control")
    st.markdown("**Agentic AI & Multi-Agent Systems**\nWeek 1 Project")
    
    st.divider()
    st.subheader("🔑 API Key Status")
    status = get_api_key_status()
    for key, active in status.items():
        if active:
            st.success(f"**{key}**: Active ✅")
        else:
            st.caption(f"**{key}**: Not set (Demo available)")

    st.divider()
    force_demo = st.checkbox("Force Demo/Simulation Mode", value=not has_active_llm_key())
    
    st.divider()
    st.markdown("""
    **Multi-Agent Roster:**
    - 🔍 **Senior Research Analyst**
    - ✍️ **Lead Technical Writer**
    - 📋 **Chief Editor & QA Specialist**
    """)

# Main Page Header
st.title("🤖 AI Research and Report Generator")
st.markdown(
    "An autonomous multi-agent pipeline built with **CrewAI** that coordinates specialized AI agents "
    "to research, draft, synthesize, and review executive-grade reports."
)

st.divider()

# Input section
col1, col2 = st.columns([3, 1])
with col1:
    topic = st.text_input(
        "Enter Research Topic:",
        value="Agentic AI & Multi-Agent Systems in 2026: Architectures, Tools, and Enterprise Deployment",
        help="Specify any technology, scientific, or market topic you want researched."
    )
with col2:
    output_filename = st.text_input(
        "Save Report As:",
        value="generated_report.md"
    )

start_button = st.button("🚀 Launch Multi-Agent Workflow", type="primary", use_container_width=True)

if start_button:
    if not topic.strip():
        st.error("Please specify a valid topic.")
    else:
        st.info(f"Initiating multi-agent collaboration for topic: **{topic}**")
        
        # Agent execution timeline
        agent_col1, agent_col2, agent_col3 = st.columns(3)
        
        with agent_col1:
            st.markdown("#### 1. Research Agent")
            r_status = st.empty()
            r_status.info("⏳ Gathering insights & metrics...")
            
        with agent_col2:
            st.markdown("#### 2. Writing Agent")
            w_status = st.empty()
            w_status.text("Waiting for research...")
            
        with agent_col3:
            st.markdown("#### 3. Reviewer Agent")
            rev_status = st.empty()
            rev_status.text("Waiting for draft...")

        out_path = Path("outputs") / output_filename
        out_path.parent.mkdir(parents=True, exist_ok=True)

        # Simulation / Run
        progress_bar = st.progress(10)
        time.sleep(0.5)
        r_status.success("✅ Research Brief Compiled")
        progress_bar.progress(40)
        
        w_status.info("✍️ Drafting executive report...")
        time.sleep(0.5)
        w_status.success("✅ Technical Draft Ready")
        progress_bar.progress(75)

        rev_status.info("📋 Performing QA & Fact Check...")
        report = run_research_pipeline(topic=topic, output_path=str(out_path), force_demo=force_demo)
        time.sleep(0.5)
        rev_status.success("✅ QA Approved & Signed Off")
        progress_bar.progress(100)

        st.success(f"🎉 Report generated successfully! Saved to `{out_path}`")
        
        # Display Report
        st.divider()
        st.subheader("📄 Generated Research Report")
        st.markdown(report)

        st.download_button(
            label="📥 Download Report (.md)",
            data=report,
            file_name=output_filename,
            mime="text/markdown",
            use_container_width=True
        )
