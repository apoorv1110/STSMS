
import base64
import requests

GOOGLE_GEMINI_API_KEY = "AIzaSyAtLMUaUDfxtDtSt-p-4Pe_qoGRYAs_qkM"
LLM_URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={GOOGLE_GEMINI_API_KEY}"
IMAGE_FETCH_URL = "http://127.0.0.1:8000/llm"
IMAGE_PATH = "captured_images/captured_frame.jpg"  # Ensure this matches the path in capture.py

def upload_image_to_server(image_path):
    """Uploads an image to the local server."""
    with open(image_path, "rb") as image_file:
        files = {"image": image_file}
        response = requests.post(IMAGE_FETCH_URL, files=files)

    if response.status_code != 200:
        raise Exception(f"Failed to upload image: {response.status_code} - {response.text}")

    print("Image uploaded successfully.")

def fetch_latest_image():
    """Fetches the latest uploaded image from the server and returns its Base64 encoding."""
    response = requests.get(IMAGE_FETCH_URL)
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
                return response_text  # Return the actual response
            else:
                raise Exception("No valid response from LLM")

        else:
            raise Exception(f"Google Gemini API error: {response.status_code} - {response.text}")

    except Exception as e:
        print("Error communicating with Google Gemini API:", e)
        raise

def process_image_through_pipeline():
    """Uploads an image, retrieves it, and sends it to the Gemini LLM."""
    try:
        upload_image_to_server(IMAGE_PATH)  # Uploads the image first
        image_base64 = fetch_latest_image()  # Fetches the stored image
        result = send_image_to_llm(image_base64)  # Sends the image to Gemini

        print("Final LLM Response:", result)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    process_image_through_pipeline()