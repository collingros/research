import cv2
import os
import csv
import pickle
import numpy as np
import argparse
import time


def init(SETTINGS):
    face_rec = cv2.face.LBPHFaceRecognizer_create()
    cascade = cv2.CascadeClassifier(SETTINGS["CASCADE"])

    try:
        face_rec.read(SETTINGS["TRAIN_DATA"])
    except:
        print("error: \"" + SETTINGS["TRAIN_DATA"] + "\" not found")
        print("\tyou need to run the trainer first!")
        exit()

    return face_rec, cascade


def get_labels():
    with open("labels.pickle", "rb") as f:
        og_labels = pickle.load(f)
    labels = {v:k for k, v in og_labels.items()}

    return labels


def get_settings():
    SETTINGS = {
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
        SETTINGS["SF"] = args.s
    if args.n: # MINIMUM NEIGHBORS
        SETTINGS["MN"] = args.n
    if args.p: # TEST HEIGHT
        SETTINGS["TEST_HEIGHT"] = args.p
    if args.t: # TARGET
        SETTINGS["TARGET"] = args.t
    if args.w: # INCLUDE WARM PICTURES?
        SETTINGS["WARM"] = args.w
    if args.c: # INCLUDE COLD PICTURES?
        SETTINGS["COLD"] = args.c
    if args.l: # INCLUDE LOW PICTURES?
        SETTINGS["LOW"] = args.l
    if args.m: # INCLUDE MED PICTURES?
        SETTINGS["MED"] = args.m
    if args.b: # INCLUDE HIGH PICTURES?
        SETTINGS["HIGH"] = args.b
    if args.e: # INCLUDE GLASSES PICTURES?
        SETTINGS["GLASSES"] = args.e
    if args.f: # INCLUDE HAT PICTURES?
        SETTINGS["HAT"] = args.f
    if args.v: # INCLUDE VANILLA PICTURES?
        SETTINGS["VANILLA"] = args.v
    if args.x: # INCLUDE PROFILES PICTURES?
        SETTINGS["PROFILES"] = args.x
    if args.a: # INCLUDE ANGLED POS PICTURES?
        SETTINGS["ANGLED"] = args.a
    if args.o: # INCLUDE CENTER POS PICTURES?
        SETTINGS["CENTER"] = args.o
    if args.g: # INCLUDE SHADOWS LIGHTING ANGLES?
        SETTINGS["SHADOWS"] = args.g
    if args.i: # INCLUDE CENTER LIGHTING ANGLES?
        SETTINGS["CENTER_SHADOW"] = args.i
    if args.j: # INCLUDE CENTER LIGHTING ANGLES?
        SETTINGS["BEARDS"] = args.j
    #if args.z: # DATA FILE
    #    SETTINGS["DATA"] = args.z
    # ASSUMING THAT THE DATAFILE IS IN "./train.yml"
    SETTINGS["TRAIN_DATA"] = "train.yml"
    # ASSUMING THAT THE PICTURES TO BE TESTED ARE IN "./test"
    SETTINGS["TEST_DIR"] = "test"
    SETTINGS["RATIO"] = 1.5
    if args.z:
        SETTINGS["CASCADE"] = args.z
    if args.d: # CONFIDENCE CUTOFF THRESHOLD
        SETTINGS["CONF_CUTOFF"] = args.d
    if args.k:
        SETTINGS["OUT"] = args.k

    return SETTINGS

def save_face(x, y, w, h, pic, name, c, pic_path, SETTINGS):
    font = cv2.FONT_HERSHEY_SIMPLEX
    color = (255, 0, 0)
    stroke = 2

    cv2.rectangle(pic, (x, y), (x + w, y + h), (255, 0, 0), stroke)
    cv2.putText(pic, name, (x, y - 10), font,
                1, (0, 0, 255), stroke, cv2.LINE_AA)

    pic = cv2.resize(pic, (int(300 * SETTINGS["RATIO"]), 300))

    string = os.getcwd() + "/" + SETTINGS["OUT"] + "/" + name + str(c) + ".JPG"
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

def guess(pic_path, name, SETTINGS, labels, dir_count, face_rec, cascade, faces,
          people, c):
    pic = cv2.imread(pic_path, 0)

    pic = cv2.resize(pic, (int(SETTINGS["TEST_HEIGHT"] * SETTINGS["RATIO"]),
                     SETTINGS["TEST_HEIGHT"]))

    detected_faces = cascade.detectMultiScale(pic, scaleFactor=SETTINGS["SF"],
						                           minNeighbors=SETTINGS["MN"]);
    if not len(detected_faces):
        data["skipped"] += 1

    # might want to delete for and
    # (x, y, w, h) = face[0]

    #TODO: add a size restriction. clean up. <CDG>

    else:
        for (x, y, w, h) in detected_faces:
            data["reviewed"] += 1
            #show_face(x, y, w, h, pic, name)

            #save_face(x, y, w, h, pic, name, c, pic_path, SETTINGS)

            face = pic[y:y+h, x:x+w]
            label, conf = face_rec.predict(face)
            guess = labels[label]

            if name == guess:
                data["c_names"] += 1
            else:
                data["w_names"] += 1


def train_data(face_rec, cascade, data, SETTINGS):
    people = {}
    labels = get_labels()
    dir_count = 0
    total_imgs = 0 # imgs found, including those that are ignored from
                   # custom user input filters
    img_count = 0

    dir_test = sorted(os.listdir(SETTINGS["TEST_DIR"]))
    for pic_owner in dir_test:
        name = pic_owner
        pic_owner_path = SETTINGS["TEST_DIR"] + "/" + pic_owner

        if pic_owner == "1" or pic_owner == "2" and not SETTINGS["BEARDS"]:
            continue

        people[pic_owner] = dir_count
        pics = sorted(os.listdir(pic_owner_path))
        for pic_type in pics:
            dir_pos_path = pic_owner_path + "/" + pic_type

            if pic_type == "glasses" and not SETTINGS["GLASSES"]:
                continue
            if pic_type == "hat" and not SETTINGS["HAT"]:
                continue
            if pic_type == "vanilla" and not SETTINGS["VANILLA"]:
                continue

            dir_pos = sorted(os.listdir(dir_pos_path))
            for pos in dir_pos:
                dir_angle_path = dir_pos_path + "/" + pos

                if (pos == "pos_0" or pos == "pos_4") and not 
                    SETTINGS["PROFILES"]:
                    continue
                if (pos == "pos_1" or pos == "pos_3") and not
                    SETTINGS["ANGLED"]:
                    continue
                if pos == "pos_2" and not SETTINGS["CENTER"]:
                    continue

                dir_angle = sorted(os.listdir(dir_angle_path))
                for angle in dir_angle:
                    dir_img_path = dir_angle_path + "/" + angle

                    if angle == "angle_4" and not SETTINGS["CENTER_SHADOW"]:
                        continue
                    if angle != "angle_4" and not SETTINGS["SHADOWS"]:
                        continue

                    dir_img = sorted(os.listdir(dir_img_path))
                    img_num = 0
                    for img in dir_img:
                        total_imgs += 1
                        pic = ""
                        img_path = dir_img_path + "/" + img

                        if img_num == 0 and SETTINGS["WARM"]:
                            pic = img_path
                        elif img_num == 1 and SETTINGS["COLD"]:
                            pic = img_path
                        elif img_num == 2 and SETTINGS["LOW"]:
                            pic = img_path
                        elif img_num == 3 and SETTINGS["MED"]:
                            pic = img_path
                        elif img_num == 4 and SETTINGS["HIGH"]:
                            pic = img_path

                        if pic:
                            img_count += 1
                            guess(pic, name, SETTINGS, labels, dir_count, face_rec,
                                  cascade, people, c)
                        img_num += 1
        dir_count += 1

    return img_count

data = {
    "skipped":0, # number of pictures skipped
    "reviewed":0, # number of pictures reviewed
    "c_names":0, # number of correctly guessed images
    "w_names":0, # number of wrongly guessed images
}
SETTINGS = get_settings()

start_time = time.time()

face_rec, cascade = init()

img_count = train_data(face_rec, cascade, data, SETTINGS)

finish_time = time.time()
sec = finish_time - start_time


print("finished\t" + str(sec) + " secs\n")
for k, v in sorted(SETTINGS.items()):
    print(str(k) + "\t" + str(v))
print("\n")
for k, v in sorted(data.items()):
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

