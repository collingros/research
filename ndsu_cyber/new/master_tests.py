import os
import subprocess


# train w, test w
# train c, test w
# train l, test w
# ..
# train w, test c
# ..
# train w, test l
# ..
# train w, test h
# ..
# train w + c, test w - h
# train l + m + h, test w - h

def train(settings):
    pass


def test(settings):
    pass


settings = {
    "tr_sf":1.01,
    "tr_mn":1,
    "tr_test_height":480,
    "tr_cascade":"haar_default.xml",
    "tr_color":[],
    # w, c, l, m, b
    "tr_props":[],
    # v, g, h
    "tr_pos":[],
    # x, a, o
    "tr_shadows":[],
    # g, i
    "tr_out_dir":"/home/reu3/git/research/ndsu_cyber/new/out_tr_final",
    "tr_z":,

    "ts_sf":1.3,
    "ts_mn":10,
    "ts_test_height":480,
    "ts_cascade":"haar_default.xml",
    "ts_out_dir":"/home/reu3/git/research/ndsu_cyber/new/out_ts_final",
}



train(settings)
test(settings)


































