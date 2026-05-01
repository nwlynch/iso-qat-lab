# main.py - Agent Definition for QA Report Generator

from agent.adk.agents import Agent
from agent.adk.tools import FunctionTool
from auth import LocalAuthService

# --- 1. Initialize Authentication Service ---
auth_service = LocalAuthService()

# --- 2. Define Tools ---
def get_test_results(report_id: str) -> dict:
    """Fetches raw test execution results from the local metrics database based on a unique report ID."""
    print(f"--> Connecting to local metrics DB for report {report_id}...")
    # In a real implementation, this would query a local SQLite or local Postgres instance.
    return {
        "id": report_id, 
        "overall_status": "Completed", 
        "total_tests": 150, 
        "passed": 135, 
        "failed": 15, 
        "flaky": 0
    }

def summarize_failures(results: dict) -> str:
    """Analyzes the raw test results to generate a human-readable summary of failures."""
    if results.get("failed", 0) == 0:
        return "All tests passed successfully. The system is operating within defined quality parameters."
    
    failure_summary = (
        f"## ⚠️ Executive Summary of Key Failures\n"
        f"The QA cycle identified {results['failed']} critical test failures out of {results['total_tests']} tests. "
        f"While core pass rates are high ({results['passed']}/{results['total_tests']}), "
        f"the issues suggest instability in two key areas: Authentication and User Interface (UI). "
        f"Specifically, the intermittent Database Connection errors require immediate investigation "
        f"as they threaten the reliability of the core features."
    )
    return failure_summary

# Create tool instances
get_results_tool = FunctionTool(func=get_test_results, name="get_test_results")
summary_tool = FunctionTool(func=summarize_failures, name="summarize_failures")

# --- 2. Define Agent ---
qa_agent = Agent(
    name="QA Report Generator",
    model="qwen3.5:9b",  # Using our local, canonical model
    instruction="You are a Senior QA Analyst. Your role is to receive a raw report ID, fetch the raw test metrics, analyze the failures, and generate a professional, executive summary report in Markdown format.",
    tools=[get_results_tool, summary_tool],
    before_agent_callback=auth_service._authenticate_before_tool_call  # Run auth check before any tool execution
)

# 3. Agent Initialization Point (simulated entry point)
if __name__ == "__main__":
    print("--- QA Report Generator Initialized ---")
    print(f"Model: {qa_agent.model}")
    
    # Authenticate before any tool calls
    auth_token = auth_service.authenticate("qa-analyst", "local-secret")
    if not auth_token:
        print("❌ Agent cannot proceed without valid authentication.")
        print("Use: qa-report-generator main.py --token <your-token>")
        exit(1)
    
    print(f"✅ Authentication successful. Token: {auth_token.token}")
    print("Ready to process report IDs via the 'get_test_results' tool.")
    
