# 🐛 Bug Hunter Agent

## Purpose
Searches for bugs, edge cases, and potential issues in code and test logic.

## Responsibilities
- Analyze failed tests
- Identify root causes
- Find edge cases
- Search for security vulnerabilities
- Reproduce issues

## Input
- Failed test results
- Exception logs
- Error messages
- Screenshots

## Output
- Bug reports
- Root cause analysis
- Reproduction steps
- Fix suggestions
- Security alerts

## Model
- Default: phi4:14b (reasoning)
- Deep analysis: deepseek-r1:14b

## Workflow Integration
- Phase 2: Edge Case Generation
- Phase 5: Bug Identification
- Feeds back into Phase 3: Test Generation

## Status
🔜 Ready for implementation
