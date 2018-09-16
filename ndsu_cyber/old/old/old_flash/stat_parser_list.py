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
people = ["collin_gros", "william_clemons", "demitrius", "isaac_burton",
          "marco_colasito", "nick_snell"]
stats = []
with open("data_2/2pm.txt", "r") as f:
    for line in f:
        #print("new line!")
        if not line.strip():
            #print("end of set, adding -1!")
            stats.append("-1")
            #print("added \"" + data + "\" to the statistics!")
            continue
        if line[0] == ".":
            #print("detected shitty ../ line!")
            continue
        data = line.split(":")[1].lstrip().rstrip("\n")

        try:
            float(data)
            #print("can convert to float!")
            stats.append(data)
            #print("added \"" + data + "\" to the statistics!")
        except:
            if "MP4" in data:
                if "cold" in data:
                    stats.append("0")
                    #print("added \"" + data + "\" to the statistics as 0!")
                elif "warm" in data:
                    stats.append("1")
                    #print("added \"" + data + "\" to the statistics as 1!")
                elif "low" in data:
                    stats.append("2")
                    #print("added \"" + data + "\" to the statistics as 2!")
                elif "med" in data:
                    stats.append("3")
                    #print("added \"" + data + "\" to the statistics as 3!")
                elif "high" in data:
                    stats.append("4")
                    #print("added \"" + data + "\" to the statistics as 4!")
            else:
                i = 0
                for person in people:
                    if person in data:
                        stats.append(str(i))
                        #print("added \"" + data + "\" to the statistics as \"" + str(i) + "\" !")
                    i += 1

        # get rid of "video" line
        line.lstrip().rstrip("\n")
        # empty line between sets
        line.lstrip().rstrip("\n")
        # start new set


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

high_accuracy_tests = []
warm_tests = []
cold_tests = []
low_tests = []
med_tests = []
high_tests = []
vanilla_tests = []
hat_tests = []
glasses_tests = []
shadow_off = []
shadow_on = []
shadow_all = []
profiles_on = []
angles_on = []
center_on = []
i = 0
for test in tests:
    if round(float(test[6]), 2) >= 100 and round(float(test[6]), 2) <= 100:
        accuracies.append(round(float(test[6]), 2))
        high_accuracy_tests.append(i)
    if test[14] == "1":
        warm_tests.append(test)
    if test[15] == "1":
        cold_tests.append(test)
    if test[16] == "1":
        low_tests.append(test)
    if test[17] == "1":
        med_tests.append(test)
    if test[18] == "1":
        high_tests.append(test)
    if test[13] == "1":
        vanilla_tests.append(test)
    if test[12] == "1":
        hat_tests.append(test)
    if test[11] == "1":
        glasses_tests.append(test)
    if test[19] == "0":
        shadow_off.append(test)
    if test[19] == "1":
        shadow_on.append(test)
    if test[19] == "2":
        shadow_all.append(test)
    if test[20] == "1":
        profiles_on.append(test)
    if test[21] == "1":
        angles_on.append(test)
    if test[22] == "1":
        center_on.append(test)
    i += 1
'''
print("len of shadow_off: " + str(len(shadow_off)) +
      "\nlen of shadow_on: " + str(len(shadow_on)) +
      "\nlen of shadow_all: " + str(len(shadow_all)) +
      "\nlen of profiles_on: " + str(len(profiles_on)) +
      "\nlen of angles_on: " + str(len(angles_on)) +
      "\nlen of center_on: " + str(len(center_on)))
'''

i = 0
for value in accuracies:
    print("test: " + str(high_accuracy_tests[i]) + "\taccuracy: " + str(value))
    i += 1

x = 0
for test_num in high_accuracy_tests:
    i = 0
    print("test: " + str(high_accuracy_tests[x]))
    for value in tests[test_num]:
        value = float(value)
        if i == 6:
            print("ACCURACY: " + str(value))
        if i == 7:
            if value == 0:
                print("COLD VIDEO")
            elif value == 1:
                print("WARM VIDEO")
            elif value == 2:
                print("LOW VIDEO")
            elif value == 3:
                print("MED VIDEO")
            elif value == 4:
                print("HIGH VIDEO")
        if i == 8:
            l = 0
            for person in people:
                if l == value:
                    print("TARGET: " + str(person)) 
                l += 1
        if i == 11 and value == 1:
            print("TRAINED GLASSES")
        if i == 12 and value == 1:
            print("TRAINED HAT")
        if i == 13 and value == 1:
            print("TRAINED VANILLA")
        if i == 14 and value == 1:
            print("TRAINED COLD")
        if i == 15 and value == 1:
            print("TRAINED WARM")
        if i == 16 and value == 1:
            print("TRAINED LOW")
        if i == 17 and value == 1:
            print("TRAINED MED")
        if i == 18 and value == 1:
            print("TRAINED HIGH")
        if i == 19 and value == 0:
            print("ONLY CENTRAL LIGHTING ANGLES")
        if i == 19 and value == 1:
            print("ONLY NON-CENTRAL LIGHTING ANGLES")
        if i == 19 and value == 2:
            print("ALL LIGHTING ANGLES")
        if i == 20 and value == 1:
            print("INCLUDED POS PROFILES")
        if i == 21 and value == 1:
            print("INCLUDED POS ANGLES")
        if i == 22 and value == 1:
            print("INCLUDED POS CENTRAL")
        i += 1
    x += 1
average(warm_tests, "warm")
average(cold_tests, "cold")
average(low_tests, "low")
average(med_tests, "med")
average(high_tests, "high")
average(vanilla_tests, "vanilla")
average(glasses_tests, "glasses")
average(hat_tests, "hat")
average(shadow_off, "shadow off")
average(shadow_on, "shadow on")
average(shadow_all, "shadow all")
average(profiles_on, "profiles on")
average(angles_on, "angles on")
average(center_on, "center on")















