#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Code to FSM Analyzer CLI
Analyze code to extract state machines and generate Mermaid diagrams
"""

import sys
import os
import argparse
from pathlib import Path
from analyzer import CodeToFSMAnalyzer

# Fix Windows console encoding issues
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

def main():
    parser = argparse.ArgumentParser(
        prog='code-to-fsm',
        description='Analyze code to extract state machines and generate Mermaid diagrams'
    )

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Analyze command
    analyze_parser = subparsers.add_parser('analyze', help='Analyze a codebase to extract state machine patterns using Claude CLI')
    analyze_parser.add_argument('workspace', help='Path to the workspace/project directory')
    analyze_parser.add_argument('-o', '--output', default='./fsm-output', help='Output directory for generated files')
    analyze_parser.add_argument('-f', '--files', nargs='+', help='Specific files to analyze (relative to workspace)')
    analyze_parser.add_argument('-p', '--patterns', nargs='+', help='File patterns to match (e.g., "*.py" "*.js")')
    analyze_parser.add_argument('--focus', help='Focus area or component to analyze (e.g., "robot controller")')

    # Interactive command
    interactive_parser = subparsers.add_parser('interactive', help='Interactive mode - chat with Claude about your state machine using Claude CLI')
    interactive_parser.add_argument('workspace', help='Path to the workspace/project directory')
    interactive_parser.add_argument('-f', '--files', nargs='+', help='Specific files to analyze')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == 'analyze':
        run_analyze(args)
    elif args.command == 'interactive':
        run_interactive(args)

def run_analyze(args):
    """Run the analyze command"""
    try:
        workspace_path = Path(args.workspace).resolve()

        if not workspace_path.exists():
            print(f"❌ Error: Workspace not found: {args.workspace}")
            sys.exit(1)

        print('🚀 Starting code analysis...')
        print(f'📂 Workspace: {workspace_path}')
        if args.focus:
            print(f'🎯 Focus: {args.focus}')

        analyzer_options = {}
        if args.patterns:
            analyzer_options['file_patterns'] = args.patterns

        analyzer = CodeToFSMAnalyzer(str(workspace_path), analyzer_options)
        results = analyzer.analyze(args.focus, args.files)

        # Save results
        output_dir = Path(args.output).resolve()
        saved_files = analyzer.save_results(results, str(output_dir))

        print('\n✨ Done! Your state machine has been extracted.')
        print(f'\n🌐 Open in browser: {saved_files["html_path"]}')
        print(f'📊 Mermaid source: {saved_files["mermaid_path"]}')
        print(f'📄 Full analysis: {saved_files["analysis_path"]}')

        # Auto-open HTML file in browser
        import webbrowser
        print(f'\n🚀 Opening diagram in your default browser...')
        webbrowser.open('file://' + saved_files["html_path"])

    except Exception as error:
        print(f'❌ Error: {error}')
        if os.getenv('DEBUG'):
            import traceback
            traceback.print_exc()
        sys.exit(1)

def run_interactive(args):
    """Run the interactive command"""
    print('🤖 Interactive mode - Chat with Claude about your state machine')
    print('   Type your questions or "exit" to quit\n')

    workspace_path = Path(args.workspace).resolve()
    analyzer = CodeToFSMAnalyzer(str(workspace_path))

    # Read files once
    print('📖 Reading files...')
    if args.files:
        file_paths = [str(Path(workspace_path) / f) for f in args.files]
    else:
        file_paths = analyzer.scan_workspace()

    files = analyzer.read_files(file_paths)

    conversation_history = []

    # Initial context message
    files_content = '\n---\n\n'.join([
        f'File: {f["path"]}\n```\n{f["content"]}\n```\n'
        for f in files
    ])

    context_message = f"""You are helping analyze code to understand state machine patterns.

Here are the relevant files:

{files_content}

Please help the user understand the state machine logic in this code."""

    conversation_history.append({"role": "user", "content": context_message})

    print('✅ Ready! Ask me anything about the state machine in your code.\n')

    while True:
        try:
            user_input = input('You: ').strip()

            if user_input.lower() in ['exit', 'quit']:
                print('👋 Goodbye!')
                break

            if not user_input:
                continue

            conversation_history.append({"role": "user", "content": user_input})

            print('\n🤔 Claude is thinking...\n')

            # Build prompt from conversation history
            prompt = '\n\n'.join([
                f'User: {msg["content"]}' if msg["role"] == "user" else f'Assistant: {msg["content"]}'
                for msg in conversation_history
            ])

            # Call Claude CLI
            import subprocess
            import tempfile

            with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
                f.write(prompt)
                temp_file = f.name

            try:
                result = subprocess.run(
                    ['claude', '--print'],
                    stdin=open(temp_file, 'r'),
                    capture_output=True,
                    text=True,
                    check=True
                )
                assistant_message = result.stdout.strip()
                conversation_history.append({"role": "assistant", "content": assistant_message})
                print(f'Claude: {assistant_message}\n')
            finally:
                os.unlink(temp_file)

        except KeyboardInterrupt:
            print('\n👋 Goodbye!')
            break
        except Exception as error:
            print(f'❌ Error: {error}')

if __name__ == '__main__':
    main()
