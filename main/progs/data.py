# Collin Gros
# 12/21/18
#
# Draw graph for each tests' train_stats.txt file
#
import os
import matplotlib.pyplot as plt
import argparse


def read_info(item, var_type):
    with open(item, "r") as info:
        for line in info:
            line_substr = line.split(":")
            if len(line_substr) < 2:
                continue

            cur_type = line_substr[0]
            cur_val = line_substr[1]

            if cur_type == var_type:
                return cur_val

    return -1


parser = argparse.ArgumentParser()
parser.add_argument("-i")

args = parser.parse_args()
if not args.i:
    print("no type specified, exiting...")
    exit()

var_type = args.i
fig = plt.figure()
plt.rc("xtick", labelsize=6)
plt.rc("ytick", labelsize=6)
x = []
y = []
# graph x axis' name is var_type (set up here)
# graph y axis' name is range 0 to (num of images)

cur_total = 0
tests = "./stockpile"
for test in sorted(os.listdir(tests)):
    test_path = tests + "/" + test
    info_path = test_path + "/" + "train_info.txt"

    try:
        cur_val = int(read_info(info_path, var_type))
    except:
        cur_val = str(read_info(info_path, var_type))

    stats_path = test_path + "/" + "train_stats.txt"
    cur_viewed = int(read_info(stats_path, "viewed"))
    cur_total = int(read_info(stats_path, "total"))

    cur_diff = abs(cur_viewed - cur_total)

    x.append(cur_val)
    y.append(cur_diff)

x = sorted(x)
y = sorted(y)
plt.plot(x, y)

print(x)
print(y)
print("\n")

goal = y
for i in range (0, len(goal)):
    goal[i] = cur_total
print(x)
print(goal)
plt.plot(x, goal)

fig.savefig("./data.png")
