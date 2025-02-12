import time
from traffic_controller import traffic_controller
class SignalUpdater:
    def __init__(self, traffic_controller):
        self.traffic_controller = traffic_controller

    def update_signals(self):
        """ Updates traffic lights in real-time based on ambulance movement """
        while True:
            time.sleep(5)
            print(f"Updated Signals: {self.traffic_controller.signals}")

signal_updater = SignalUpdater(traffic_controller)
