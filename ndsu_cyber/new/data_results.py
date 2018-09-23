import os


class Test:
    def __init__(self):
        self.data = {"path": "",
                     "train": "",
                     "stats": "",
                     "labels": "",
                     "imgs": [],
                     "speed": -1,
                     "cascade": "",
                     "sf": 1,
                     "mn": -1,
                     "res": -1,
                     "accuracy": -1.0,
                     "total_imgs": 0,
                     "reviewed_imgs": 0,
                     "skipped_imgs": 0,
                     "id": -1
                     }


def print_tests(tests, custom):
    print("*BEGINNING OF " + custom + "*")
    for test in tests:
        print("\t***DATA FOR TEST " + str(test.data["id"]) + "***")

        for key, value in test.data.items():
            print(str(key) + ":\t" + str(value))

        print("\t***END OF DATA FOR TEST " + str(test.data["id"]) + "***")
    print("*END OF " + custom + "*")


def show_results(tests, LENIENCY):
    '''
    SHITTY, INEFFICIENT, NOT WHAT I WANT, but keeping it for now as
    last resort (in case i'm too stupid to figure this out)

    ordered_acc = []
    last_acc = -1
    for test in tests:
        acc = test.data["accuracy"]
        if last_acc == -1 and acc <= 100:
            last_acc = acc
        elif last_acc != -1 and acc > last_acc and acc <= 100:
            ordered_acc.append(test)

    ordered_acc = ordered_acc[-10:]

    print("tests with the highest accuracy (top 10: lowest to highest)")
    test_c = 0
    for test in ordered_acc:
        test_c += 1
        print("test number " + str(test_c))
        for key, value in test.data.items():
            print(key + ":\t" + str(value))
        input()
    '''

    total_imgs = tests[0].data["total_imgs"]
    best_tests = tests
    last_ids = []
    tmp_tests = []
    # making worst possible outcomes for initial last_r and last_s
    last_s = tests[0].data["total_imgs"]
    last_r = 0
    # tests[0] should have the same total_imgs number as the rest
    while len(best_tests) > 10 and LENIENCY >= 0:
        #print("current tests length: " + str(len(tests)))
        for test in best_tests:
            #print("\ncurrent test id: " + str(test.data["id"]))
            for key, value in test.data.items():
                if key == "reviewed_imgs":
                    reviewed = value
                elif key == "skipped_imgs":
                    skipped = value

            #print("if " + str(reviewed) + " <= " + str(total_imgs) +
            #      " + " + str(LENIENCY) + " and")
            #print(str(reviewed) + " > " + str(last_r) + " - " +
            #      str(LENIENCY) + " and " +
            #      str(skipped) + " < " + str(last_s) + " + " +
            #      str(LENIENCY) + " and")
            #print(str(test.data["id"]) + " not in " + str(last_ids))

            if ((reviewed <= total_imgs + LENIENCY) and
                ((reviewed > last_r - LENIENCY) and
                 (skipped < last_s + LENIENCY)) and
                (test.data["id"] not in last_ids)):
                # if the num of detected faces is about the same as the num
                # of images and the current value is better than the last
                # set new max

                #print("PASSED IF")
                last_ids.append(test.data["id"])
                last_r = reviewed
                last_s = skipped
                tmp_tests.append(test)
            else:
                pass
                #print("FAILED IF")
        best_tests = tmp_tests
        LENIENCY -= 1


    print_tests(best_tests, "BEST TESTS")



def add_data(tests, path):
    new_test = Test()

    new_test.data["path"] = path

    path_subs = path.split("/")
    test_id = ''.join(filter(str.isdigit, path_subs[-1]))
    new_test.data["id"] = test_id
    # need a unique test id for differentiating tests, test num works
    # (test num is int at last part of path)

    for item in os.listdir(path):
        item_path = path + "/" + item

        if item == "scriptstat.txt":
            new_test.data["stats"] = item_path

            with open(item_path, "r") as info:
                line_c = 1
                for line in info:
                    line_subs = line.strip("\n").split("\t")

                    if line_c == 1:
                        speed = line_subs[-1].split(" ")[0]
                        new_test.data["speed"] = float(speed)
                    elif line_c == 5:
                        new_test.data["cascade"] = line_subs[-1]
                    elif line_c == 19:
                        new_test.data["sf"] = float(line_subs[-1])
                    elif line_c == 15:
                        new_test.data["mn"] = int(line_subs[-1])
                    elif line_c == 23:
                        new_test.data["res"] = int(line_subs[-1])
                    elif line_c == 33:
                        if line_subs[-1] == "skipped_is_0":
                            new_test.data["accuracy"] = -1
                        else:
                            new_test.data["accuracy"] = float(line_subs[-1])
                    elif line_c == 29:
                        new_test.data["reviewed_imgs"] = int(line_subs[-1])
                    elif line_c == 30:
                        new_test.data["skipped_imgs"] = int(line_subs[-1])
                    elif line_c == 31:
                        new_test.data["total_imgs"] = int(line_subs[-1])

                    line_c += 1

        elif item.split(".")[1] == "JPG":
            new_test.data["imgs"].append(item_path)
        elif item.split("/")[-1] == "train.yml":
            new_test.data["train"] = item_path
        elif item.split("/")[-1] == "labels.pickle":
            new_test.data["labels"] = item_path

    if new_test.data["accuracy"] == -1:
        # "accuracy" only means # of faces detected / # of imgs skipped
        # so if skipped is 0, and there are an unreasonable amount of
        # faces detected, the accuracy is bad, this if is to correct the
        # assumtion of a bad result by checking if # of faces detected
        # is a reasonable number (300 is the total # of tests)
        new_test.data["accuracy"] = new_test.data["reviewed_imgs"]

    tests.append(new_test)


tests = []
parent_dir = os.getcwd() + "/"
for result_dir in sorted(os.listdir(parent_dir + "out/")):
    result_path = parent_dir + "out/" + result_dir

    add_data(tests, result_path)

#print_tests(tests, "INITIAL RESULTS")
show_results(tests, 30)

