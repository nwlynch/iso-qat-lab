# Orchestrator Script for QA Cycle
# run_qa_cycle.py

import asyncio
import os
from playwright.async_api import async_playwright
# Import all the agent modules, using relative imports for package structure
# Note: Module import paths must reflect the correct package path structure.
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

async def run_qa_cycle(requirements: str):
    """
    The main asynchronous coordinator function that runs the full QA lifecycle.
    This function manages the context (Playwright) and orchestrates calls between agents.
    """
    print("=====================================================================")
    print("--- QA Lab Orchestration Cycle Initiated ---")
    print("=========================================================")
    
    model_rules = load_model_rules()
    if not model_rules:
        print("FATAL: Cannot proceed due to model configuration error.")
        return

    async with async_playwright() as p:
        try:
            # 1. Test Generator Agent
            print("\n--- PHASE 1: Test Case Generation ---")
            test_generator_results = await generate_test_cases(requirements, model_rules)

            if test_generator_results and test_generator_results.get("test_cases"):
                # 2. Test Executor Agent (Requires Playwright context 'p')
                print("\n--- PHASE 2: Test Execution ---")
                test_executor_results = await execute_test_suite(
                    test_generator_results["test_cases"], 
                    p
                )

                # 3. Analytics Agent (Uses results from Executor)
                print("\n--- PHASE 3: Analytics & Reporting ---")
                analysis_results = analyze_test_results(
                    test_executor_results["results"]
                )

                # 4. Bug Hunter Agent (Acts on failures to find new weaknesses)
                print("\n--- PHASE 4: Bug Hunting ---")
                bug_hunter_results = await generate_fuzzing_tests(
                    requirements, 
                    {k: v for k, v in test_executor_results["results"].items() if v == "FAIL"}
                )

                # 5. Code Review Agent (Feeds its report back into the process)
                print("\n--- PHASE 5: Code Review & Improvement Suggestion ---")
                review_suggestions = await review_failure_report(
                    analysis_results, 
                    {k: v for k, v in test_executor_results["results"].items() if v == "FAIL"}
                )

                # 6. Regression Agent (Checks if new failures broke old functionality)
                print("\n--- PHASE 6: Regression Smoke Test ---")
                regression_report = await run_regression_suite(p, "baseline_v1.2")

                # 7. Documentation Agent (Synthesis)
                print("\n--- PHASE 7: Final Report Generation ---")
                final_report = await generate_final_report(
                    analysis_results, 
                    review_suggestions, 
                    regression_report
                )
                
                print("\n=========================================================")
                print("✨ QA CYCLE COMPLETE ✨")
                print("The comprehensive report has been generated:")
                print("=========================================================")
                print(final_report)
            else:
                print("\n[HALT] Cannot proceed. Test Generation failed.")


# Initialization Logic to handle the initial execution context setup
async def main_orchestrator(requirements: str):
    await run_qa_cycle(requirements)


if __name__ == "__main__":
    # Use the absolute path for execution compatibility.
    # This function call now drives the entire async workflow.
    asyncio.run(main_orchestrator("The user must be able to log in with valid credentials, and the login form must reject empty fields."))