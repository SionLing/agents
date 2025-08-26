#!/bin/bash

# Create the .claude/agents directory if it doesn't exist
mkdir -p .claude/agents

# Copy all .md files from parent directory to .claude/agents/
# The -f flag forces overwrite of existing files
cp ../*.md .claude/agents/

echo "Successfully copied all .md files from ../ to .claude/agents/"