# ISO-QA-Lab

**ISO/IEC/IEEE 12207:2017 Compliant Multi-Agent QA Testing Lab**

## 📋 Overview

ISO-QA-Lab is a comprehensive multi-agent QA testing system organized according to the **ISO/IEC/IEEE 12207:2017** Software and System Life Cycle Processes standard.

### 🎯 What is ISO/IEC/IEEE 12207:2017?

The **Software and System Life Cycle Processes** standard defines:
- **Acquisition Process** - Requirements gathering
- **Project Management Process** - Planning and control
- **Product Management Process** - Product lifecycle
- **Configuration Management Process** - Change control
- **Quality Assurance Process** - Quality monitoring
- **Operation Support & Maintenance Process** - Operations
- **Supplier Process** - Supplier management
- **Organizational Process** - Organizational assets
- **Monitoring & Evaluation Process** - Monitoring activities
- **Validation Process** - User acceptance
- **Verification Process** - Testing and validation

### 🚀 Quick Start

```bash
# Load environment
source config/env.sh

# Enable verbose mode
export QA_VERBOSE=1

# Run full lifecycle workflow
./workflow/full-lifecycle
```

### 🔧 Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `QA_VERBOSE` | 0 | Enable detailed status output (1) |
| `QA_MODEL` | qwen3.5:9b | Model to use for agents |
| `QA_TIMEOUT` | 600 | Agent timeout in seconds |
| `QA_LOG_LEVEL` | INFO | Logging level (DEBUG/INFO/WARN/ERROR) |

### 📦 Available Models

- **qwen3.5:9b** (6.6 GB) - Default, general QA tasks
- **deepseek-coder-v2:16b** (8.9 GB) - Code review, generation
- **phi4:14b** (9.1 GB) - Bug hunting, reasoning
- **llama3.1:8b** (4.9 GB) - Fast inference
- **mixtral:8x7b** (26 GB) - Complex reasoning
- **llava:7b** (4.7 GB) - Vision tasks
- **gemma4** series - High performance models

### 🏗️ Agent Architecture

#### Acquisition Process
- `acq-requirements-parser` - Parse requirements documents (12207.3.1)
- `acq-stakeholder-input` - Manage stakeholder feedback (12207.3.2)

#### Project Management Process
- `pm-project-planning` - Create project plans (12207.4.1)
- `pm-risks-management` - Risk management (12207.4.2)
- `pm-cost-estimation` - Cost estimation (12207.4.3)

#### Product Management Process
- `pm-product-lifecycle` - Lifecycle tracking
- `pm-delivery-mgmt` - Delivery management

#### Configuration Management Process
- `cfg-configuration` - Manage CIs (12207.5.1)
- `cfg-baseline` - Baseline management (12207.5.2)
- `cfg-logging` - Logging and reporting (12207.5.3)

#### Verification Process
- `ver-test-generator` - Generate test cases (12207.7.1)
- `ver-test-executor` - Execute tests (12207.7.2)
- `ver-test-analytics` - Analyze results (12207.7.3)
- `ver-code-review` - Code quality review
- `ver-regression` - Regression testing

#### Validation Process
- `val-user-acceptance` - UAT scenarios (12207.6.1)
- `val-conformance-check` - Standards validation (12207.6.2)

#### Quality Assurance Process
- `qa-audit` - Quality audits (12207.8.1)
- `qa-improvement` - Quality improvements (12207.8.2)
- `qa-bug-hunter` - Proactive defect detection

#### Operation Support & Maintenance Process
- `ops-operation` - Daily operations (12207.10.1)
- `ops-maintenance` - Maintenance activities (12207.10.2)
- `ops-monitoring` - System monitoring (12207.10.3)

### 🔄 Workflows

#### 1. Full Lifecycle Workflow
Complete QA lifecycle from requirements to maintenance:
```bash
./workflow/run-full-lifecycle.sh
```

#### 2. Test Execution Workflow
Lightweight test execution and reporting:
```bash
./workflow/run-test-execution.sh
```

#### 3. Continuous Testing Workflow
CI/CD integration with automated regression:
```bash
# Create continuous workflow (example)
./workflow/run-full-lifecycle.sh --continuous
```

#### 4. Compliance Audit Workflow
ISO 12207 compliance audit evidence generation:
```bash
# Create audit workflow (example)
./workflow/run-full-lifecycle.sh --audit
```

#### 5. Bug Hunt Workflow
Proactive defect discovery:
```bash
# Create bug hunt workflow (example)
./workflow/run-full-lifecycle.sh --bug-hunt
```

### 📊 Verbose Mode

Enable detailed status output by setting `QA_VERBOSE=1`:

```bash
export QA_VERBOSE=1
./workflow/full-lifecycle
```

Verbose output includes:
- Timestamps for all actions
- Model parameters and inference settings
- Resource consumption (tokens, time)
- Step-by-step reasoning
- Error logs with stack traces

Example verbose output:
```
[2026-04-12T17:06:00+00:00] [ACTION: ver-test-generator]
[2026-04-12T17:06:01+00:00] [MODEL: qwen3.5:9b]
[2026-04-12T17:06:02+00:00] [STATUS: Executing: Generate test cases]
---
Steps Taken:
- Step 1: Extract requirements from input
- Step 2: Map to test scenarios
- Step 3: Generate test cases
[2026-04-12T17:06:03+00:00] [OUTPUT: test-cases.yaml]
```

### 📁 Project Structure

```
iso-qa-lab/
├── README.md
├── AGENTS.md
├── workflow/                 # Workflow execution scripts
├── agents/
│   ├── acq-requirements-parser/
│   ├── pm-project-planning/
│   ├── cfg-configuration/
│   ├── ver-test-generator/
│   ├── ver-test-executor/
│   ├── ver-code-review/
│   ├── ver-regression/
│   ├── val-user-acceptance/
│   ├── qa-audit/
│   ├── qa-bug-hunter/
│   ├── ops-operation/
│   ├── ops-maintenance/
│   └── ...
├── tests/
├── harness/
├── results/
└── docs/
```

### 🛠️ Usage Examples

#### Run with verbose mode:
```bash
export QA_VERBOSE=1
export QA_MODEL=qwen3.5:9b
./workflow/run-full-lifecycle.sh
```

#### Override model:
```bash
export QA_MODEL=deepseek-coder-v2:16b
export QA_VERBOSE=1
./workflow/run-full-lifecycle.sh
```

#### Check env.sh utility:
```bash
./config/env.sh status
./config/env.sh list-models
./config/env.sh validate
```

### 📜 Compliance

This project is compliant with:
- **ISO/IEC/IEEE 12207:2017** - Software and System Life Cycle Processes
- All agents are mapped to specific ISO clauses
- Workflows follow the standard's lifecycle process flow
- Verification and validation activities align with standard requirements

### 📝 License

MIT License

### 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

---

**Project Name:** ISO-QA-Lab  
**Standard:** ISO/IEC/IEEE 12207:2017  
**Default Model:** qwen3.5:9b  
**Default Timeout:** 600 seconds
