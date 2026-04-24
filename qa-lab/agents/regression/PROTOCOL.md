# Agent Protocol - Regression Agent
This file outlines the operational procedures, inputs, expected outputs, and communication standards for the Regression Agent.

## Purpose
The Regression Agent ensures that new changes do not introduce regressions by automatically running the full regression suite and comparing results to the established baseline.

## Inputs
- **Required:** Version Tag/Commit SHA, Defined baseline test suite, Execution environment.
- **Format:** Git references, Test suite configurations.

## Outputs
- **Required:** Regression Summary Report (JSON/YAML) listing all tests run, all tests passed, and all regressions detected (breaking changes).
- **Example Output Schema:** [Provide regression report schema].

## Workflow Guidelines
1. **Baseline:** Load the last known good test suite.
2. **Execute:** Run the entire regression suite against the current codebase.
3. **Compare:** Compare the results against the baseline report, flagging deviations.

---
*Last updated: YYYY-MM-DD*
