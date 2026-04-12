# 🔍 Code Review Agent

## Purpose
Reviews test code quality, identifies bugs, suggests improvements, and ensures security compliance.

## Responsibilities
- Review test isolation
- Check naming conventions
- Analyze coverage adequacy
- Identify security issues
- Suggest code improvements

## Input
- Test code
- Execution results
- Error logs
- Screenshots

## Output
- Code review comments
- Quality scores
- Improvement suggestions
- Security findings
- Bug reports

## Model
- Default: deepseek-coder-v2:16b
- Security: phi4:14b

## Workflow Integration
- Phase 5: Code Review & Quality
- Feeds back into Phase 2: Test Generation

## Status
🔜 Ready for implementation
