# Collin Gros
#
# organization
import os
import subprocess
import argparse


def cp(src, dst):
    cmd = "cp -r {0} {1}".format(src, dst)
    run_cmd(cmd)


def run_cmd(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    process.wait()


parser = argparse.ArgumentParser()
parser.add_argument("-i")

args = parser.parse_args()
if not args.i:
    print("no type specified, exiting...")
    exit()

var_type = args.i
src = "./stockpile"
dst = "./tests/{0}".format(var_type)

cp(src, dst)
