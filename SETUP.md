# 🛠️ Setup Guide: Getting Started with the QA Lab v1.0.0
Welcome to the ISO-QA-Lab! This guide walks you through setting up the environment and running the automated quality assurance cycle.

## 🚀 Prerequisites
Before starting, ensure you have the following installed:
1.  **Python 3.x:** For running agent logic (pip).
2.  **Node.js:** Required for Playwright test execution (npm).
3.  **Git:** For source control.
4.  **Recommended Environment:** **Windows Subsystem for Linux (WSL) with Bash** is highly recommended due to the script dependencies (`.sh` files).

## 🛠️ Step 1: Environment Setup
1.  **Install Python Dependencies:** Navigate to the root directory and install the necessary Python libraries:
    \`\`\`bash
    pip install -r requirements.txt
    \`\`\`
2.  **Install Node Dependencies:** Navigate to the root directory and install Playwright:
    \`\`\`bash
    npm install playwright
    npx playwright install
    \`\`\`

## 💡 Running the Full Cycle (The Primary Workflow)
The entire process is now orchestrated by `run-full-lifecycle.sh`. **Always run this script.**

\`\`\`bash
./run-full-lifecycle.sh
\`\`\`

**What it does:**
1.  Generates all necessary test artifacts from mock requirements.
2.  Executes the generated Playwright tests.
3.  Analyzes the raw results to provide a summary report.

## 💻 Platform Specific Notes

**For Windows PowerShell Users:**
If running in a native PowerShell environment, the core workflow is managed by the dedicated PowerShell script: `./run-full-lifecycle.ps1`. This script handles the necessary PowerShell syntax conversions for the agent calls.

## 📄 Understanding the Output
*   **`qa-lab/agents/test-generator/docs/`:** Contains generated test reports and initial test cases.
*   **`qa-lab/agents/analytics/analyzer.py`:** The final Markdown report here contains actionable insights derived from the run.

**Next Steps:**
1.  Run the full lifecycle script.
2.  Inspect the final report for mandatory fixes.
3.  Proceed to development tasks (e.g., developing the Bug Hunter Agent logic).
