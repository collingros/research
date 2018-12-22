import os
import argparse


def read_info(item, var_type):
    with open(item, "r") as info:
        for line in info:
            line_substr = line.split(":")
            cur_type = line_substr[0]
            cur_val = line_substr[1]

            if cur_type == var_type:
                return cur_val

    return -1


parser = argparse.ArgumentParser()
pasrer.add_argument("-i")

args = parser.parse_args()
if not args.i:
    print("no type specified, exiting...")
    exit()

var_type = args.i
# graph x axis' name is var_type (set up here)
# graph y axis' name is range 0 to (num of images)

tests = "./stockpile"
for test in os.listdir(tests):
    for item in os.listdir(test):
        if item == "train_info.txt":
            cur_val = read_info(item, var_type)
            cur_viewed = read_info(item, "viewed")
            cur_skipped = read_info(item, "skipped")
            cur_diff = abs(cur_viewed - cur_skipped)

# for each training directory
#     get the variable to look for changes from prog args
#     get the variable's used value from train_info.txt
#     get number of faces detected
#     draw graph based showing each test by num faces detected vs variable value
#     output as data.png in cwd

