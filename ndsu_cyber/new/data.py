# Collin Gros
#
# to parse data output from training and testing sessions
# (currently, to get the best training data and use it for testing f.r. acc)
#
# context:

#   FOR TRAINING OPTIMIZATION:

#   every test was ran with some different setting than the previous
#   in scriptstat.txt:
#        split into two parts:
#           1. all-caps output are the specific test settings the test was ran
#              with ("filters")
#           2. lowercase output are the results from the test:
#                   processed_faces is the number of FACES detected in total
#
#                   reviewed is the number of IMGS looked at in total
#
#                   size_skipped is the number of images skipped as a result of
#                   an experimental method to attempt to find false faces from
#                   a comparison between "face area" and the detected "face"
#
#                   skipped is the number of images skipped because no face was
#                   detected
#
#                   time is the total amount of time it took to process (sec)
#
#                   total_faces is the number of IMGS with at least one face
#                   detected
#
#   FOR TESTING OPTIMIZATION:
#
#   tests structured just like training optimization,
#   the scriptstat file is different:
#
#       c_names: dict with key as username and value as an array containing
#                the confidences of each prediction, as well as the num of
#                confidences in that array - NOTE - the fact that there is
#                an element with someone's name means that the person
#                has one prediction already. ('11':[[],0] still means one
#                prediction took place)
#
# TODO:
# debug
# fix fixme's
# support for test.py results
#
import os
import cv2
from subprocess import call
import time

'''
class Test:
    def __init__(self):
        self.gen_data = {
                # general data: file paths
                "imgs":[],
                "path":"",
                "id":-1,
                "perc_detect":0,
                "perc_skip":0,
                "perc_img_detect":0,
                "num_c":0
            }

        self.data = {
                # scriptstat.txt statistics
                "filters":{},
                "results":{}
            }
'''
class Statistics:
    def __init__(self, IS_TEST):
        # IS_TEST: True if the folder we want to view stats of is from tested
        # data, not trained data

        self.IS_TEST = IS_TEST
        self.tests = self.init_tests()

        if not (len(self.tests)):
            print("no tests")
        else:
            print("expert")

        for data_dir, tests in self.tests.items():
            for test in tests:
                test.print_test()


    def init_tests(self):
        tests = {}

        if self.IS_TEST:
            data_dir_path = os.getcwd() + "/" + "out2"

            for data_dir in sorted(os.listdir(data_dir_path)):
                test_dir_path = data_dir_path + "/" + data_dir

                tests[data_dir] = []
                id_num = 0
                for test_dir in sorted(os.listdir(test_dir_path)):
                    stat_dir_path = test_dir_path + "/" + test_dir

                    self.add_test(tests[data_dir], stat_dir_path, id_num)
                    id_num += 1
        else:
            test_dir_path = os.getcwd() + "/" + "out"

            tests["TRAIN"] = []
            id_num = 0
            for test_dir in sorted(os.listdir(test_dir_path)):
                stat_dir_path = test_dir_path + "/" + test_dir

                self.add_test(tests["TRAIN"], stat_dir_path, id_num, IS_TEST)
                id_num += 1

        return tests


    def add_test(self, tests, path, id_num):
        new_test = Test(self.IS_TEST)

        new_test.fill(path, id_num)

        tests.append(new_test)





class Test:
    def __init__(self, IS_TEST):
        # IS_TEST: should the scriptstat.txt file have the expected format
        # for train.py output or test.py output? IS_TEST = test.py
        self.IS_TEST = IS_TEST
        if self.IS_TEST:
            self.gen_data = {
                    # general data
                    "imgs":[],
                    "path":"",
                    "id":-1,
                    "num_c":0,
                    "num_w":0
                }
        else:
            self.gen_data = {
                    "imgs":[],
                    "path":"",
                    "id":-1
                }


        self.data = {
                # scriptstat.txt statistics
                "filters":{},
                "results":{}
            }


    def print_test(self):
        filter_vars = ["sf", "mn", "test_height"]
        result_vars = ["total_faces"]

        test_id = self.gen_data["id"]
        path = self.gen_data["path"]
        print("\nTEST:\t{0}\nPATH:\t{1}".format(test_id, path))

        for key, value in test.data.items():
            print("{0}".format(key))
            for key_2, value_2 in test.data[key].items():
                if key_2 in result_vars or key_2 in filter_vars:
                    print("\t{0}:\t\t{1}".format(key_2, value_2))
            print("\n\n")


    def disp_imgs(self):
        test_id = self.gen_data["id"]
        for img in self.gen_data["imgs"]:
            loaded_img = cv2.imread(img, 1)
            cv2.imshow("TEST:\t{0}".format(test_id), loaded_img)
            cv2.waitKey(50)
            cv2.destroyAllWindows()


    def fill(self, path, id_num):
        self.gen_data["path"] = path
        self.gen_data["id"] = id_num

        for item in sorted(os.listdir(path)):
            item_path = path + "/" + item
            item_substr = item.split(".")

            ext = item_substr[-1]
            # file extension

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
                            self.data["filters"][key] = value
                        else:
                            self.data["results"][key] = value

            elif ext == "JPG":
                self.gen_data["imgs"].append(item_path)


