import cv2
import os
import csv
import pickle
import numpy as np
import argparse
import time

start_time = time.time()

SF = 1.3
MN = 3
TEST_DIR = "../../../collin_database/pic_test"
TEST = ""
#CASCADE = "cascades/data/haarcascade_frontalface_default.xml"
CASCADE = "cascades/data/haarcascade_frontalface_alt2.xml"
DATA = "trained_data.yml"
TARGET = ""
SAVED_DIR = ""
TEST_HEIGHT = 100
TEST_RATIO = 1.5

# category restriction
GLASSES = 0
HAT = 0
VANILLA = 0

WARM = 0
COLD = 0
LOW = 0
MED = 0
HIGH = 0

# person position
PROFILES = 0
ANGLED = 0
CENTER = 0

face_recognizer = cv2.face.LBPHFaceRecognizer_create()

def detect_face(pic_n):
    total_faces = 0
    accuracy = 0
    correct = 0
    unknown_true = False
    unknown_correct = 0
    unknown_total = 0
    false_negative = 0
    false_positive = 0

    #print("current picture name is " + pic_n)

    pic = cv2.imread(pic_n, 0)

    pic = cv2.resize(pic, (int(TEST_HEIGHT * 1.5), TEST_HEIGHT))



    face_cascade = cv2.CascadeClassifier(CASCADE)
    faces = face_cascade.detectMultiScale(pic, scaleFactor = SF,
						                  minNeighbors = MN);
    if not len(faces):
        #print("couldn't find a face!")
        pass
    else:
        for (x, y, w, h) in faces:
            total_faces += 1
            face = pic[y:y+h, x:x+w]
            label, conf = face_recognizer.predict(face)
            name = labels[label]
            if not (str(TARGET) in labels.values()):
                unknown_true = 1 # so we know the correct answer is "unknown"
                unknown_total += 1

            if conf > 99999:
                name = "unknown"


            font = cv2.FONT_HERSHEY_SIMPLEX
            color = (255, 0, 0)
            stroke = 2
            cv2.rectangle(pic, (x, y), (x + w, y + h), (255, 0, 0), stroke)
            cv2.putText(pic, name, (x, y - 10), font,
                        1, (0, 0, 255), stroke, cv2.LINE_AA)
            cv2.putText(pic, str(round(conf, 2)), (x, y + h + 20), font,
                        0.6, (0, 255, 0), stroke, cv2.LINE_AA)
            #cv2.imshow("frame", pic)
            #cv2.waitKey(0)
            #print("name: " + name)
            #print("target: " + TARGET)
            if name == str(TARGET):
                #print("correctly identified as " + name + "!")
                correct += 1
            elif name == "unknown" and unknown_true:
                #print("true unknown individual!")
                unknown_correct += 1
            elif name == "unknown" and not unknown_true:
                #print("false unknown individual \"" + labels[label] + "\"!")
                if labels[label] == str(TARGET): # unknown triggered when it
                                                 # shouldn't have
                    false_negative += 1
            else:
                #print("incorrectly identified as " + labels[label] + "!")
                if unknown_true: # unknown did not trigger when it should
                    false_positive += 1
            #print("confidence: " + str(conf) + "\n")
            #input()


            cv2.destroyAllWindows()

    data = []
    data.append(correct)
    data.append(total_faces)
    data.append(unknown_correct)
    data.append(unknown_total)
    data.append(false_negative)
    data.append(false_positive)
    #print("correct: " + str(correct))
    #print("total_faces: " + str(total_faces))
    return data



parser = argparse.ArgumentParser(description="train the f.r. algorithm")
parser.add_argument("-s", help="training scale factor", type=float)
parser.add_argument("-n", help="training min neighbors", type=int)
parser.add_argument("-p", help="resized height", type=int)
parser.add_argument("-t", help="target", type=str)
parser.add_argument("-w", help="warm", type=str)
parser.add_argument("-c", help="cold", type=str)
parser.add_argument("-l", help="low", type=str)
parser.add_argument("-m", help="medium", type=str)
parser.add_argument("-b", help="high", type=str)
parser.add_argument("-e", help="include glasses pictures", type=int)
parser.add_argument("-f", help="include hat pictures", type=int)
parser.add_argument("-v", help="include vanilla pictures", type=int)
parser.add_argument("-x", help="include profile positions", type=int)
parser.add_argument("-a", help="include angled positions", type=int)
parser.add_argument("-o", help="include central positions", type=int)
args = parser.parse_args()

if args.s:
    SF = args.s
if args.n:
    MN = args.n
if args.p:
    TEST_HEIGHT = args.p
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
if args.e:
    GLASSES = args.e
if args.f:
    HAT = args.f
if args.v:
    VANILLA = args.v
if args.x:
    PROFILES = args.x
if args.a:
    ANGLED = args.a
if args.o:
    CENTER = args.o

#get the labels from tainer output
with open("labels_v2.pickle", "rb") as f:
    og_labels = pickle.load(f)
    labels = {v:k for k, v in og_labels.items()}


try:
    face_recognizer.read(DATA)
