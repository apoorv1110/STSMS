import os
import cv2
import dlib
import numpy as np

# Initialize models
face_detector = dlib.get_frontal_face_detector()
MODEL_PATH = os.path.join(os.path.dirname(__file__), "models", "shape_predictor_68_face_landmarks.dat")
shape_predictor = dlib.shape_predictor(MODEL_PATH)
MODEL_PATH = os.path.join(os.path.dirname(__file__), "models", "dlib_face_recognition_resnet_model_v1.dat")
face_recognition_model = dlib.face_recognition_model_v1(MODEL_PATH)

WANTED_FOLDER = os.path.join(os.path.dirname(__file__), "wanted")

def get_wanted_faces():
    """Loads all wanted faces from the 'wanted/' directory and extracts encodings."""
    wanted_faces = []
    
    if not os.path.exists(WANTED_FOLDER):
        os.makedirs(WANTED_FOLDER)

    for filename in os.listdir(WANTED_FOLDER):
        filepath = os.path.join(WANTED_FOLDER, filename)

        image = cv2.imread(filepath)
        if image is None:
            print(f"Skipping {filename}, unable to read image.")
            continue

        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        faces = face_detector(rgb_image)

        if len(faces) == 0:
            print(f"No face detected in {filename}, skipping...")
            continue

        shape = shape_predictor(rgb_image, faces[0])
        face_encoding = np.array(face_recognition_model.compute_face_descriptor(rgb_image, shape))

        wanted_faces.append({"name": filename.split(".")[0], "encoding": face_encoding})

    print(f"Loaded {len(wanted_faces)} wanted faces")
    return wanted_faces
