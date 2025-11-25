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

REM Run demo
echo 🎬 Running demo...
echo.
echo Demo: Analyzing example robot code
echo -----------------------------------
echo The code-to-fsm tool analyzes your robot code.
echo Here's what it does:
echo.
echo 1. Scan your codebase for state machine patterns
echo 2. Call Claude to analyze the state logic
echo 3. Generate a beautiful Mermaid diagram
echo 4. Open interactive visualization in browser
echo.
type EXAMPLE_OUTPUT.txt
echo.

echo ✨ Setup complete!
echo.
echo 📚 Next steps:
echo.
echo    Analyze your own code:
echo    ^> cd code-to-fsm
echo    ^> node cli.js analyze C:\path\to\your\project
echo.
echo    Try interactive mode:
echo    ^> node cli.js interactive C:\path\to\your\project
echo.
echo    Read the docs:
echo    ^> type ..\README.md
echo    ^> type WORKFLOW_GUIDE.md
echo.
echo Happy state machine engineering! 🎉
