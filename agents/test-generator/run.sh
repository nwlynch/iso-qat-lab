#!/bin/bash
# 🧬 Test Generator Agent - Execution Script

# This script runs the Test Generator Agent session

echo "🧬 Test Generator Agent Starting..."

# Create session
SESSION=$(sessions_spawn \
  --runtime subagent \
  --mode session \
  --label "Test Generator" \
  --agent-id test-generator \
  --task "Generate test cases from requirements" \
  --stream-to parent \
)

echo "Session created: $SESSION"

# Wait for completion
sleep 30

echo "✅ Test Generator Agent completed"
