# 🤖 Agent Directory

## Overview
This directory contains the 7 agents that make up the QA Lab multi-agent system.

## Agent Status

| Agent | Purpose | Status | Location |
|-------|---------|--------|----------|
| 🧬 Test Generator | Create test cases from requirements | 🔜 Ready | [test-generator/](test-generator/) |
| 🤖 Test Executor | Run tests and capture results | 🔜 Ready | [test-executor/](test-executor/) |
| 📊 Analytics Agent | Analyze results and generate insights | 🔜 Ready | [analytics-agent/](analytics-agent/) |
| 🔍 Code Review Agent | Review code and suggest improvements | 🔜 Ready | [code-review-agent/](code-review-agent/) |
| 🐛 Bug Hunter Agent | Find issues and edge cases | 🔜 Ready | [bug-hunter-agent/](bug-hunter-agent/) |
| 📋 Regression Agent | Run regression tests automatically | 🔜 Ready | [regression-agent/](regression-agent/) |
| 📝 Documentation Agent | Maintain test documentation | 🔜 Ready | [documentation-agent/](documentation-agent/) |

## Next Steps
1. Create execution scripts for each agent
2. Add system prompts
3. Define agent communication patterns
4. Test individual agents
5. Build orchestration layer

## See Also
- [../config/models.yaml](../config/models.yaml) - Model assignments
- [../config/workflows.yaml](../config/workflows.yaml) - Orchestration patterns
- [../docs/workflow-proposal.md](../docs/workflow-proposal.md) - Complete workflow
