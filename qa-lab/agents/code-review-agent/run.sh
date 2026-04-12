#!/bin/bash
# 🔍 Code Review Agent - Execution Script

echo "🔍 Code Review Agent Starting..."

SESSION=$(sessions_spawn \
  --runtime subagent \
  --mode session \
  --label "Code Review Agent" \
  --agent-id code-review-agent \
  --task "Review test code and identify bugs" \
  --stream-to parent \
)

echo "Session created: $SESSION"

sleep 30

echo "✅ Code Review Agent completed"
