import cv2
import os
import csv
import pickle
import numpy as np
import argparse
import time

def save_labels(people):
    string = os.getcwd() + "/" + C["OUT"] + "/"
    with open(string + "labels.pickle", "wb") as f:
        pickle.dump(people, f)

def save_train(fr, faces, labels):
    fr.train(faces, np.array(labels))
    string = os.getcwd() + "/" + C["OUT"] + "/"
    fr.save(string + "train.yml")

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
    parser.add_argument("-k", help="pic out dir", type=str)

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
    C["TEST_DIR"] = "train"
    C["RATIO"] = 1.5
    if args.z:
        C["CASCADE"] = args.z
    if args.d: # CONFIDENCE CUTOFF THRESHOLD
        C["CONF_CUTOFF"] = args.d
    if args.k:
        C["OUT"] = args.k

    return C

def save_face(x, y, w, h, pic, name, c, pic_path, C):
    font = cv2.FONT_HERSHEY_SIMPLEX
    color = (255, 0, 0)
    stroke = 2

    cv2.rectangle(pic, (x, y), (x + w, y + h), (255, 0, 0), stroke)
    cv2.putText(pic, name, (x, y - 10), font,
                1, (0, 0, 255), stroke, cv2.LINE_AA)

    pic = cv2.resize(pic, (int(300 * C["RATIO"]), 300))

    string = os.getcwd() + "/" + C["OUT"] + "/" + name + str(c) + ".JPG"
    cv2.imwrite(string, pic)

def show_face(x, y, w, h, pic, name):
    font = cv2.FONT_HERSHEY_SIMPLEX
    color = (255, 0, 0)
    stroke = 2

    cv2.rectangle(pic, (x, y), (x + w, y + h), (255, 0, 0), stroke)
    cv2.putText(pic, name, (x, y - 10), font,
                1, (0, 0, 255), stroke, cv2.LINE_AA)

    cv2.imshow("pic", pic)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def add_face(pic_path, name, C, labels, dir_count, face_cascade, faces,
             people, c):
    pic = cv2.imread(pic_path, 0)

    pic = cv2.resize(pic, (int(C["TEST_HEIGHT"] * C["RATIO"]),
                     C["TEST_HEIGHT"]))

    detected_faces = face_cascade.detectMultiScale(pic, scaleFactor = C["SF"],
						                  minNeighbors = C["MN"]);
    if not len(detected_faces):
        data["skipped"] += 1

    # might want to delete for and
    # (x, y, w, h) = face[0]
    else:
        for (x, y, w, h) in detected_faces:
            data["reviewed"] += 1
            #show_face(x, y, w, h, pic, name)

            save_face(x, y, w, h, pic, name, c, pic_path, C)

            face = pic[y:y+h, x:x+w]
            faces.append(face)
            labels.append(dir_count)


def train_data(fr, cascade, data, C):
    people = {}
    labels = []
    faces = []
    dir_count = 0
    c = 0
    img_count = 0

    dir_test = sorted(os.listdir(C["TEST_DIR"]))
    for pic_owner in dir_test:
        name = pic_owner
        pic_owner_path = C["TEST_DIR"] + "/" + pic_owner

        if pic_owner == "1" or pic_owner == "2" and not C["BEARDS"]:
            continue

        people[pic_owner] = dir_count
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
                    dir_img_path = dir_angle_path + "/" + angle

                    if angle == "angle_4" and not C["CENTER_SHADOW"]:
                        continue

                    if angle != "angle_4" and not C["SHADOWS"]:
                        continue

                    dir_img = sorted(os.listdir(dir_img_path))

                    x = 0
                    for img in dir_img:
                        c += 1
                        pic = ""
                        img_path = dir_img_path + "/" + img

                        if x == 0 and C["WARM"]:
                            pic = img_path

                        elif x == 1 and C["COLD"]:
                            pic = img_path

                        elif x == 2 and C["LOW"]:
                            pic = img_path

                        elif x == 3 and C["MED"]:
                            pic = img_path

                        elif x == 4 and C["HIGH"]:
                            pic = img_path

                        if pic:
                            img_count += 1
                            add_face(pic, name, C, labels, dir_count, cascade,
                                     faces, people, c)
                        x += 1
        dir_count += 1
    save_train(fr, faces, labels)
    save_labels(people)

    return img_count

data = {
    "skipped":0, # number of pictures skipped
    "reviewed":0, # number of pictures reviewed
}
C = get_settings()

start_time = time.time()

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
cascade = cv2.CascadeClassifier(C["CASCADE"])

img_count = train_data(face_recognizer, cascade, data, C)

finish_time = time.time()
sec = finish_time - start_time


print("finished\t" + str(sec) + " secs\n")
for k, v in C.items():
    print(str(k) + "\t" + str(v))
print("\n")
for k, v in data.items():
    print(str(k) + "\t" + str(v))
print("total_imgs\t" + str(img_count))

extra = data["reviewed"] - img_count
if extra < 0:
    print("extra_faces\t0")
else:
    print("extra_faces\t" + str(extra))

try:
    print("percent_learned\t" + str((data["reviewed"] / data["skipped"]) * 100))
except:
    print("skipped_is_0")