except:
    print("error: \"" + DATA + "\" not found")
    print("\tyou need to run the trainer first!")
    exit()

stats = []
c = 0
if not TEST:
    dir_test = sorted(os.listdir(TEST_DIR))
    for pic_owner in dir_test:
        TARGET = pic_owner
    #if pic_owner == TARGET:
        pic_owner_path = TEST_DIR + "/" + pic_owner
        #print("pic owner: " + pic_owner_path)
        pics = sorted(os.listdir(pic_owner_path))

        for pic_type in pics:
            dir_pos_path = pic_owner_path + "/" + pic_type
            #print("new pic")
            if pic_type == "glasses" and not GLASSES:
                #print("unwanted glasses! (glasses are off)")
                continue
            if pic_type == "hat" and not HAT:
                #print("unwanted hat! (hats are off)")
                continue
            if pic_type == "vanilla" and not VANILLA:
                #print("unwanted vanilla faces! (vanilla is off)")
                continue
            dir_pos = sorted(os.listdir(dir_pos_path))
            for pos in dir_pos:
                #print("pos: " + pos)
                dir_angle_path = dir_pos_path + "/" + pos
                if (pos == "pos_0" or pos == "pos_4") and not PROFILES:
                    #print("unwanted profile view! (profiles are off)")
                    continue
                if (pos == "pos_1" or pos == "pos_3") and not ANGLED:
                    #print("unwanted angled view! (angles are off)")
                    continue
                if pos == "pos_2" and not CENTER:
                    #print("unwanted central view! (central view is off)")
                    continue
                dir_angle = sorted(os.listdir(dir_angle_path))

                for angle in dir_angle:
                    #print("angle: " + angle)
                    dir_img_path = dir_angle_path + "/" + angle
                    dir_img = sorted(os.listdir(dir_img_path))

                    x = 0
                    for img in dir_img:
                        TEST = ""
                        img_path = dir_img_path + "/" + img
                        #print("img: " + img)
                        #print("x: " + str(x))
                        if x == 0 and WARM:
                            #print("warm!")
                            TEST = img_path
                        elif x == 1 and COLD:
                            #print("cold!")
                            TEST = img_path
                        elif x == 2 and LOW:
                            #print("low!")
                            TEST = img_path
                        elif x == 3 and MED:
                            #print("med!")
                            TEST = img_path
                        elif x == 4 and HIGH:
                            #print("high!")
                            TEST = img_path

                        x += 1


                        if TEST:
                            #print("test: " + str(TEST))
                            data = detect_face(TEST)
                            #print("data: " )
                            #print(data)
                            stats.append(data[0])
                            stats.append(data[1])
                            stats.append(data[2])
                            stats.append(data[3])
                            stats.append(data[4]) # false negative
                            stats.append(data[5]) # false positive
                            c += 1
                            #print("hi!!")
                    #print("TEST: " + TEST)
length = len(stats)
#print(stats)
x = 1
faces = 0
accuracy = 0
correct = 0
unknown_correct = 0
unknown_total = 0
unknown = 0 # percentage correct unknown
false_negative = 0
false_positive = 0

total_faces = sum(stats[1::6])
#print("total faces is " + str(total_faces))
total_correct = sum(stats[0::6])
#print("total correct is " + str(total_correct) + " out of " + str(c))
unknown_correct = sum(stats[2::6])
#print("total unknown correct is " + str(unknown_correct))
unknown_total = sum(stats[3::6])
#print("total unknown is " + str(unknown_total))
false_negative = sum(stats[4::6])
#print("total false negative is " + str(false_negative))
false_positive = sum(stats[5::6])
#print("total false positive is " + str(false_positive))

try:
    accuracy = (total_correct / total_faces) * 100
    accuracy = round(accuracy, 2)
except:
    pass

#print("total accuracy: " + str(accuracy))

try:
    unknown = (unknown_correct / unknown_total) * 100
    unknown = round(unknown, 2)
except:
    pass

#print("unknown accuracy: " + str(unknown))

negatives = 0
try:
    negatives = (false_negative / unknown_total) * 100
    negatives = round(negatives, 2)
except:
    pass

#print("unknown false negative percentage: " + str(negatives))

positives = 0
try:
    positives = (false_positive / unknown_total) * 100
    positives = round(positives, 2)
except:
    pass

#print("unknown false positive percentage: " + str(positives))


id_acc = 0
try:
    #print("unknown correct: " + str(unknown_correct) + "\ttotal correct: " + str(total_correct))
    #print("c: " + str(c))
    id_acc = ((unknown_correct + total_correct) / c) * 100
    id_acc = round(id_acc, 2)
except:
    pass

print("% identified: " + str(id_acc))

acc = 0
try:
    #print("unknown correct: " + str(unknown_correct))
    #print("total_correct: " + str(total_correct))
    #print("total_faces: " + str(total_faces))
    acc = ((unknown_correct + total_correct) / total_faces) * 100
    acc = round(acc, 2)
except:
    pass

print("% accuracy: " + str(acc))

finish_time = time.time()
sec = finish_time - start_time

