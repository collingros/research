# for alt optimize_part_1

train = True

train_stat = []
# [75, 'a', 0, 'a', 'a', 'c', 'a', 'w', 'a', 'd', 'a', 'm', 'a']
test_stat = []
changed = False
changed2 = False
avg_id = 0
avg_acc = 0
acc_t = 0
id_t = 0
avgs = []
with open("alt_part_1.txt", "r") as f:
    for num, line in enumerate(f, 1):
        split_line = line.split()
        changed = False
        changed2 = False
        save = False

        if "tests" in line:
            train = False
        elif "training" in line:
            train = True

        if num == 207:

            changed = True
        if train:
            if "current sf:" in line:
                tr_sf = split_line[2]
                #print("n: "+ str(num) + "\t" + "tr_sf setting is: " + tr_sf)
                if len(train_stat) >= 1 and tr_sf == train_stat[0]:
                    #print("same tr_sf as before! skipping n: " + str(num))
                    continue
                elif len(train_stat) >= 1:
                    changed = True
                    train_stat[0] = float(tr_sf)
                else:
                    changed = True
                    train_stat.append(float(tr_sf))
            elif "current mn:" in line:
                tr_mn = split_line[2]
                #print("n: "+ str(num) + "\t" + "tr_mn setting is: " + tr_mn)
                if len(train_stat) >= 2 and tr_mn == train_stat[1]:
                    #print("same tr_mn as before! skipping n: " + str(num))
                    continue
                elif len(train_stat) >= 2:
                    changed2 = True
                    train_stat[1] = int(tr_mn)
                else:
                    changed2 = True
                    train_stat.append(int(tr_mn))
            elif "all lighting" in line:
                tr_light_set = "a"
                #print("n: "+ str(num) + "\t" + "tr_light setting is: " + tr_light_set)
                if len(train_stat) >= 3 and tr_light_set == train_stat[2]:
                    #print("same tr_light_set as before! skipping n: " + str(num))
                    continue
                elif len(train_stat) >= 3:
                    train_stat[2] = tr_light_set
                else:
                    train_stat.append(tr_light_set)
            elif "light setting" in line:
                tr_light_set = split_line[2]
                #print("n: "+ str(num) + "\t" + "tr_light setting is: " + tr_light_set)
                if len(train_stat) >= 3 and tr_light_set == train_stat[2]:
                    #print("same tr_light_set as before! skipping n: " + str(num))
                    continue
                elif len(train_stat) >= 3:
                    train_stat[2] = tr_light_set
                else:
                    train_stat.append(tr_light_set)
            else:
                #print("1 skipped n: " + str(num))
                pass
        else:
            if "current sf:" in line:
                sf = split_line[2]
                #print("n: "+ str(num) + "\t" + "sf setting is: " + sf)
                if len(test_stat) >= 1 and sf == test_stat[0]:
                    #print("same sf as before! skipping n: " + str(num))
                    continue
                elif len(test_stat) >= 1:
                    test_stat[0] = float(sf)
                else:
                    test_stat.append(float(tr_sf))
            elif "current mn:" in line:
                mn = split_line[2]
                #print("n: "+ str(num) + "\t" + "mn setting is: " + mn)
                if len(test_stat) >= 2 and mn == test_stat[1]:
                    #print("same mn as before! skipping n: " + str(num))
                    continue
                elif len(test_stat) >= 2:
                    test_stat[1] = int(mn)
                else:
                    test_stat.append(int(mn))
            elif "all lighting" in line:
                light_set = "a"
                #print("n: "+ str(num) + "\t" + "light setting is: " + light_set)
                if len(test_stat) >= 3 and light_set == test_stat[2]:
                    #print("same light_set as before! skipping n: " + str(num))
                    continue
                elif len(test_stat) >= 3:
                    test_stat[2] = light_set
                else:
                    test_stat.append(light_set)
            elif "light setting" in line:
                light_set = split_line[2]
                #print("n: "+ str(num) + "\t" + "light setting is: " + light_set)
                if len(test_stat) >= 3 and light_set == test_stat[2]:
                    #print("same light_set as before! skipping n: " + str(num))
                    continue
                elif len(test_stat) >= 3:
                    test_stat[2] = light_set
                else:
                    test_stat.append(light_set)
            elif "% identified" in line:
                ident = split_line[2]
                #print("n: "+ str(num) + "\t" + "identified percentage is: " + ident)
                if len(test_stat) >= 4 and ident == test_stat[3]:
                    #print("same ident as before! skipping n: " + str(num))
                    continue
                elif len(test_stat) >= 4:
                    test_stat[3] = float(ident)
                else:
                    test_stat.append(float(ident))
            elif "% accuracy" in line:
                acc = split_line[2]
                #print("n: "+ str(num) + "\t" + "accuracy percentage is: " + acc)
                if len(test_stat) >= 5 and acc == test_stat[4]:
                    #print("same acc as before! skipping n: " + str(num))
                    continue
                elif len(test_stat) >= 5:
                    test_stat[4] = float(acc)
                    save = True
                else:
                    test_stat.append(float(acc))
                    save = True
            else:
                #print("2 skipped n: " + str(num))
                pass

        #input()
        if len(test_stat) >= 5:
            # check if settings have changed outside of test
            if not changed and save:
                print("tiny setting changed!")
                print(train_stat)
                print(test_stat)
                print("results recorded!")
            elif changed:
                print("big setting changed! averaging results..")
                print(train_stat)
                print(test_stat)
                print("new results recorded!")
            elif changed2:
                print("small setting changed! averaging results..")
                print(train_stat)
                print(test_stat)
                print("new results recorded!")










