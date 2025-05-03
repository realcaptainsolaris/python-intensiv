from enum import Enum


# Define an enum for TrafficLightState
class TrafficLightState(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3


# Create a class for the TrafficLight
class TrafficLight:
    def __init__(self):
        self.state = TrafficLightState.RED

    def next_state(self):
        transitions = {
            TrafficLightState.RED: TrafficLightState.GREEN,
            TrafficLightState.GREEN: TrafficLightState.YELLOW,
            TrafficLightState.YELLOW: TrafficLightState.RED,
        }
        current_state = self.state
        next_state = transitions.get(current_state)
        self.state = next_state

    def __str__(self):
        return str(self.state.name)


# Client code
if __name__ == "__main__":
    traffic_light = TrafficLight()

    print("Initial state:", traffic_light)

    # Simulate traffic light changes
    for _ in range(5):
        traffic_light.next_state()
        print("Next state:", traffic_light)
