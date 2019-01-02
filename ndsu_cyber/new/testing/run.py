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


    def default_prog(self):
        self.prog["sf"] = 1.3
        self.prog["mn"] = 10
        self.prog["res"] = 480
        self.prog["c"] = "haar_default.xml"


    def build_cmd(self, test_dir):
        cmd = "python3 ./progs/test.py "

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
        with open("test_info.txt", "w") as info:
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


    def run(self, dir_path):
        test_dir = "{0}/{1}".format(dir_path, self.id)
        mkdir(test_dir)

        test = self.build_cmd(test_dir)
        run_cmd(test)
        self.write_info()

        stat_name = "/test_stats.txt"
        mv("." + stat_name, test_dir + stat_name)

        pic_name = "/*.JPG"
        mv("." + pic_name, test_dir + "/")

        test_info = "/test_info.txt"
        mv("." + test_info, test_dir + test_info)

        rm("./train.yml")
        rm("./labels.pickle")

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


    def default_prog(self):
        self.prog["sf"] = 1.05
        self.prog["mn"] = 3
        self.prog["res"] = 300
        self.prog["c"] = "haar_default.xml"


    def build_cmd(self):
        cmd = "python3 ./progs/train.py "

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
        with open("train_info.txt", "w") as info:
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


    def run(self):
        dir_path = ""
        dir_path = self.get_copy()
        if dir_path == "":
            dir_path = "./stockpile/{0}".format(self.id)
            mkdir(dir_path)

            train = self.build_cmd()
            run_cmd(train)
            self.write_info()

            pic_name = "/*.JPG"
            mv("." + pic_name, dir_path + "/")

            stat_name = "/train_stats.txt"
            mv("." + stat_name, dir_path + stat_name)

            train_name = "/train.yml"
            mv("." + train_name, dir_path + train_name)

            labels_name = "/labels.pickle"
            mv("." + labels_name, dir_path + labels_name)

            train_info = "/train_info.txt"
            mv("." + train_info, dir_path + train_info)

            self.id += 1

        train_path = dir_path + "/train.yml"
        cp(train_path, ".")

        labels_path = dir_path + "/labels.pickle"
        cp(labels_path, ".")

        return dir_path


def reset_dict(my_dict):
    for key, value in my_dict.items():
        my_dict[key] = 0


def rm(path):
    cmd = "rm -r {0}".format(path)
    run_cmd(cmd)


def cp(src, dst):
    cmd = "cp -r {0} {1}".format(src, dst)
    run_cmd(cmd)


def mv(src, dst):
    cmd = "mv {0} {1}".format(src, dst)
    run_cmd(cmd)


def mkdir(path):
    cmd = "mkdir {0}".format(path)
    run_cmd(cmd)


def run_cmd(cmd):
    print("running: " + cmd)
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    process.wait()


train_obj = Train()
test_obj = Test()
objs = [train_obj, test_obj]

# OPTIMIZATION
#
# using vanilla, center and angled pos, center lighting, medium color (all)
# first: without any combination of changes
train_obj.set_occ(["v"])
train_obj.set_pos(["c"])
train_obj.set_light(["c"])
train_obj.set_color(["c", "w", "l", "m", "h"])

sf_l = [1.005, 1.01, 1.03, 1.05, 1.07, 1.1, 1.2,
        1.3, 1.4, 1.5]
mn_l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res_l = [96, 112, 128, 144, 160, 176, 192,
        208, 224, 240, 256, 272, 288, 304,
        320, 336, 352, 368, 384, 400, 416,
        432, 448, 464, 480, 720, 1920]
# multiples of 16
cascs = ["lbph_frontal.xml", "haar_default.xml"]

train_obj.default_prog()
for sf in sf_l:
    train_obj.prog["sf"] = sf
    train_obj.run()
run_cmd("python3 ./progs/mv.py -i sf")

train_obj.default_prog()
for mn in mn_l:
    train_obj.prog["mn"] = mn
    train_obj.run()
run_cmd("python3 ./progs/mv.py -i mn")

train_obj.default_prog()
for res in res_l:
    train_obj.prog["res"] = res
    train_obj.run()
run_cmd("python3 ./progs/mv.py -i res")

train_obj.default_prog()
for casc in cascs:
    train_obj.prog["c"] = casc
    train_obj.run()
run_cmd("python3 ./progs/mv.py -i c")

num = 0
train_obj.default_prog()
for sf in sf_l:
    train_obj.prog["sf"] = sf
    for mn in mn_l:
        train_obj.prog["mn"] = mn
        train_obj.run()
    run_cmd("python3 ./progs/mv.py -i mn_sf_{0}".format(num))

    num += 1

'''
# MAIN TESTING
train_obj.default_prog()
test_obj.default_prog()

for obj in objs:
    obj.set_occ(["v"])
    obj.set_pos(["c"])
    obj.set_light(["c", "s"])

print("\nbasic color tests\n")
colors = ["w", "c", "l", "m", "h"]
for te_color in colors:
    dir_path = ""

    test_obj.set_color(list(te_color))
    for tr_color in colors:
        train_obj.set_color(list(tr_color))
        dir_path = train_obj.run()

        test_obj.run(dir_path)

print("\nmixed color tests\n")
tr_colors = [["w", "c"], ["l", "m", "b"]]
te_colors = ["w", "c", "l", "m", "h"]
for te_color in te_colors:
    dir_path = ""
    test_obj.set_color(list(te_color))
    for tr_color_l in tr_colors:
        train_obj.set_color(tr_color_l)
        dir_path = train_obj.run()

        test_obj.run(dir_path)
'''

