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


        def train(self):
            pass


        def test(self):
            pass


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


train_settings = Settings(False)
test_settings = Settings(True)


