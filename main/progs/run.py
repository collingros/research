# collin gros
# 05/11/2019
from bash import bash
import os


bash = bash.Run()
class Test:
    def __init__(self, train):
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
            self.prog["sf"] = 1.3
            self.prog["mn"] = 5
            self.prog["res"] = 480
            self.prog["c"] = "haar_default.xml"
        else:
            self.prog["sf"] = 1.3
            self.prog["mn"] = 5
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

        print("\t" + cmd)
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
                bash.mkdir(dir_path)

                train = self.build_cmd()
                bash.run(train)
                self.write_info()

                pic_name = "/*.JPG"
                bash.mv("." + pic_name, dir_path + "/")

                stat_name = "/train_stats.txt"
                bash.mv("." + stat_name, dir_path + stat_name)

                train_name = "/train.yml"
                bash.mv("." + train_name, dir_path + train_name)

                labels_name = "/labels.pickle"
                bash.mv("." + labels_name, dir_path + labels_name)

                train_info = "/train_info.txt"
                bash.mv("." + train_info, dir_path + train_info)

                self.id += 1

            train_path = dir_path + "/train.yml"
            bash.cp(train_path, ".")

            labels_path = dir_path + "/labels.pickle"
            bash.cp(labels_path, ".")

            return dir_path

        else:
            test_dir = "{0}/{1}".format(dir_path, self.id)
            bash.mkdir(test_dir)

            train_path = "{0}/{1}".format(dir_path, "train.yml")
            labels_path = "{0}/{1}".format(dir_path, "labels.pickle")
            bash.cp(train_path, ".")
            bash.cp(labels_path, ".")

            test = self.build_cmd()
            bash.run(test)
            self.write_info()

            stat_name = "/test_stats.txt"
            bash.mv("." + stat_name, test_dir + stat_name)

            pic_name = "/*.JPG"
            bash.mv("." + pic_name, test_dir + "/")

            test_info = "/test_info.txt"
            bash.mv("." + test_info, test_dir + test_info)

            bash.rm("./train.yml")
            bash.rm("./labels.pickle")

            self.id += 1


# potential data loss
bash.rm("./stockpile")
bash.mkdir("./stockpile")
bash.rm("./tests")
bash.mkdir("./tests")
bash.rm("*.JPG train.yml labels.pickle")

test_obj = Test(False)
train_obj = Test(True)

# ./tests/color
# train on cold and warm, test on warm cold low medium high,
# train on low, medium, high, test on warm cold low medium high,
print("color tests")

train_obj.set_default()
train_obj.set_occ(["v", "h", "g"])
train_obj.set_pos(["c", "p", "a"])
train_obj.set_light(["c", "s"])

test_obj.set_default()
test_obj.set_occ(["v", "h", "g"])
test_obj.set_pos(["c", "p", "a"])
test_obj.set_light(["c", "s"])

colors = [["w", "c"], ["l", "m", "h"], ["w"], ["c"], ["l"], ["m"], ["h"]]
for color_1 in colors:
    train_obj.set_color(color_1)
    dir_path = train_obj.run()
    for color_2 in colors:
        test_obj.set_color(color_2)
        test_obj.run(dir_path)

bash.mv("./stockpile", "./tests/color")
bash.mkdir("./stockpile")

# ./tests/occ
# train on vanilla, test on hat glasses
# train on hat, test on vanilla glasses
# train on glasses, test on vanilla hat
print("occ tests")

train_obj.set_default()
train_obj.set_color(["w", "c", "l", "m", "h"])
train_obj.set_pos(["c", "p", "a"])
train_obj.set_light(["c", "s"])

test_obj.set_default()
test_obj.set_color(["w", "c", "l", "m", "h"])
test_obj.set_pos(["c", "p", "a"])
test_obj.set_light(["c", "s"])

occs = [["v", "h", "g"], ["v", "h"], ["v", "g"], ["h", "g"],
        ["v"], ["h"], ["g"]]
for occ_1 in occs:
    train_obj.set_occ(occ_1)
    dir_path = train_obj.run()
    for occ_2 in occs:
        test_obj.set_occ(occ_2)
        test_obj.run(dir_path)

bash.mv("./stockpile", "./tests/occ")
bash.mkdir("./stockpile")

# ./tests/pos
# train on each position combination, test on each position
print("pos tests")

train_obj.set_default()
train_obj.set_color(["w", "c", "l", "m", "h"])
train_obj.set_occ(["v", "h", "g"])
train_obj.set_light(["c", "s"])

test_obj.set_default()
test_obj.set_color(["w", "c", "l", "m", "h"])
test_obj.set_light(["c", "s"])

positions = [["c", "p", "a"], ["c", "a"], ["c"], ["p"], ["a"]]
for pos_1 in positions:
    train_obj.set_pos(pos_1)
    dir_path = train_obj.run()
    for pos_2 in positions:
        test_obj.set_pos(pos_2)
        test_obj.run(dir_path)

bash.mv("./stockpile", "./tests/pos")
bash.mkdir("./stockpile")

# ./tests/light
# train on each lighting, test on each lighting
print("light tests")

train_obj.set_default()
train_obj.set_color(["w", "c", "l", "m", "h"])
train_obj.set_occ(["v", "h", "g"])
train_obj.set_pos(["c", "p", "a"])

test_obj.set_default()
test_obj.set_color(["w", "c", "l", "m", "h"])
test_obj.set_occ(["v", "h", "g"])
test_obj.set_pos(["c", "p", "a"])

lights = [["c"], ["s"], ["c", "s"]]
for light_1 in lights:
    train_obj.set_light(light_1)
    dir_path = train_obj.run()
    for light_2 in lights:
        test_obj.set_light(light_2)
        test_obj.run(dir_path)

bash.mv("./stockpile", "./tests/light")
bash.mkdir("./stockpile")

