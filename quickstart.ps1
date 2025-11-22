# FSM Toolkit Quick Start Script (PowerShell)
# Sets up both tools and runs a demo

$ErrorActionPreference = "Stop"

Write-Host "🚀 FSM Toolkit Quick Start" -ForegroundColor Cyan
Write-Host "==========================" -ForegroundColor Cyan
Write-Host ""

# Check if Node.js is installed
$nodeVersion = node --version 2>$null
if (-not $nodeVersion) {
    Write-Host "❌ Node.js is not installed. Please install Node.js 14+ first." -ForegroundColor Red
    exit 1
}

Write-Host "✅ Node.js found: $nodeVersion" -ForegroundColor Green
Write-Host ""

# Setup code-to-fsm
Write-Host "📦 Setting up code-to-fsm..." -ForegroundColor Yellow
Set-Location code-to-fsm
npm install --silent
Write-Host "✅ code-to-fsm ready" -ForegroundColor Green
Write-Host ""

# Setup mermaid-to-xstate
Write-Host "📦 Setting up mermaid-to-xstate..." -ForegroundColor Yellow
Set-Location ..\mermaid-to-xstate
npm install --silent
Write-Host "✅ mermaid-to-xstate ready" -ForegroundColor Green
Write-Host ""

# Run demo
Write-Host "🎬 Running demo..." -ForegroundColor Cyan
Write-Host ""
Write-Host "Demo 1: Converting a Mermaid diagram to XState" -ForegroundColor Yellow
Write-Host "----------------------------------------------"
node cli.js example.mmd
Write-Host ""

Write-Host "Demo 2: Analyzing example robot code" -ForegroundColor Yellow
Write-Host "-------------------------------------"
Set-Location ..\code-to-fsm
Write-Host "The code-to-fsm tool would analyze your robot code here."
Write-Host "Since it requires Claude API access, here's what it would do:"
Write-Host ""
Write-Host "1. Scan your codebase for state machine patterns"
Write-Host "2. Call Claude to analyze the state logic"
Write-Host "3. Generate a Mermaid diagram"
Write-Host "4. Optionally convert to XState"
Write-Host ""
Get-Content EXAMPLE_OUTPUT.txt
Write-Host ""

Write-Host "✨ Setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "📚 Next steps:" -ForegroundColor Cyan
Write-Host ""
Write-Host "   Try the Mermaid converter:"
Write-Host "   PS> cd mermaid-to-xstate"
Write-Host "   PS> node cli.js example.mmd -o output.js"
Write-Host ""
Write-Host "   Analyze your own code (requires Claude API):"
Write-Host "   PS> cd code-to-fsm"
Write-Host "   PS> node cli.js analyze C:\path\to\your\project --to-xstate"
Write-Host ""
Write-Host "   Read the docs:"
Write-Host "   PS> Get-Content README.md"
Write-Host "   PS> Get-Content code-to-fsm\WORKFLOW_GUIDE.md"
Write-Host ""
Write-Host "Happy state machine engineering! 🎉" -ForegroundColor Magenta
