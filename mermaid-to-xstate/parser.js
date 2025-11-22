/**
 * Mermaid to XState Parser
 * Converts Mermaid stateDiagram-v2 syntax to XState machine definitions
 */

class MermaidToXStateParser {
  constructor() {
    this.states = {};
    this.initialState = null;
    this.finalStates = new Set();
  }

  parse(mermaidText) {
    const lines = mermaidText
      .split('\n')
      .map(line => line.trim())
      .filter(line => line && !line.startsWith('stateDiagram'));

    for (const line of lines) {
      this.parseLine(line);
    }

    return this.buildXStateMachine();
  }

  parseLine(line) {
    // Handle initial state: [*] --> StateName
    if (line.match(/^\[\*\]\s*-->\s*(\w+)/)) {
      const match = line.match(/^\[\*\]\s*-->\s*(\w+)/);
      this.initialState = match[1];
      this.ensureStateExists(match[1]);
      return;
    }

    // Handle final state: StateName --> [*]
    if (line.match(/(\w+)\s*-->\s*\[\*\]/)) {
      const match = line.match(/(\w+)\s*-->\s*\[\*\]/);
      const stateName = match[1];
      this.ensureStateExists(stateName);
      this.finalStates.add(stateName);
      return;
    }

    // Handle transitions: StateA --> StateB: event
    const transitionMatch = line.match(/(\w+)\s*-->\s*(\w+)\s*:\s*(.+)/);
    if (transitionMatch) {
      const [, fromState, toState, event] = transitionMatch;
      this.ensureStateExists(fromState);
      this.ensureStateExists(toState);
      this.addTransition(fromState, toState, event.trim());
      return;
    }

    // Handle transitions without events: StateA --> StateB
    const simpleTransitionMatch = line.match(/(\w+)\s*-->\s*(\w+)/);
    if (simpleTransitionMatch) {
      const [, fromState, toState] = simpleTransitionMatch;
      this.ensureStateExists(fromState);
      this.ensureStateExists(toState);
      // For transitions without events, we'll create an auto-transition or skip
      // In XState, this could be an always transition
      this.addTransition(fromState, toState, null);
      return;
    }

    // Handle state notes/descriptions (optional, can be ignored for now)
    if (line.includes(':') && !line.includes('-->')) {
      // This might be a state note like "State1: This is a description"
      // We'll ignore these for now but could add them as comments
      return;
    }
  }

  ensureStateExists(stateName) {
    if (!this.states[stateName]) {
      this.states[stateName] = {
        transitions: {}
      };
    }
  }

  addTransition(fromState, toState, event) {
    if (event === null) {
      // Immediate transition (always)
      if (!this.states[fromState].always) {
        this.states[fromState].always = [];
      }
      this.states[fromState].always.push({ target: toState });
    } else {
      // Event-based transition
      if (!this.states[fromState].transitions[event]) {
        this.states[fromState].transitions[event] = toState;
      } else {
        // Handle multiple transitions for same event (convert to array if needed)
        const existing = this.states[fromState].transitions[event];
        if (Array.isArray(existing)) {
          existing.push(toState);
        } else {
          this.states[fromState].transitions[event] = [existing, toState];
        }
      }
    }
  }

  buildXStateMachine() {
    const xstateStates = {};

    for (const [stateName, stateData] of Object.entries(this.states)) {
      const state = {};

      // Add transitions
      if (Object.keys(stateData.transitions).length > 0) {
        state.on = stateData.transitions;
      }

      // Add always transitions
      if (stateData.always) {
        state.always = stateData.always;
      }

      // Mark final states
      if (this.finalStates.has(stateName)) {
        state.type = 'final';
      }

      xstateStates[stateName] = state;
    }

    return {
      id: 'generatedMachine',
      initial: this.initialState || Object.keys(this.states)[0],
      states: xstateStates
    };
  }

  generateXStateCode(machine, format = 'esm') {
    const machineJson = JSON.stringify(machine, null, 2);
    
    if (format === 'esm') {
      return `import { createMachine } from 'xstate';

const machine = createMachine(${machineJson});

export default machine;
`;
    } else if (format === 'cjs') {
      return `const { createMachine } = require('xstate');

const machine = createMachine(${machineJson});

module.exports = machine;
`;
    } else if (format === 'json') {
      return machineJson;
    }

    return machineJson;
  }
}

module.exports = MermaidToXStateParser;
