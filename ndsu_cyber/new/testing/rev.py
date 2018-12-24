import os
import subprocess


def write_score(score):
    with open("score.txt", "w") as info:
        for key, value in score.items():
            str = "{0}:{1}\n".format(key, value)
            info.write(str)


def run_cmd(cmd):
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    process.wait()


score = {}
cwd = os.getcwd()
stockpile_path = "{0}/{1}".format(cwd, "stockpile")
for test in sorted(os.listdir(stockpile_path)):
    test_path = "{0}/{1}".format(stockpile_path, test)
    for item in os.listdir(test_path):
        item_path = "{0}/{1}".format(test_path, item)
        substr = item.split(".")

        if len(substr) < 2:
            continue
        if substr[-1] != "JPG":
            continue

        cmd = "feh {0}".format(item_path)
        run_cmd(cmd)

    rating = input("")
    score[test] = rating

write_score(score)
