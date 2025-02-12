import time

class TrafficController:
    def __init__(self):
        # Only one green signal at a time
        self.signal_order = ["A", "B", "C", "D"]
        self.current_green = 0  # Index in signal_order
        self.signals = {sig: "RED" for sig in self.signal_order}
        self.signals[self.signal_order[self.current_green]] = "GREEN"

    def reset_signals(self):
        """ Reset signals to default after an ambulance passes """
        print("🔄 Restoring normal traffic cycle...")
        self.current_green = 0
        self.signals = {sig: "RED" for sig in self.signal_order}
        self.signals[self.signal_order[self.current_green]] = "GREEN"

    def run_traffic_cycle(self):
        """ Simulates normal traffic light changes """
        while True:
            time.sleep(5)  # Change signal every 5 seconds
            self.toggle_signals()
            print("Updated Signals:", self.signals)

    def toggle_signals(self):
        """ Moves to the next signal in the cycle """
        # Set current green to RED
        self.signals[self.signal_order[self.current_green]] = "RED"

        # Move to the next intersection
        self.current_green = (self.current_green + 1) % len(self.signal_order)

        # Set new green signal
        self.signals[self.signal_order[self.current_green]] = "GREEN"
