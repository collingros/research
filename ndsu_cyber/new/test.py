# Collin Gros
#
# TODO:
# change data_results.py, to account for different printing,
# move stuff at bottom
#
# figure out how to make a good estimate for a face area
# for each position of each subject
#
# add a show_face function, so that a face with a box around
# it will be shown, but the face will not be saved in a file
#
# change testing script to account for extra settings
# <CG>

# IDEA:
# only use first detected face, no others
# <CG>

import cv2
import os
import csv
import pickle
import numpy as np
import argparse
import time


def dump(data):
    data["cascade"] = None
    data["face_rec"] = None
    data["faces"] = []
    data["labels"] = []
    data["people"] = {}


def print_all(SETTINGS, data):
    for k, v in sorted(SETTINGS.items()):
        print(str(k) + "\t" + str(v))

    print("\n")

    for k, v in sorted(data.items()):
        print(str(k) + "\t" + str(v))


def init(SETTINGS, data):
    cascade = SETTINGS["CASCADE"]
    data["cascade"] = cv2.CascadeClassifier(cascade)

    face_rec = cv2.face.LBPHFaceRecognizer_create()
    data["face_rec"] = face_rec

    out_dir = SETTINGS["OUT"]
    trained_data = out_dir + "/" + SETTINGS["TRAIN_DATA"]
    try:
        face_rec.read(trained_data)
    except:
        print("error: \"" + trained_data + "\" not found")
        print("\tyou need to run the trainer first!")
        exit()


def get_labels(SETTINGS, data):
    filename = SETTINGS["LABELS"]
    out_dir = SETTINGS["OUT"]
    file_path = os.getcwd() + "/" + out_dir + "/" + filename

    with open(file_path, "rb") as f:
        og_labels = pickle.load(f)

    labels = {v:k for k, v in og_labels.items()}
    data["labels"] = labels


