import os
import subprocess


def cvt_mirror(src, dst):
    cmd = "convert {0} -flop {1}".format(src, dst)
    run_cmd(cmd)


def run_cmd(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    process.wait()


def cp(src, dst):
    cmd = "cp -r {0} {1}".format(src, dst)
    run_cmd(cmd)


def mirror(path, copy):
    sub = path.split("/")
    idx = sub.index("full")
    sub[idx] = "mirrored"

    new_path = "/".join(sub)

    if copy:
        cp(path, new_path)
    else:
        cvt_mirror(path, new_path)


blacklisted = ["pos_0", "pos_1", "pos_2"]
cwd = os.getcwd()
for id in sorted(os.listdir(cwd)):
    if os.path.isfile(id):
        continue

    id_path = "{0}/{1}".format(cwd, id)
    for occ in sorted(os.listdir(id_path)):
        occ_path = "{0}/{1}".format(id_path, occ)
        for pos in sorted(os.listdir(occ_path)):
            pos_path = "{0}/{1}".format(occ_path, pos)

            copy = False
            if pos in blacklisted:
                copy = True

            for light in sorted(os.listdir(pos_path)):
                light_path = "{0}/{1}".format(pos_path, light)
                for color in sorted(os.listdir(light_path)):
                    color_path = "{0}/{1}".format(light_path, color)

                    mirror(color_path, copy)
