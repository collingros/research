# Collin Gros
# 11/29/18 - 12/04/18(current date)
import os
import subprocess


class Test:
    def __init__(self):
        self.prog = {
        # scale factor, minimum neighbors, resolution height, cascade file
            "sf":0,
            "mn":0,
            "res":0,
            "c":""
        }
        self.color = {
        # include warm, cold, low, medium, or high images
            "w":1,
            "c":0,
            "l":0,
            "m":0,
            "h":0
        }
        self.occ = {
        # include vanilla, hat, or glasses occlusion sets
            "v":1,
            "h":0,
            "g":0
        }
        self.pos = {
        # include profiles, angled, or central positions
            "p":0,
            "a":0,
            "c":1
        }
        self.light = {
        # include angled lighting, or central lighting positions
            "s":0,
            "c":1
        }
        self.id = 0

        self.init_prog()
        # set testing prog values


    def set_pos(self, pos_l):
        reset_dict(self.pos)
        for key, value in self.pos.items():
            for pos in pos_l:
                if key == pos:
                    self.pos[key] = 1


    def set_light(self, lights):
        reset_dict(self.light)
        for key, value in self.light.items():
            for light in lights:
                if key == light:
                    self.light[key] = 1


    def set_occ(self, occs):
        reset_dict(self.occ)
        for key, value in self.occ.items():
            for occ in occs:
                if key == occ:
                    self.occ[key] = 1


    def set_color(self, colors):
        reset_dict(self.color)
        for key, value in self.color.items():
            for color in colors:
                if key == color:
                    self.color[key] = 1


    def init_prog(self):
        self.prog["sf"] = 1.3
        self.prog["mn"] = 10
        self.prog["res"] = 480
        self.prog["c"] = "haar_default.xml"



    def build_cmd(self):
        cmd = "python3 test.py "

        for key, value in self.prog.items():
            if key == "sf":
                cmd += " -s " + str(value)
            elif key == "mn":
                cmd += " -n " + str(value)
            elif key == "res":
                cmd += " -p " + str(value)
            elif key == "c":
                cmd += " -z " + str(value)

        for key, value in self.color.items():
            if key == "w":
                cmd += " -w " + str(value)
            elif key == "c":
                cmd += " -c " + str(value)
            elif key == "l":
                cmd += " -l " + str(value)
            elif key == "m":
                cmd += " -m " + str(value)
            elif key == "h":
                cmd += " -b " + str(value)

        for key, value in self.occ.items():
            if key == "v":
                cmd += " -v " + str(value)
            elif key == "h":
                cmd += " -f " + str(value)
            elif key == "g":
                cmd += " -e " + str(value)

        for key, value in self.pos.items():
            if key == "p":
                cmd += " -x " + str(value)
            elif key == "a":
                cmd += " -a " + str(value)
            elif key == "c":
                cmd += " -o " + str(value)

        for key, value in self.light.items():
            if key == "s":
                cmd += " -g " + str(value)
            elif key == "c":
                cmd += " -i " + str(value)

        return cmd


    def run(self, dir_path):
        test_dir = "{0}/{1}".format(dir_path, self.id)
        mkdir(test_dir)

        test = self.build_cmd()
        run_cmd(test)

        mv("./stats.txt", test_dir + "/stats.txt")
        mv("./test_info.txt", test_dir + "/test_info.txt")

        rm("./train.yml")

        self.id += 1


