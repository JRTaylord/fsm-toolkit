#!/usr/bin/env python3
"""
Sync test-viewer.html with the HTML structure from viewer-template.html.
This script copies the HTML structure from the template and populates it with
the CSS and JS from the template files.
"""

import os


def read_file(filepath):
    """Read and return the contents of a file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def write_file(filepath, content):
    """Write content to a file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def main():
    # Define paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(script_dir, 'code-to-fsm', 'templates')

    template_html = os.path.join(template_dir, 'viewer-template.html')
    css_file = os.path.join(template_dir, 'viewer.css')
    js_file = os.path.join(template_dir, 'viewer.js')
    output_file = os.path.join(script_dir, 'test-viewer.html')

    # Read template files
    print("Reading template files...")
    html_template = read_file(template_html)
    css_content = read_file(css_file)
    js_content = read_file(js_file)

    # Test mermaid diagram
    test_diagram = """stateDiagram-v2
    [*] --> Idle
    Idle --> Processing : start_process
    Idle --> ConfigMode : enter_config
    Processing --> Validating : validate
    Processing --> Error : validation_failed
    Processing --> Idle : cancel
    Validating --> Success : validation_passed
    Validating --> Error : validation_failed
    Validating --> Processing : retry
    Success --> Idle : reset
    Success --> ExportData : export
    ExportData --> Idle : export_complete
    ExportData --> Error : export_failed
    Error --> Idle : acknowledge
    Error --> Processing : retry
    ConfigMode --> Idle : save_config
    ConfigMode --> Idle : cancel_config
    note right of Processing
        This state handles the main processing logic
    end note
    note right of Error
        Errors can be retried or acknowledged
    end note"""

    # Replace placeholders
    print("Replacing placeholders...")
    output_html = html_template.replace('{{STYLES}}', css_content)
    output_html = output_html.replace('{{SCRIPTS}}', js_content)
    output_html = output_html.replace('{{MERMAID_DIAGRAM}}', test_diagram)

    # Write output file
    print(f"Writing to {output_file}...")
    write_file(output_file, output_html)

    print("SUCCESS: test-viewer.html has been synced with the template structure!")


if __name__ == '__main__':
    main()
