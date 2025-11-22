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

# Setup mermaid-to-xstate
echo "📦 Setting up mermaid-to-xstate..."
cd ../mermaid-to-xstate
npm install --silent
echo "✅ mermaid-to-xstate ready"
echo ""

# Run demo
echo "🎬 Running demo..."
echo ""
echo "Demo 1: Converting a Mermaid diagram to XState"
echo "----------------------------------------------"
node cli.js example.mmd
echo ""

echo "Demo 2: Analyzing example robot code"
echo "-------------------------------------"
cd ../code-to-fsm
echo "The code-to-fsm tool would analyze your robot code here."
echo "Since it requires Claude API access, here's what it would do:"
echo ""
echo "1. Scan your codebase for state machine patterns"
echo "2. Call Claude to analyze the state logic"
echo "3. Generate a Mermaid diagram"
echo "4. Optionally convert to XState"
echo ""
cat EXAMPLE_OUTPUT.txt
echo ""

echo "✨ Setup complete!"
echo ""
echo "📚 Next steps:"
echo ""
echo "   Try the Mermaid converter:"
echo "   $ cd mermaid-to-xstate"
echo "   $ node cli.js example.mmd -o output.js"
echo ""
echo "   Analyze your own code (requires Claude API):"
echo "   $ cd code-to-fsm"
echo "   $ node cli.js analyze /path/to/your/project --to-xstate"
echo ""
echo "   Read the docs:"
echo "   $ cat README.md"
echo "   $ cat code-to-fsm/WORKFLOW_GUIDE.md"
echo ""
echo "Happy state machine engineering! 🎉"
