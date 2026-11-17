import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Ensure cache directory exists for CrewAI credentials on Windows
ROOT_DIR = Path(__file__).resolve().parent.parent
CACHE_DIR = ROOT_DIR / ".cache" / "localappdata"
CACHE_DIR.mkdir(parents=True, exist_ok=True)

if sys.platform == "win32":
    # If LOCALAPPDATA is unset or pointing to a restricted directory, point to local cache
    current_localappdata = os.environ.get("LOCALAPPDATA", "")
    if not current_localappdata or "AppData\\Local" in current_localappdata:
        try:
            # Test if writable
            test_dir = Path(current_localappdata) / "test_write_check"
            test_dir.mkdir(parents=True, exist_ok=True)
            test_dir.rmdir()
        except (PermissionError, OSError):
            os.environ["LOCALAPPDATA"] = str(CACHE_DIR)

# Disable CrewAI telemetry and OpenTelemetry tracing prompts
os.environ["CREWAI_TELEMETRY_OPT_OUT"] = "true"
os.environ["OTEL_SDK_DISABLED"] = "true"

# Load environment variables from .env file
load_dotenv(ROOT_DIR / ".env")

def get_api_key_status() -> dict:
    """Check which LLM provider API keys are available in the environment."""
    return {
        "OPENAI_API_KEY": bool(os.getenv("OPENAI_API_KEY")),
        "GEMINI_API_KEY": bool(os.getenv("GEMINI_API_KEY")),
        "GROQ_API_KEY": bool(os.getenv("GROQ_API_KEY")),
        "ANTHROPIC_API_KEY": bool(os.getenv("ANTHROPIC_API_KEY")),
    }

def has_active_llm_key() -> bool:
    """Return True if at least one LLM API key is present."""
    status = get_api_key_status()
    return any(status.values())

def get_configured_llm():
    """
    Returns a configured CrewAI LLM instance based on available environment variables.
    Returns None if no API key is detected.
    """
    if not has_active_llm_key():
        return None

    try:
        from crewai import LLM
        
        if os.getenv("OPENAI_API_KEY"):
            model_name = os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini")
            return LLM(model=model_name, temperature=0.7)
        elif os.getenv("GEMINI_API_KEY"):
            model_name = os.getenv("MODEL", "gemini/gemini-1.5-flash")
            return LLM(model=model_name, temperature=0.7, api_key=os.getenv("GEMINI_API_KEY"))
        elif os.getenv("GROQ_API_KEY"):
            model_name = os.getenv("MODEL", "groq/llama-3.1-70b-versatile")
            return LLM(model=model_name, temperature=0.7, api_key=os.getenv("GROQ_API_KEY"))
        elif os.getenv("ANTHROPIC_API_KEY"):
            model_name = os.getenv("MODEL", "anthropic/claude-3-5-sonnet-20241022")
            return LLM(model=model_name, temperature=0.7, api_key=os.getenv("ANTHROPIC_API_KEY"))
    except Exception as e:
        print(f"[Config Warning] Could not instantiate remote LLM ({e}). Falling back to simulation mode.")
        return None
