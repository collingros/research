import os
import subprocess


def reset():
    cmd = "./progs/reset.sh"
    run_cmd(cmd)


def data(test_type):
    cmd = "python3 ./progs/data.py -i {0}".format(test_type)
    run_cmd(cmd)


def cp(src, dst):
    cmd = "cp -r {0} {1}".format(src, dst)
    run_cmd(cmd)


def mv(src, dst):
    cmd = "mv {0} {1}".format(src, dst)
    run_cmd(cmd)


def run_cmd(cmd):
    print("running:\t{0}".format(cmd))
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    process.wait()


tests_path = "./tests"
stockpile_path = "./stockpile"
for test_type in sorted(os.listdir(tests_path)):
    test_type_path = "{0}/{1}".format(tests_path, test_type)
    test_path = "{0}/{1}".format(test_type_path, "*")

    cp(test_path, stockpile_path)
    data(test_type)

    src = "./data.png"
    dst = "./graphs/{0}.png".format(test_type)
    mv(src, dst)
    reset()
