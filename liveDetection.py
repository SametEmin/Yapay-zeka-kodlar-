import cv2

# Load the pre-trained face detection cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 
'haarcascade_frontalface_default.xml')


# Create a VideoCapture object and specify the source (0 for default camera)
video_cap = cv2.VideoCapture(0)

while True:
    ret, frame = video_cap.read()

    # Check if frame was read successfully
    if not ret:
        print("Error reading frame")
        break
    
    # Convert frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Display the frame with detected faces
    cv2.imshow("Face Detection", frame)
    
    # Check for key press to exit (press 'q' to exit)
    if cv2.waitKey(10) == ord("q"):
        break

# Release the VideoCapture and close the window
video_cap.release()
cv2.destroyAllWindows()
