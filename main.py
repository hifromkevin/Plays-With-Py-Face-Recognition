import cv2
import face_recognition
import pickle
import os

# File to store known faces
KNOWN_FACES_FILE = "faces.pkl"

# Load known faces if they exist
if os.path.exists(KNOWN_FACES_FILE):
    with open(KNOWN_FACES_FILE, "rb") as f:
        known_faces = pickle.load(f)
else:
    known_faces = {"encodings": [], "names": []}

# Open webcam
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces and get their encodings
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_faces["encodings"], face_encoding)
        name = "Unknown"

        if True in matches:
            name = known_faces["names"][matches.index(True)]
        else:
            # New face detected: Register it
            name = input("New face detected! Enter name: ")
            known_faces["encodings"].append(face_encoding)
            known_faces["names"].append(name)
            print(f"New face registered as: {name}")

        # Draw box and name
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # Show video feed
    cv2.imshow("Face Recognition", frame)

    # Save updated known faces
    with open(KNOWN_FACES_FILE, "wb") as f:
        pickle.dump(known_faces, f)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()