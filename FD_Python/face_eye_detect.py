import  cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

img = cv2.imread('player.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3,5)

for (x, y, w, h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    roi_gray = gray[y:y + h, x:x+w]
    roi_color = img[y:y + h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray,1.3,5)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 255), 2)
cv2.imshow('Eyes Detection', img)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()