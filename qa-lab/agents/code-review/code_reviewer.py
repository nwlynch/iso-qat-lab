import re
from typing import List, Dict, Any

# --- SIMULATION CONSTANTS ---
# These simulate known best practices or vulnerabilities for checking purposes
SECURITY_RULES = {
    "database_query": "DO NOT use string formatting for SQL queries (SQL Injection risk). Use prepared statements.",
    "api_call": "Always validate input parameters before making an external API call."
}

def review_code_snippet(file_path: str, code_content: str) -> List[Dict[str, Any]]:
    """
    Simulates a static code analysis pass over a file snippet.
    Checks for common patterns indicative of bugs or vulnerabilities.
    """
    findings = []
    
    # 1. Security Review Check
    if "SELECT * FROM users WHERE id = " in code_content:
        findings.append({
            "description": "Potential SQL Injection Vulnerability.",
            "severity": "Blocker",
            "suggested_fix": SECURITY_RULES["database_query"],
            "location": f"Line 1 of {file_path}"
        })
        
    # 2. Best Practice Check (e.g., using synchronous calls)
    if "await some_function_sync()" in code_content:
        findings.append({
            "description": "Mixing async/await with synchronous calls is discouraged.",
            "severity": "Major",
            "suggested_fix": "Ensure all I/O operations use async/await pattern consistently.",
            "location": "Overall structure"
        })

    # 3. API Dependency Check
    if "fetch('external/api')" in code_content:
        findings.append({
            "description": "External API call detected. Lacks input validation.",
            "severity": "Major",
            "suggested_fix": SECURITY_RULES["api_call"],
            "location": "API call site"
        })
        
    return findings

def review_test_suite(test_files: List[str], code_content: str) -> List[Dict[str, Any]]:
    """
    Reviews the test suite structure for coverage gaps based on the code it tests.
    """
    coverage_gaps = []
    # Simulated analysis: If we see 'login' in the code, but no 'logout' test, raise a gap.
    if "login" in code_content and "logout" not in code_content:
        coverage_gaps.append({
            "description": "Incomplete coverage detected. The user session must include an explicit logout test case.",
            "severity": "Major",
            "suggested_fix": "Add a test case specifically for session termination (logout).",
            "location": "Test Coverage"
        })
        
    return coverage_gaps

def run_code_review(test_files: List[str], source_code_context: str) -> str:
    """
    Runs the full review process across code and tests.
    """
    print("--- Starting Code Review ---")
    all_findings = []
    
    # 1. Review the source code context
    code_findings = review_code_snippet(
        "SourceCodeContext", 
        source_code_context
    )
    all_findings.extend(code_findings)
    
    # 2. Review the test coverage provided by the tests
    test_findings = review_test_suite(
        test_files, 
        source_code_context
    )
    all_findings.extend(test_findings)
    
    # 3. Generate final report
    report_markdown = "# 🛡️ Code Review Findings\n\n"
    report_markdown += f"## Code Reviewed:\n{source_code_context[:100]}...\n\n"
    
    if not all_findings:
        report_markdown += "✅ No major issues found. Code quality is high for this iteration."
    else:
        report_markdown += "### Actionable Review Points\n"
        for i, finding in enumerate(all_findings):
            report_markdown += f"\n**{i+1}. {finding['description']}**\n"
            report_markdown += f"*   *Severity:* {finding['severity']}\n"
            report_markdown += f"*   *Suggestion:* {finding['suggested_fix']}\n"
            report_markdown += f"*   *Location:* {finding['location']}\n"
            
    return report_markdown

# Example usage:
if __name__ == "__main__":
    print("--- Running Code Review Agent ---")
    # Mock data for demonstration
    mock_code = "await page.locator('#user-id-field').setValue('123'); console.log('Hello'); fetch('external/api/data');"
    mock_test_files = ["test1.spec.ts"]
    
    report = run_code_review(mock_test_files, mock_code)
    print("\n\n=== CODE REVIEW REPORT ===\n")
    print(report)