def get_settings():
    SETTINGS = {
    "SF":0,
    "MN":0,
    "TEST_HEIGHT":0,
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
    "SHADOWS":0,
    "CENTER_SHADOW":0,
    "BEARDS":0,
    "OUT":"",
    "RESTRICT_SIZE":0,

    # TRAIN_DATA, TEST_DIR, RATIO are not set by the user
    "TRAIN_DATA":"train.yml",
    "TRAIN_DIR":"train",
    "TEST_DIR":"test",
    "RATIO":1.5,
    "LABELS":"labels.pickle"
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
    parser.add_argument("-q", help="enable size restriction (pixels)", type=int)

    args = parser.parse_args()

    if args.s: # SCALE FACTOR
        SETTINGS["SF"] = args.s
    if args.n: # MINIMUM NEIGHBORS
        SETTINGS["MN"] = args.n
    if args.p: # TEST HEIGHT
        SETTINGS["TEST_HEIGHT"] = args.p
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
    if args.z: # CASCADE FILE, HAAR OR LBPH (XML)
        SETTINGS["CASCADE"] = args.z
    if args.d: # CONFIDENCE CUTOFF THRESHOLD
        SETTINGS["CONF_CUTOFF"] = args.d
    if args.k: # DIRECTORY TO SAVE CAPTURED FACES TO
        SETTINGS["OUT"] = args.k
    if args.q: # SIZE RESTRICTION ON DETECTED FACE AREA
               # (GOAL IS TO TRY TO MINIMIZE FALSE POSITIVES)

               # MAKE SURE TO SET RESTRICT_SIZE RELATIVE TO
               # WHAT YOU THINK THE AREA OF A FACE WOULD BE
               # AT 100 x 150 RESOLUTION (e.g., 30)
        SETTINGS["RESTRICT_SIZE"] = args.q

    return SETTINGS


def save_face(SETTINGS, coords, pic, name, id_num, conf, corr):
    ratio = SETTINGS["RATIO"]
    origin_height = SETTINGS["TEST_HEIGHT"]
    origin_width = int(origin_height * SETTINGS["RATIO"])
    resized_height = 300
    resized_width = int(resized_height * ratio)

    x = int(coords[0] * (resized_width / origin_width))
    y = int(coords[1] * (resized_height / origin_height))
    w = int(coords[2] * (resized_width / origin_width))
    h = int(coords[3] * (resized_height / origin_height))
    resized = [x, y, w, h]

    BLUE = (255, 0, 0)
    GREEN = (0, 255, 0)
    PURP = (255, 0, 255)
    RED = (0, 0, 255)
    font = cv2.FONT_HERSHEY_SIMPLEX
    stroke = 2
    line_type = cv2.LINE_AA

    pic = cv2.resize(pic, (int(300 * ratio), 300))

    # for drawing the rectangle around the person's face
    cv2.rectangle(pic, (x, y), (x + w, y + h), BLUE, stroke)

    # for drawing the persons' name on the screen
    draw_color = (255, 255, 255)
    if corr:
        draw_color = GREEN
    else:
        draw_color = RED
    cv2.putText(pic, name, (x, y - 10), font,
                0.5, RED, stroke, line_type)

    # for drawing area value on screen
    cv2.putText(pic, str(w * h), (x, y + h + 10), font,
                0.5, GREEN, stroke, line_type)

    # TESTING ONLY
    # for drawing confidence value on screen
    cv2.putText(pic, str(conf), (x + w, y + h + 10), font,
                0.5, PURP, stroke, line_type)

    out_dir = SETTINGS["OUT"]
    file_path = (os.getcwd() + "/" + out_dir + "/" + name + "_" +
              str(id_num) + ".JPG")
    cv2.imwrite(file_path, pic)

    # FOR SHOWING THE FACE ONLY:
    cv2.imshow("pic", pic)
    cv2.waitKey(50)
    cv2.destroyAllWindows()


def guess(SETTINGS, data, pic_path, name):
    color_pic = cv2.imread(pic_path, 1) # opens in color
    gray_pic = cv2.imread(pic_path, 0) # opens in grayscale

    # BE AWARE THAT THIS MAY GIVE AN UNEVEN ASPECT RATIO (int roundoff)
    ratio = SETTINGS["RATIO"]
    resized_height = SETTINGS["TEST_HEIGHT"]
    resized_width = int(resized_height * ratio)
    color_pic = cv2.resize(color_pic, (resized_width, resized_height))
    gray_pic = cv2.resize(gray_pic, (resized_width, resized_height))

    cascade = data["cascade"]
    detected_faces = cascade.detectMultiScale(gray_pic,
                                              scaleFactor=SETTINGS["SF"],
					                          minNeighbors=SETTINGS["MN"]);
    if not len(detected_faces):
        data["skipped"] += 1

    else:
        data["total_faces"] += 1

        # could potentially just use the first face detected, but nah
        for (x, y, w, h) in detected_faces:
            restrict_area = SETTINGS["RESTRICT_SIZE"]
            if restrict_area > 0:
                # we have to adjust area according to the height ratio
                # adjusted_area = (res_height / ratio_height)^2 * restrict_area
                actual_area = w * h
                adjusted_area = pow((resized_height / 100), 2) * restrict_area

                # for leniency on small variances between detected face
                # measurements and theoretical face measurements
                close_perc = (100 * ((adjusted_area - (abs(adjusted_area -
                             actual_area) / adjusted_area))))
                if close_perc < 80:
                    data["size_skipped"] += 1
                    continue

            data["processed_faces"] += 1

            coords = [x, y, w, h]
            id_num = data["processed_faces"]

            face_rec = data["face_rec"]
            face = gray_pic[y:y+h, x:x+w]
            label, conf = face_rec.predict(face)

            labels = data["labels"]
            guess = labels[label]

            # correct flag
            corr = 0
            if name == guess:
                corr = 1
                data["c_names"][name] = conf
            else:
                data["w_names"][name] = conf

            save_face(SETTINGS, coords, color_pic, name, id_num, conf, corr)


def test_data(SETTINGS, data):
    test_dir = SETTINGS["TEST_DIR"]
    dir_test = sorted(os.listdir(test_dir))
    for pic_owner in dir_test:
        name = pic_owner
        pic_owner_path = test_dir + "/" + pic_owner

        if pic_owner == "1" or pic_owner == "2" and not SETTINGS["BEARDS"]:
            continue

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

                if ((pos == "pos_0" or pos == "pos_4") and not
                    SETTINGS["PROFILES"]):
                    continue
                if ((pos == "pos_1" or pos == "pos_3") and not
                    SETTINGS["ANGLED"]):
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
                        pic_path = ""
                        img_path = dir_img_path + "/" + img

                        if img_num == 0 and SETTINGS["WARM"]:
                            pic_path = img_path
                        elif img_num == 1 and SETTINGS["COLD"]:
                            pic_path = img_path
                        elif img_num == 2 and SETTINGS["LOW"]:
                            pic_path = img_path
                        elif img_num == 3 and SETTINGS["MED"]:
                            pic_path = img_path
                        elif img_num == 4 and SETTINGS["HIGH"]:
                            pic_path = img_path

                        if pic_path:
                            data["reviewed"] += 1
                            guess(SETTINGS, data, pic_path, name)

                        img_num += 1


data = {
    "time":0,
    "skipped":0, # number of pictures where a face wasn't detected
    "reviewed":0, # number of pictures reviewed (filtered images)
    "c_names":{}, # each correctly id'd person and their confidence value
    "w_names":{}, # each wrongly id'd person and their confidence value
    "total_faces":0, # total of detected faces (to tell if multiple are detected
                     # in a single image)
    "size_skipped":0, # detected faces skipped due to size restriction
    "processed_faces":0, # number of faces predicted
    "labels":[], # for id'ing each face from training data
    "face_rec":cv2.face_LBPHFaceRecognizer, # for training data using LBPH
    "cascade":cv2.CascadeClassifier # for detecting faces using a classifier
}

start_time = time.time()

SETTINGS = get_settings()

init(SETTINGS, data)
get_labels(SETTINGS, data)

test_data(SETTINGS, data)

finish_time = time.time()
data["time"] = finish_time - start_time

print_all(SETTINGS, data)

