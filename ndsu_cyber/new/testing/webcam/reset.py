import os
import subprocess


def rm(src):
    cmd = "rm {0}".format(src)
    runcmd(cmd)


def runcmd(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    process.wait()


cwd = os.getcwd()
train_path = "./train"
for id in sorted(os.listdir(train_path)):
    id_path = "{0}/{1}".format(train_path, id)
    for item in sorted(os.listdir(id_path)):
        substr = item.split(".")
        if len(substr) > 1:
            continue

        dir_path = "{0}/{1}".format(id_path, item)
        for pic in sorted(os.listdir(dir_path)):
            pic_path = "{0}/{1}".format(dir_path, pic)
            rm(pic_path)
