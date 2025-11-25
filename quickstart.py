#!/usr/bin/env python3
"""
FSM Toolkit Quick Start Script
Cross-platform setup and demo script
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def check_python_version():
    """Check if Python version is 3.7+"""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7+ is required. You have:", sys.version)
        sys.exit(1)
    print(f"✅ Python found: {sys.version.split()[0]}")

def check_claude_cli():
    """Check if Claude CLI is installed"""
    try:
        result = subprocess.run(['claude', '--version'], capture_output=True, text=True)
        print(f"✅ Claude CLI found")
        return True
    except FileNotFoundError:
        print("⚠️  Claude CLI not found - install from https://claude.com/claude-code")
        return False

def main():
    print("🚀 FSM Toolkit Quick Start")
    print("==========================")
    print()

    check_python_version()
    print()

    has_claude = check_claude_cli()
    print()

    # Setup code-to-fsm
    print("📦 Setting up code-to-fsm...")
    code_to_fsm_dir = Path(__file__).parent / 'code-to-fsm'
    os.chdir(code_to_fsm_dir)

    # Make cli.py executable on Unix-like systems
    if platform.system() != 'Windows':
        cli_path = code_to_fsm_dir / 'cli.py'
        os.chmod(cli_path, 0o755)

    print("✅ code-to-fsm ready")
    print()

    # Run demo
    print("🎬 Running demo...")
    print()
    print("Demo: Analyzing example robot code")
    print("-----------------------------------")
    print("The code-to-fsm tool analyzes your robot code.")
    print("Here's what it does:")
    print()
    print("1. Scan your codebase for state machine patterns")
    print("2. Call Claude to analyze the state logic")
    print("3. Generate a beautiful Mermaid diagram")
    print("4. Open interactive visualization in browser")
    print()

    # Show example output
    example_output = code_to_fsm_dir / 'EXAMPLE_OUTPUT.txt'
    if example_output.exists():
        with open(example_output, 'r', encoding='utf-8') as f:
            print(f.read())
    print()

    print("✨ Setup complete!")
    print()
    print("📚 Next steps:")
    print()
    print("   Analyze your own code:")
    if platform.system() == 'Windows':
        print("   > cd code-to-fsm")
        print("   > python cli.py analyze C:\\path\\to\\your\\project")
    else:
        print("   $ cd code-to-fsm")
        print("   $ python3 cli.py analyze /path/to/your/project")
        print("   ")
        print("   Or use the CLI directly:")
        print("   $ ./cli.py analyze /path/to/your/project")
    print()
    print("   Try interactive mode:")
    if platform.system() == 'Windows':
        print("   > python cli.py interactive C:\\path\\to\\your\\project")
    else:
        print("   $ python3 cli.py interactive /path/to/your/project")
    print()
    print("   Read the docs:")
    if platform.system() == 'Windows':
        print("   > type ..\\README.md")
        print("   > type WORKFLOW_GUIDE.md")
    else:
        print("   $ cat ../README.md")
        print("   $ cat WORKFLOW_GUIDE.md")
    print()

    if not has_claude:
        print("⚠️  Note: You need Claude CLI to run the analyzer.")
        print("   Install from: https://claude.com/claude-code")
        print()

    print("Happy state machine engineering! 🎉")

if __name__ == '__main__':
    main()
