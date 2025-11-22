@echo off
REM FSM Toolkit Quick Start Script (Windows Batch)
REM Sets up both tools and runs a demo

echo.
echo 🚀 FSM Toolkit Quick Start
echo ==========================
echo.

REM Check if Node.js is installed
where node >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Node.js is not installed. Please install Node.js 14+ first.
    exit /b 1
)

for /f "tokens=*" %%i in ('node --version') do set NODE_VERSION=%%i
echo ✅ Node.js found: %NODE_VERSION%
echo.

REM Setup code-to-fsm
echo 📦 Setting up code-to-fsm...
cd code-to-fsm
call npm install --silent
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Failed to install code-to-fsm dependencies
    exit /b 1
)
echo ✅ code-to-fsm ready
echo.

REM Setup mermaid-to-xstate
echo 📦 Setting up mermaid-to-xstate...
cd ..\mermaid-to-xstate
call npm install --silent
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Failed to install mermaid-to-xstate dependencies
    exit /b 1
)
echo ✅ mermaid-to-xstate ready
echo.

REM Run demo
echo 🎬 Running demo...
echo.
echo Demo 1: Converting a Mermaid diagram to XState
echo ----------------------------------------------
node cli.js example.mmd
echo.

echo Demo 2: Analyzing example robot code
echo -------------------------------------
cd ..\code-to-fsm
echo The code-to-fsm tool would analyze your robot code here.
echo Since it requires Claude API access, here's what it would do:
echo.
echo 1. Scan your codebase for state machine patterns
echo 2. Call Claude to analyze the state logic
echo 3. Generate a Mermaid diagram
echo 4. Optionally convert to XState
echo.
type EXAMPLE_OUTPUT.txt
echo.

echo ✨ Setup complete!
echo.
echo 📚 Next steps:
echo.
echo    Try the Mermaid converter:
echo    ^> cd mermaid-to-xstate
echo    ^> node cli.js example.mmd -o output.js
echo.
echo    Analyze your own code (requires Claude API):
echo    ^> cd code-to-fsm
echo    ^> node cli.js analyze C:\path\to\your\project --to-xstate
echo.
echo    Read the docs:
echo    ^> type README.md
echo    ^> type code-to-fsm\WORKFLOW_GUIDE.md
echo.
echo Happy state machine engineering! 🎉
