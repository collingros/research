import matplotlib.pyplot as plt
import decimal
from numpy import array
import numpy as np

def average(test_list, t):
    i = 0
    s = 0
    for test in test_list:
        s += round(float(test[6]), 2)
        i += 1
    try:
        print("number of pictures used: " + str(i) + "\tavg " + t + " accuracy: "
              + str(round((float(s) / i), 2)) + "%")
    except:
        print("number of pictures used: 0\tavg " + t + " accuracy: 0%")
'''
def average2(test_list1, test_list2, t):
    i = 0
    x = 0
    s = 0
    for test1 in test_list1:
        i = 0
        for test2 in test_list2:
            if i == "14"
        x = 0 
'''
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
key: 9	value: HEIGHT (int)
key: 10	value: RATIO (float)
key: 11	value: GLASSES (int)
key: 12	value: HAT (int)
key: 13	value: VANILLA (int)
key: 14	value: WARM (int)
key: 15	value: COLD (int)
key: 16	value: LOW (int)
key: 17	value: MED (int)
key: 18	value: HIGH (int)
key: 19	value: SHADOWS (int)
key: 20	value: PROFILES (int)
key: 21	value: ANGLED (int)
key: 22	value: CENTER (int)
key: 23	value: -1 NEW TEST
'''
people = ["collin_gros", "isaac_burton", "marco_colasito", "nick_snell",
          "william_clemons"]
stats = []
with open("data_2/2pm.txt", "r") as f:
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
x = 0
rec = 0
dec = 0
rec_c= 0
rec_w = 0
rec_l = 0
rec_m = 0
rec_h = 0
for test in tests:
    avg_r = round(float(test[6]), 2)
    avg_d = round(float(test[5])/float(test[4]) * 100, 2)
    if x == 0:
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
        print("BEGIN")
        print("\nPhase 1\nVanilla, Cold, All Lighting Angles, No Profiles, All Angled Positions, Central Positions\n")
    if x < 25:
        if test[7] == "0":
            rec_c += avg_r
            dec_c += avg_d
            print("cold")
        elif test[7] == "1":
            rec_w += avg_r
            dec_w += avg_d
            print("warm")
        elif test[7] == "2":
            rec_l += avg_r
            dec_l += avg_d
            print("low")
        elif test[7] == "3":
            rec_m += avg_r
            dec_m += avg_d
            print("medium")
        elif test[7] == "4":
            rec_h += avg_r
            dec_h += avg_d
            print("high")
        print(str(avg_r) + "\t:\t" + str(avg_d))
    if x == 25:
        print("avg r cold: " + str(rec_c / 5) + "\tavg d cold: " + str(dec_c / 5))
        print("avg r warm: " + str(rec_w / 5) + "\tavg d warm: " + str(dec_w / 5))
        print("avg r low: " + str(rec_l / 5) + "\tavg d low: " + str(dec_l / 5))
        print("avg r med: " + str(rec_m / 5) + "\tavg d med: " + str(dec_m / 5))
        print("avg r high: " + str(rec_h / 5) + "\tavg d high: " + str(dec_h / 5))
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
        print("\nPhase 2\nVanilla, Warm, All Lighting Angles, No Profiles, All Angled Positions, Central Positions\n")
    if x >= 25 and x < 50:
        if test[7] == "0":
            rec_c += avg_r
            dec_c += avg_d
            print("cold")
        elif test[7] == "1":
            rec_w += avg_r
            dec_w += avg_d
            print("warm")
        elif test[7] == "2":
            rec_l += avg_r
            dec_l += avg_d
            print("low")
        elif test[7] == "3":
            rec_m += avg_r
            dec_m += avg_d
            print("medium")
        elif test[7] == "4":
            rec_h += avg_r
            dec_h += avg_d
            print("high")
        print(str(avg_r) + "\t:\t" + str(avg_d))
    if x == 50:
        print("avg r cold: " + str(rec_c / 5) + "\tavg d cold: " + str(dec_c / 5))
        print("avg r warm: " + str(rec_w / 5) + "\tavg d warm: " + str(dec_w / 5))
        print("avg r low: " + str(rec_l / 5) + "\tavg d low: " + str(dec_l / 5))
        print("avg r med: " + str(rec_m / 5) + "\tavg d med: " + str(dec_m / 5))
        print("avg r high: " + str(rec_h / 5) + "\tavg d high: " + str(dec_h / 5))
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
        print("\nPhase 3\nVanilla, Cold and Warm, All Lighting Angles, No Profiles, All Angled Positions, Central Positions\n")
    if x >= 50 and x < 75:
        if test[7] == "0":
            rec_c += avg_r
            dec_c += avg_d
            print("cold")
        elif test[7] == "1":
            rec_w += avg_r
            dec_w += avg_d
            print("warm")
        elif test[7] == "2":
            rec_l += avg_r
            dec_l += avg_d
            print("low")
        elif test[7] == "3":
            rec_m += avg_r
            dec_m += avg_d
            print("medium")
        elif test[7] == "4":
            rec_h += avg_r
            dec_h += avg_d
            print("high")
        print(str(avg_r) + "\t:\t" + str(avg_d))
    if x == 75:
        print("avg r cold: " + str(rec_c / 5) + "\tavg d cold: " + str(dec_c / 5))
        print("avg r warm: " + str(rec_w / 5) + "\tavg d warm: " + str(dec_w / 5))
        print("avg r low: " + str(rec_l / 5) + "\tavg d low: " + str(dec_l / 5))
        print("avg r med: " + str(rec_m / 5) + "\tavg d med: " + str(dec_m / 5))
        print("avg r high: " + str(rec_h / 5) + "\tavg d high: " + str(dec_h / 5))
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
        print("\nPhase 4\nVanilla, Low Brightness, All Lighting Angles, No Profiles, All Angled Positions, Central Positions\n")
    if x >= 75 and x < 100:
        if test[7] == "0":
            rec_c += avg_r
            dec_c += avg_d
            print("cold")
        elif test[7] == "1":
            rec_w += avg_r
            dec_w += avg_d
            print("warm")
        elif test[7] == "2":
            rec_l += avg_r
            dec_l += avg_d
            print("low")
        elif test[7] == "3":
            rec_m += avg_r
            dec_m += avg_d
            print("medium")
        elif test[7] == "4":
            rec_h += avg_r
            dec_h += avg_d
            print("high")
        print(str(avg_r) + "\t:\t" + str(avg_d))
    if x == 100:
        print("avg r cold: " + str(rec_c / 5) + "\tavg d cold: " + str(dec_c / 5))
        print("avg r warm: " + str(rec_w / 5) + "\tavg d warm: " + str(dec_w / 5))
        print("avg r low: " + str(rec_l / 5) + "\tavg d low: " + str(dec_l / 5))
        print("avg r med: " + str(rec_m / 5) + "\tavg d med: " + str(dec_m / 5))
        print("avg r high: " + str(rec_h / 5) + "\tavg d high: " + str(dec_h / 5))
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
        print("\nPhase 5\nVanilla, Medium Brightness, All Lighting Angles, No Profiles, All Angled Positions, Central Positions\n")
    if x >= 100 and x < 125:
        if test[7] == "0":
            rec_c += avg_r
            dec_c += avg_d
            print("cold")
        elif test[7] == "1":
            rec_w += avg_r
            dec_w += avg_d
            print("warm")
        elif test[7] == "2":
            rec_l += avg_r
            dec_l += avg_d
            print("low")
        elif test[7] == "3":
            rec_m += avg_r
            dec_m += avg_d
            print("medium")
        elif test[7] == "4":
            rec_h += avg_r
            dec_h += avg_d
            print("high")
        print(str(avg_r) + "\t:\t" + str(avg_d))
    if x == 125:
        print("avg r cold: " + str(rec_c / 5) + "\tavg d cold: " + str(dec_c / 5))
        print("avg r warm: " + str(rec_w / 5) + "\tavg d warm: " + str(dec_w / 5))
        print("avg r low: " + str(rec_l / 5) + "\tavg d low: " + str(dec_l / 5))
        print("avg r med: " + str(rec_m / 5) + "\tavg d med: " + str(dec_m / 5))
        print("avg r high: " + str(rec_h / 5) + "\tavg d high: " + str(dec_h / 5))
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
        print("\nPhase 6\nVanilla, High Brightness, All Lighting Angles, No Profiles, All Angled Positions, Central Positions\n")
    if x >= 125 and x < 150:
        if test[7] == "0":
            rec_c += avg_r
            dec_c += avg_d
            print("cold")
        elif test[7] == "1":
            rec_w += avg_r
            dec_w += avg_d
            print("warm")
        elif test[7] == "2":
            rec_l += avg_r
            dec_l += avg_d
            print("low")
        elif test[7] == "3":
            rec_m += avg_r
            dec_m += avg_d
            print("medium")
        elif test[7] == "4":
            rec_h += avg_r
            dec_h += avg_d
            print("high")
        print(str(avg_r) + "\t:\t" + str(avg_d))
    if x == 150:
        print("avg r cold: " + str(rec_c / 5) + "\tavg d cold: " + str(dec_c / 5))
        print("avg r warm: " + str(rec_w / 5) + "\tavg d warm: " + str(dec_w / 5))
        print("avg r low: " + str(rec_l / 5) + "\tavg d low: " + str(dec_l / 5))
        print("avg r med: " + str(rec_m / 5) + "\tavg d med: " + str(dec_m / 5))
        print("avg r high: " + str(rec_h / 5) + "\tavg d high: " + str(dec_h / 5))
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
        print("\nPhase 7\nVanilla, Low, Medium, and High Brightness, All Lighting Angles, No Profiles, All Angled Positions, Central Positions\n")
    if x >= 150 and x < 175:
        if test[7] == "0":
            rec_c += avg_r
            dec_c += avg_d
            print("cold")
        elif test[7] == "1":
            rec_w += avg_r
            dec_w += avg_d
            print("warm")
        elif test[7] == "2":
            rec_l += avg_r
            dec_l += avg_d
            print("low")
        elif test[7] == "3":
            rec_m += avg_r
            dec_m += avg_d
            print("medium")
        elif test[7] == "4":
            rec_h += avg_r
            dec_h += avg_d
            print("high")
        print(str(avg_r) + "\t:\t" + str(avg_d))
    if x == 175:
        print("avg r cold: " + str(rec_c / 5) + "\tavg d cold: " + str(dec_c / 5))
        print("avg r warm: " + str(rec_w / 5) + "\tavg d warm: " + str(dec_w / 5))
        print("avg r low: " + str(rec_l / 5) + "\tavg d low: " + str(dec_l / 5))
        print("avg r med: " + str(rec_m / 5) + "\tavg d med: " + str(dec_m / 5))
        print("avg r high: " + str(rec_h / 5) + "\tavg d high: " + str(dec_h / 5))
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
        print("\nPhase 8\nVanilla, Low, Medium, and High Brightness, Warm, Cold, All Lighting Angles, No Profiles, All Angled Positions, Central Positions\n")
    if x >= 175 and x < 200:
        if test[7] == "0":
            rec_c += avg_r
            dec_c += avg_d
            print("cold")
        elif test[7] == "1":
            rec_w += avg_r
            dec_w += avg_d
            print("warm")
        elif test[7] == "2":
            rec_l += avg_r
            dec_l += avg_d
            print("low")
        elif test[7] == "3":
            rec_m += avg_r
            dec_m += avg_d
            print("medium")
        elif test[7] == "4":
            rec_h += avg_r
            dec_h += avg_d
            print("high")
        print(str(avg_r) + "\t:\t" + str(avg_d))
    if x == 200:
        print("avg r cold: " + str(rec_c / 5) + "\tavg d cold: " + str(dec_c / 5))
        print("avg r warm: " + str(rec_w / 5) + "\tavg d warm: " + str(dec_w / 5))
        print("avg r low: " + str(rec_l / 5) + "\tavg d low: " + str(dec_l / 5))
        print("avg r med: " + str(rec_m / 5) + "\tavg d med: " + str(dec_m / 5))
        print("avg r high: " + str(rec_h / 5) + "\tavg d high: " + str(dec_h / 5))
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
        print("\nPhase 9\nHat, Low, Medium, and High Brightness, Warm, Cold, All Lighting Angles, No Profiles, All Angled Positions, Central Positions\n")
    if x >= 200 and x < 225:
        if test[7] == "0":
            rec_c += avg_r
            dec_c += avg_d
            print("cold")
        elif test[7] == "1":
            rec_w += avg_r
            dec_w += avg_d
            print("warm")
        elif test[7] == "2":
            rec_l += avg_r
            dec_l += avg_d
            print("low")
        elif test[7] == "3":
            rec_m += avg_r
            dec_m += avg_d
            print("medium")
        elif test[7] == "4":
            rec_h += avg_r
            dec_h += avg_d
            print("high")
        print(str(avg_r) + "\t:\t" + str(avg_d))
    if x == 225:
        print("avg r cold: " + str(rec_c / 5) + "\tavg d cold: " + str(dec_c / 5))
        print("avg r warm: " + str(rec_w / 5) + "\tavg d warm: " + str(dec_w / 5))
        print("avg r low: " + str(rec_l / 5) + "\tavg d low: " + str(dec_l / 5))
        print("avg r med: " + str(rec_m / 5) + "\tavg d med: " + str(dec_m / 5))
        print("avg r high: " + str(rec_h / 5) + "\tavg d high: " + str(dec_h / 5))
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
        print("\nPhase 10\nGlasses, Low, Medium, and High Brightness, Warm, Cold, All Lighting Angles, No Profiles, All Angled Positions, Central Positions\n")
    if x >= 225 and x < 250:
        if test[7] == "0":
            rec_c += avg_r
            dec_c += avg_d
            print("cold")
        elif test[7] == "1":
            rec_w += avg_r
            dec_w += avg_d
            print("warm")
        elif test[7] == "2":
            rec_l += avg_r
            dec_l += avg_d
            print("low")
        elif test[7] == "3":
            rec_m += avg_r
            dec_m += avg_d
            print("medium")
        elif test[7] == "4":
            rec_h += avg_r
            dec_h += avg_d
            print("high")
        print(str(avg_r) + "\t:\t" + str(avg_d))
    if x == 250:
        print("avg r cold: " + str(rec_c / 5) + "\tavg d cold: " + str(dec_c / 5))
        print("avg r warm: " + str(rec_w / 5) + "\tavg d warm: " + str(dec_w / 5))
        print("avg r low: " + str(rec_l / 5) + "\tavg d low: " + str(dec_l / 5))
        print("avg r med: " + str(rec_m / 5) + "\tavg d med: " + str(dec_m / 5))
        print("avg r high: " + str(rec_h / 5) + "\tavg d high: " + str(dec_h / 5))
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
        print("END")
        x += 1
        break
    x += 1





















