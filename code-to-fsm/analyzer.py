"""
Code to FSM Analyzer
Uses Claude to analyze code and extract state machine patterns
"""

import os
import re
import subprocess
import tempfile
from pathlib import Path
from glob import glob as glob_sync


class CodeToFSMAnalyzer:
    def __init__(self, workspace_path, options=None):
        self.workspace_path = workspace_path
        options = options or {}
        self.options = {
            'file_patterns': options.get('file_patterns', [
                '**/*.py', '**/*.js', '**/*.ts', '**/*.cpp', '**/*.c', '**/*.java'
            ]),
            'exclude_patterns': options.get('exclude_patterns', [
                '**/node_modules/**', '**/venv/**', '**/build/**', '**/.git/**',
                '**/__pycache__/**', '**/*.pyc'
            ]),
            'max_file_size': options.get('max_file_size', 100000)  # 100KB max per file
        }

    def scan_workspace(self):
        """Scan the workspace for relevant files"""
        files = []
        workspace = Path(self.workspace_path)

        for pattern in self.options['file_patterns']:
            matches = workspace.glob(pattern)
            for match in matches:
                # Check if file should be excluded
                should_exclude = False
                for exclude_pattern in self.options['exclude_patterns']:
                    exclude_glob = exclude_pattern.replace('**/', '')
                    if exclude_glob in str(match):
                        should_exclude = True
                        break

                if not should_exclude and match.is_file():
                    # Check file size
                    if match.stat().st_size <= self.options['max_file_size']:
                        files.append(str(match))

        return files

    def read_files(self, file_paths):
        """Read and prepare file contents for analysis"""
        file_contents = []

        for file_path in file_paths:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    relative_path = os.path.relpath(file_path, self.workspace_path)
                    file_contents.append({
                        'path': relative_path,
                        'content': content
                    })
            except Exception as error:
                print(f'Warning: Could not read {file_path}: {error}')

        return file_contents

    def create_analysis_prompt(self, files, focus_area=None):
        """Create analysis prompt for Claude"""
        files_summary = '\n---\n\n'.join([
            f'File: {f["path"]}\n```\n{f["content"]}\n```\n'
            for f in files
        ])

        prompt = f"""You are analyzing a codebase to extract state machine patterns.

Here are the relevant files from the project:

{files_summary}

Your task is to:
1. Identify any state machine logic, state transitions, or finite state machine patterns
2. Extract the states, events/transitions, and their relationships
3. Generate a Mermaid stateDiagram-v2 that represents this state machine

"""

        if focus_area:
            prompt += f'\nFocus specifically on: {focus_area}\n'

        prompt += """
Look for patterns like:
- Explicit state variables or enums (e.g., state = "IDLE", State.RUNNING)
- State transition functions (e.g., transition_to(), setState())
- Switch/case statements on state variables
- If/else chains checking state
- Event handlers that change state
- Robot control states (idle, moving, stopped, error, etc.)

Output format:
1. First, provide a brief explanation of what state machine you found
2. Then output ONLY the Mermaid diagram code, starting with "stateDiagram-v2"
3. Use clear, descriptive state names
4. Label transitions with the events/conditions that trigger them

Example output format:
I found a robot control state machine with 4 states...

stateDiagram-v2
    [*] --> Idle
    Idle --> Moving: start_command
    Moving --> Stopped: stop_command
    Moving --> Error: sensor_fault
    Error --> Idle: reset
    Stopped --> [*]
"""

        return prompt

    def analyze_with_claude(self, prompt):
        """Call Claude CLI to analyze the code"""
        print('🖥️  Using Claude CLI...')

        # Write prompt to temp file to avoid command line length limits
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8') as f:
            f.write(prompt)
            tmp_file = f.name

        try:
            # Use shell redirection to read from temp file
            result = subprocess.run(
                'claude --print < "{}"'.format(tmp_file),
                shell=True,
                capture_output=True,
                text=True,
                encoding='utf-8'
            )

            if result.returncode != 0:
                raise Exception(f'Claude CLI exited with code {result.returncode}: {result.stderr}')

            return result.stdout.strip()

        finally:
            # Clean up temp file
            try:
                os.unlink(tmp_file)
            except:
                pass

    def extract_mermaid_diagram(self, response):
        """Extract Mermaid diagram from Claude's response"""
        # Look for stateDiagram-v2 block
        diagram_match = re.search(r'stateDiagram-v2[\s\S]*?(?=\n\n|\n```|$)', response)

        if diagram_match:
            return diagram_match.group(0).strip()

        # Fallback: look for anything between ```mermaid and ```
        code_block_match = re.search(r'```mermaid\n([\s\S]*?)```', response)
        if code_block_match:
            return code_block_match.group(1).strip()

        # Last resort: return the whole response if it looks like a diagram
        if 'stateDiagram-v2' in response:
            return response

        raise Exception('Could not extract Mermaid diagram from response')

    def analyze(self, focus_area=None, selected_files=None):
        """Main analysis workflow"""
        print('🔍 Scanning workspace...')

        if selected_files:
            file_paths = [os.path.join(self.workspace_path, f) for f in selected_files]
        else:
            file_paths = self.scan_workspace()

        print(f'📁 Found {len(file_paths)} files to analyze')

        if len(file_paths) == 0:
            raise Exception('No files found to analyze')

        print('📖 Reading file contents...')
        files = self.read_files(file_paths)

        print('🤖 Calling Claude to analyze state machine patterns...')
        prompt = self.create_analysis_prompt(files, focus_area)
        response = self.analyze_with_claude(prompt)

        print('✅ Analysis complete!')
        print('\n' + '=' * 60)
        print('CLAUDE\'S ANALYSIS:')
        print('=' * 60 + '\n')
        print(response)
        print('\n' + '=' * 60 + '\n')

        mermaid_diagram = self.extract_mermaid_diagram(response)

        return {
            'analysis': response,
            'mermaid_diagram': mermaid_diagram,
            'files_analyzed': [f['path'] for f in files]
        }

    def generate_html_viewer(self, mermaid_diagram, output_dir):
        """Generate HTML viewer for the diagram"""
        html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>State Machine Diagram</title>
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }}
        .container {{
            max-width: 100%;
            margin: 0 auto;
        }}
        h1 {{
            color: white;
            text-align: center;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}
        .subtitle {{
            color: rgba(255,255,255,0.9);
            text-align: center;
            margin-bottom: 30px;
            font-size: 14px;
        }}
        .controls {{
            background: white;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin-bottom: 20px;
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 10px;
        }}
        button {{
            padding: 10px 20px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 500;
            transition: all 0.3s ease;
        }}
        button:hover {{
            background: #5568d3;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }}
        button:active {{
            transform: translateY(0);
        }}
        #diagram-container {{
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            overflow: auto;
            transition: transform 0.3s ease;
        }}
        .footer {{
            text-align: center;
            color: rgba(255,255,255,0.8);
            margin-top: 30px;
            font-size: 12px;
        }}
        .zoom-indicator {{
            position: fixed;
            top: 20px;
            right: 20px;
            background: rgba(0,0,0,0.7);
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 14px;
            font-weight: 500;
            display: none;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🤖 State Machine Diagram</h1>
        <p class="subtitle">Generated by FSM Toolkit</p>

        <div class="controls">
            <button onclick="zoomIn()" title="Zoom In">🔍 Zoom In</button>
            <button onclick="zoomOut()" title="Zoom Out">🔎 Zoom Out</button>
            <button onclick="resetZoom()" title="Reset Zoom">↺ Reset</button>
            <button onclick="fitToScreen()" title="Fit to Screen">⛶ Fit Screen</button>
            <button onclick="downloadSVG()" title="Download SVG">💾 Download SVG</button>
            <button onclick="downloadPNG()" title="Download PNG">📷 Download PNG</button>
        </div>

        <div id="diagram-container">
            <div class="mermaid">
{mermaid_diagram}
            </div>
        </div>

        <div class="footer">
            Generated with FSM Toolkit • Powered by Mermaid.js
        </div>
    </div>

    <div id="zoom-indicator" class="zoom-indicator"></div>

    <script>
        mermaid.initialize({{
            startOnLoad: true,
            theme: 'default',
            securityLevel: 'loose',
            flowchart: {{
                useMaxWidth: false
            }}
        }});

        let currentZoom = 1;
        const container = document.getElementById('diagram-container');
        const zoomIndicator = document.getElementById('zoom-indicator');

        function showZoomIndicator() {{
            zoomIndicator.textContent = Math.round(currentZoom * 100) + '%';
            zoomIndicator.style.display = 'block';
            setTimeout(() => {{
                zoomIndicator.style.display = 'none';
            }}, 1000);
        }}

        function zoomIn() {{
            currentZoom = Math.min(3, currentZoom + 0.1);
            applyZoom();
        }}

        function zoomOut() {{
            currentZoom = Math.max(0.3, currentZoom - 0.1);
            applyZoom();
        }}

        function resetZoom() {{
            currentZoom = 1;
            applyZoom();
        }}

        function fitToScreen() {{
            const svg = container.querySelector('svg');
            if (svg) {{
                const containerWidth = container.clientWidth;
                const svgWidth = svg.getBBox().width;
                currentZoom = (containerWidth - 60) / svgWidth;
                applyZoom();
            }}
        }}

        function applyZoom() {{
            container.style.transform = `scale(${{currentZoom}})`;
            container.style.transformOrigin = 'top left';
            showZoomIndicator();
        }}

        function downloadSVG() {{
            const svg = container.querySelector('svg');
            if (svg) {{
                const serializer = new XMLSerializer();
                const svgString = serializer.serializeToString(svg);
                const blob = new Blob([svgString], {{ type: 'image/svg+xml' }});
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = 'state-machine.svg';
                a.click();
                URL.revokeObjectURL(url);
            }}
        }}

        function downloadPNG() {{
            const svg = container.querySelector('svg');
            if (svg) {{
                const canvas = document.createElement('canvas');
                const ctx = canvas.getContext('2d');
                const svgData = new XMLSerializer().serializeToString(svg);
                const img = new Image();

                img.onload = function() {{
                    canvas.width = img.width * 2;
                    canvas.height = img.height * 2;
                    ctx.fillStyle = 'white';
                    ctx.fillRect(0, 0, canvas.width, canvas.height);
                    ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

                    canvas.toBlob(function(blob) {{
                        const url = URL.createObjectURL(blob);
                        const a = document.createElement('a');
                        a.href = url;
                        a.download = 'state-machine.png';
                        a.click();
                        URL.revokeObjectURL(url);
                    }});
                }};

                img.src = 'data:image/svg+xml;base64,' + btoa(unescape(encodeURIComponent(svgData)));
            }}
        }}

        // Keyboard shortcuts
        document.addEventListener('keydown', (e) => {{
            if (e.ctrlKey || e.metaKey) {{
                if (e.key === '=') {{
                    e.preventDefault();
                    zoomIn();
                }} else if (e.key === '-') {{
                    e.preventDefault();
                    zoomOut();
                }} else if (e.key === '0') {{
                    e.preventDefault();
                    resetZoom();
                }}
            }}
        }});

        // Auto-fit on load
        window.addEventListener('load', () => {{
            setTimeout(fitToScreen, 500);
        }});
    </script>
</body>
</html>"""

        html_path = os.path.join(output_dir, 'view-diagram.html')
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        return html_path

    def save_results(self, results, output_dir):
        """Save results to files"""
        os.makedirs(output_dir, exist_ok=True)

        # Save Mermaid diagram
        mermaid_path = os.path.join(output_dir, 'state-machine.mmd')
        with open(mermaid_path, 'w', encoding='utf-8') as f:
            f.write(results['mermaid_diagram'])
        print(f'💾 Mermaid diagram saved to: {mermaid_path}')

        # Save full analysis
        analysis_path = os.path.join(output_dir, 'analysis.txt')
        full_analysis = f'Files Analyzed:\n' + '\n'.join(results['files_analyzed']) + '\n\n'
        full_analysis += f'Analysis:\n{results["analysis"]}'
        with open(analysis_path, 'w', encoding='utf-8') as f:
            f.write(full_analysis)
        print(f'💾 Full analysis saved to: {analysis_path}')

        # Generate HTML viewer
        html_path = self.generate_html_viewer(results['mermaid_diagram'], output_dir)
        print(f'🌐 HTML viewer saved to: {html_path}')

        return {
            'mermaid_path': mermaid_path,
            'analysis_path': analysis_path,
            'html_path': html_path
        }
