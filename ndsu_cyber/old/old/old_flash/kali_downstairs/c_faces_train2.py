import cv2
import os
import pickle
import numpy as np
import argparse
TRAIN_SF = 1.1
TRAIN_MN = 5
TRAIN_DIR = "../database/usable"
SAVED_DIR = ""

CASCADE = "cascades/data/haarcascade_frontalface_default.xml"
HEIGHT = 1000
RATIO = 1.5
# category restriction
GLASSES = 0
HAT = 0
VANILLA = 0
# image restrictions
WARM = 0
COLD = 0
LOW = 0
MED = 0
HIGH = 0
# lighting angle
# 1 to exclude central light, 0 to exclude anything but central, 2 to include
# everything
SHADOWS = 0
# person position
PROFILES = 0
ANGLED = 0
CENTER = 0

parser = argparse.ArgumentParser(description="train the f.r. algorithm")
parser.add_argument("-s", help="training scale factor", type=float)
parser.add_argument("-n", help="training min neighbors", type=int)
parser.add_argument("-l", help="height to resize images to", type=int)
parser.add_argument("-e", help="include glasses pictures", type=int)
parser.add_argument("-f", help="include hat pictures", type=int)
parser.add_argument("-v", help="include vanilla pictures", type=int)
parser.add_argument("-w", help="include warm pictures", type=int)
parser.add_argument("-c", help="include cool pictures", type=int)
parser.add_argument("-d", help="include dim light", type=int)
parser.add_argument("-m", help="include medium light", type=int)
parser.add_argument("-b", help="include bright light", type=int)
parser.add_argument("-q", help="0: exclude anything but central lighting" +
                               "\n1: exclude central lighting" +
                               "\n2: include every type of lighting", type=int)
parser.add_argument("-p", help="include profile positions", type=int)
parser.add_argument("-a", help="include angled positions", type=int)
parser.add_argument("-t", help="include central positions", type=int)
parser.add_argument("-r", help="directory to save to", type=str)
args = parser.parse_args()

if args.s:
    TRAIN_SF = args.s
if args.n:
    TRAIN_MN = args.n
if args.l:
    HEIGHT = args.l
if args.e:
    GLASSES = args.e
if args.f:
    HAT = args.f
if args.v:
    VANILLA = args.v
if args.w:
    WARM = args.w
if args.c:
    COLD = args.c
if args.d:
    LOW = args.d
if args.m:
    MED = args.m
if args.b:
    HIGH = args.b
if args.q:
    SHADOWS = args.q
if args.p:
    PROFILES = args.p
if args.a:
    ANGLED = args.a
if args.t:
    CENTER = args.t
if args.r:
    SAVED_DIR = args.r

dir_train = sorted(os.listdir(TRAIN_DIR))

faces = []
labels = []
p = {}

face_recognizer = cv2.face.LBPHFaceRecognizer_create()

dir_c = 0
img_c = 0
skipped = 0
for dir_name in dir_train:
    label = dir_c
    p[dir_name] = dir_c

   # p_path = TRAIN_DIR + "/" + dir_name
   # p_img_names = os.listdir(p_path)

    p_types = TRAIN_DIR + "/" + dir_name #picture type directories, vanilla etc.
    p_type_names = sorted(os.listdir(p_types))

    for p_type in p_type_names:
        #img_c = 0
        p_type_path = p_types + "/" + p_type

        if p_type == "glasses" and not GLASSES:
            #print("unwanted glasses! (glasses are off)")
            continue
        if p_type == "hat" and not HAT:
            #print("unwanted hat! (hats are off)")
            continue
        if p_type == "vanilla" and not VANILLA:
            #print("unwanted vanilla faces! (vanilla is off)")
            continue

        pos_types = p_type_path
        pos_type_names = sorted(os.listdir(pos_types))

        for pos_type in pos_type_names:

            pos_type_path = pos_types + "/" + pos_type

            if (pos_type == "pos_0" or pos_type == "pos_4") and not PROFILES:
                #print("unwanted profile view! (profiles are off)")
                continue
            if (pos_type == "pos_1" or pos_type == "pos_3") and not ANGLED:
                #print("unwanted angled view! (angles are off)")
                continue
            if pos_type == "pos_2" and not CENTER:
                #print("unwanted central view! (central view is off)")
                continue

            angle_types = pos_type_path
            angle_type_names = sorted(os.listdir(angle_types))

            for angle_type in angle_type_names:
                angle_type_path = angle_types + "/" + angle_type
                if angle_type == "angle_4" and SHADOWS == 1:
                    #print("unwanted central angle! (shadows are on)")
                    continue
                if angle_type != "angle_4" and SHADOWS == 0:
                    #print("unwanted shadow angle! (shadows are off)")
                    continue
                    

                imgs = angle_type_path
                img_names = sorted(os.listdir(imgs))
                img_num = 0 # images are in order by color and brightness
                for img_name in img_names:
                    img_path = imgs + "/" + img_name



                    if img_num == 0 and not WARM:
                        #print("unwanted warm image! (warmth is off)")
                        img_num += 1
                        continue
                    if img_num == 1 and not COLD:
                        #print("unwanted cold image! (cold is off)")
                        img_num += 1
                        continue
                    if img_num == 2 and not LOW:
                        #print("unwanted dim image! (low is off)")
                        img_num += 1
                        continue
                    if img_num == 3 and not MED:
                        #print("unwanted medium-bright image! (med is off)")
                        img_num += 1
                        continue
                    if img_num == 4 and not HIGH:
                        #print("unwanted bright image! (high is off)")
                        img_num += 1
                        continue
                    #print("img path: " + img_path)
                    #print("listdir key: " + str(img_num))
                    img = cv2.imread(img_path)

                    h, w = img.shape[:2]
                    img = cv2.resize(img, (int(RATIO * HEIGHT), HEIGHT))


                    img_num += 1 # DO THINGS FOR IMAGES BASED ON ORDER BEFORE THIS!!!
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    face_cascade = cv2.CascadeClassifier(CASCADE)
                    face = face_cascade.detectMultiScale(gray, scaleFactor = TRAIN_SF,
                                                         minNeighbors = TRAIN_MN);

                    if not len(face):
                        #print("could not detect face from: " + img_name + "\tskipping...")
                        skipped += 1
                        continue
                    #print("img processed: " + img_name)

                    (x, y, w, h) = face[0]

                    rect = gray[y:y + h, x:x + w]
                    faces.append(rect)
                    labels.append(label)

                    cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 0, 0), 2)

                   # cv2.imshow("frame", gray)
                   # cv2.waitKey(0)

                    img_c += 1

                  #  cv2.destroyAllWindows()
    dir_c += 1

