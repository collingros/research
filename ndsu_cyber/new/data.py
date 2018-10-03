import os
import cv2
from subprocess import call


class Test:
    def __init__(self):
        self.gen_data = {
                # general data: file paths
                "imgs":[],
                "path":"",
                "id":-1
            }

        self.data = {
                # scriptstat.txt statistics
                "filters":{},
                "results":{}
            }


def get_best(tests):
    for test in tests:
        curr_dir = test.gen_data["path"]


def add_test(tests, test_dir, id_num):
    new_test = Test()
    new_test.gen_data["path"] = test_dir
    new_test.gen_data["id"] = id_num

    for item in sorted(os.listdir(test_dir)):
        item_path = test_dir + "/" + item
        item_substr = item.split(".")
        ext = item_substr[-1]

        if ext == "txt":
            with open(item_path, "r") as stats:
                filters = 1

                for line in stats:
                    line_subs = line.strip("\n").split("\t")
                    key = line_subs[0]

                    if key.islower():
                        # the options in the stat file are uppercase when
                        # dealing with filters, lowercase otherwise
                        filters = 0

                    key = key.lower()
                    value = line_subs[-1]
                        
                    if filters:
                        new_test.data["filters"][key] = value
                    else:
                        new_test.data["results"][key] = value

        elif ext == "JPG":
            new_test.gen_data["imgs"].append(item_path)


SET = input("Enter \"out\" for the training data, and \"out2\" otherwise: ")

stat_dir = os.getcwd() + "/" + SET

id_num = 0
tests = []
for test_dir in sorted(os.listdir(stat_dir)):
    add_test(tests, test_dir, id_num)
    id_num += 1

best_tests = get_best(tests)

