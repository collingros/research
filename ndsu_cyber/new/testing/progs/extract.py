import os
import subprocess


def run_cmd(cmd):
    print("running:\t{0}".format(cmd))
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    process.wait()


def cp(src, dst):
    cmd = "cp -r {0} {1}".format(src, dst)
    run_cmd(cmd)


def cp_pic(path, new_path):
    cp(path, new_path)


num = 100
names = []
blacklisted = ["pos_3", "pos_4"]
cwd = os.getcwd()
for id in sorted(os.listdir(cwd)):
    if os.path.isfile(id):
        continue

    id_path = "{0}/{1}".format(cwd, id)
    for occ in sorted(os.listdir(id_path)):
        occ_path = "{0}/{1}".format(id_path, occ)
        for pos in sorted(os.listdir(occ_path)):
            pos_path = "{0}/{1}".format(occ_path, pos)
            if pos in blacklisted:
                continue

            for light in sorted(os.listdir(pos_path)):
                light_path = "{0}/{1}".format(pos_path, light)
                for color in sorted(os.listdir(light_path)):
                    '''
                    num += 1

                    if color in names:
                        new_path = "../dump/{0}_{1}".format(color, num)
                        cp(color, new_path)

                        continue

                    names.append(color)
                    '''

                    num += 1
                    new_path = "../dump/{0}_{1}".format(num, color)
                    color_path = "{0}/{1}".format(light_path, color)

                    cp_pic(color_path, new_path)
