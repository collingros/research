# Collin Gros
# 11/29/18
# REFACTORING ATTEMPT 1
import os
import subprocess


class Test:
    def __init__(self):
        pass


class Train:
    def __init__(self):
        self.trained = None
        self.id = 0


    def build_cmd(self):
        return ""


    def update_trained(self):
        self.trained = False


    def run(self):
        self.update_trained()
        if not self.trained:
            dir_path = "./stockpile/{0}".format(self_id)
            mkdir(dir_path)

            train = self.build_cmd()
            run_cmd(train)

            train_path = "./train.yml"
            mv(train_data, dir_path + train_path)

            train_info = "./train_info.txt"
            mv(train_info, dir_path + train_info)
            # psuedocode is WRONG: can't move program into directories,
            # as the training program requires the current directory to have
            # the database
            # aka: must move output train.yml and train_info.txt into dir_path
            # (as well as test data)


def mkdir(path):
    cmd = "mkdir {0}".format(name)
    run_cmd(cmd)


def run_cmd(cmd):
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    process.wait()
