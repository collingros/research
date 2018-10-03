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


def print_tests(tests):
    for test in tests:
        test_id = test.gen_data["id"]
        print("TEST:\t{0}".format(test_id))

        for key, value in test.gen_data.items():
            print("{0}:\t{1}".format(key, value))

        print("\n")
        for key, value in test.data.items():
            print("{0}:\t{1}".format(key, value))


def disp_imgs(tests):
    for test in tests:
        test_id = test.gen_data["id"]
        for img in test.gen_data["imgs"]:
            loaded_img = cv2.imread(img, 1)
            cv2.imshow("TEST:\t{0}".format(test_id), loaded_img)
            cv2.waitKey(50)
            cv2.destroyAllWindows()


def get_best(tests, perf):
    if perf == "1":
        for test in tests:
            test_dir = test.gen_data["path"]


def add_test(tests, test_dir_path, id_num):
    new_test = Test()
    new_test.gen_data["path"] = test_dir
    new_test.gen_data["id"] = id_num

    for item in sorted(os.listdir(test_dir_path)):
        # item_path: /home/surv/git/research/ndsu_cyber/new/SET/opt_$dir_n/"item"
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


SET = input("Enter \"out\" for the training data, and \"out2\" otherwise: ")

# stat_dir = /home/surv/git/research/ndsu_cyber/new/SET (out or out2)
stat_dir_path = os.getcwd() + "/" + SET

id_num = 0
tests = []
for test_dir in sorted(os.listdir(stat_dir_path)):
    test_dir_path = stat_dir + "/" + test_dir

    add_test(tests, test_dir_path, id_num)
    id_num += 1

best_tests = get_best(tests)

print_tests(best_tests)
disp_imgs(best_tests)




















