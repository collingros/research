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


class Statistics:
    def __init__(self, IS_TEST):
        # IS_TEST: True if the folder we want to view stats of is from tested
        # data, not trained data

        self.IS_TEST = IS_TEST
        self.tests = self.init_tests()


    def init_tests(self):
        tests = {}

        if self.IS_TEST:
            data_dir_path = os.getcwd() + "/" + "out2"

            id_num = 0
            for data_dir in sorted(os.listdir(data_dir_path)):
                test_dir_path = data_dir_path + "/" + data_dir

                tests[data_dir] = []
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


    def sort_accs(self):
        for direct, test in self.tests.items():
            self.tests[direct] = sorted(self.tests[direct],
                                        key=lambda test: test.gen_data["acc"],
                                        reverse=False)


    def add_test(self, tests, path, id_num):
        new_test = Test(self.IS_TEST)

        new_test.fill(path, id_num)

        tests.append(new_test)


    def print_tests(self):
        for data_dir, tests in self.tests.items():
            for test in tests:
                test.print_test()

    def get_accs(self):
        for data_dir, tests in self.tests.items():
            for test in tests:
                test.get_acc()


    def disp_test(self, test_id):
        for data_dir, tests in self.tests.items():
            for test in tests:
                if test.gen_data["id"] == test_id:
                    test.disp_imgs()


    def print_avg_accs(self):
        keys = ["sf", "mn", "test_height"]
        for data_dir, tests in self.tests.items():
            print("NEW TRAINING DATA")

            avg_accs = {}
            num_val = 0

            for test in tests:
                for key, val in test.data["filters"]:
                    if key in keys:
                        avg_accs[val] += test.data["results"]["acc"]
                        num_val += 1 

            print("avg_accs before avgs")
            print(avg_accs)

            for key, val in avg_accs:
                val = val / num_val



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


    def get_acc(self):
        results_filter = ["c_names", "w_names"]
        num_c = 0
        num_w = 0

        for result in results_filter:
            for person, arrs in eval(self.data["results"][result]).items():
                if result == "c_names":
                    num_c += 1 + arrs[1]
                else:
                    num_w += 1 + arrs[1]

        try:
            acc = round((num_c / (num_c + num_w)), 2)
        except:
            acc = 0
        acc *= 100

        self.gen_data["acc"] = acc


    def print_test(self):
        filter_vars = ["sf", "mn", "test_height"]
        result_vars = ["acc", "id", "path"]

        test_id = self.gen_data["id"]
        path = self.gen_data["path"]
        print("\nTEST:\t{0}\nPATH:\t{1}".format(test_id, path))

        for key, value in self.data.items():
            print("{0}".format(key))
            for key_2, value_2 in self.data[key].items():
                if key_2 in result_vars or key_2 in filter_vars:
                    print("\t{0}:\t\t{1}".format(key_2, value_2))
            print("\n")

        for key, value in self.gen_data.items():
            if key in result_vars or key in filter_vars:
                print("\t{0}:\t\t{1}".format(key, value))


    def disp_imgs(self):
        test_id = self.gen_data["id"]
        opt = self.gen_data["path"].split("/")[-1]
        data = self.gen_data["path"].split("/")[-2]
        for img in self.gen_data["imgs"]:
            loaded_img = cv2.imread(img, 1)
            cv2.imshow("ID: {0} OPT: {1} DATA: {2}".format(test_id, opt,
                       data), loaded_img)
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

stats.get_accs()
stats.sort_accs()

#stats.print_tests()

stats.print_avg_accs()

#while True:
#    test_id = int(input("disp imgs for which test?\t"))
#    stats.disp_test(test_id)





