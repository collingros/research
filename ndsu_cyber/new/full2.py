import os
import subprocess


def run_cmd(cmd):
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()


def flop(src, dst):
    cmd = "convert -flop {0} tmp.JPG".format(src)
    run_cmd(cmd)

    move("tmp.JPG", dst)


def move(src, dst):
    cmd = "mv {0} {1}".format(src, dst)
    run_cmd(cmd)


def mk_dir(path):
    cmd = "mkdir {0}".format(path)
    run_cmd(cmd)


def rm_dir(path):
    cmd = "rm -r {0}".format(path)
    run_cmd(cmd)


def refresh(path):
    rm_dir(path)
    mk_dir(path)

    angles = ["angle_1", "angle_2", "angle_3", "angle_4", "angle_5",
              "angle_6", "angle_7"]
    for angle in angles:
        angle_path = "{0}{1}/".format(path, angle)

        mk_dir(angle)


def reverse_all(path, pos, angle):
    src = ""
    dst = ""

    full_path = "{0}{1}/{2}/".format(path, pos, angle)
    for img in sorted(os.listdir(full_path)):
        src = "{0}{1}".format(full_path, img)

        if pos == "pos_0":
            dst = "{0}pos_4/".format(path)
        elif pos == "pos_1":
            dst = "{0}pos_3/".format(path)

        if angle == "angle_1":
            dst = "{0}angle_7/{1}".format(dst, img)

        elif angle == "angle_2":
            dst = "{0}angle_6/{1}".format(dst, img)

        elif angle == "angle_3":
            dst = "{0}angle_5/{1}".format(dst, img)

        elif angle == "angle_4":
            continue

        elif angle == "angle_5":
            dst = "{0}angle_3/{1}".format(dst, img)

        elif angle == "angle_6":
            dst = "{0}angle_2/{1}".format(dst, img)

        elif angle == "angle_7":
            dst = "{0}angle_1/{1}".format(dst, img)

        print("flopping\nsrc: {0}\ndst: {1}".format(src, dst))
        flop(src, dst)


cwd = os.getcwd()
for person in sorted(os.listdir(cwd)):
    if os.path.isfile(person):
        continue

    person_path = "{0}/{1}/".format(cwd, person)

    for base in sorted(os.listdir(person_path)):
        base_path = "{0}{1}/".format(person_path, base)

        for pos in sorted(os.listdir(base_path), reverse=True):
            pos_path = "{0}{1}/".format(base_path, pos)

            if pos == "pos_2":
                continue
            elif pos == "pos_3" or pos == "pos_4":
                refresh(pos_path)

            for angle in sorted(os.listdir(pos_path)):
                reverse_all(base_path, pos, angle)








                
