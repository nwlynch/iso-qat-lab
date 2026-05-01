# chaos_runner.py - Resilience Testing Module

from agent.adk.agents import Agent
from agent.adk.tools import FunctionTool
import time
import random

# --- 1. Failure Simulation Utilities ---

def simulate_network_timeout(service_name: str, duration: float) -> Exception:
    """Raises a simulated network timeout error."""
    print(f"\n!!! 🚨 CHAOS INJECTOR: Simulating NETWORK PARTITION to {service_name} for {duration} seconds. !!! 🚨")
    # In a real system, this would raise a dedicated Timeout exception.
    time.sleep(duration) 
    raise TimeoutError(f"Network connection failed to {service_name}.")

def simulate_resource_exhaustion(resource: str, duration: float):
    """Simulates running out of CPU or Memory."""
    print(f"\n!!! 💥 CHAOS INJECTOR: Simulating {resource} exhaustion for {duration} seconds. !!! 💥")
    # In a real system, this would trigger a MemoryError or CPU overload hook.
    time.sleep(duration)
    raise MemoryError(f"Insufficient {resource} resources available.")

# --- 2. Enhanced Tool Implementation for Chaos Testing ---

def get_test_results(report_id: str, simulate_failure: str = None, failure_duration: float = 0.0) -> dict:
    """
    Fetches raw test execution results, with optional chaos injection capability.
    (Enhanced to handle failure simulation)
    """
    if simulate_failure:
        if simulate_failure == "network_timeout":
            # This failure must be explicitly handled by the calling function
            simulate_network_timeout("local metrics DB", failure_duration)
            # If it gets here, the failure was not caught, which is bad.
            return {"error": "Test DB connection failed due to simulation."}
        elif simulate_failure == "memory_error":
            simulate_resource_exhaustion("Memory", failure_duration)
            return {"error": "Test DB read failed due to memory constraints."}

    print(f"--> Connecting to local metrics DB for report {report_id}...")
    # Original successful logic returns here if no failure was simulated.
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
    # The summary logic remains the same, as it is assumed to be resilient to tool failure.
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

# --- 2. Define Agent (Updated to support chaos context) ---
qa_agent = Agent(
    name="QA Report Generator (Resilient)",
    model="qwen3.5:9b",
    instruction="You are a Senior QA Analyst. Your role is to execute the entire report cycle. CRITICAL: If the test results tool fails due to a simulated failure (network/memory), do not panic. Your fallback is to log the error and continue with best-effort analysis.",
    tools=[get_results_tool, summary_tool],
    before_agent_callback=None
)
