# collin gros
# 05/11/2019
# because it's annoying to constantly import os, subprocess and
# redefine these functions over and over again, so it's a package!

import os
import subprocess


class Run:
    def __init__(self):
        pass


    def run(self, cmd):
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        process.wait()


    def mkdir(self, name):
        cmd = "mkdir {0}".format(name)
        self.run(cmd)


    def rm(self, src):
        cmd = "rm -r {0}".format(src)
        self.run(cmd)


    def cp(self, src, dst):
        cmd = "cp -r -p {0} {1}".format(src, dst)
        self.run(cmd)


    def mv(self, src, dst):
        cmd = "mv {0} {1}".format(src, dst)
        self.run(cmd)


    def mirror(self, src, dst):
        cmd = "convert {0} -flop {1}".format(src, dst)
        self.run(cmd)
