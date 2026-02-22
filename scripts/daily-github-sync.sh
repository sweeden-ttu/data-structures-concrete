#!/bin/bash
set -e

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_DIR"

echo "=== Daily GitHub Sync ==="
echo "Project: data-structures-concrete"
echo "Time: $(date)"

if git rev-parse --git-dir > /dev/null 2>&1; then
    echo "Fetching updates..."
    git fetch --all --prune
    
    echo "Checking branch status..."
    git branch -vv | grep ': gone]'
    
    echo "Sync complete at $(date)"
else
    echo "Not a git repository. Skipping sync."
fi

echo "=== End Sync ==="
