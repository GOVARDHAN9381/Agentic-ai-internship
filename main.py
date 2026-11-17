import argparse
import sys
from pathlib import Path
from src.config import get_api_key_status, has_active_llm_key
from src.crew import run_research_pipeline

def print_banner():
    banner = """
======================================================================
         AI RESEARCH AND REPORT GENERATOR (CREWAI)                    
         Agentic AI & Multi-Agent Systems - Week 1 Project            
======================================================================
    """
    print(banner)

def main():
    print_banner()

    parser = argparse.ArgumentParser(
        description="AI Research and Report Generator using CrewAI multi-agent orchestration."
    )
    parser.add_argument(
        "--topic",
        type=str,
        default="Agentic AI & Multi-Agent Systems: Architecture, Orchestration, and Enterprise Adoption",
        help="The research topic to analyze and generate a report on."
    )
    parser.add_argument(
        "--output",
        type=str,
        default="outputs/sample_report_agentic_ai.md",
        help="Output file path where the final Markdown report will be saved."
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Force run in demo/simulation mode without connecting to remote LLM APIs."
    )
    parser.add_argument(
        "--check-env",
        action="store_true",
        help="Display the status of configured LLM API keys and exit."
    )

    args = parser.parse_args()

    # Display API Key status
    status = get_api_key_status()
    print("Environment Configuration:")
    for key, active in status.items():
        state = "[Configured]" if active else "[Not Set]"
        print(f"  * {key:20}: {state}")
    
    if args.check_env:
        sys.exit(0)

    print(f"\n[Target Topic] : {args.topic}")
    print(f"[Output File]  : {args.output}")
    print(f"[Execution Mode]: {'Demo / Local Simulation' if (args.demo or not has_active_llm_key()) else 'Live LLM Multi-Agent Orchestration'}")

    # Run the pipeline
    output_path = Path(args.output)
    report = run_research_pipeline(
        topic=args.topic,
        output_path=str(output_path),
        force_demo=args.demo
    )

    print("\n" + "="*70)
    print("  [SUCCESS] Project Execution Completed Successfully!")
    print(f"  Report generated ({len(report)} characters)")
    print(f"  Location: {output_path.resolve()}")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
