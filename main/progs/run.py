# collin gros
# 05/11/2019
from bash import bash
import os


class Test:
    def __init__(self, train):
        self.bash = bash.Run()
        self.train = train
        self.prog = {
        # scale factor, minimum neighbors, resolution height, cascade file
            "sf":0,
            "mn":0,
            "res":0,
            "c":""
        }
        self.color = {
        # include warm, cold, low, medium, or high images
            "w":0,
            "c":0,
            "l":0,
            "m":0,
            "h":0
        }
        self.occ = {
        # include vanilla, hat, or glasses occlusion sets
            "v":0,
            "h":0,
            "g":0
        }
        self.pos = {
        # include profiles, angled, or central positions
            "p":0,
            "a":0,
            "c":0
        }
        self.light = {
        # include angled lighting, or central lighting positions
            "s":0,
            "c":0
        }
        self.id = 0


    def reset_dict(self, my_dict):
        for key, value in my_dict.items():
            my_dict[key] = 0


    def set_color(self, colors):
        self.reset_dict(self.color)
        for key, value in self.color.items():
            for color in colors:
                if key == color:
                    self.color[key] = 1


    def set_occ(self, occs):
    # pass custom occs dict to alter Test.occ
        self.reset_dict(self.occ)
        for key, value in self.occ.items():
            for occ in occs:
                if key == occ:
                    self.occ[key] = 1


    def set_pos(self, pos_l):
        self.reset_dict(self.pos)
        for key, value in self.pos.items():
            for pos in pos_l:
                if key == pos:
                    self.pos[key] = 1


    def set_light(self, lights):
        self.reset_dict(self.light)
        for key, value in self.light.items():
            for light in lights:
                if key == light:
                    self.light[key] = 1


    def set_default(self):
        if self.train:
            self.prog["sf"] = 1.05
            self.prog["mn"] = 3
            self.prog["res"] = 300
            self.prog["c"] = "haar_default.xml"
        else:
            self.prog["sf"] = 1.3
            self.prog["mn"] = 10
            self.prog["res"] = 480
            self.prog["c"] = "haar_default.xml"


    def build_cmd(self):
        cmd = ""
        if self.train:
            cmd = "python3 ./train.py"
        else:
            cmd = "python3 ./test.py"

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


    def write_info(self):
        state = "prog"

        name = ""
        if self.train:
            name = "train_info.txt"
        else:
            name = "test_info.txt"

        with open(name, "w") as info:
            info.write(state + "\n")
            for key, value in self.prog.items():
                write_str = "{0}:{1}\n".format(key, value)
                info.write(write_str)

            state = "color"
            info.write(state + "\n")
            for key, value in self.color.items():
                write_str = "{0}:{1}\n".format(key, value)
                info.write(write_str)

            state = "occ"
            info.write(state + "\n")
            for key, value in self.occ.items():
                write_str = "{0}:{1}\n".format(key, value)
                info.write(write_str)

            state = "pos"
            info.write(state + "\n")
            for key, value in self.pos.items():
                write_str = "{0}:{1}\n".format(key, value)
                info.write(write_str)

            state = "light"
            info.write(state + "\n")
            for key, value in self.light.items():
                write_str = "{0}:{1}\n".format(key, value)
                info.write(write_str)


    def is_copy(self, path):
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
    # to avoid running training data using same settings again when
    # a copy has already ran and already exists
        stockpile = "./stockpile"
        for id_dir in os.listdir(stockpile):
            id_dir_path = stockpile + "/" + id_dir
            for item in os.listdir(id_dir_path):
                if item == "train_info.txt":
                    item_path = ("./stockpile/{0}/{1}"
                                 "".format(id_dir, item))
                    if self.is_copy(item_path):
                        dir_path = "./stockpile/{0}".format(id_dir)

                        return dir_path
        return ""


    def run(self, dir_path=""):
        if self.train:
            dir_path = self.get_copy()
            if dir_path == "":
                dir_path = "./stockpile/{0}".format(self.id)
                self.bash.mkdir(dir_path)

                train = self.build_cmd()
                self.bash.run(train)
                self.write_info()

                pic_name = "/*.JPG"
                self.bash.mv("." + pic_name, dir_path + "/")

                stat_name = "/train_stats.txt"
                self.bash.mv("." + stat_name, dir_path + stat_name)

                train_name = "/train.yml"
                self.bash.mv("." + train_name, dir_path + train_name)

                labels_name = "/labels.pickle"
                self.bash.mv("." + labels_name, dir_path + labels_name)

                train_info = "/train_info.txt"
                self.bash.mv("." + train_info, dir_path + train_info)

                self.id += 1

            train_path = dir_path + "/train.yml"
            self.bash.cp(train_path, ".")

            labels_path = dir_path + "/labels.pickle"
            self.bash.cp(labels_path, ".")

            return dir_path
        else:
            test_dir = "{0}/{1}".format(dir_path, self.id)
            self.bash.mkdir(test_dir)

            test = self.build_cmd(test_dir)
            self.bash.run(test)
            self.write_info()

            stat_name = "/test_stats.txt"
            self.bash.mv("." + stat_name, test_dir + stat_name)

            pic_name = "/*.JPG"
            self.bash.mv("." + pic_name, test_dir + "/")

            test_info = "/test_info.txt"
            self.bash.mv("." + test_info, test_dir + test_info)

            self.bash.rm("./train.yml")
            self.bash.rm("./labels.pickle")

            self.id += 1




#bash = bash.Run()
#bash.mkdir("hi")


test_obj = Test(False)
train_obj = Test(True)

# OPTIMIZATION
#
# using vanilla, center and angled pos, center lighting, medium color (all)
# first: without any combination of changes
train_obj.set_occ(["v"])
train_obj.set_pos(["c"])
train_obj.set_light(["c"])
train_obj.set_color(["c", "w", "l", "m", "h"])

SF_L = [1.005, 1.01, 1.015, 1.2, 1.25, 1.3, 1.35,
        1.4, 1.45, 1.5]
MN_L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
RES_L = [96, 112, 128, 144, 160, 176, 192,
        208, 224, 240, 256, 272, 288, 304,
        320, 336, 352, 368, 384, 400, 416,
        432, 448, 464, 480, 720, 1920]
# multiples of 16
CASCS = ["lbph_frontal.xml", "haar_default.xml"]

train_obj.set_default()
for sf in SF_L:
    train_obj.prog["sf"] = sf
    train_obj.run()
cmd = "python3 ./mv.py -i sf_only"
train_obj.bash.run(cmd)

train_obj.set_default()
for mn in MN_L:
    train_obj.prog["mn"] = mn
    train_obj.run()
cmd = "python3 ./mv.py -i mn_only"
train_obj.bash.run(cmd)

train_obj.set_default()
for res in RES_L:
    train_obj.prog["res"] = res
    train_obj.run()
cmd = "python3 ./mv.py -i res_only"
train_obj.bash.run(cmd)

train_obj.set_default()
for casc in CASCS:
    train_obj.prog["c"] = casc
    train_obj.run()
cmd = "python3 ./mv.py -i c_only"
train_obj.bash.run(cmd)

num = 0
train_obj.set_default()
for casc in CASCS:
    train_obj.prog["c"] = casc
    for res in RES_L:
        train_obj.prog["res"] = res
        for sf in SF_L:
            train_obj.prog["sf"] = sf
            for mn in MN_L:
                train_obj.prog["mn"] = mn
                train_obj.run()

                cmd = "python3 ./progs/mv.py -i combo_{0}".format(num)
                train_obj.bash.run(cmd)

                num += 1




















