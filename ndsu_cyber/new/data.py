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


    def print_tests(self):
        for data_dir, tests in self.tests.items():
            for test in tests:
                test.print_test()

    def print_accs(self):
        for data_dir, tests in self.tests.items():
            for test in tests:
                test.print_acc()



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


    def print_acc(self):
        results_filter = ["c_names", "w_names"]
        num_c = 0
        num_w = 0

        self.print_test()

        for key, item in self.data["results"].items():
            if key in results_filter:
                item = eval(item)

        for result in results_filter:
            print("result: {0}".format(result))
            for person, arr in self.data["results"][result].items():
                # FIXME: i assumed that results[result] was a dict
                #        but is in fact just a printed dict, so a str...
                if result == "c_names":
                    num_c += 1
                else:
                    num_w += 1

                for conf_arr, len_of_arr in arr.items():
                    if result == "c_names":
                        num_c += len_of_arr
                    else:
                        num_w += len_of_arr

        print("test id:\t{0}\n"
              "test path:\t{1}\n"
              "".format(self.gen_data["id"], self.gen_data["path"]))
        print("number of correctly identified images:\t{0}\n"
              "number of incorrectly identified images:\t{1}"
              "".format(num_c, num_w))


    def print_test(self):
        filter_vars = ["sf", "mn", "test_height"]
        result_vars = ["total_faces"]

        test_id = self.gen_data["id"]
        path = self.gen_data["path"]
        print("\nTEST:\t{0}\nPATH:\t{1}".format(test_id, path))

        for key, value in self.data.items():
            print("{0}".format(key))
            for key_2, value_2 in self.data[key].items():
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

stats.print_accs()








