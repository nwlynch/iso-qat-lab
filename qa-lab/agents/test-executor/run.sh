#!/bin/bash
# 🤖 Test Executor Agent - Execution Script

echo "🤖 Test Executor Agent Starting..."

SESSION=$(sessions_spawn \
  --runtime subagent \
  --mode session \
  --label "Test Executor" \
  --agent-id test-executor \
  --task "Execute test cases and capture results" \
  --stream-to parent \
)

echo "Session created: $SESSION"

sleep 30

echo "✅ Test Executor Agent completed"
