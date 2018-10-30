import os
import subprocess


def delete_dir(directory):
    cmd = "rm -r {0}".format(directory)

    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()


def copy_img(src, dst):
    cmd = "cp {0} {1}".format(src, dst)

    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()


def flop(src, dst):
    cmd = "convert -flop {0} {1}".format(src, dst)

    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()


def reverse_imgs(path):
    path_substr = path.split("glasses")
    old_angle = path_substr.split("/")[-1]
    old_pos = path_substr.split("/")[-2]

    for img in sorted(os.listdir(path)):
        img_path = path + "/" + img

        if old_pos == "pos_0":
            flop(img_path, 



def navigate(path=os.getcwd()):
    del_pos = ["pos_3", "pos_4"]
    pos = ["pos_0", "pos_1", "pos_3", "pos_4"]

    if os.path.isfile(path):
        return

    os.chdir(path)
    cwd = os.getcwd()
    for item in sorted(os.listdir(cwd)):
        item_path = cwd + "/" + item
        if item in pos:
            if item in del_pos:
                delete_dir(item_path)

            reverse_imgs(item_path)
            continue

        navigate(item)


navigate()

reverse_imgs()






