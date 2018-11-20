# Collin Gros
# 11/19/18

'''
the goal:
    run different testing sets against different training sets

train cold
test cold warm etc etc
'''

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
        self.trained = []

        self.init_states()


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
                    cmd += "-s " + str(value)
                elif key == "mn":
                    cmd += "-n " + str(value)
                elif key == "res":
                    cmd += "-p " + str(value)
                elif key == "c":
                    cmd += "-z " + str(value)

            for key, value in self.color.items():
                if key == "w":
                    cmd += "-w " + str(value)
                elif key == "c":
                    cmd += "-c " + str(value)
                elif key == "l":
                    cmd += "-l " + str(value)
                elif key == "m":
                    cmd += "-m " + str(value)
                elif key == "h":
                    cmd += "-b " + str(value)

            for key, value in self.occ.items():
                if key == "v":
                    cmd += "-v " + str(value)
                elif key == "h":
                    cmd += "-f " + str(value)
                elif key == "g":
                    cmd += "-e " + str(value)

            for key, value in self.pos.items():
                if key == "p":
                    cmd += "-x " + str(value)
                elif key == "a":
                    cmd += "-a " + str(value)
                elif key == "c":
                    cmd += "-o " + str(value)

            for key, value in self.light.items():
                if key == "s":
                    cmd += "-g " + str(value)
                elif key == "c":
                    cmd += "-i " + str(value)

            return cmd


        def pull_train(self):
        # pull trained data from stockpile, copy it into testing dir
            pass


        def save_train(self):
        # copy fresh trained data into testing directory
            pass


        def train(self):
            cmd = self.build_cmd()
            # python3 train.py -blah blah blah

            if self.already_trained():
            # if we already trained using these settings
                self.pull_train()
                # pull the trained data from our stockpile of trained data
                # and copy it into the testing directory
            else:
            # otherwise, if we didnt train using these settings
                run_cmd(cmd)
                # train using these settings
                self.save_train()
                # and copy it into the testing directory


        def test(self):
        # ** only works AFTER training data is present (obviously)
            cmd = self.build_cmd()
            # python3 test.py -blah blah blah

            # using the training data in our testing directory,
            # run the test


        def already_trained(self):
            return False


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


        if is_test:
            init_test()
        else:
            init_train()


    def rotate(self):
    # if currently cold, do warm, if warm, do low, if low, do med, etc
        pass


def mkdir(name):
# (shell) mkdir cmd
    cmd = "mkdir {0}".format(name)
    run_cmd(cmd)


def mv(src, dst):
# (shell) mv cmd
    cmd = "mv {0} {1}".format(src, dst)
    run_cmd(cmd)


def run_cmd(cmd):
# run a shell cmd
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    process.wait()


def init_dirs():
# create testing dir, trained data stockpile dir, results/graphs dir
    pass

train_settings = Settings(False)
test_settings = Settings(True)

train(train_settings)
test(test_settings)







