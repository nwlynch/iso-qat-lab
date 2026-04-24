# 🧪 Test Harness

## Overview
This directory contains the end-to-end test harness for running the QA Lab multi-agent workflow.

---

## Files

### test-runner.sh
**Purpose:** End-to-end workflow runner for all 7 agents

**Usage:**
```bash
# Run complete workflow
./test-runner.sh full

# Show agent status
./test-runner.sh status

# Run individual phases
./test-runner.sh generate    # Phase 2: Test Generation
./test-runner.sh execute     # Phase 3: Test Execution
./test-runner.sh analyze     # Phase 4: Analysis & Reporting
./test-runner.sh bugs        # Phase 5: Bug Hunting
./test-runner.sh regression  # Phase 6: Regression
./test-runner.sh docs        # Phase 4/6: Documentation
```

**Features:**
- Runs all 7 agents sequentially
- Validates each phase completion
- Collects results
- Generates comprehensive reports

---

## Workflow

### Phase 1: Requirements
- Input: User stories, specs
- Output: Requirements document

### Phase 2: Test Generation
- Input: Requirements
- Agent: Test Generator + Bug Hunter
- Output: Test cases, fixtures

### Phase 3: Execution
- Input: Test cases, fixtures
- Agent: Test Executor
- Output: Execution results

### Phase 4: Analysis & Reporting
- Input: Execution results
- Agents: Analytics + Documentation
- Output: Test reports

### Phase 5: Code Review
- Input: Execution results, code
- Agents: Code Review + Bug Hunter
- Output: Bug reports, improvements

### Phase 6: Regression
- Input: Code changes
- Agent: Regression Agent
- Output: Regression results

### Phase 7: Continuous Improvement
- Input: All results
- Agents: Analytics + Documentation
- Output: Updated knowledge, best practices

---

## Commands

```bash
# Run full workflow
qa-lab/harness/test-runner.sh full

# Show status
qa-lab/harness/test-runner.sh status

# Quick execution (test phase only)
qa-lab/harness/test-runner.sh execute
```

---

## Status

**All agents ready:**
- ✅ Test Generator
- ✅ Test Executor
- ✅ Analytics Agent
- ✅ Code Review Agent
- ✅ Bug Hunter Agent
- ✅ Regression Agent
- ✅ Documentation Agent

**Harness ready:**
- ✅ Full workflow runner
- ✅ Individual phase runners
- ✅ Status checker

**Sample data ready:**
- ✅ Requirements document
- ✅ Config files

**Ready to run:**
- ⏳ First end-to-end workflow test
- ⏳ Integration with OpenClaw sessions
