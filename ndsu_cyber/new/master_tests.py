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

def call(cmd):
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)

def train(settings):
    cmd = "python3 train.py -s {0} -n {1} -p {2} -w {3} -c {4} -l {5}"
          " -m {6} -b {7} -e {8} -f {9} -v {10} -x {11} -a {12} -o {13}"
          " -z {14} -g {15} -i {16} -j {17} -k {18}"
          "".format(s, n, p, w, c, l, m, b, e, f, v, x,
                    a, o, z, g, i, j, k)

    for key, value in settings.items():
        key_substr = key.split("_")
        key = key_substr[0]

        if key == "sf":

    cmd = "python3 train.py -s {0} -n {1} -p {2} -w {3} -c {4} -l {5}"
          " -m {6} -b {7} -e {8} -f {9} -v {10} -x {11} -a {12} -o {13}"
          " -z {14} -g {15} -i {16} -j {17} -k {18}"
          "".format(s, n, p, w, c, l, m, b, e, f, v, x,
                    a, o, z, g, i, j, k)
            


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


































