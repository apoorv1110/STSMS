
from flask import Flask, request, jsonify, send_file
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
LAST_IMAGE_PATH = os.path.join(UPLOAD_FOLDER, "latest_image.jpg")

@app.route("/llm", methods=["POST"])
def process_image():
    """Handles image input and saves it for retrieval."""
    if "image" not in request.files:
        return jsonify({"error": "No image found"}), 400

    image = request.files["image"]
    image.save(LAST_IMAGE_PATH)

    return jsonify({"response": "Image uploaded successfully"}), 200

@app.route("/llm", methods=["GET"])
def get_latest_image():
    """Returns the last uploaded image."""
    if not os.path.exists(LAST_IMAGE_PATH):
        return jsonify({"error": "No image uploaded yet"}), 404

    return send_file(LAST_IMAGE_PATH, mimetype="image/jpeg")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)