if SAVED_DIR == "":
    with open("labels_v2.pickle", "wb") as f:
        pickle.dump(p, f)
else:
    with open(SAVED_DIR + "/" + "labels_v2.pickle", "wb") as f:
        pickle.dump(p, f)

face_recognizer.train(faces, np.array(labels))
if SAVED_DIR == "":
    face_recognizer.save("trained_data.yml")
else:
    face_recognizer.save(SAVED_DIR + "/" + "trained_data.yml")

#print("number of images scanned: " + str(img_c))
#print("number of images skipped: " + str(skipped))
#print("number of directories scanned: " + str(dir_c))

if SAVED_DIR == "":
    with open("stat_train.txt", "w") as f:
        f.write("TRAIN_SF: " + str(TRAIN_SF) + "\n")
        f.write("TRAIN_MN: " + str(TRAIN_MN) + "\n")
        f.write("HEIGHT: " + str(HEIGHT) + "\n")
        f.write("RATIO: " + str(RATIO) + "\n")
        f.write("GLASSES: " + str(GLASSES) + "\n")
        f.write("HAT: " + str(HAT) + "\n")
        f.write("VANILLA: " + str(VANILLA) + "\n")
        f.write("WARM: " + str(WARM) + "\n")
        f.write("COLD: " + str(COLD) + "\n")
        f.write("LOW: " + str(LOW) + "\n")
        f.write("MED: " + str(MED) + "\n")
        f.write("HIGH: " + str(HIGH) + "\n")
        f.write("SHADOWS: " + str(SHADOWS) + "\n")
        f.write("PROFILES: " + str(PROFILES) + "\n")
        f.write("ANGLED: " + str(ANGLED) + "\n")
        f.write("CENTER: " + str(CENTER) + "\n\n")
else:
    with open(SAVED_DIR + "/" + "stat_train.txt", "w") as f:
        f.write("TRAIN_SF: " + str(TRAIN_SF) + "\n")
        f.write("TRAIN_MN: " + str(TRAIN_MN) + "\n")
        f.write("HEIGHT: " + str(HEIGHT) + "\n")
        f.write("RATIO: " + str(RATIO) + "\n")
        f.write("GLASSES: " + str(GLASSES) + "\n")
        f.write("HAT: " + str(HAT) + "\n")
        f.write("VANILLA: " + str(VANILLA) + "\n")
        f.write("WARM: " + str(WARM) + "\n")
        f.write("COLD: " + str(COLD) + "\n")
        f.write("LOW: " + str(LOW) + "\n")
        f.write("MED: " + str(MED) + "\n")
        f.write("HIGH: " + str(HIGH) + "\n")
        f.write("SHADOWS: " + str(SHADOWS) + "\n")
        f.write("PROFILES: " + str(PROFILES) + "\n")
        f.write("ANGLED: " + str(ANGLED) + "\n")
        f.write("CENTER: " + str(CENTER) + "\n\n")
