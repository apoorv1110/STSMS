import cv2
import dlib
import numpy as np
from flask import Flask, request, jsonify
import database
import config
import os

# Initialize models
face_detector = dlib.get_frontal_face_detector()
MODEL_PATH = os.path.join(os.path.dirname(__file__), "models", "shape_predictor_68_face_landmarks.dat")
shape_predictor = dlib.shape_predictor(MODEL_PATH)
MODEL_PATH = os.path.join(os.path.dirname(__file__), "models", "dlib_face_recognition_resnet_model_v1.dat")
face_recognition_model = dlib.face_recognition_model_v1(MODEL_PATH)

app = Flask(__name__)

# ✅ Root route to avoid 404 on GET /
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Face recognition API running"}), 200

# ✅ Define only one /judge route
@app.route("/judge", methods=["POST"])
def judge_image():
    """Receives an image, detects faces, and matches them against stored suspects."""
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400

    # Read image
    file = request.files["image"].read()
    nparr = np.frombuffer(file, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convert to RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    faces = face_detector(rgb_image)

    if len(faces) == 0:
        return jsonify({"message": "No face detected"}), 200

    # ✅ Load wanted faces from the "wanted" folder
    wanted_faces = database.get_wanted_faces()

    if not wanted_faces:
        return jsonify({"message": "No wanted faces found in database"}), 200

    results = []

    for face in faces:
        shape = shape_predictor(rgb_image, face)
        face_encoding = np.array(face_recognition_model.compute_face_descriptor(rgb_image, shape))

        print(f"Computed face encoding: {face_encoding}")  # Debugging

        best_match = None
        best_score = float("inf")

        for suspect in wanted_faces:
            score = np.linalg.norm(face_encoding - suspect["encoding"])  # Euclidean Distance
            if score < best_score:
                best_score = score
                best_match = suspect["name"]

        if best_score < config.MATCH_THRESHOLD:
            results.append({"match": best_match, "score": best_score})
        else:
            results.append({"match": "No match", "score": best_score})

    return jsonify({"results": results}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT)