# MAIN
IS_TEST = bool(input("is this test.py output (True/False)?:\t"))
stats = Statistics(IS_TEST)


'''
def print_test(test):
    filter_vars = ["sf", "mn", "test_height"]
    result_vars = ["processed_faces", "skipped", "total_faces"]

    test_id = test.gen_data["id"]
    path = test.gen_data["path"]
    print("\nTEST:\t{0}\nPATH:\t{1}".format(test_id, path))

    for key, value in test.data.items():
        print("{0}".format(key))
        for key_2, value_2 in test.data[key].items():
            if key_2 in result_vars or key_2 in filter_vars:
                print("\t{0}:\t\t{1}".format(key_2, value_2))
        print("\n\n")


def disp_imgs(test):
    test_id = test.gen_data["id"]
    for img in test.gen_data["imgs"]:
        loaded_img = cv2.imread(img, 1)
        cv2.imshow("TEST:\t{0}".format(test_id), loaded_img)
        cv2.waitKey(50)
        cv2.destroyAllWindows()


def test_sort(tests, IS_TEST):
    # change test_sort arg2 to processed_faces for trained data, otherwise,
    # keep at c_names
    if IS_TEST:
        tests.sort(key=lambda test: int(
                   test.data["results"]["c_names"]
                   ),
                   reverse=False)
    else:
        tests.sort(key=lambda test: int(
                   test.data["results"]["processed_faces"]),
                   reverse=False)

    return tests


def add_test(tests, test_dir_path, id_num, IS_TEST):
    new_test = Test()
    new_test.gen_data["path"] = test_dir
    new_test.gen_data["id"] = id_num

    for item in sorted(os.listdir(test_dir_path)):
        item_path = test_dir_path + "/" + item
        item_substr = item.split(".")

        # file extension
        ext = item_substr[-1]

        if ext == "txt":
            with open(item_path, "r") as stats:
                # stats file is split in two sections: results and filters
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

    if len(new_test.data["results"]) > 0:
        processed = int(new_test.data["results"]["processed_faces"])
        reviewed = int(new_test.data["results"]["reviewed"])
        total_faces = int(new_test.data["results"]["total_faces"])
        skipped = int(new_test.data["results"]["skipped"])

        new_test.gen_data["perc_img_detect"] = round((total_faces/reviewed), 2)
        new_test.gen_data["perc_skip"] = round((skipped/reviewed), 2)
        new_test.gen_data["perc_detect"] = round((processed/reviewed), 2)

    if 


        tests.append(new_test)


def get_tests(SET, IS_TEST, TRAINED_DIR):
    tests = {}

    if IS_TEST:
        data_dir_path = os.getcwd() + "/" + SET

        for data_dir in sorted(os.listdir(data_dir_path)):
            test_dir_path = os.getcwd() + "/" + data_dir

            tests[data_dir] = []
            id_num = 0
            for test_dir in sorted(os.listdir(test_dir_path)):
                stat_dir_path = test_dir_path + "/" + test_dir

                add_test(tests[data_dir], stat_dir_path, id_num, IS_TEST)
                id_num += 1
    else:
        test_dir_path = os.getcwd() + "/" + SET

        tests[""] = []
        id_num = 0
        for test_dir in sorted(os.listdir(test_dir_path)):
            stat_dir_path = test_dir_path + "/" + test_dir

            add_test(tests[""], stat_dir_path, id_num, IS_TEST)
            id_num += 1

    return tests


SET = "out2"
LENIENCY = 30

IS_TEST = True
# is the output from running test.py? the dir format and scripstat is then
# different

tests = get_tests(SET, IS_TEST, TRAINED_DIR)
# ** NOW A DICTIONARY **

new_tests = {}
for key, value in tests.items():
    new_tests[key] = test_sort(value, IS_TEST)

while True:
    for test in new_tests:
        processed = int(test.data["results"]["processed_faces"])
        actual = int(test.data["results"]["reviewed"])

        if (processed > actual + LENIENCY or
            processed < actual - LENIENCY):
            # bad test results, according to leniency
            continue

        print_test(test)

    print("select test ID to disp images")
    choice = int(input("\t"))

    for test in new_tests:
        if test.gen_data["id"] == choice:
            disp_imgs(test)
'''

