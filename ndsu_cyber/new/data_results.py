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
                     "skipped_imgs": 0
                     }


def print_tests(tests):
    test_c = 1
    for test in tests:
        print("\t**DATA FOR TEST " + str(test_c) + "**")

        for key, value in test.data.items():
            print(str(key) + ":\t" + str(value))

        print("\t**END OF DATA FOR TEST " + str(test_c) + "**")
        test_c += 1  


def show_results(tests):
    ordered_acc = []
    last_acc = -1
    for test in tests:
        acc = test.data["accuracy"]
        print("ACC IS " + str(acc))
        if last_acc == -1 and acc <= 100:
            last_acc = acc
        elif last_acc != -1 and acc > last_acc and acc <= 100:
            print("adding test!!")
            ordered_acc.append(test)

    print("before cutoff")
    print(ordered_acc)
    ordered_acc = ordered_acc[-10:]
    print("after cutoff")
    print(ordered_acc)

    print("tests with the highest accuracy (top 10: lowest to highest)")
    for test in ordered_acc:
        for key, value in test.items():
            print(key + ":\t" + value)
            


def add_data(tests, path):
    new_test = Test()

    new_test.data["path"] = path

    for item in os.listdir(path):
        item_path = path + "/" + item

        print("item:\t" + item_path)

        if item == "scriptstat.txt":
            new_test.data["stats"] = item_path

            with open(item_path, "r") as info:
                line_c = 1
                for line in info:
                    line_subs = line.strip("\n").split("\t")

                    # COMMENTING UNTIL TESTED DATA IS SORTED CORRECTLY!!!
                    
                    if line_c == 1:
                        speed = line_subs[-1].split(" ")[0]
                        new_test.data["speed"] = float(speed)
                        #print("adding speed...")
                        #print(str(speed))
                    elif line_c == 5:
                        new_test.data["cascade"] = line_subs[-1]
                        #print("adding cascade...")
                        #print(str(line_subs[-1]))
                    elif line_c == 19:
                        new_test.data["sf"] = float(line_subs[-1])
                        #print("adding sf...")
                        #print(str(line_subs[-1]))
                    elif line_c == 15:
                        new_test.data["mn"] = int(line_subs[-1])
                        #print("adding mn...")
                        #print(str(line_subs[-1]))
                    elif line_c == 23:
                        new_test.data["res"] = int(line_subs[-1])
                        #print("adding res...")
                        #print(str(line_subs[-1]))
                    elif line_c == 33:
                        if line_subs[-1] == "skipped_is_0":
                            new_test.data["accuracy"] = 100
                        else:
                            new_test.data["accuracy"] = float(line_subs[-1])
                        #print("adding accuracy...")
                        #print(str(line_subs[-1]))
                    elif line_c == 29:
                        new_test.data["reviewed_imgs"] = int(line_subs[-1])
                    elif line_c == 30:
                        new_test.data["skipped_imgs"] = int(line_subs[-1])
                    elif line_c == 31:
                        new_test.data["total_imgs"] = int(line_subs[-1])
                    

                    #print("item_path: " + item_path)
                    line_c += 1

        elif item.split(".")[1] == "JPG":
            new_test.data["imgs"].append(item_path)
        elif item.split("/")[-1] == "train.yml":
            new_test.data["train"] = item_path
        elif item.split("/")[-1] == "labels.pickle":
            new_test.data["labels"] = item_path


    tests.append(new_test)

tests = []
parent_dir = os.getcwd() + "/"
for result_dir in sorted(os.listdir(parent_dir + "out/")):
    result_path = parent_dir + "out/" + result_dir

    add_data(tests, result_path)

#print_tests(tests)
print("now show results")
show_results(tests)

