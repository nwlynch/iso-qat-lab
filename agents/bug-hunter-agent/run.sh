#!/bin/bash
# 🐛 Bug Hunter Agent - Execution Script

echo "🐛 Bug Hunter Agent Starting..."

SESSION=$(sessions_spawn \
  --runtime subagent \
  --mode session \
  --label "Bug Hunter Agent" \
  --agent-id bug-hunter-agent \
  --task "Find bugs and edge cases in test logic" \
  --stream-to parent \
)

echo "Session created: $SESSION"

sleep 30

echo "✅ Bug Hunter Agent completed"
