# Collin Gros
#
# to parse data output from training and testing sessions
# (currently, to get the best training data and use it for testing f.r. acc)
#
# context:
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
# TODO:
# debug
# fix fixme's
# run test on training sets to get results for testing sets
#
import os
import cv2
from subprocess import call
import time


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
        path = test.gen_data["path"]
        print("\nTEST:\t{0}\nPATH:\t{1}".format(test_id, path))

        for key, value in test.data.items():
            print("{0}".format(key))
            for key_2, value_2 in test.data[key].items():
                print("\t{0}:\t{1}".format(key_2, value_2))


def disp_imgs(tests):
    for test in tests:
        test_id = test.gen_data["id"]
        for img in test.gen_data["imgs"]:
            loaded_img = cv2.imread(img, 1)
            cv2.imshow("TEST:\t{0}".format(test_id), loaded_img)
            cv2.waitKey(50)
            cv2.destroyAllWindows()


def avg_test(tests, perf):
    # show avg result from tests by SF, MN, RES, or other things
    pass


def get_best(tests, LENIENCY):
    # simply get the top 10 best results

    total_imgs = int(tests[0].data["results"]["reviewed"])
    # (same total amount of images looked at for all our tests)
    best_tests = []
    last_ids = []

#   starting with worst case scenarios
    last_s = total_imgs
    last_p = 0
    processed = 0
    skipped = 0

#   FIXME
#   in its current state, this loop will perform a sort only to the first 10
#   tests, meaning the last test in best_tests will have the best value of
#   the reviewed tests, however, the last test in best_tests may not be the
#   best test in ALL of the tests. the loop halts after 10 are chosen.
    for test in tests:
        for key, value in test.data["results"].items():
            if key == "processed_faces":
                processed = int(value)
            elif key == "skipped":
                skipped = int(value)

        if ((processed <= total_imgs + LENIENCY) and
           ((processed > last_p - LENIENCY) and
           (skipped < last_s + LENIENCY)) and
           (test.gen_data["id"] not in last_ids)):
           # if the num of processed faces is about the same as the total
           # num of images and the current values are better than the last
           # set new max

            last_ids.append(test.gen_data["id"])
            print(last_ids)
            last_p = processed
            last_s = skipped
            best_tests.append(test)

    return best_tests


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

    tests.append(new_test)


user_input = {
    "SET":"",
    "LENIENCY":""
}

for key, value in user_input.items():
    value = input("Enter \"{0}\":\t".format(key))
    user_input[key] = value

SET = user_input["SET"]
LENIENCY = int(user_input["LENIENCY"])

stat_dir_path = os.getcwd() + "/" + SET

# stat_dir = /home/surv/git/research/ndsu_cyber/new/SET (out or out2)

id_num = 0
tests = []
for test_dir in sorted(os.listdir(stat_dir_path)):
    test_dir_path = stat_dir_path + "/" + test_dir

    add_test(tests, test_dir_path, id_num)
    id_num += 1

best_tests = get_best(tests, LENIENCY)

#print("**ALL TESTS**")
#print_tests(tests)
#print("**BEST TESTS**")
print_tests(best_tests)
#disp_imgs(best_tests)




















