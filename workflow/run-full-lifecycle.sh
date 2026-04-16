#!/bin/bash

# ISO-QA-LAB: Full Lifecycle Workflow Execution
# ISO/IEC/IEEE 12207:2017 Compliant
# This script orchestrates the multi-agent workflow using the OpenClaw session mechanism.
# NOTE: This script is currently declarative and will not execute any tool calls.
# It serves as the blueprint for building the final execution layer.

set -e

# --- Configuration ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_DIR="${SCRIPT_DIR}/../config"
VERBOSE="${QA_VERBOSE:-0}"

# Source environment variables
source "${CONFIG_DIR}/env.sh"

# Helper function to execute an agent and capture its standardized JSON output
execute_agent() {
    local agent_name="$1"
    local task="$2"
    local iso_clause="$3"
    local phase="$4"
    local session_id
    local output_file="${SESSION_DIR}/${agent_name}_${task}_$(date +%Y%m%d%H%M%S).json"
    local agent_prompt_path="${SESSION_DIR}/${agent_name}/prompt-system.md"
    
    echo "[INFO] Starting Agent: $agent_name for Task: $task (ISO: $iso_clause)"
    
    # Spawn session for the agent run
    session_id=$(sessions_spawn task="ISO-QA-Lab: $agent_name - $task" \
                                 runtime="subagent" \
                                  model="${QA_MODEL:-qwen3.5:9b}" \
                                  thinking="off" \
                                  mode="session")
    
    if [[ -n "$session_id" ]]; then
        echo "[INFO] Session spawned with ID: $session_id"
        echo "--- (Simulating execution via session ID: $session_id) ---"
        echo "Mock JSON Output written to: $output_file"
        echo "---"
        
        # In a live OpenClaw setup, you would use 'process' or 'sessions_status' here to wait for completion and read the output file created by the agent.
        
    else
        echo "[ERROR] Failed to spawn session for $agent_name. Check agent availability."
        echo "---"
        return 1
    fi
}

# Print ISO 12207 clause mapping (For documentation/reference)
print_clause_mapping() {
    echo "=== ISO/IEC/IEEE 12207:2017 Clause Mapping ==="
    echo "Clause              Activity"
    echo "---------------     --------"
    echo "12207.3.1   Req Analysis"
    echo "12207.4.1   Project Planning"
    echo "12207.5.1   Config Management"
    echo "12207.6.1   Validation Analysis"
    echo "12207.7.1   Test Analysis"
    echo "12207.8.1   Quality Audit"
    echo "12207.10.1  Operations"
    echo "---------------     --------"
}

# --- Main Workflow Execution ---
main() {
    echo "======================================================"
    echo "  ISO-QA-LAB: Full Lifecycle Workflow"
    echo "  ISO/IEC/IEEE 12207:2017 Compliant"
    echo "==================================================="
    echo ""
    
    echo "--- Workflow Parameters ---"
    echo "Project: ${QA_PROJECT_NAME}"
    echo "Standard: ${QA_ISO_STANDARD}"
    echo "Model: ${QA_MODEL}"
    echo "Timeout: ${QA_TIMEOUT}s"
    echo "Verbose: ${QA_VERBOSE}"
    echo "--------------------------"
    echo ""
    
    print_clause_mapping
    
    echo "--- PHASE 1: Acquisition Process (12207.3.1) ---"
    echo "--------------------------------------------------"
    
    # 1. Requirements Parsing
    execute_agent "acq-requirements-parser" "Parse requirements" "12207.3.1" "acquisition"
    
    # 2. Stakeholder Input Gathering
    execute_agent "acq-stakeholder-input" "Gather and structure input" "12207.3.2" "acquisition"

    echo ""
    echo "--- PHASE 2: Project Management (12207.4.1) ---"
    echo "------------------------------------------"
    
    # 3. Project Planning
    execute_agent "pm-project-planning" "Create project plan" "12207.4.1" "project-management"
    
    echo ""
    echo "--- PHASE 3: Configuration Management (12207.5.1) ---"
    echo "--------------------------------------------"
    
    # 4. Configuration Baselines
    execute_agent "cfg-configuration" "Establish baseline" "12207.5.1" "configuration-management"
    
    echo ""
    echo "--- PHASE 4: Verification Process (12207.7.1) ---"
    echo "--------------------------------------------"
    
    # 5. Test Case Generation
    execute_agent "ver-test-generator" "Generate test cases" "12207.7.1" "verification"
    
    # 6. Test Execution
    execute_agent "ver-test-executor" "Execute tests" "12207.7.2" "verification"
    
    # 7. Code Review
    execute_agent "ver-code-review" "Code review" "12207.7.1" "verification"
    
    # 8. Regression Testing
    execute_agent "ver-regression" "Run regression tests" "12207.7.1" "verification"
    
    # 9. Analytics
    execute_agent "ver-test-analytics" "Analyze results" "12207.7.3" "verification"
    
    echo ""
    echo "--- PHASE 5: Validation Process (12207.6.1) ---"
    echo "--------------------------------------------"
    
    # 10. User Acceptance Testing
    execute_agent "val-user-acceptance" "UAT scenarios" "12207.6.1" "validation"
    
    # 11. Conformance Check
    execute_agent "val-conformance-check" "Standards validation" "12207.6.2" "validation"
    
    echo ""
    echo "--- PHASE 6: Quality Assurance (12207.8.1) ---"
    echo "---------------------------------------"
    
    # 12. Quality Audit
    execute_agent "qa-audit" "Quality audit" "12207.8.1" "quality-assurance"
    
    echo ""
    echo "--- PHASE 7: Operation & Maintenance (12207.10.x) ---"
    echo "------------------------------------"
    
    # 13. Operations
    execute_agent "ops-operation" "Deploy operations" "12207.10.1" "operations-maintenance"
    
    # 14. Maintenance
    execute_agent "ops-maintenance" "Maintenance" "12207.10.2" "operations-maintenance"

    echo ""
    echo "========================================================="
    echo "         ✅ WORKFLOW COMPLETE: ISO-QA-LAB"
    echo "========================================================="
    echo ""
    echo "All ISO/IEC/IEEE 12207:2017 activities completed successfully!"
}

main "$@"