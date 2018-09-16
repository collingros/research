import matplotlib.pyplot as plt
import decimal
from numpy import array
import numpy as np

TESTS_NUM = 25
# KEYS
'''
key: 0	value: SF (float)
key: 1	value: TRAIN_SF (float)
key: 2	value: MN (int)
key: 3	value: TRAIN_MN (int)
key: 4	value: TOTAL FRAMES (int)
key: 5	value: DETECTED FRAMES (int)
key: 6	value: ACCURACY (float)
key: 7	value: VIDEO (str) - 0 for cold, 1 for warm, 2 for low 3 for med,
                             4 for bright
key: 8	value: TARGET (str) - index of person's name in people []
key: 9  value: TEST_HEIGHT (int)
key: 10 value: BEARDS (int)
key: 11	value: HEIGHT (int)
key: 12	value: RATIO (float)
key: 13	value: GLASSES (int)
key: 14	value: HAT (int)
key: 15	value: VANILLA (int)
key: 16	value: WARM (int)
key: 17	value: COLD (int)
key: 18	value: LOW (int)
key: 19	value: MED (int)
key: 20	value: HIGH (int)
key: 21	value: SHADOWS (int)
key: 22	value: PROFILES (int)
key: 23	value: ANGLED (int)
key: 24	value: CENTER (int)
key: 25	value: -1 NEW TEST
'''
people = ["collin_gros", "isaac_burton", "marco_colasito", "nick_snell",
          "william_clemons", "demitrius"]
stats = []
with open("stat.txt", "r") as f:
    for line in f:
        if not line.strip():
            stats.append("-1")
            continue
        if line[0] == ".":
            continue
        data = line.split(":")[1].lstrip().rstrip("\n")

        try:
            float(data)
            stats.append(data)
        except:
            if "MP4" in data:
                if "cold" in data:
                    stats.append("0")
                elif "warm" in data:
                    stats.append("1")
                elif "low" in data:
                    stats.append("2")
                elif "med" in data:
                    stats.append("3")
                elif "high" in data:
                    stats.append("4")
            else:
                i = 0
                for person in people:
                    if person in data:
                        stats.append(str(i))
                    i += 1

        line.lstrip().rstrip("\n")
        line.lstrip().rstrip("\n")

i = 0
prev_i = 0
stats_x = []
tests = [] # test number
accuracies = []
max_accuracy = 0
for value in stats:
    stats_x.append(i)
    if value == "-1":
        tests.append(stats[prev_i:i])
        prev_i = i + 1
    i += 1


print("total tests: " + str(len(tests)))

test_len = len(tests)
x = 0
c = 0
phase = 1
for test in tests:
    avg_r = round(float(test[6]), 2)
    avg_d = round(float(test[5])/float(test[4]) * 100, 2)
    if x % TESTS_NUM == 0:
        c = x
        rec_c= 0
        rec_w = 0
        rec_l = 0
        rec_m = 0
        rec_h = 0
        dec_c = 0
        dec_w = 0
        dec_l = 0
        dec_m = 0
        dec_h = 0
        print("\nPhase " + str(phase) + "\n")
    if x - c < TESTS_NUM:
        if test[7] == "0":
            rec_c += avg_r
            dec_c += avg_d
            #print("cold")
        elif test[7] == "1":
            rec_w += avg_r
            dec_w += avg_d
            #print("warm")
        elif test[7] == "2":
            rec_l += avg_r
            dec_l += avg_d
            #print("low")
        elif test[7] == "3":
            rec_m += avg_r
            dec_m += avg_d
            #print("medium")
        elif test[7] == "4":
            rec_h += avg_r
            dec_h += avg_d
            #print("high")
        #print(str(avg_r) + "\t:\t" + str(avg_d) + "\n")
    if x % TESTS_NUM == TESTS_NUM - 1:
        print("avg r cold: " + str(rec_c / 5) + "\tavg d cold: " + str(dec_c / 5))
        print("avg r warm: " + str(rec_w / 5) + "\tavg d warm: " + str(dec_w / 5))
        print("avg r low: " + str(rec_l / 5) + "\tavg d low: " + str(dec_l / 5))
        print("avg r med: " + str(rec_m / 5) + "\tavg d med: " + str(dec_m / 5))
        print("avg r high: " + str(rec_h / 5) + "\tavg d high: " + str(dec_h / 5))
        c += TESTS_NUM
        phase += 1
    if x + 1 == test_len:
        print("avg r cold: " + str(rec_c / 5) + "\tavg d cold: " + str(dec_c / 5))
        print("avg r warm: " + str(rec_w / 5) + "\tavg d warm: " + str(dec_w / 5))
        print("avg r low: " + str(rec_l / 5) + "\tavg d low: " + str(dec_l / 5))
        print("avg r med: " + str(rec_m / 5) + "\tavg d med: " + str(dec_m / 5))
        print("avg r high: " + str(rec_h / 5) + "\tavg d high: " + str(dec_h / 5))
        print("\nEND")
        break
    x += 1





















