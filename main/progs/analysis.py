# analyze each test result and write to file accuracy of test result
# color:
#     train on cold:
#         test on cold:
#             50% accuracy
# etc
from bash import bash
import os


bash = bash.Run()

def print_train(path, test_type):
# read train_info.txt, print what was trained
    train_str = ""
    with open(path, "r") as info:
        for line in info:
            line = line.rstrip()
            line_sub = line.split(":")
            key = line_sub[0]

            if len(line_sub) < 2:
                continue

            val = line_sub[1]

            train_str += "{0}:{1} ".format(key, val)

    print("\t" + train_str)


def print_test(path, test_type):
# read test_info.txt, print what was tested
    test_str = ""
    with open(path, "r") as info:
        for line in info:
            line = line.rstrip()
            line_sub = line.split(":")
            key = line_sub[0]

            if len(line_sub) < 2:
                continue

            val = line_sub[-1]

            test_str += "{0}:{1} ".format(key, val)

    print("\t\t" + test_str)


def print_stats(path, test_type):
# read test_stats.txt, print accuracy, skipped percentages
    acc = -1
    with open(path, "r") as info:
        cor = 0
        tot = 0
        for line in info:
            line = line.rstrip()
            line_sub = line.split(":")
            key = line_sub[0]

            if key == "correct":
                cor = int(line_sub[-1])
            elif key == "viewed":
                tot = int(line_sub[-1])

            if not cor or not tot:
                continue

            acc = cor / tot

    acc *= 100
    acc = round(acc, 2)
    print("\t\t\t" + str(acc))


cwd = os.getcwd()
tests = "{0}/tests".format(cwd)
for test_type in sorted(os.listdir(tests)):
    print(test_type)
    type_path = "{0}/{1}".format(tests, test_type)
    for train in sorted(os.listdir(type_path)):
        print("\t{0}".format(train))
        train_path = "{0}/{1}".format(type_path, train)
        for test in sorted(os.listdir(train_path)):
            test_path = "{0}/{1}".format(train_path, test)
            if not os.path.isfile(test_path):
                for item in sorted(os.listdir(test_path)):
                    item_path = "{0}/{1}".format(test_path, item)
                    if item == "test_info.txt":
                        print_test(item_path, test_type)
                    elif item == "test_stats.txt":
                        print_stats(item_path, test_type)
            else:
                if test == "train_info.txt":
                    print_train(test_path, test_type)
    print()
#   for each type of test ran
#       print test type
#
#       for each set of trained data
#           print what was trained (indented)
#
#           for each set of tests
#               print what was tested (indented)
#               get the percent accuracy and skipped
#
#       print newline

# ex:
#
