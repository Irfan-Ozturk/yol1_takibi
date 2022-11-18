import cv2
import numpy as np
import matplotlib as pl
#hazır kullandığım video için cap tanımı
cap= cv2.VideoCapture("/Users/irfanozturk/Desktop/Opencv-udemy/Udemy-opcv/kendimi_deneme/videolar/yol.mp4")

while True:
    ret,frame=cap.read()

    frame = cv2.resize(frame, (640, 480))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 89, 175, cv2.THRESH_BINARY)
    blur = cv2.GaussianBlur(thresh, (5, 5), 3)
    canny = cv2.Canny(blur, 39, 175)


    def mask_of_frame(frame):
        height = frame.shape[0]
        polygons = np.array([[(0, height-60), (910, height), (300, 220)]])# kamera açısına göre manuel olarak polygon oluştruldu
        mask = np.zeros_like(frame)
        cv2.fillPoly(mask, polygons, (255, 255, 255))
        masked_frame = cv2.bitwise_and(frame, mask)
        return masked_frame

    lines = cv2.HoughLinesP(canny, 1, np.pi / 180, 30)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)




    cv2.imshow("Original", frame)
    cv2.imshow("Mask", mask_of_frame(frame))

    key=cv2.waitKey(20)
    if key==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()