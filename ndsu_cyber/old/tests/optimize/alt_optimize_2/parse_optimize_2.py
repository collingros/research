# for alt optimize_part_2

train = True

train_stat = []
# [75, 'a', 0, 'a', 'a', 'c', 'a', 'w', 'a', 'd', 'a', 'm', 'a']
test_stat = []
changed = False
avg_id = 0
avg_acc = 0
acc_t = 0
id_t = 0
avgs = []
with open("alt_part_2.txt", "r") as f:
    for num, line in enumerate(f, 1):
        split_line = line.split()
        changed = False
        save = False

        if "tests" in line:
            train = False
        elif "training" in line:
            train = True

        if train:
            if "res setting" in line:
                tr_res = split_line[2]
                print("n: "+ str(num) + "\t" + "tr_res setting is: " + tr_res)
                if len(train_stat) >= 1 and tr_res == train_stat[0]:
                    print("same tr_res as before! skipping n: " + str(num))
                    continue
                elif len(train_stat) >= 1:
                    changed = True
                    train_stat[0] = int(tr_res)
                else:
                    changed = True
                    train_stat.append(int(tr_res))
            elif "pos setting" in line and not "subj" in line:
                tr_pos = split_line[2]
                print("n: "+ str(num) + "\t" + "tr_pos setting is: " + tr_pos)
                if len(train_stat) >= 2 and tr_pos == train_stat[1]:
                    print("same tr_pos as before! skipping n: " + str(num))
                    continue
                elif len(train_stat) >= 2:
                    train_stat[1] = tr_pos
                else:
                    train_stat.append(tr_pos)
            elif "lighting position" in line:
                tr_light_pos = split_line[2]
                print("n: "+ str(num) + "\t" + "tr_light pos setting is: " + tr_light_pos)
                if len(train_stat) >= 3 and tr_light_pos == train_stat[2]:
                    print("same tr_light_pos as before! skipping n: " + str(num))
                    continue
                elif len(train_stat) >= 3:
                    train_stat[2] = int(tr_light_pos)
                else:
                    train_stat.append(int(tr_light_pos))
            elif "all lighting" in line:
                tr_light_set = "a"
                print("n: "+ str(num) + "\t" + "tr_light setting is: " + tr_light_set)
                if len(train_stat) >= 4 and tr_light_set == train_stat[3]:
                    print("same tr_light_set as before! skipping n: " + str(num))
                    continue
                elif len(train_stat) >= 4:
                    train_stat[3] = tr_light_set
                else:
                    train_stat.append(tr_light_set)
            elif "light setting" in line:
                tr_light_set = split_line[2]
                print("n: "+ str(num) + "\t" + "tr_light setting is: " + tr_light_set)
                if len(train_stat) >= 4 and tr_light_set == train_stat[3]:
                    print("same tr_light_set as before! skipping n: " + str(num))
                    continue
                elif len(train_stat) >= 4:
                    train_stat[3] = tr_light_set
                else:
                    train_stat.append(tr_light_set)
            elif "including all subj pos" in line:
                tr_sub_pos = "a"
                print("n: "+ str(num) + "\t" + "tr_subject position is: " + tr_sub_pos)
                if len(train_stat) >= 5 and tr_sub_pos == train_stat[4]:
                    print("same tr_sub_pos as before! skipping n: " + str(num))
                    continue
                elif len(train_stat) >= 5:
                    train_stat[4] = tr_sub_pos
                else:
                    train_stat.append(tr_sub_pos)
            elif "subj pos setting" in line:
                tr_sub_pos = split_line[3]
                print("n: "+ str(num) + "\t" + "subj pos setting is " + tr_sub_pos)
                if len(train_stat) >= 5 and tr_sub_pos == train_stat[4]:
                    print("same tr_sub_pos as before! skipping n: " + str(num))
                    continue
                elif len(train_stat) >= 5:
                    train_stat[4] = tr_sub_pos
                else:
                    train_stat.append(tr_sub_pos)
            else:
                print("1 skipped n: " + str(num))
                pass
        else:
            if "res setting" in line:
                res = split_line[2]
                print("n: "+ str(num) + "\t" + "res setting is: " + res)
                if len(test_stat) >= 1 and res == test_stat[0]:
                    print("same res as before! skipping n: " + str(num))
                    continue
                elif len(test_stat) >= 1:
                    #changed = True
                    test_stat[0] = int(res)
                else:
                    #changed = True
                    test_stat.append(int(res))
            elif "all lighting" in line:
                light_set = "a"
                print("n: "+ str(num) + "\t" + "light setting is: " + light_set)
                if len(test_stat) >= 2 and light_set == test_stat[1]:
                    print("same light_set as before! skipping n: " + str(num))
                    continue
                elif len(test_stat) >= 2:
                    test_stat[1] = light_set
                else:
                    test_stat.append(light_set)
            elif "light setting" in line:
                light_set = split_line[2]
                print("n: "+ str(num) + "\t" + "light setting is: " + light_set)
                if len(test_stat) >= 2 and light_set == test_stat[1]:
                    print("same light_set as before! skipping n: " + str(num))
                    continue
                elif len(test_stat) >= 2:
                    test_stat[1] = light_set
                else:
                    test_stat.append(light_set)
            elif "% identified" in line:
                ident = split_line[2]
                print("n: "+ str(num) + "\t" + "identified percentage is: " + ident)
                if len(test_stat) >= 3 and ident == test_stat[2]:
                    print("same ident as before! skipping n: " + str(num))
                    continue
                elif len(test_stat) >= 3:
                    test_stat[2] = float(ident)
                else:
                    test_stat.append(float(ident))
            elif "% accuracy" in line:
                acc = split_line[2]
                print("n: "+ str(num) + "\t" + "accuracy percentage is: " + acc)
                if len(test_stat) >= 4 and acc == test_stat[3]:
                    print("same acc as before! skipping n: " + str(num))
                    continue
                elif len(test_stat) >= 4:
                    save = True
                    test_stat[3] = float(acc)
                else:
                    test_stat.append(float(acc))
                    save = True
            else:
                print("2 skipped n: " + str(num))
                pass
        #print(train_stat)
        print(train_stat)
        print(test_stat)

        if len(test_stat) >= 4:
            # check if settings have changed outside of test
            if not changed and save:
                avg_acc += test_stat[3]
                id_t += 1
                avg_id += test_stat[2]
                acc_t += 1
                print("results recorded!")
            elif changed:
                print("setting changed! averaging results..")
                avg = round(float(avg_acc / acc_t), 2)
                print("acc avg: " + str(avg))
                avgs.append(avg)
                avg = round(float(avg_id / id_t), 2)
                print("id avg: " + str(avg))
                avgs.append(avg)
                avg_acc = 0
                id_t = 0
                avg_id = 0
                acc_t = 0
                avg_acc += test_stat[3]
                id_t += 1
                avg_id += test_stat[2]
                acc_t += 1
                print("new results recorded!")

print("train_stat")
print(train_stat)
print("test_stat")
print(test_stat)
print("averages")
print(avgs)







