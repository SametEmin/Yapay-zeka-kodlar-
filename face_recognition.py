import cv2
import dlib

# Load a sample image with known faces
known_image_path = "known_face.jpg"
known_image = cv2.imread(known_image_path)
known_face_name = "Known Person"

# Initialize webcam
video_capture = cv2.VideoCapture(0)

# Load the face detector from dlib
face_detector = dlib.get_frontal_face_detector()

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Convert frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_detector(gray)

    # Iterate through detected faces
    for face in faces:
        x, y, w, h = face.left(), face.top(), face.width(), face.height()

        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Display the name
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, known_face_name, (x + 6, y - 6), font, 0.5, (255, 255, 255), 1)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close all windows
video_capture.release()
cv2.destroyAllWindows()
