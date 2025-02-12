import threading
from traffic_controller import TrafficController
from ambulance_detector import AmbulanceDetector
from visualization import start_ui 

def run_system():
    """ Starts traffic management system """
    traffic_controller = TrafficController()
    ambulance_detector = AmbulanceDetector(traffic_controller)

    # Start traffic light cycle in a separate thread
    traffic_thread = threading.Thread(target=traffic_controller.run_traffic_cycle, daemon=True)
    traffic_thread.start()

    # 🚨 Now, the input loop for detecting ambulances runs in the background
    while True:
        location = input("Enter intersection where ambulance is detected: ").strip().upper()
        if location in traffic_controller.signals:
            ambulance_detector.detect_ambulance(location)

if __name__ == "__main__":
    run_system()