class Train:
    def __init__(self):
        self.prog = {
        # scale factor, minimum neighbors, resolution height, cascade file
            "sf":0,
            "mn":0,
            "res":0,
            "c":""
        }
        self.color = {
        # include warm, cold, low, medium, or high images
            "w":1,
            "c":0,
            "l":0,
            "m":0,
            "h":0
        }
        self.occ = {
        # include vanilla, hat, or glasses occlusion sets
            "v":1,
            "h":0,
            "g":0
        }
        self.pos = {
        # include profiles, angled, or central positions
            "p":0,
            "a":0,
            "c":1
        }
        self.light = {
        # include angled lighting, or central lighting positions
            "s":0,
            "c":1
        }

        self.id = 0

        self.init_prog()
        # set training prog values


    def set_pos(self, pos_l):
        reset_dict(self.pos)
        for key, value in self.pos.items():
            for pos in pos_l:
                if key == pos:
                    self.pos[key] = 1


    def set_light(self, lights):
        reset_dict(self.light)
        for key, value in self.light.items():
            for light in lights:
                if key == light:
                    self.light[key] = 1


    def set_occ(self, occs):
        reset_dict(self.occ)
        for key, value in self.occ.items():
            for occ in occs:
                if key == occ:
                    self.occ[key] = 1


    def set_color(self, colors):
        reset_dict(self.color)
        for key, value in self.color.items():
            for color in colors:
                if key == color:
                    self.color[key] = 1


    def init_prog(self):
        self.prog["sf"] = 1.01
        self.prog["mn"] = 1
        self.prog["res"] = 480
        self.prog["c"] = "haar_default.xml"


    def build_cmd(self):
        cmd = "python3 train.py "

        for key, value in self.prog.items():
            if key == "sf":
                cmd += " -s " + str(value)
            elif key == "mn":
                cmd += " -n " + str(value)
            elif key == "res":
                cmd += " -p " + str(value)
            elif key == "c":
                cmd += " -z " + str(value)

        for key, value in self.color.items():
            if key == "w":
                cmd += " -w " + str(value)
            elif key == "c":
                cmd += " -c " + str(value)
            elif key == "l":
                cmd += " -l " + str(value)
            elif key == "m":
                cmd += " -m " + str(value)
            elif key == "h":
                cmd += " -b " + str(value)

        for key, value in self.occ.items():
            if key == "v":
                cmd += " -v " + str(value)
            elif key == "h":
                cmd += " -f " + str(value)
            elif key == "g":
                cmd += " -e " + str(value)

        for key, value in self.pos.items():
            if key == "p":
                cmd += " -x " + str(value)
            elif key == "a":
                cmd += " -a " + str(value)
            elif key == "c":
                cmd += " -o " + str(value)

        for key, value in self.light.items():
            if key == "s":
                cmd += " -g " + str(value)
            elif key == "c":
                cmd += " -i " + str(value)

        return cmd


    def is_copy(path):
        state = "prog"
        copy = True
        with open(path, "r") as info:
            for line in info:
                line = line.rstrip()

                if state == "prog":
                    for key, value in self.prog.items():
                        line_sub = line.split(":")
                        if (line_sub[0] == key and
                            line_sub[-1] != str(value)):
                            copy = False
                elif state == "color":
                    for key, value in self.color.items():
                        line_sub = line.split(":")
                        if (line_sub[0] == key and
                            line_sub[-1] != str(value)):
                            copy = False
                elif state == "occ":
                    for key, value in self.occ.items():
                        line_sub = line.split(":")
                        if (line_sub[0] == key and
                            line_sub[-1] != str(value)):
                            copy = False
                elif state == "pos":
                    for key, value in self.pos.items():
                        line_sub = line.split(":")
                        if (line_sub[0] == key and
                            line_sub[-1] != str(value)):
                            copy = False
                elif state == "light":
                    for key, value in self.light.items():
                        line_sub = line.split(":")
                        if (line_sub[0] == key and
                            line_sub[-1] != str(value)):
                            copy = False

                if "color" in line:
                    state = "color"
                elif "occ" in line:
                    state = "occ"
                elif "pos" in line:
                    state = "pos"
                elif "light" in line:
                    state = "light"

        return copy


    def get_copy(self):
        stockpile = "./stockpile"
        for id_dir in os.listdir(stockpile):
            for item in os.listdir(id_dir):
                if item == "train_info.txt":
                    item_path = ("./stockpile/{0}/{1}"
                                 "".format(id_dir, item))
                    if is_copy(item_path):
                        dir_path = "./stockpile/{0}"

                        return dir_path

        return ""


    def run(self):
        dir_path = ""
        dir_path = self.get_copy()
        if dir_path == "":
            dir_path = "./stockpile/{0}".format(self.id)
            mkdir(dir_path)

            train = self.build_cmd()
            run_cmd(train)

            train_name = "/train.yml"
            mv("." + train_name, dir_path + train_name)

            train_info = "/train_info.txt"
            mv("." + train_info, dir_path + train_info)

            self.id += 1

        train_path = dir_path + "/train.yml"
        cp(train_path, ".")

        return dir_path


def reset_dict(my_dict):
    for key, value in my_dict.items():
        my_dict[key] = 0


def rm(path):
    cmd = "rm {0}".format(path)
    run_cmd(cmd)


def cp(src, dst):
    cmd = "cp {0} {1}".format(src, dst)
    run_cmd(cmd)


def mv(src, dst):
    cmd = "mv {0} {1}".format(src, dst)
    run_cmd(cmd)


def mkdir(path):
    cmd = "mkdir {0}".format(path)
    run_cmd(cmd)


def run_cmd(cmd):
    print(cmd)
#    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
#    process.wait()


train_obj = Train()
test_obj = Test()
objs = [train_obj, test_obj]

for obj in objs:
    obj.set_occ(["v"])
    obj.set_pos(["c"])

colors = ["w", "c", "l", "m", "h"]
for te_color in colors:
    test_obj.set_color(list(te_color))
    for tr_color in colors:
        train_obj.set_color(list(tr_color))
        train_obj.run()

    test_obj.run()


