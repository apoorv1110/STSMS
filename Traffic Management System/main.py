import cv2
import numpy as np

# Load the image
image_path = r"images\traffic.png"
image = cv2.imread(image_path)

# Load Haar Cascade Classifier
cascade_path = r"models\haarcascade_car.xml"
car_cascade = cv2.CascadeClassifier(cascade_path)

if image is None:
    print("❌ Failed to load image. Check the file path and format.")
    exit()

if car_cascade.empty():
    print("❌ Error loading Haar cascade. Check file path or OpenCV installation.")
    exit()

print("✅ Image and Haar Cascade loaded successfully.")

# Step 1: Preprocessing
resized = cv2.resize(image, (640, 480))  # Resize before grayscale
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
blurred = cv2.GaussianBlur(gray, (5, 5), 0)  # Apply Gaussian blur

# Step 2: Vehicle Detection using Haar Cascade Classifier
cars = car_cascade.detectMultiScale(blurred, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))

# Step 3: Draw bounding boxes and count vehicles
vehicle_count = len(cars)

for (x, y, w, h) in cars:
    cv2.rectangle(resized, (x, y), (x + w, y + h), (0, 255, 0), 2)

print(f"🚗 Detected Vehicles: {vehicle_count}")

# Step 4: Adjust Traffic Signal Timing
default_time = 30  # Default green signal time in seconds
additional_time = min(vehicle_count * 2, 30)  # Increase by 2 sec per vehicle (max +30 sec)
final_signal_time = default_time + additional_time

print(f"⏳ Adjusted Signal Timing: {final_signal_time} seconds")

# Show the processed image
cv2.imshow("Detected Vehicles", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
