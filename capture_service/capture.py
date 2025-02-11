import cv2
import time
import requests
import config

def capture_and_send():
    cap = cv2.VideoCapture(config.CAMERA_INDEX)

    if not cap.isOpened():
        print("Error: Could not access the camera.")
        return
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            continue

        _, img_encoded = cv2.imencode('.jpg', frame)
        response = requests.post(config.JUDGING_SERVICE_URL, files={'image': img_encoded.tobytes()})
        
        print(f"Sent image to judging service. Response: {response.text}")

        time.sleep(config.CAPTURE_INTERVAL)  # Wait before capturing the next frame

    cap.release()

if __name__ == "__main__":
    capture_and_send()
