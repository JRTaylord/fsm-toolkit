#!/bin/bash

# FSM Toolkit Quick Start Script
# Sets up both tools and runs a demo

set -e

echo "🚀 FSM Toolkit Quick Start"
echo "=========================="
echo ""

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 14+ first."
    exit 1
fi

echo "✅ Node.js found: $(node --version)"
echo ""

# Setup code-to-fsm
echo "📦 Setting up code-to-fsm..."
cd code-to-fsm
npm install --silent
echo "✅ code-to-fsm ready"
echo ""

# Run demo
echo "🎬 Running demo..."
echo ""
echo "Demo: Analyzing example robot code"
echo "-----------------------------------"
echo "The code-to-fsm tool analyzes your robot code."
echo "Here's what it does:"
echo ""
echo "1. Scan your codebase for state machine patterns"
echo "2. Call Claude to analyze the state logic"
echo "3. Generate a beautiful Mermaid diagram"
echo "4. Open interactive visualization in browser"
echo ""
cat EXAMPLE_OUTPUT.txt
echo ""

echo "✨ Setup complete!"
echo ""
echo "📚 Next steps:"
echo ""
echo "   Analyze your own code:"
echo "   $ cd code-to-fsm"
echo "   $ node cli.js analyze /path/to/your/project"
echo ""
echo "   Try interactive mode:"
echo "   $ node cli.js interactive /path/to/your/project"
echo ""
echo "   Read the docs:"
echo "   $ cat ../README.md"
echo "   $ cat WORKFLOW_GUIDE.md"
echo ""
echo "Happy state machine engineering! 🎉"
