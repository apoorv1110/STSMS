from traffic_controller import TrafficController  # Import class, not instance
import time

class AmbulanceDetector:
    def __init__(self, traffic_controller):
        self.traffic_controller = traffic_controller  # Store reference

    def detect_ambulance(self, location):
        print(f"🚑 Ambulance detected at {location}")

        # Turn all signals RED
        for intersection in self.traffic_controller.signals:
            self.traffic_controller.signals[intersection] = "RED"

        # Make only the ambulance's location GREEN
        self.traffic_controller.signals[location] = "GREEN"

        print(f"⚠️ Alert sent to nearby intersections about ambulance at {location}")

        # Hold for 10 seconds
        time.sleep(10)

        # Restore traffic cycle
        self.traffic_controller.reset_signals()
