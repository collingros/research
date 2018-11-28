# Collin Gros
# 11/19/18

'''
the goal:
    run different testing sets against different training sets

train cold
test cold warm etc etc
'''
import os
import subprocess

class Settings:
    def __init__(self, is_test):
        self.is_test = is_test
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

        self.init_states()

        if is_test:
            self.init_test()
        else:
            self.init_train()


    def init_states(self):
    # set dicts to initial testing/training values
        pass

    def rotate(self, type):
    # 'rotate' a value in testing/training dicts to next value
    # to be tested/trained
        pass


    def build_cmd(self):
        cmd = ""
        if self.is_test:
            cmd += "python3 test.py "
        else:
            cmd += "python3 train.py "

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

        print(cmd)
        return cmd


    def pull_train(self, train_path):
    # "pull" trained data from stockpile, copy it into testing dir
        cwd = os.getcwd()
        cp(train_path, cwd)
                

    def save_train(self):
    # move fresh trained data into testing directory
        cwd = os.getcwd()

        new_dir = "{0}/stockpile/{1}".format(cwd, self.id)
        mkdir(new_dir)

        train_path = cwd + "/" + "train.yml"
        new_path = new_dir + "/train.yml"
        mv(train_path, new_path)

        label_path = cwd + "/" + "labels.pickle"
        new_path = new_dir + "/labels.pickle"
        mv(label_path, new_path)

        mv("*.JPG", new_dir)


    def train(self):
        trained_path = self.get_trained()
        if trained_path != "":
        # if we already trained using these settings
            self.pull_train(trained_path)
            # pull the trained data from our stockpile of trained data
            # and copy it into the testing directory
        else:
        # otherwise, if we didnt train using these settings
            cmd = self.build_cmd()
            # python3 train.py -blah blah blah
            run_cmd(cmd)
            # train using these settings
            self.save_train()
            # and copy it into the testing directory (cwd) (side effect
            # of train.py)

        self.id += 1


    def test(self):
    # ** only works AFTER training data is present (obviously)
        cmd = self.build_cmd()
        # python3 test.py -blah blah blah

        # using the training data in our testing directory,
        # run the test


    def is_copy(self, path):
    # open txt file specified at path, return true if the file represents
    # our current settings, false otherwise
        state = "prog"
        copy = True
        with open(path, "r") as info:
            for line in info:
                line = line.rstrip()

                if state == "prog":
                    # prog settings
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


    def get_trained(self):
    # path of trained data if data was already trained using our settings,
    # otherwise empty str
        trained_path = ""
        cwd = os.getcwd()
        pile_path = cwd + "/stockpile"

        for directory in os.listdir(pile_path):
            dir_path = pile_path + "/" + directory

            info_path = dir_path + "/" + "info.txt"
            if (self.is_copy(info_path)):
                trained_path = dir_path + "/" + "train.yml"

        return trained_path


    def init_test(self):
    # fill settings with default testing values
        self.prog["sf"] = 1.3
        self.prog["mn"] = 10
        self.prog["res"] = 480
        self.prog["c"] = "haar_default.xml"


    def init_train(self):
    # fill settings with default training values
        self.prog["sf"] = 1.01
        self.prog["mn"] = 1
        self.prog["res"] = 480
        self.prog["c"] = "haar_default.xml"


    def rotate(self):
    # if currently cold, do warm, if warm, do low, if low, do med, etc
        self.color["w"] = 0
        self.color["c"] = 1


def touch(name):
# (shell) touch cmd
    cmd = "touch {0}".format(name)
    run_cmd(cmd)


def mkdir(name):
# (shell) mkdir cmd
    cmd = "mkdir {0}".format(name)
    run_cmd(cmd)


def mv(src, dst):
# (shell) mv cmd
    cmd = "mv {0} {1}".format(src, dst)
    run_cmd(cmd)


def cp(src, dst):
# (shell) cp cmd
    cmd = "cp {0} {1}".format(src, dst)
    run_cmd(cmd)


def run_cmd(cmd):
# run a shell cmd
    print(cmd)
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    process.wait()


def init_dirs():
# create testing dir, trained data stockpile dir, results/graphs dir
    pass

train_settings = Settings(False)
train_settings.train()

train_settings.rotate()
train_settings.train()






