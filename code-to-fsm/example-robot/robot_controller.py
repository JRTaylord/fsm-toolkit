"""
Robot Controller - Simple state machine example
"""

class RobotState:
    IDLE = "idle"
    INITIALIZING = "initializing"
    READY = "ready"
    MOVING = "moving"
    PAUSED = "paused"
    ERROR = "error"
    SHUTDOWN = "shutdown"

class RobotController:
    def __init__(self):
        self.state = RobotState.IDLE
        self.position = (0, 0)
        self.error_message = None
    
    def initialize(self):
        """Initialize the robot"""
        if self.state == RobotState.IDLE:
            self.state = RobotState.INITIALIZING
            print("Initializing robot...")
            # Perform initialization
            self.state = RobotState.READY
            print("Robot ready!")
        else:
            print(f"Cannot initialize from state: {self.state}")
    
    def start_moving(self, target):
        """Start moving to target position"""
        if self.state == RobotState.READY:
            self.state = RobotState.MOVING
            print(f"Moving to {target}...")
        elif self.state == RobotState.PAUSED:
            self.state = RobotState.MOVING
            print("Resuming movement...")
        else:
            print(f"Cannot move from state: {self.state}")
    
    def pause(self):
        """Pause current operation"""
        if self.state == RobotState.MOVING:
            self.state = RobotState.PAUSED
            print("Robot paused")
        else:
            print(f"Cannot pause from state: {self.state}")
    
    def stop(self):
        """Stop and return to ready state"""
        if self.state in [RobotState.MOVING, RobotState.PAUSED]:
            self.state = RobotState.READY
            print("Robot stopped")
        else:
            print(f"Cannot stop from state: {self.state}")
    
    def handle_error(self, error_msg):
        """Handle error condition"""
        if self.state != RobotState.SHUTDOWN:
            self.error_message = error_msg
            self.state = RobotState.ERROR
            print(f"ERROR: {error_msg}")
    
    def reset_error(self):
        """Reset from error state"""
        if self.state == RobotState.ERROR:
            self.error_message = None
            self.state = RobotState.IDLE
            print("Error reset, returning to idle")
        else:
            print(f"Cannot reset from state: {self.state}")
    
    def shutdown(self):
        """Shutdown the robot"""
        if self.state in [RobotState.IDLE, RobotState.READY, RobotState.ERROR]:
            self.state = RobotState.SHUTDOWN
            print("Robot shutdown complete")
        else:
            print(f"Cannot shutdown from state: {self.state}")
    
    def get_state(self):
        """Get current state"""
        return self.state

# Example usage
if __name__ == "__main__":
    robot = RobotController()
    
    robot.initialize()
    robot.start_moving((10, 10))
    robot.pause()
    robot.start_moving((10, 10))  # Resume
    robot.stop()
    robot.shutdown()
