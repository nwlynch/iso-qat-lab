# Agent Protocol - Code Review Agent
This file outlines the operational procedures, inputs, expected outputs, and communication standards for the Code Review Agent.

## Purpose
The Code Review Agent examines code changes (PRs) to identify potential bugs, vulnerabilities, and areas for test improvement before merging.

## Inputs
- **Required:** Git diff/Pull Request details, Component specification, High-level requirements.
- **Format:** Diff format (Unified/Patch).

## Outputs
- **Required:** A list of detailed comments and suggested changes (JSON/Markdown) structured by severity (Blocker, Major, Minor).
- **Example Output Schema:** [Provide structured comment schema].

## Workflow Guidelines
1. **Review:** Methodically check code paths against best practices and security guidelines.
2. **Suggest:** Formulate non-trivial, actionable suggestions.
3. **Report:** Output the findings clearly, separating bugs from suggestions.

---
*Last updated: YYYY-MM-DD*
