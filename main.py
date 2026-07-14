# type: ignore
import cv2
import mediapipe as mp


cap = cv2.VideoCapture(0)


while True:
    success, img = cap.read()
    
    if not success:
        print("kurcina")
        break

    img = img.copy()
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
 
    cv2.imshow("Hand Tracker", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()