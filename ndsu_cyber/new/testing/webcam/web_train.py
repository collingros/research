import cv2
import os
import numpy as np
import pickle
import math
import time


faces = []
labels = []
people = {}
cascade = cv2.CascadeClassifier("./haar_default.xml")
face_rec = cv2.face.LBPHFaceRecognizer_create()


def train():
    face_rec.train(faces, np.array(labels))
    face_rec.save("./train.yml")

    with open("./labels.pickle", "wb") as info:
        pickle.dump(people, info)


def draw(pic, coords, color_str):
    if color_str == "green":
        color = (0, 255, 0)

    x = coords[0]
    y = coords[1]
    w = coords[2]
    h = coords[3]

    cv2.rectangle(pic, (x, y), (x+w, y+h), color, 2)


def add(path, dir_num, num):
    gray_pic = cv2.imread(path, 0)

    height = 120
    width = 160

    gray_pic = cv2.resize(gray_pic, (width, height))
    detected = cascade.detectMultiScale(gray_pic, scaleFactor=1.005,
                                        minNeighbors=10)
    if not len(detected):
        print("skipped: {0}".format(path))
        return

    for (x, y, w, h) in detected:
        print("saved: {0}".format(path))
        face = gray_pic[y:y+h, x:x+w]
        faces.append(face)
        labels.append(dir_num)

        coords = [x, y, w, h]

    draw(gray_pic, coords, "green")

    name = "./train/{0}/faces/{1}.png".format(id, num)
    cv2.imwrite(name, gray_pic)

cwd = os.getcwd()
dir_num = 0
num = 0
train_path = "{0}/{1}".format(cwd, "train")
for id in sorted(os.listdir(train_path)):
    people[id] = dir_num
    id_path = "{0}/{1}".format(train_path, id)

    for pic in sorted(os.listdir(id_path)):
        if pic == "faces":
            continue

        pic_path = "{0}/{1}".format(id_path, pic)
        add(pic_path, dir_num, num)

        num += 1
    dir_num += 1

train()
