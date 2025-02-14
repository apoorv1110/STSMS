# *STSMS (Smart Traffic and Street Safety Management System)*

## *Overview*
STSMS is an AI-powered system designed to enhance *street safety , ambulance prioritization and traffic control* using computer vision and machine learning. It integrates real-time surveillance and automated decision-making for improved urban management.

## *Key Components*

### *🚨 Street Safety Management*
- AI-powered accident , threat , face recongnition and women safety management system.

### *🚑 Ambulance Management System*
- Detects ambulances at intersections.
- Adjusts traffic signals dynamically to prioritize emergency vehicles.

### *🚦 Traffic Management System*
- Analyzes vehicle density using AI-driven traffic monitoring.
- Optimizes signal timing to reduce congestion and improve flow.

## *Technology Stack*
- *Computer Vision & AI:* OpenCV, Deep Learning Models.
- *Incident Detection:* LLM with Flask API.
- *Traffic & Ambulance Detection:* YOLO-based object detection.
- *Backend:* Flask API for real-time processing.
- *Database:* PostgreSQL / MySQL for incident and vehicle data storage.

![WhatsApp Image 2025-02-14 at 12 14 27_dcb930a0](https://github.com/user-attachments/assets/0f2cc300-42d0-4b31-8cc8-6e6749f47da3)


# *Street Safety Management System*

## *Overview*
The *Street Safety Management System* is an AI-powered solution designed to enhance urban safety by monitoring streets through cameras, recognizing faces using *OpenCV, and detecting incidents using **a Large Language Model (LLM) with Flask*. It integrates real-time surveillance, face matching, and an automated alert system to notify law enforcement and the public about emergencies.

## *Technology Stack*
- *Face Recognition:* OpenCV and Deep Learning Models (Python-based real-time detection and matching)
- *Incident Detection:* LLM integrated with Flask (AI-based classification of incidents)
- *Backend:* Flask for API development
- *Database:* PostgreSQL / MySQL for storing wanted persons and incident reports

## *System Components*

### *1. Camera Module*
- *Camera Capture:* Captures live footage from street cameras.
- *Captured Frame:* Stores individual frames extracted from video footage.
- *Frame Storage:* Saves frames for further analysis by the system.

### *2. Face Recognition System (Using OpenCV)*
- *Face Detection:* Uses OpenCV to detect human faces in captured frames.
- *Feature Extraction:* Extracts facial features using OpenCV's deep learning models.
- *Face Matching:* Compares detected faces with a database of wanted persons.
- *Wanted Person DB:* Contains records of individuals flagged as wanted.
- *Police Alert System:* Triggers alerts to law enforcement if a match is found.

### *3. Incident Detection Module (LLM + Flask API)*
- *Image Preprocessing:* Enhances image quality for better analysis.
- *Incident Classification Model:* Uses an LLM to classify incidents (e.g., fights, accidents, theft, women harassment).
- *Flask API Integration:* A REST API built with Flask connects the LLM to the system for real-time processing.
- *Incident Type:* Determines the nature of the detected incident.
- *User Alert System:* Notifies Emergency Services based on the incident type.

### *4. Control Center*
- *Emergency Alert Successful:* Confirms that the alert has been successfully sent to authorities.

## *Workflow Summary*
1. *Camera Module* captures real-time footage and extracts frames.
2. Frames are analyzed using *OpenCV-based Face Recognition* to identify known suspects.
3. The same frames are processed by the *LLM-powered Incident Detection Module via Flask API* to classify events.
4. If a wanted suspect is found or an incident is detected, the *Police Alert System* is triggered.
5. Alerts are sent to the *Control Center, nearby law enforcement via the **Alert & Response System*.

## *How to Run*
### *1. Clone the Repository*
bash
git clone https://github.com/apoorv1110/STSMS.git
cd Street-Safety-Management-System


### *2. Start the LLM Service*
bash
python3 llm_service.py


### *3. Run the Face Recognition System*
bash
python3 judging_service/run_judge.py


### *4. Start the Incident Detection Module*
bash
python3 LLM.py


### *5. Run the Camera Capture Service*
bash
python3 capture_service/run_capture.py


## *System Execution Flow*
- The *camera* captures images in real time.
- The images are matched against the *wanted database*.
- The *LLM service* processes the image for incident detection.
- The system returns results from both modules and triggers alerts if necessary.

## *Key Features*
✅ *Real-time Face Recognition with OpenCV* – Identifies wanted persons instantly.
✅ *AI-powered Incident Detection with LLM + Flask* – Classifies incidents in real-time.
✅ *Automated Police Alerts* – Notifies law enforcement of emergencies.
✅ *REST API Integration* – Ensures smooth communication between different modules.

## *Future Enhancements*
- *Expanded Missing Persons Database* – To assist in rescue operations.
- 
![WhatsApp Image 2025-02-14 at 02 21 48_69ea89cf](https://github.com/user-attachments/assets/cd1024f2-877f-436d-ac68-c6929dc94195)
