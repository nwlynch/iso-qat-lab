# 🧬 Test Generator Agent

## Purpose
Generates comprehensive test cases from requirements, including edge cases, security tests, and performance scenarios.

## Responsibilities
- Parse requirements and acceptance criteria
- Generate functional test cases (happy paths)
- Generate negative/edge case tests
- Create test data fixtures
- Define expected results

## Input
- Requirements documents
- User stories
- Acceptance criteria
- Feature specifications

## Output
- Structured test cases (JSON/YAML)
- Test data requirements
- Expected result definitions
- Test execution scripts

## Model
- Default: qwen3.5:9b
- Edge cases: deepseek-coder-v2:16b
- Security tests: phi4:14b

## Workflow Integration
- Phase 2: Test Case Generation
- Feeds into Phase 3: Test Execution

## Status
🔜 Ready for implementation
