# ISO-QA-Lab - ISO/IEC/IEEE 12207:2017 Compliance Structure

## Project Name: ISO-QA-Lab

This multi-agent QA testing lab is organized to comply with **ISO/IEC/IEEE 12207:2017** - Software and System Life Cycle Processes.

---

## 🏗️ ISO/IEC/IEEE 12207:2017 Process Organization

### 1. Acquisition Process
Handles requirements gathering and acquisition activities.

**Agents:**
- `acq-requirements-parser/` - Parses and analyzes requirements documents
- `acq-stakeholder-input/` - Manages stakeholder feedback collection

### 2. Project Management Process
Plans, manages, and controls project activities.

**Agents:**
- `pm-project-planning/` - Creates project plans and schedules
- `pm-risks-management/` - Identifies and mitigates project risks
- `pm-cost-estimation/` - Estimates project costs and resources

### 3. Product Management Process
Manages the product lifecycle from inception to retirement.

**Agents:**
- `pm-product-lifecycle/` - Tracks product lifecycle stages
- `pm-delivery-mgmt/` - Manages product delivery activities

### 4. Verification Process
Provides evidence that software products meet specified requirements.

**Agents:**
- `ver-test-generator/` - Creates test cases from requirements
- `ver-test-executor/` - Executes tests and captures results
- `ver-test-analytics/` - Analyzes test results and generates insights
- `ver-code-review/` - Reviews code for bugs and quality
- `ver-regression/` - Runs regression test suites

### 5. Validation Process
Provides evidence that product meets user needs and intended use.

**Agents:**
- `val-user-acceptance/` - Manages UAT scenarios
- `val-conformance-check/` - Validates against standards and regulations

### 6. Quality Assurance Process
Monitors and improves quality throughout the life cycle.

**Agents:**
- `qa-audit/` - Performs quality audits
- `qa-improvement/` - Implements quality improvements
- `qa-bug-hunter/` - Actively searches for issues

### 7. Configuration Management Process
Manages product configuration and baselines.

**Agents:**
- `cfg-configuration/` - Manages configuration items
- `cfg-baseline/` - Creates and manages baselines
- `cfg-logging/` - Handles logging and reporting

### 8. Operation Support and Maintenance Process
Supports operations and maintains the product.

**Agents:**
- `ops-operation/` - Handles daily operations
- `ops-maintenance/` - Manages maintenance activities
- `ops-monitoring/` - Monitors system health

### 9. Supplier Process
Manages supplier relationships.

**Agents:**
- `sup-supplier-mgmt/` - Manages supplier relationships
- `sup-qualification/` - Qualifies and evaluates suppliers

### 10. Organizational Process
Manages organizational assets and improvements.

**Agents:**
- `org-process-improvement/` - Captures and shares lessons learned
- `org-knowledge-base/` - Maintains organizational knowledge

---

## 🔄 Lifecycle Workflows

The agents orchestrate across lifecycle phases:

```
Acquisition → Project Planning → Configuration → Verification → Validation → Quality → Operations → Maintenance → Retirement
```

---

## 📋 Environment Variables

### Verbose Mode
Set `QA_VERBOSE=1` to enable detailed status output for all agents.

Example verbose output includes:
- Agent execution timestamps
- Model parameters used
- Resource consumption metrics
- Detailed step-by-step progress
- Error logs with stack traces

### Available Variables
```bash
export QA_VERBOSE=1          # Enable verbose mode
export QA_MODEL=qwen3.5:9b   # Model override
export QA_TIMEOUT=600        # Agent timeout in seconds
export QA_LOG_LEVEL=DEBUG    # Logging level
```

---

## 🎯 Quick Start

```bash
# Enable verbose mode
export QA_VERBOSE=1

# Initialize agent
./agents/ver-test-generator/run.sh

# Run full lifecycle workflow
./workflow/lifecycle.sh
```
