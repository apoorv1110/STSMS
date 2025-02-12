import tkinter as tk
import time
from traffic_controller import TrafficController

class TrafficUI:
    def __init__(self, root, traffic_controller):
        self.root = root
        self.traffic_controller = traffic_controller
        self.root.title("Traffic Signal Visualization")

        # Create labels for signals
        self.signal_labels = {}
        for i, signal in enumerate(self.traffic_controller.signals):
            label = tk.Label(root, text=f"Signal {signal}", font=("Arial", 14), width=10, height=2, bg="gray")
            label.grid(row=0, column=i, padx=20, pady=20)
            self.signal_labels[signal] = label
        
        # Update UI every second
        self.update_ui()

    def update_ui(self):
        """ Updates the UI with current traffic light colors """
        for signal, status in self.traffic_controller.signals.items():
            color = "green" if status == "GREEN" else "red"
            self.signal_labels[signal].config(bg=color)

        self.root.after(1000, self.update_ui)  # Refresh every 1 second

def start_ui(traffic_controller):
    """ Launches the UI for the traffic signals """
    root = tk.Tk()
    ui = TrafficUI(root, traffic_controller)
    root.mainloop()
