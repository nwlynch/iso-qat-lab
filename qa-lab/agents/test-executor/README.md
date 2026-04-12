# 🤖 Test Executor Agent

## Purpose
Executes test cases and captures results, including screenshots, logs, and performance metrics.

## Responsibilities
- Run test scripts (Selenium/Playwright)
- Capture execution results (pass/fail)
- Take screenshots on failures
- Collect logs and metrics
- Track execution timing

## Input
- Generated test cases
- Test environment config
- Execution parameters
- Test data fixtures

## Output
- Execution results (JSON)
- Screenshots with timestamps
- Log files
- Performance metrics

## Model
- Default: llama3.1:8b (fast execution)
- Complex tests: mixtral:8x7b

## Workflow Integration
- Phase 3: Test Execution
- Feeds into Phase 4: Analysis & Reporting

## Status
🔜 Ready for implementation
