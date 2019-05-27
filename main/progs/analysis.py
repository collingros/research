# analyze each test result and write to file accuracy of test result
# color:
#     train on cold:
#         test on cold:
#             50% accuracy
# etc
from bash import bash
import os


bash = bash.Run()


cwd = os.getcwd()
tests = "{0}/tests".format(cwd)
for test_type in os.listdir(tests):
    print(test_type)

    path = "{0}/{1}".format(tests, test_type)
    for train in os.listdir(path):
        print("\t" + train)

        path = "{0}/{1}".format(path, train)
        for test in os.listdir(path):
            if os.path.isfile(test):
                if test == "train_info.txt":
                    print("\t\ttrain info!!")
                    continue

                print("\t\t" + test)

                path = "{0}/{1}".format(path, test)
                for item in os.listdir(path):
                    print("\t\t\t" + item)
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
