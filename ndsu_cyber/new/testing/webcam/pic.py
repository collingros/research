import cv2


cap = cv2.VideoCapture(0)
num = 0
while(True):
    ret, frame = cap.read()
    cv2.imshow("frame", frame)

    c = cv2.waitKey(1)
    if 's' == chr(c & 255):
        name = "{0}.png".format(num)
        cv2.imwrite(name, frame)
        num += 1
    elif 'q' == chr(c & 255):
        break

cv2.destroyAllWindows()
cap.release()
