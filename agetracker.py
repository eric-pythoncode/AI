import cv2
import cv2.data

facecascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

agenet = cv2.dnn.readNetFromCaffe(
    'age_deploy.prototxt'
    'age_net.caffemodel'
)

agelist = ['(0 - 2)', '(4 - 6)', '(8 - 12)', '(15 - 20)', '(25 - 32)', '(38 - 43)', '(48 - 53)', '(60 - 100)']

modelmeanvalues = (78.4263377603, 87.7689143744, 114.895847746)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame = cv2.COLOR_BGR2GRAY)

    faces = facecascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        faceimg = frame[y:y+h, x:x+w]
        blob = cv2.dnn.blobFromImage(faceimg, 1.0, (277, 277), modelmeanvalues, swapRB=False)

        agenet.setInput(blob)
        agepreds = agenet.forward()
        age = agelist[agepreds[0].argmax()]

        label = f"Age: {age}"
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    cv2.imshow("Age Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('5'):
        break


cap.release()
cv2.destroyAllWindows()