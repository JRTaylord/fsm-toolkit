import { createMachine } from 'xstate';

const machine = createMachine({
  "id": "generatedMachine",
  "initial": "Idle",
  "states": {
    "Idle": {
      "on": {
        "FETCH": "Loading"
      }
    },
    "Loading": {
      "on": {
        "SUCCESS": "Success",
        "ERROR": "Error"
      }
    },
    "Success": {
      "type": "final"
    },
    "Error": {
      "on": {
        "RETRY": "Idle"
      },
      "type": "final"
    }
  }
});

export default machine;
