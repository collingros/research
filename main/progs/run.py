# collin gros
# 05/11/2019
from bash import bash


def reset_dict(my_dict):
    for key, value in my_dict.items():
        my_dict[key] = 0


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


    def set_color(self, colors):
        reset_dict(self.color)
        for key, value in self.color.items():
            for color in colors:
                if key == color:
                    self.color[key] = 1


    def set_occ(self, occs):
    # pass custom occs dict to alter Test.occ
        reset_dict(self.occ)
        for key, value in self.occ.items():
            for occ in occs:
                if key == occ:
                    self.occ[key] = 1


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


obj = Test(False)
obj.set_light(["s", "c"])
print(obj.light)
obj.set_light(["s"])
print(obj.light)









