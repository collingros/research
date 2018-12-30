import os
import subprocess


def cvt_mirror(src):
    cmd = "convert {0} -flop {1}".format(src, dst)
    run_cmd(cmd)


def run_cmd(cmd):
    print("running:\t{0}".format(cmd))
#    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
#    process.wait()


def mirror(path):
    sub = path.split("/")
    idx = sub.index("full")
    sub[idx] = "mirrored"

    new_path = "".join(sub)
    cvt_mirror(path, new_path)


cwd = os.getcwd()
for id in sorted(os.listdir(cwd)):
    if os.path.isfile(id):
        continue

    id_path = "{0}/{1}".format(cwd, id)
    for occ in sorted(os.listdir(id_path)):
        occ_path = "{0}/{1}".format(id_path, occ)
        for pos in sorted(os.listdir(occ_path)):
            pos_path = "{0}/{1}".format(occ_path, pos)
            for light in sorted(os.listdir(pos_path)):
                light_path = "{0}/{1}".format(pos_path, light)
                for color in sorted(os.listdir(light_path)):
                    color_path = "{0}/{1}".format(light_path, color)

                    mirror(color_path)
