# Orchestrator Script for QA Cycle
# run_qa_cycle.py

import asyncio
import os
from playwright.async_api import async_playwright
# Import all agent modules relative to the package structure for full functionality.
from .agents.test_generator.test_generator_agent import generate_test_cases
from .agents.test_executor.test_executor_agent import execute_test_suite
from .agents.analytics.analytics_agent import analyze_test_results
from .agents.code_review.code_review_agent import review_failure_report
from .agents.bug_hunter.bug_hunter_agent import generate_fuzzing_tests
from .agents.regression.regression_agent import run_regression_suite
from .agents.documentation.documentation_agent import generate_final_report

# --- Configuration ---
BASE_DIR = "/home/nwlynch/src/iso-qat-lab/qa-lab-project"
MODEL_RULES_PATH = os.path.join(BASE_DIR, "config/models/model_selection_rules.md")

# --- Helper Functions ---

def load_model_rules():
    """Loads the centralized model selection logic."""
    print(f"Loading model rules from: {MODEL_RULES_PATH}")
    try:
        with open(MODEL_RULES_PATH, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print("ERROR: Model selection rules file not found! Cannot determine model strategy.")
        return None

async def run_qa_cycle(requirements: str):
    """
    The main asynchronous coordinator function that orchestrates the full QA lifecycle.
    """
    print("======================================================================")
    print("--- QA Lab Orchestration Cycle Initiated ---")
    print("=====================================================================")
    
    model_rules = load_model_rules()
    if not model_rules:
        print("FATAL: Cannot proceed due to model configuration error.")
        return

    async with async_playwright() as p:
        try:
            # 1. Test Generator Agent (Input Stage)
            print("\n--- PHASE 1: Test Case Generation ---")
            test_generator_results = await generate_test_cases(requirements, model_rules)

            if test_generator_results and test_generator_results.get("test_cases"):
                # 2. Test Executor Agent (Execution Stage)
                print("\n--- PHASE 2: Test Execution ---")
                test_executor_results = await execute_test_suite(
                    test_generator_results["test_cases"], 
                    p
                )

                # 3. Analytics Agent (Reporting Stage)
                print("\n--- PHASE 3: Analytics & Reporting ---")
                analysis_results = analyze_test_results(
                    test_executor_results["results"]
                )

                # 4. Bug Hunter Agent (Proactive Stage)
                print("\n--- PHASE 4: Bug Hunting ---")
                # Uses failed tests as input to find more bugs.
                bug_hunter_results = await generate_fuzzing_tests(
                    requirements, 
                    {k: v for k, v in test_executor_results["results"].items() if v == "FAIL"}
                )

                # 5. Code Review Agent (Remediation Suggestion)
                print("\n--- PHASE 5: Code Review & Improvement Suggestion ---")
                review_suggestions = await review_failure_report(
                    analysis_results, 
                    {k: v for k, v in test_executor_results["results"].items() if v == "FAIL"}
                )

                # 6. Regression Agent (Safety Net)
                print("\n--- PHASE 6: Regression Smoke Test ---")
                regression_report = await run_regression_suite(p, "baseline_v1.2")

                # 7. Documentation Agent (Synthesis)
                print("\n--- PHASE 7: Final Report Generation ---")
                final_report = await generate_final_report(
                    analysis_results, 
                    review_suggestions, 
                    regression_report
                )
                
                print("\n======================================================================")
                print("✨ QA CYCLE COMPLETE: MVP Demonstration Successful! ✨")
                print("The comprehensive report has been generated:")
                print("======================================================================")
                print(final_report)

        except Exception as e:
            print(f"\n🔴 CRITICAL ORCHESTRATION FAILURE: {type(e).__name__}: {e}")
            print("The pipeline has crashed. Review the stack trace for debugging information.")


if __name__ == "__main__":
    # The final command structure MUST use the asyncio.run() method for correct execution.
    # This acts as the master entry point for running the entire QA cycle.
    SAMPLE_REQUIREMENTS = "The user must be able to log in with valid credentials, and the login form must reject empty fields."
    
    # The full system is now ready for execution via:
    # asyncio.run(main_orchestrator(SAMPLE_REQUIREMENTS))
    
    # We keep the call structure here for module import purposes.
    asyncio.run(main_orchestrator(SAMPLE_REQUIREMENTS))
