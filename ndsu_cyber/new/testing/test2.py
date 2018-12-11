# Collin Gros
# 12/11/18


# arg description
# "s":scale_factor, "n":min_neighbors, "p":resolution_height, "z":cascade_xml,
# "w":warm, "c":cold, "l":low, "m":medium, "b":high,
# "v":vanilla_set, "f":hat_set, "e":glasses_set,
# "x":profile_pictures, "a":angled_pictures, "o":central_pictures,
# "g":shadows, "i":central_lighting


import cv2
import os
import time


settings = {}
data = {}
labels = {}

cascade = None
face_rec = cv2.face_LBPHFaceRecognizer_create()


def read_settings():
# set appropriate settings from argument input
    int_settings = ["n", "p", "w", "c", "l",
                    "m", "b", "v", "f", "e",
                    "x", "a", "o", "g", "i"]
    float_settings = ["s"]
    str_settings = ["z"]

    parser = argparse.ArgumentParser()
    for key in init_settings:
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
        if arg.key:
            settings[key] = args.key


def load_data():
# load training data
    xml = settings["cascade"]
    cascade = cv2.CascadeClassifier(xml)

    trained_path = "./train.yml"
    try:
        face_rec.read(trained_path)
    except:
        print("error: no training data was found\nexiting...\n")
        exit()

    labels_path = "./labels.pickle"
    with open(labels_path, "rb") as info:
        og_labels = pickle.load(info)


def




start = time.time()

read_settings()
load_data()

finish = time.time()
data["time"] = start - finish

write_data()

