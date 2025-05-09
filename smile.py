import cv2

facecascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smilecascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = facecascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        faceroi = gray[y:y+h, x:x+w]
        coloroi = frame[y:y+h, x:x+w]

        smiles = smilecascade.detectMultiScale(faceroi, scaleFactor=1.7, minNeighbors=22)

        if len(smiles) > 0:
            label = "Happy"
            color = (0, 255, 0)
        else:
            label = "Sad"
            color = (0, 0, 255)

            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
        
        cv2.imshow("Emotion Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()