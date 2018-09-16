import cv2
import os
import csv
import pickle
import numpy as np
import argparse

SF = 1.3
MN = 3
TEST_DIR = "../database/test"
TEST = ""
CASCADE = "cascades/data/haarcascade_frontalface_default.xml"
DATA = "trained_data.yml"
TARGET = ""
SAVED_DIR = ""
TEST_HEIGHT = 100
TEST_RATIO = 1.5

WARM = 0
COLD = 0
LOW = 0
MED = 0
HIGH = 0

parser = argparse.ArgumentParser(description="train the f.r. algorithm")
parser.add_argument("-s", help="training scale factor", type=float)
parser.add_argument("-n", help="training min neighbors", type=int)
parser.add_argument("-p", help="resized height", type=int)
parser.add_argument("-v", help="video name", type=str)
parser.add_argument("-t", help="target", type=str)
parser.add_argument("-w", help="warm", type=str)
parser.add_argument("-c", help="cold", type=str)
parser.add_argument("-l", help="low", type=str)
parser.add_argument("-m", help="medium", type=str)
parser.add_argument("-b", help="high", type=str)
parser.add_argument("-r", help="directory to save to", type=str)
args = parser.parse_args()

if args.s:
    SF = args.s
if args.n:
    MN = args.n
if args.p:
    TEST_HEIGHT = args.p
if args.v:
    TEST = args.v 
if args.t:
    TARGET = args.t
if args.w:
    WARM = args.w
if args.c:
    COLD = args.c
if args.l:
    LOW = args.l
if args.m:
    MED = args.m
if args.b:
    HIGH = args.b
if args.r:
    SAVED_DIR = args.r

#print("s: " + str(SF) + "\tn: " + str(MN) + "\tv: " + TEST)

#get the labels from tainer output
if SAVED_DIR == "":
    with open("labels_v2.pickle", "rb") as f:
	    og_labels = pickle.load(f)
	    labels = {v:k for k, v in og_labels.items()}
else:
    with open(SAVED_DIR + "/" + "labels_v2.pickle", "rb") as f:
	    og_labels = pickle.load(f)
	    labels = {v:k for k, v in og_labels.items()}
with open("stat_train.txt", "r") as f:
    TRAIN_SF = f.readline().rstrip()
    TRAIN_MN = f.readline().rstrip()
    HEIGHT = f.readline().rstrip()
    RATIO = f.readline().rstrip()
    GLASSES = f.readline().rstrip()
    HAT = f.readline().rstrip()
    VANILLA = f.readline().rstrip()
    TR_WARM = f.readline().rstrip()
    TR_COLD = f.readline().rstrip()
    TR_LOW = f.readline().rstrip()
    TR_MED = f.readline().rstrip()
    TR_HIGH = f.readline().rstrip()
    SHADOWS = f.readline().rstrip()
    PROFILES = f.readline().rstrip()
    ANGLED = f.readline().rstrip()
    CENTER = f.readline().rstrip()
    BEARDS = f.readline().rstrip()

face_recognizer = cv2.face.LBPHFaceRecognizer_create()

try:
    if SAVED_DIR == "":
        face_recognizer.read(DATA)
    else:
        face_recognizer.read(SAVED_DIR + "/" + DATA)
except:
    #print("error: \"" + DATA + "\" not found")
    #print("\tyou need to run the trainer first!")
    exit()

if not TEST:
    dir_test = sorted(os.listdir(TEST_DIR))
    for vid_owner in dir_test:
        if vid_owner == TARGET:
            vid_owner_path = TEST_DIR + "/" + vid_owner
            vids = os.listdir(vid_owner_path)
            for vid in vids:
                if vid.find("warm") != -1 and WARM:
                    TEST = vid
                elif vid.find("cold") != -1 and COLD:
                    TEST = vid
                elif vid.find("low") != -1 and LOW:
                    TEST = vid
                elif vid.find("med") != -1 and MED:
                    TEST = vid
                elif vid.find("high") != -1 and HIGH:
                    TEST = vid

    TEST = vid_owner_path + "/" + TEST
#print("vid set as: " + TEST)

total_frames = 0
total_faces = 0
correct = 0
#test = cv2.imread("test/" + TEST) pic
cap = cv2.VideoCapture(TEST) #vid
#test = cv2.imread("test/" + "test.JPG", 0)
#test = cv2.resize(test, (640, 480))
#cap = cv2.VideoCapture(0)
#while cap.isOpened():
while cap.isOpened():
    ret, test = cap.read()
    if not ret:
        break
    test = cv2.resize(test, (int(TEST_HEIGHT * 1.5), TEST_HEIGHT))
    gray = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)
    #gray = test
    face_cascade = cv2.CascadeClassifier(CASCADE)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = SF,
							              minNeighbors = MN);
    if not len(faces):
        #print("couldn't find a face!")
        pass
    else:
        for (x, y, w, h) in faces:
            face = gray[y:y+h, x:x+w]
            label, conf = face_recognizer.predict(face)

            name = labels[label]

            font = cv2.FONT_HERSHEY_SIMPLEX
            color = (255, 0, 0)
            stroke = 2
            cv2.rectangle(test, (x, y), (x + w, y + h), (255, 0, 0), stroke)
            cv2.putText(test, name, (x, y - 10), font,
	                    1, (0, 0, 255), stroke, cv2.LINE_AA)
            cv2.putText(test, str(round(conf, 2)), (x, y + h + 20), font,
	                    0.6, (0, 255, 0), stroke, cv2.LINE_AA)

            if name == TARGET:
                correct += 1
            total_faces += 1

    cv2.imshow("test", test)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    total_frames += 1
cap.release()
cv2.destroyAllWindows()

try:
    accuracy = (float(correct) / float(total_faces)) * 100
except:
    accuracy = 0
#print("accuracy: " + (str(accuracy)))

with open("stat.txt", "a") as f:
    f.write("SF: " + str(SF) + "\n")
    f.write(str(TRAIN_SF) + "\n")
    f.write("MN: " + str(MN) + "\n")
    f.write(str(TRAIN_MN) + "\n")
    f.write("TOTAL FRAMES: " + str(total_frames) + "\n")
    f.write("DETECTED FACES: " + str(total_faces) + "\n")
    f.write("ACCURACY: " + str(accuracy) + "\n")
    f.write("VIDEO: " + TEST + "\n")
    f.write("TARGET: " + TARGET + "\n")
    f.write("TEST_HEIGHT: " + str(TEST_HEIGHT) + "\n")
    f.write("BEARDS: " + str(BEARDS) + "\n")
    f.write(str(HEIGHT) + "\n")
    f.write(str(RATIO) + "\n")
    f.write(str(GLASSES) + "\n")
    f.write(str(HAT) + "\n")
    f.write(str(VANILLA) + "\n")
    f.write(str(TR_WARM) + "\n")
    f.write(str(TR_COLD) + "\n")
    f.write(str(TR_LOW) + "\n")
    f.write(str(TR_MED) + "\n")
    f.write(str(TR_HIGH) + "\n")
    f.write(str(SHADOWS) + "\n")
    f.write(str(PROFILES) + "\n")
    f.write(str(ANGLED) + "\n")
    f.write(str(CENTER) + "\n")
    f.write(str(TEST) + "\n\n")

