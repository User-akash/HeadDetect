import cv2
cap = cv2.VideoCapture(0)
face_reg = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:
    fps , frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # img = cv2.adaptiveThreshold(gray,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
    faces = face_reg.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame,(x,y), (x+w,y+h), (255, 0, 0), 2)
    cv2.imshow("shadhin",cv2.flip(frame,1))
    if cv2.waitKey(1) & 255 == ord('q'):
        break

cap.release()
cv2.destroyWindow()