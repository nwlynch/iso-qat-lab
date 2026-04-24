import json
from typing import Dict, Any, List

# Assume a function/method exists to load the previous successful baseline report/state
def load_baseline_report(target_component: str) -> Dict[str, Any]:
    """
    Loads the last known good state (the baseline) for a given component.
    In a real system, this would query a dedicated storage or artifact store.
    """
    print(f"Simulating loading baseline for {target_component}...")
    # Placeholder: Simulating a successful load of a previous successful run's results.
    return {
        "test_suite_name": "Initial Core Suite",
        "baseline_metrics": {
            "total_tests": 5,
            "passed": 5,
            "failed": 0,
            "flakiness_score": 0.0
        },
        "baseline_report": "Simulated Baseline Report Content..."
    }

def run_regression_test(component_name: str, current_test_report_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Compares the current execution metrics against the stored baseline.
    """
    print(f"Comparing current run against baseline for component: {component_name}")
    
    # 1. Load Baseline
    baseline = load_baseline_report(component_name)
    
    # 2. Comparison Logic
    report = {"regressions_found": []}
    
    # Check for functional regression (e.g., did a test that passed before now fail?)
    if current_test_report_data.get("failed", 0) > baseline['baseline_metrics']['failed']:
        report["regressions_found"].append({
            "description": "Regression Alert: New failures detected in critical paths.",
            "severity": "High",
            "details": f"Baseline failures: {baseline['baseline_metrics']['failed']} vs Current failures: {current_test_report_data.get('failed', 0)}."
        })
    
    # Check for performance regression (e.g., did the execution time spike?)
    if current_test_report_data.get("duration_ms", 0) > baseline['baseline_metrics'].get('duration_ms', 0) * 1.5:
        report["regressions_found"].append({
            "description": "Performance Regression: Execution time is significantly slower than baseline.",
            "severity": "Medium",
            "details": f"Baseline Time: {baseline['baseline_metrics'].get('duration_ms', 0)}ms vs Current Time: {current_test_report_data.get('duration_ms', 0)}ms."
        })
        
    return report

def generate_regression_report(regression_report: Dict[str, Any], raw_report: str) -> str:
    """
    Generates the final markdown report, detailing regressions found.
    """
    report = "# 🔁 Regression Test Report\n\n"
    report += "## Executive Summary\n"
    
    if not regression_report['regressions_found']:
        report += "✅ Regression check passed. The current codebase maintains stability against the established baseline."
    else:
        report += f"❌ WARNING: {len(regression_report['regressions_found'])} regressions detected. IMMEDIATE ACTION REQUIRED."
        
        for i, finding in enumerate(regression_report['regressions_found']):
            report += f"\n### Regression {i+1}: {finding['description']} ({finding['severity']})\n"
            report += f"*   **Details:** {finding['details']}\n"
            
    return report


# Example usage:
if __name__ == "__main__":
    print("--- Regression Agent Initialized ---")
    
    # Mock current report data (simplified metrics)
    current_metrics = {
        "total_tests": 5,
        "passed": 3,
        "failed": 2, # Increased from baseline
        "duration_ms": 1500, # Increased from baseline
        "flakiness_score": 0.3
    }
    
    # 1. Run comparison
    report_data = run_regression_test("User Auth Module", {"failed": 2, "duration_ms": 1500})
    
    # 2. Generate final report
    final_report = generate_regression_report(report_data, "Simulated Raw Report...")
    print("\n==============================================")
    print("FINAL REGRESSION REPORT")
    print("==============================================")
    print(final_report)
