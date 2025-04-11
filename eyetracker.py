import cv2
import cv2.data

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        rol_gray = gray[y:y + h, x:x + w]
        rol_color = frame[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(rol_gray)

        for (ox, oy ,ow, oh) in eyes:
            cv2.rectangle(rol_color, (ox, oy), (ox + ow, oy + oh), (255, 2550, 0), 2)

    cv2.imshow('Eye Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()