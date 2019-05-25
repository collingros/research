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
