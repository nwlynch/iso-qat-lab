# Test Executor Agent Module (test_executor_agent.py)
# This module encapsulates all Playwright interaction for running automated tests.
# Dependencies: playwright library, browser context.

from playwright.async_api import async_playwright, Playwright
from typing import List, Dict, Any

async def execute_test_suite(test_cases: List[Dict[str, str]], playwright_context: async_playwright) -> dict:
    """
    Runs a batch of test cases using Playwright across multiple contexts/pages.
    :param test_cases: List of dictionaries containing test metadata from Test Generator.
    :param playwright_context: The active Playwright context managed by the orchestrator.
    :return: A dictionary containing execution results per test ID.
    """
    print(f"--- [Test Executor] Starting execution for {len(test_cases)} tests ---")
    results = {}
    
    # We use one primary page context for efficiency, rather than spawning a new browser for every test.
    async with playwright_context.new_page() as page:
        for case in test_cases:
            test_id = case.get("id", "UNKNOWN")
            test_desc = case.get("description", "No description")
            
            print(f"\n[RUNNING] Test ID: {test_id} | Desc: {test_desc}...")
            
            try:
                # 1. Setup: Navigate to the base URL.
                await page.goto("http://localhost:3000/login", wait_until="domcontentloaded")
                
                # 2. Action: Simulate filling credentials and clicking the button.
                # Robust action sequence based on typical login flow.
                await page.wait_for_selector("#username", timeout=8000)
                await page.fill("#username", "user@example.com")
                await page.fill("#password", "securepass123")
                await page.click("#login-button")
                
                # 3. Assertion: Check the final state.
                # We wait for a known element on the dashboard page to confirm success.
                await page.wait_for_selector("text=Welcome Dashboard", timeout=10000)
                
                results[test_id] = "PASS"
                print(f"  [SUCCESS] Test {test_id} passed.")

            except Exception as e:
                # Catch all playwright exceptions (Timeout, SelectorNotFound, etc.)
                error_message = f"Execution failed: {type(e).__name__}: {str(e)}"
                results[test_id] = "FAIL"
                print(f"  [FAILURE] Test {test_id} failed. Error: {error_message[:100]}...")
        
    print("--- [Test Executor] Execution batch complete. ---")
    return {"results": results, "status": "EXECUTED"}

# Example usage (for testing the module in isolation)
async def main_test_run():
    # This function should not be called directly if the orchestrator is running.
    print("--- Running Test Executor Module Test ---")
    # A dummy list of test cases for self-test
    dummy_cases = [
        {"id": "L-001", "type": "E2E", "description": "Successful login with valid credentials", "framework": "Playwright", "priority": "High"}
    ]
    async with async_playwright() as p:
        await execute_test_suite(dummy_cases, p)

if __name__ == "__main__":
    # This allows the module to be run directly for isolated debugging.
    import asyncio
    asyncio.run(main_test_run())
