import os
import subprocess


def delete_dir(directory):
    cmd = "rm -r {0}".format(directory)

    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()


def flop(src, dst):
    cmd = "convert -flop {0} {1}".format(src, dst)

    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()


def get_new_pos(pos, angle):
    if pos == 0:
        pos = 4
    elif pos == 1:
        pos = 3

    if angle == 1:
        angle = 7
    elif angle == 2:
        angle = 6
    elif angle == 3:
        angle = 5

    return pos, angle

        


def reverse_imgs(path):
    print("current path: {0}".format(path))

    path_substr = path.split("/")

    angle_str = path_substr[-1]
    pos_str = path_substr[-2]

    pos_path = path.split("angle_")[-1]
    base_path = path.split("pos_")[-1]

    print("path_substr: {0}\tpos_str: {1}".format(path_substr, pos_str))
    angle = int(angle_str[-1])
    pos = int(pos_str[-1])

    if pos == 2:
        print("center position, returning..")
        return
    elif pos == 3 or pos == 4:
        print("pos_3 or pos_4: deleting..")
        delete_dir(pos_path)

    pos, angle = get_new_pos(pos, angle)
    for img in sorted(os.listdir(path)):
        img_path = path + "/" + img
        new_path = "{0}pos_{1}/angle_{2}".format(base_path, pos, angle)

        print("flopping from: {0}\tto: {1}".format(img_path, new_path))
        flop(img_path, new_path)


def navigate(path=os.getcwd()):
    pos = ["pos_0", "pos_1", "pos_3", "pos_4"]

    if os.path.isfile(path):
        print("path is file: {0}".format(path))
        return

    print("path is not file: {0}".format(path))

    os.chdir(path)
    cwd = os.getcwd()
    for item in sorted(os.listdir(cwd)):
        item_path = cwd + "/" + item
        if item in pos:
            print("item \"{0}\" in pos".format(item))
            print("item_path: {0}".format(item_path))

            reverse_imgs(item_path)
            continue

        print("navigate")
        navigate(item)


navigate()







