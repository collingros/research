import os
import cv2
import pickle


people = {}
faces = {}
labels = {}
cascade = cv2.CascadeClassifier("./haar_default.xml")
face_rec = cv2.face.LBPHFaceRecognizer_create()

def draw(pic, name, conf, coords, color_str):
    if color_str == "green":
        color = (0, 255, 0)

    x = coords[0]
    y = coords[1]
    w = coords[2]
    h = coords[3]

    cv2.rectangle(pic, (x, y), (x+w, y+h), color, 2)
    cv2.putText(pic, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, color, 2, cv2.LINE_AA)
    cv2.putText(pic, str(conf), (x+w, y+h+10), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, color, 2, cv2.LINE_AA)


def guess(color_pic):
# draw rect on pic with guess on rect
    height = 120
    width = 160

    gray_pic = cv2.cvtColor(color_pic, cv2.COLOR_BGR2GRAY)
    gray_pic = cv2.resize(gray_pic, (width, height))

    detected = cascade.detectMultiScale(gray_pic, scaleFactor=1.01,
                                        minNeighbors=10)
    if not len(detected):
        return gray_pic

    for (x, y, w, h) in detected:
        face = gray_pic[y:y+h, x:x+w]
        label, conf = face_rec.predict(face)

        guess = labels[label]
        coords = [x, y, w, h]

        draw(gray_pic, guess, conf, coords, "green")

    return gray_pic


def load():
    face_rec.read("./train.yml")
    with open("./labels.pickle", "rb") as info:
        og_labels = pickle.load(info)

    for k, v in og_labels.items():
        labels[v] = k

load()

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()

    frame = guess(frame)
    cv2.imshow("frame", frame)

    c = cv2.waitKey(1)
    if 'q' == chr(c & 255):
        break

cv2.destroyAllWindows()
cap.release()

