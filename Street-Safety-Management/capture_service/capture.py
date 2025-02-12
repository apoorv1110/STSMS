
import cv2
import time
import base64
import requests
import os

# Configurations
CAMERA_INDEX = 0  # Change if using an external camera
CAPTURE_INTERVAL = 2  # Time (in seconds) between captures
IMAGE_PATH = "captured_images/captured_frame.jpg"

# Ensure the captured_images folder exists
os.makedirs("captured_images", exist_ok=True)

# URLs
IMAGE_UPLOAD_URL = "http://127.0.0.1:8000/llm"  # For LLM service
JUDGE_URL = "http://127.0.0.1:5000/judge"  # For face detection and recognition
GOOGLE_GEMINI_API_KEY = "AIzaSyDWFmyny36jYVIcMYv5msXl3Y-Ni_0lMpQ"
LLM_URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={GOOGLE_GEMINI_API_KEY}"

def capture_image():
    """Captures an image from the camera and saves it."""
    cap = cv2.VideoCapture(CAMERA_INDEX)

    if not cap.isOpened():
        print("Error: Could not access the camera.")
        return None

    # Allow the camera to initialize (optional but recommended)
    time.sleep(7)

    # Read and discard a few frames to clear the buffer
    for _ in range(5):  # Adjust the number of frames to discard if needed
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to discard buffered frames.")
            cap.release()
            return None

    # Capture a new frame
    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("Error: Failed to capture frame.")
        return None

    # Save the image
    cv2.imwrite(IMAGE_PATH, frame)
    print(f"Image captured and saved as {IMAGE_PATH}")
    return IMAGE_PATH

def upload_image(image_path, url):
    """Uploads an image to the specified URL."""
    with open(image_path, "rb") as image_file:
        files = {"image": image_file}
        response = requests.post(url, files=files)

    if response.status_code != 200:
        raise Exception(f"Failed to upload image: {response.status_code} - {response.text}")

    print(f"Image uploaded successfully to {url}.")
    return response.json()  # Return the JSON response from the server

def fetch_latest_image():
    """Fetches the latest uploaded image from the server and returns its Base64 encoding."""
    response = requests.get(IMAGE_UPLOAD_URL)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch image: {response.status_code} - {response.text}")

    with open("captured_images/captured_frame.jpg", "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def send_image_to_llm(image_base64):
    """Sends the image to Google Gemini API and extracts the response."""
    try:
        question = "Tell what is present in this image. If there is an accident in the image, then only write 'accident'. If there is a woman making a cross sign, then only write 'woman harassment'."

        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [
                        {"text": question},
                        {"inline_data": {"mime_type": "image/jpeg", "data": image_base64}}
                    ]
                }
            ]
        }

        headers = {"Content-Type": "application/json"}
        response = requests.post(LLM_URL, json=payload, headers=headers)

        if response.status_code == 200:
            result = response.json()
            
            # Ensure response contains expected structure
            if "candidates" in result and result["candidates"]:
                response_text = result["candidates"][0]["content"]["parts"][0]["text"]
                print("Response Text:", response_text)
                return response_text
            else:
                raise Exception("No valid response from LLM")

        else:
            raise Exception(f"Google Gemini API error: {response.status_code} - {response.text}")

    except Exception as e:
        print("Error communicating with Google Gemini API:", e)
        raise

def process_image_pipeline():
    """Captures an image, uploads it for face detection, and sends it to the Gemini LLM."""
    try:
        # Step 1: Capture image
        image_path = capture_image()
        if not image_path:
            return

        # Step 2: Upload image to judge.py for face detection and recognition
        print("Sending image to judge.py for face detection...")
        judge_response = upload_image(image_path, JUDGE_URL)
        print("Face detection results:", judge_response)

        # Step 3: Upload image to llm_service.py for LLM processing
        print("Sending image to llm_service.py for LLM analysis...")
        upload_image(image_path, IMAGE_UPLOAD_URL)
        image_base64 = fetch_latest_image()
        llm_response = send_image_to_llm(image_base64)

        print("Final LLM Response:", llm_response)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    process_image_pipeline()