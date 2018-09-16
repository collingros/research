import cv2
import os
import csv
import pickle
import numpy as np
import argparse
import time

def init(face_recognizer):
    try:
        face_recognizer.read(C["TRAIN_DATA"])
    except:
        print("error: \"" + C["TRAIN_DATA"] + "\" not found")
        print("\tyou need to run the trainer first!")
        exit()

def get_settings():
    C = {
    "SF":0,
    "MN":0,
    "TEST_HEIGHT":0,
    "TARGET":"",
    "WARM":0,
    "COLD":0,
    "LOW":0,
    "MED":0,
    "HIGH":0,
    "GLASSES":0,
    "HAT":0,
    "VANILLA":0,
    "PROFILES":0,
    "ANGLED":0,
    "CENTER":0,
    "CASCADE":"",
    "CONF_CUTOFF":0,
    "SHADOWS":0, # added for training
    "CENTER_SHADOW":0,
    "BEARDS":0
    }

    parser = argparse.ArgumentParser(description="testing LBPH")
    parser.add_argument("-s", help="testing scale factor", type=float)
    parser.add_argument("-n", help="testing min neighbors", type=int)
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
    parser.add_argument("-z", help="cascade path", type=str)
    parser.add_argument("-d", help="confidence threshold", type=int)
    parser.add_argument("-g", help="include shadows", type=int)
    parser.add_argument("-i", help="include center lighting angle", type=int)
    parser.add_argument("-j", help="include people with large beards", type=int)

    args = parser.parse_args()

    if args.s: # SCALE FACTOR
        C["SF"] = args.s
    if args.n: # MINIMUM NEIGHBORS
        C["MN"] = args.n
    if args.p: # TEST HEIGHT
        C["TEST_HEIGHT"] = args.p
    if args.t: # TARGET
        C["TARGET"] = args.t
    if args.w: # INCLUDE WARM PICTURES?
        C["WARM"] = args.w
    if args.c: # INCLUDE COLD PICTURES?
        C["COLD"] = args.c
    if args.l: # INCLUDE LOW PICTURES?
        C["LOW"] = args.l
    if args.m: # INCLUDE MED PICTURES?
        C["MED"] = args.m
    if args.b: # INCLUDE HIGH PICTURES?
        C["HIGH"] = args.b
    if args.e: # INCLUDE GLASSES PICTURES?
        C["GLASSES"] = args.e
    if args.f: # INCLUDE HAT PICTURES?
        C["HAT"] = args.f
    if args.v: # INCLUDE VANILLA PICTURES?
        C["VANILLA"] = args.v
    if args.x: # INCLUDE PROFILES PICTURES?
        C["PROFILES"] = args.x
    if args.a: # INCLUDE ANGLED POS PICTURES?
        C["ANGLED"] = args.a
    if args.o: # INCLUDE CENTER POS PICTURES?
        C["CENTER"] = args.o
    if args.g: # INCLUDE SHADOWS LIGHTING ANGLES?
        C["SHADOWS"] = args.g
    if args.i: # INCLUDE CENTER LIGHTING ANGLES?
        C["CENTER_SHADOW"] = args.i
    if args.j: # INCLUDE CENTER LIGHTING ANGLES?
        C["BEARDS"] = args.j
    #if args.z: # DATA FILE
    #    C["DATA"] = args.z
    # ASSUMING THAT THE DATAFILE IS IN "./train.yml"
    C["TRAIN_DATA"] = "train.yml"
    # ASSUMING THAT THE PICTURES TO BE TESTED ARE IN "./test"
    C["TEST_DIR"] = "test"
    C["RATIO"] = 1.5
    if args.z:
        C["CASCADE"] = args.z
    if args.d: # CONFIDENCE CUTOFF THRESHOLD
        C["CONF_CUTOFF"] = args.d

    return C

def get_labels():
    with open("labels.pickle", "rb") as f:
        og_labels = pickle.load(f)
    labels = {v:k for k, v in og_labels.items()}

    return labels

