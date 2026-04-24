import random
import string
from typing import List, Dict, Any

def generate_fuzz_input(target_field: str, max_length: int = 20) -> str:
    """
    Generates a random, semi-valid input string for fuzz testing.
    """
    # Combination of random chars, numbers, and common symbols
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_+=[]{}<>?/`~"
    length = random.randint(5, max_length)
    return ''.join(random.choice(chars) for _ in range(length))

def find_boundary_conditions(field_name: str) -> List[str]:
    """
    Suggests critical boundary values for a given input field.
    """
    if "user_id" in field_name:
        return ["0", "1", "999999999999", "MAX_INT"]
    elif "email" in field_name:
        return ["a@b.c", "invalid", "test+spam@domain.com"]
    return ["default", "empty"]

def generate_bug_report(findings: List[Dict[str, Any]]) -> str:
    """
    Compiles all findings into a comprehensive, actionable Markdown report.
    """
    report = "# 🐛 Bug Hunter Report\n\n"
    report += "## Summary\n"
    report += f"The Bug Hunter Agent scanned for vulnerabilities, finding {len(findings)} potential issues.\n\n"
    
    if not findings:
        report += "No critical bugs were detected based on current constraints."
        return report

    report += "### Detected Vulnerabilities\n"
    for i, finding in enumerate(findings):
        report += f"\n#### {i+1}. {finding['description']}\n"
        report += f"*   **Severity:** {finding['severity']}\n"
        report += f"*   **Trigger:** {finding['trigger_condition']}\n"
        report += f"*   **Suggested Fix:** {finding['suggestion']}\n"
    
    return report

def run_fuzzing_test(target_field: str, selector: str) -> Dict[str, Any]:
    """
    Simulates running a specific fuzzing test case.
    """
    fuzz_input = generate_fuzz_input(target_field)
    print(f"Attempting fuzz test on '{target_field}' with input: {fuzz_input}")
    
    # Simulate finding a bug
    if "user" in target_field.lower() and "fail" in fuzz_input.lower():
        return {
            "description": f"Potential XSS vulnerability detected via input: {fuzz_input}",
            "severity": "Critical",
            "trigger_condition": f"Input field '{target_field}' accepts script tags.",
            "suggestion": "Implement proper output encoding for all user-submitted fields."
        }
    return {"description": "No bug found.", "severity": "Informational", "trigger_condition": "N/A", "suggestion": "N/A"}


# Example usage:
if __name__ == "__main__":
    print("--- Bug Hunter Agent Initialized ---")
    
    # 1. Find boundary conditions
    user_id_boundaries = find_boundary_conditions("user_id")
    print(f"Boundary conditions found for user ID: {user_id_boundaries}")
    
    # 2. Run a test for each boundary/fuzz input
    all_findings = []
    
    # Test 1: Boundary check (ID)
    bug1 = run_fuzzing_test("user_id", "#user-id-field")
    all_findings.append(bug1)
    
    # Test 2: Fuzz check (Email)
    bug2 = run_fuzzing_test("email", "#email-input")
    all_findings.append(bug2)

    # 3. Generate final report
    final_report = generate_bug_report(all_findings)
    print("\n============================================")
    print("BUGS FOUND:")
    print(final_report)
