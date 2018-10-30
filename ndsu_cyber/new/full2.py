import os
import subprocess


def run_cmd(cmd):
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()


def flop(src, dst):
    cmd = "convert -flop {0} {1}".format(src, dst)
    run_cmd(cmd)


def mk_dir(path):
    cmd = "mkdir {0}".format(path)
    run_cmd(cmd)


def rm_dir(path):
    cmd = "rm -r {0}".format(path)
    run_cmd(cmd)


def reverse_all(path, pos, angle):
    src = ""
    dst = ""

    full_path = "{0}{1}/{2}/".format(path, pos, angle)
    for img in sorted(os.listdir(full_path)):
        src = "{0}{1}/".format(full_path, img)

        if pos == 0:
            dst = "{0}pos_4/".format(path)
        elif pos == 1:
            dst = "{0}pos_3/".format(path)

        if angle == 1:
            dst = "{0}angle_7".format(dst)
        elif angle == 2:
            dst = "{0}angle_6".format(dst)
        elif angle == 3:
            dst = "{0}angle_5".format(dst)

        print("flopping\nsrc: {0}\ndst:{1}".format(src, dst))
        flop(src, dst)


cwd = os.getcwd()
for person in sorted(os.listdir(cwd)):
    if os.path.isfile(person)
        continue

    person_path = "{0}/{1}/".format(cwd, person)

    for base in sorted(os.listdir(person_path)):
        base_path = "{0}{1}/".format(person_path, base)

        for pos in sorted(os.listdir(base_path)):
            pos_path = "{0}{1}/".format(base_path, pos)

            if pos == "pos_2":
                continue
            elif pos == "pos_3" or pos == "pos_4":
                rm_dir(pos_path)
                mk_dir(pos_path)

            for angle in sorted(os.listdir(pos_path)):
                reverse_all(base_path, pos, angle)








                