def show_face(pic, name):
    font = cv2.FONT_HERSHEY_SIMPLEX
    color = (255, 0, 0)
    stroke = 2

    cv2.rectangle(pic, (x, y), (x + w, y + h), (255, 0, 0), stroke)
    cv2.putText(pic, name, (x, y - 10), font,
                1, (0, 0, 255), stroke, cv2.LINE_AA)
    cv2.putText(pic, str(round(conf, 2)), (x, y + h + 20), font,
                0.6, (0, 255, 0), stroke, cv2.LINE_AA)

    cv2.imshow("pic", pic)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def detect_face(name, data, C, labels, face_cascade):
    pic = cv2.imread(name, 0)
    pic = cv2.resize(pic, (int(C["TEST_HEIGHT"] * C["RATIO"]),
                     C["TEST_HEIGHT"]))

    faces = face_cascade.detectMultiScale(pic, scaleFactor = C["SF"],
						                  minNeighbors = C["MN"]);
    if not len(faces):
        data["skipped"] += 1

    else:
        for (x, y, w, h) in faces:
            data["reviewed"] += 1

            face = pic[y:y+h, x:x+w]
            label, conf = face_recognizer.predict(face)
            name = labels[label]

            if not (C["TARGET"] in labels.values()): # if the person in the
            # current picture is not in the dataset
                unknown = True
                data["unknown_total"] += 1
            else
                unknown = False

            if conf > C["CONF_CUTOFF"]:
                name = "unknown"

            if name == C["TARGET"]:
                data["c_names"] += 1
            elif name == "unknown" and unknown:
                data["c_unknowns"] += 1
            elif name == "unknown" and not unknown:
                if labels[label] == C["TARGET"]: # unknown triggered when it
                    # shouldn't have
                    data["c_name_unknowns"] += 1
                else
                    data["w_unknowns"] += 1
                    
            else:
                data["w_names"] += 1

def test_data(cascade, data):
    dir_test = sorted(os.listdir(C["TEST_DIR"]))
    for pic_owner in dir_test:
        name = pic_owner
        pic_owner_path = C["TEST_DIR"] + "/" + pic_owner
        pics = sorted(os.listdir(pic_owner_path))

        for pic_type in pics:
            dir_pos_path = pic_owner_path + "/" + pic_type

            if pic_type == "glasses" and not C["GLASSES"]:
                continue

            if pic_type == "hat" and not C["HAT"]:
                continue

            if pic_type == "vanilla" and not C["VANILLA"]:
                continue

            dir_pos = sorted(os.listdir(dir_pos_path))

            for pos in dir_pos:
                dir_angle_path = dir_pos_path + "/" + pos

                if (pos == "pos_0" or pos == "pos_4") and not C["PROFILES"]:
                    continue

                if (pos == "pos_1" or pos == "pos_3") and not C["ANGLED"]:
                    continue

                if pos == "pos_2" and not C["CENTER"]:
                    continue

                dir_angle = sorted(os.listdir(dir_angle_path))

                for angle in dir_angle:
                    #print("angle: " + angle)
                    dir_img_path = dir_angle_path + "/" + angle
                    if angle == "angle_4" and not C["CENTER_SHADOW"]:
                        # if central lighting angle and we don't want it
                        continue
                    if angle != "angle_4" and not C["SHADOWS"]:
                        continue
                    dir_img = sorted(os.listdir(dir_img_path))

                    x = 0
                    for img in dir_img:
                        pic = ""
                        img_path = dir_img_path + "/" + img
                        #print("img: " + img)
                        #print("x: " + str(x))
                        if x == 0 and C["WARM"]:
                            #print("warm!")
                            pic = img_path
                        elif x == 1 and C["COLD"]:
                            #print("cold!")
                            pic = img_path
                        elif x == 2 and C["LOW"]:
                            #print("low!")
                            pic = img_path
                        elif x == 3 and C["MED"]:
                            #print("med!")
                            pic = img_path
                        elif x == 4 and C["HIGH"]:
                            #print("high!")
                            pic = img_path
                        if pic:
                            data = detect_face(pic, data, C, labels, cascade)
                        x += 1

data = {
    "skipped":0, # number of pictures skipped
    "reviewed":0, # number of pictures reviewed
    "unknown_total":0, # total of unknown pictures
    "c_unknowns":0, # correct unknown guesses
    "w_unknowns":0, # wrong unknown guesses
    "c_name_unknowns":0, # had the correct name, but unknown was triggered
    "c_names":0, # correct name guesses
    "w_names":0 # wrong name guesses
}
C = get_settings()
labels = get_labels()

start_time = time.time()

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
init(face_recognizer)
cascade = cv2.CascadeClassifier(C["CASCADE"])

test_data(cascade, data)

finish_time = time.time()
sec = finish_time - start_time

print("finished in " + str(sec) + " secs: ")
print("C")
print(C)
print("data")
print(data)
