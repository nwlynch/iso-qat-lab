#!/bin/bash

# ISO-QA-Lab Environment Variables
# ISO/IEC/IEEE 12207:2017 Compliant Multi-Agent QA Testing Lab

# ===========================
# Environment Variable Descriptions
# ===========================

# Verbose Mode - Enable detailed status output
# Set to 1 for verbose output with timestamps, resources, steps
# Default: 0 (concise output)
QA_VERBOSE=0

# Model to use for agents
# Options: qwen3.5:9b (default), deepseek-coder-v2:16b, phi4:14b, etc.
# See config/models.yaml for available models
QA_MODEL=qwen3.5:9b

# Timeout for agent execution in seconds
# Default: 600 seconds (10 minutes)
QA_TIMEOUT=600
INFERENCETIMOUT=300

# Log level - DEBUG, INFO, WARN, ERROR
# Only used in verbose mode
QA_LOG_LEVEL=INFO

# Project name
QA_PROJECT_NAME=ISO-QA-Lab

# ISO standard version
QA_ISO_STANDARD="ISO/IEC/IEEE 12207:2017"

# ===========================
# Helper Functions
# ===========================

# Check if verbose mode is enabled
is_verbose() {
    [[ "${QA_VERBOSE}" == "1" ]]
}

# Log with timestamp (only in verbose mode)
log_verbose() {
    if is_verbose; then
        local timestamp
        timestamp=$(date -Iseconds)
        local tokens=""
        local time_ms=""
        echo "[$timestamp] [ACTION: $1]"
        echo "[$timestamp] [MODEL: ${QA_MODEL:-qwen3.5:9b}]"
    fi
}

# Log with timestamp (always)
log_info() {
    local timestamp
    timestamp=$(date -Iseconds)
    echo "[$timestamp] [INFO] $1"
}

# Log error
log_error() {
    local timestamp
    timestamp=$(date -Iseconds)
    echo "[$timestamp] [ERROR] $1" >&2
}

# Check available models
list_models() {
    log_info "Available models in sandbox:"
    echo "  - qwen3.5:9b (6.6 GB) - Default for most agents"
    echo "  - deepseek-coder-v2:16b (8.9 GB) - Code tasks"
    echo "  - phi4:14b (9.1 GB) - Bug hunting, reasoning"
    echo "  - llama3.1:8b (4.9 GB) - Fast inference"
    echo "  - mixtral:8x7b (26 GB) - Complex reasoning"
    echo "  - llava:7b (4.7 GB) - Vision tasks"
    echo "  - gemma4 models (7-9.6 GB) - High performance"
    echo "  - Total: 20+ models available"
}

# Validate environment
validate_env() {
    log_info "Validating environment..."
    
    if [[ -z "${QA_MODEL}" ]]; then
        log_error "QA_MODEL is not set"
        return 1
    fi
    
    if [[ "${QA_VERBOSE}" != "0" ]] && [[ "${QA_VERBOSE}" != "1" ]]; then
        log_error "QA_VERBOSE must be 0 or 1"
        return 1
    fi
    
    if [[ "${QA_TIMEOUT}" -lt 300 ]]; then
        log_error "QA_TIMEOUT must be at least 300 seconds"
        return 1
    fi
    
    log_info "Environment validation passed"
    return 0
}

# Print status
print_status() {
    log_info "ISO-QA-Lab Status"
    echo "  Project: ${QA_PROJECT_NAME}"
    echo "  Standard: ${QA_ISO_STANDARD}"
    echo "  Model: ${QA_MODEL}"
    echo "  Verbose: ${QA_VERBOSE}"
    echo "  Timeout: ${QA_TIMEOUT}s"
    echo "  Log Level: ${QA_LOG_LEVEL}"
}

# ===========================
# Usage
# ===========================

usage() {
    echo "Usage: $0 <command> [options]"
    echo ""
    echo "Commands:"
    echo "  status           Print current environment status"
    echo "  list-models      List available models"
    echo "  validate         Validate environment settings"
    echo "  reset            Reset to defaults"
    echo "  help             Show this help"
    echo ""
    echo "Examples:"
    echo "  $0 status"
    echo "  $0 list-models"
    echo "  export QA_VERBOSE=1 && $0 validate"
    echo "  $0 reset"
}

# Main entry point
case "${1:-}" in
    status)
        print_status
        ;;
    list-models)
        list_models
        ;;
    validate)
        validate_env
        ;;
    reset)
        export QA_VERBOSE=0
        export QA_MODEL=qwen3.5:9b
        export QA_TIMEOUT=600
        export QA_LOG_LEVEL=INFO
        log_info "Environment reset to defaults"
        print_status
        ;;
    help|--help|-h|"")
        usage
        ;;
    *)
        echo "Unknown command: $1"
        usage
        exit 1
        ;;
esac
