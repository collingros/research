# collin gros
# 05/11/2019


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
import numpy as np
import pickle


settings = {}
people = {}
data = {}
faces = []
labels = []

cascade = None
face_rec = None


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

    global cascade
    cascade = cv2.CascadeClassifier(xml)

    global face_rec
    face_rec = cv2.face.LBPHFaceRecognizer_create()

    int_data = ["skipped", "viewed", "total", "time"]
    for key in int_data:
        data[key] = 0


def write_data():
# train, save labels
    train_path = "./train.yml"

    face_rec.train(faces, np.array(labels))
    face_rec.save(train_path)

    labels_path = "./labels.pickle"
    with open(labels_path, "wb") as info:
        pickle.dump(people, info)

    with open("train_stats.txt", "w") as info:
        for key, value in sorted(data.items()):
            str = "{0}:{1}\n".format(key, value)
            info.write(str)


def draw(pic, coords):
# draw box and text over detected face, save to
# ./{id}.JPG
    color = (48, 48, 48)

    x = coords[0]
    y = coords[1]
    w = coords[2]
    h = coords[3]

    cv2.rectangle(pic, (x, y), (x+w, y+h), color, 2)


def add(path, dir_num):
# detect a face, store it
    data["total"] += 1
    str_arr = path.split("/")
    str_arr = str_arr[-1].split(".")
    id = str_arr[0]

    color_pic = cv2.imread(path, 1)
    gray_pic = cv2.imread(path, 0)

    height = int(settings["p"])
    width = int(height * 1.5)

    gray_pic = cv2.resize(gray_pic, (width, height))
    color_pic = cv2.resize(color_pic, (width, height))

    detected = cascade.detectMultiScale(gray_pic, scaleFactor=float(settings["s"]),
                                        minNeighbors=int(settings["n"]))
    if not len(detected):
    # no faces were detected
        data["skipped"] += 1
        return

    for (x, y, w, h) in detected:
        data["viewed"] += 1
        face = gray_pic[y:y+h, x:x+w]

        coords = [x, y, w, h]
        draw(color_pic, coords)

        faces.append(face)
        labels.append(dir_num)

    path = "./{0}.JPG".format(id)
    cv2.imwrite(path, color_pic)


def filter(name, name_type, num=0):
# if we don't want to include the specified media, return 0
    if name_type == "occ":
        if name == "vanilla" and int(settings["v"]):
            return 1
        elif name == "glasses" and int(settings["e"]):
            return 1
        elif name == "hat" and int(settings["f"]):
            return 1
    elif name_type == "pos":
        profile = ["0", "4"]
        angled = ["1", "3"]
        central = ["2"]

        str = name.split("_")
        name = str[-1]

        if name in profile and int(settings["x"]):
            return 1
        elif name in angled and int(settings["a"]):
            return 1
        elif name in central and int(settings["o"]):
            return 1
    elif name_type == "light":
        shadows = ["1", "2", "3", "5", "6", "7"]
        central = ["4"]

        str = name.split("_")
        name = str[-1]

        if name in shadows and int(settings["g"]):
            return 1
        elif name in central and int(settings["i"]):
            return 1
    elif name_type == "color":
        if num == 0 and int(settings["w"]):
            return 1
        elif num == 1 and int(settings["c"]):
            return 1
        elif num == 2 and int(settings["l"]):
            return 1
        elif num == 3 and int(settings["m"]):
            return 1
        elif num == 4 and int(settings["b"]):
            return 1

    print("filter returning 0 for {0}:{1}:{2}".format(name, name_type, num))
    return 0


def train():
# for each filtered image, add to faces arr
    dir_num = 0
    ids = "./pics"
    for id in sorted(os.listdir(ids)):

        people[id] = dir_num
        id_path = ids + "/" + id

        for occ in sorted(os.listdir(id_path)):
            if not filter(occ, "occ"):
                continue

            occ_path = id_path + "/" + occ
            for pos in sorted(os.listdir(occ_path)):
                if not filter(pos, "pos"):
                    continue

                light_path = occ_path + "/" + pos
                for light in sorted(os.listdir(light_path)):
                    if not filter(light, "light"):
                        continue

                    num = 0
                    color_path = light_path + "/" + light

                    for color in sorted(os.listdir(color_path)):
                        if not filter(color, "color", num):
                            num += 1
                            continue

                        pic_path = color_path + "/" + color
                        add(pic_path, dir_num)

                        num += 1
        dir_num += 1


start = time.time()

read_settings()
load_data()

train()

finish = time.time()
data["time"] = round(finish - start, 2)

write_data()

