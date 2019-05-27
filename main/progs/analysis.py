# analyze each test result and write to file accuracy of test result
# color:
#     train on cold:
#         test on cold:
#             50% accuracy
# etc
from bash import bash
import os


bash = bash.Run()


def print_train(path):
# read train_info.txt, print what was trained
    train_str = ""
    prog = ["sf", "mn", "res", "c"]
    with open(path, "r") as info:
        for line in info:
            line = line.rstrip()
            line_sub = line.split(":")
            key = line_sub[0]

            if len(line_sub) < 2 or key in prog:
                continue

            train_str = "{0}, {1}".format(train_str, line)

    print("\t" + train_str)


def print_test(path):
# read test_info.txt, print what was tested
    print("\t\t\t" + path)


def print_stats(path):
# read test_stats.txt, print accuracy, skipped percentages
    print("\t\t\t" + path)


cwd = os.getcwd()
tests = "{0}/tests".format(cwd)
for test_type in os.listdir(tests):
    type_path = "{0}/{1}".format(tests, test_type)
    print(test_type)
    for train in os.listdir(type_path):
        train_path = "{0}/{1}".format(type_path, train)
        print("\t" + train)
        for test in os.listdir(train_path):
            test_path = "{0}/{1}".format(train_path, test)
            if os.path.isfile(test_path):
                if test == "train_info.txt":
                    print_train(test_path)

                continue

            print("\t\t" + test)
            for item in os.listdir(test_path):
                item_path = "{0}/{1}".format(test_path, item)
                if item == "test_info.txt":
                    print_test(item_path)
                elif item == "test_stats.txt":
                    print_stats(item_path)
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
