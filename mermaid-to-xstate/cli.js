#!/usr/bin/env node

const { Command } = require('commander');
const fs = require('fs');
const path = require('path');
const MermaidToXStateParser = require('./parser');

const program = new Command();

program
  .name('mermaid-to-xstate')
  .description('Convert Mermaid state diagrams to XState machine definitions')
  .version('1.0.0');

program
  .argument('<input>', 'Input Mermaid file (.mmd or .md)')
  .option('-o, --output <file>', 'Output file (default: stdout)')
  .option('-f, --format <format>', 'Output format: esm, cjs, or json', 'esm')
  .option('-i, --id <id>', 'Machine ID (default: generatedMachine)', 'generatedMachine')
  .action((input, options) => {
    try {
      // Read input file
      const inputPath = path.resolve(input);
      if (!fs.existsSync(inputPath)) {
        console.error(`Error: Input file not found: ${input}`);
        process.exit(1);
      }

      const mermaidText = fs.readFileSync(inputPath, 'utf-8');

      // Parse Mermaid to XState
      const parser = new MermaidToXStateParser();
      const machine = parser.parse(mermaidText);
      
      // Set custom machine ID if provided
      if (options.id) {
        machine.id = options.id;
      }

      // Generate code
      const code = parser.generateXStateCode(machine, options.format);

      // Output
      if (options.output) {
        const outputPath = path.resolve(options.output);
        fs.writeFileSync(outputPath, code, 'utf-8');
        console.log(`✓ XState machine written to ${options.output}`);
        console.log(`  Format: ${options.format}`);
        console.log(`  Machine ID: ${machine.id}`);
        console.log(`  States: ${Object.keys(machine.states).length}`);
      } else {
        console.log(code);
      }
    } catch (error) {
      console.error('Error:', error.message);
      process.exit(1);
    }
  });

program.parse();
