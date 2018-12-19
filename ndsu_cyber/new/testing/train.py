# Collin Gros
# 12/15/18


# arg description
# "s":scale_factor, "n":min_neighbors, "p":resolution_height, "z":cascade_xml,
# "w":warm, "c":cold, "l":low, "m":medium, "b":high,
# "v":vanilla_set, "f":hat_set, "e":glasses_set,
# "x":profile_pictures, "a":angled_pictures, "o":central_pictures,
# "g":shadows, "i":central_lighting


import cv2
import os
import time
import argparse


settings = {}
people = {}
faces = []
labels = []

cascade = None
face_rec = cv2.face_LBPHFaceRecognizer


def read_settings():
# set appropriate settings from argument input
    int_settings = ["n", "p", "w", "c", "l",
                    "m", "b", "v", "f", "e",
                    "x", "a", "o", "g", "i"]
    float_settings = ["s"]
    str_settings = ["z"]

    parser = argparse.ArgumentParser()
    for key in int_settings:
        settings[key] = 0

        cmd_str = "-{0}".format(key)
        parser.add_argument(cmd_str)

    for key in float_settings:
        settings[key] = 0.0

        cmd_str = "-{0}".format(key)
        parser.add_argument(cmd_str)

    for key in str_settings:
        settings[key] = ""

        cmd_str = "-{0}".format(key)
        parser.add_argument(cmd_str)

    args = parser.parse_args()

    all_settings = int_settings + float_settings + str_settings
    for key in all_settings:
        attr = getattr(args, key)
        if attr:
            settings[key] = attr


def load_data():
# load training data
    xml = settings["z"]
    cascade = cv2.CascadeClassifier(xml)


def write_data():
# train, save labels
    train_path = "./train.yml"
    face_rec.train(faces, np.array(labels))
    face_rec.save(train_path)

    labels_path = "./labels.pickle"
    with open(labels_path, "w") as info:
        pickle.dump(people, info)


def add(path, dir_num):
# guess whose face it is, record results
    gray_pic = cv2.imread(path, 0)

    height = settings["p"]
    width = height * 1.5
    gray_pic = cv2.resize(gray_pic, (width, height))

    detected = cascade.detectMultiScale(gray_pic, scaleFactor=settings["sf"],
                                        minNeighbors=settings["mn"])
    if not len(detected):
    # no faces were detected
        return

    for (x, y, w, h) in detected:
        face = gray_pic[y:y+h, x:x+w]

        faces.append(face)
        labels.append(dir_num)


def filter(name, name_type, num=0):
# if we don't want to include the specified media, return 0
    if name_type == "occ":
        if name == "vanilla" and settings["v"]:
            return 1
        elif name == "glasses" and settings["e"]:
            return 1
        elif name == "hat" and settings["f"]:
            return 1
    elif name_type == "pos":
        profile = ["0", "4"]
        angled = ["1", "3"]
        central = ["2"]

        if name in profile and settings["x"]:
            return 1
        elif name in angled and settings["a"]:
            return 1
        elif name in central and settings["o"]:
            return 1
    elif name_type == "light":
        shadows = ["1", "2", "3", "5", "6", "7"]
        central = ["4"]

        if name in shadows and settings["g"]:
            return 1
        elif name in central and settings["i"]:
            return 1
    elif name_type == "color":
        if num == 0 and settings["w"]:
            return 1
        elif num == 1 and settings["c"]:
            return 1
        elif num == 2 and settings["l"]:
            return 1
        elif num == 3 and settings["m"]:
            return 1
        elif num == 4 and settings["b"]:
            return 1

    return 0


def train():
# for each filtered image, add to faces arr
    dir_num = 0

    ids = "~/database/train"
    for id in os.listdir(ids):

        people[id] = dir_num
        path = ids + "/" + id
        for occ in os.listdir(path):
            if not filter(occ, "occ"):
                continue

            path = path + "/" + occ
            for pos in os.listdir(path):
                if not filter(pos, "pos"):
                    continue

                path = path + "/" + pos
                for light in os.listdir(path):
                    if not filter(light, "light"):
                        continue

                    num = 0
                    path = path + "/" + angle
                    for color in os.listdir(path):
                        if not filter(color, "color", num):
                            continue

                        path = path + "/" + color
                        add(path, dir_num)

                        num += 1
        dir_num += 1


read_settings()
load_data()

train()

write_data()
