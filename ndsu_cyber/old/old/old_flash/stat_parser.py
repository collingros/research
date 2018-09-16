stats = {}
with open("stat.txt", "r") as f:
    stats["SF"] = f.readline().split(":")[1].lstrip().rstrip("\n")
    stats["TRAIN_SF"] = f.readline().split(":")[1].lstrip().rstrip("\n")
    stats["MN"] = f.readline().split(":")[1].lstrip().rstrip("\n")
    stats["TRAIN_MN"] = f.readline().split(":")[1].lstrip().rstrip("\n")
    stats["TOTAL_FRAMES"] = f.readline().split(":")[1].lstrip().rstrip("\n")
    stats["DETECTED_FACES"] = f.readline().split(":")[1].lstrip().rstrip("\n")
    stats["ACCURACY"] = f.readline().split(":")[1].lstrip().rstrip("\n")
    stats["VIDEO"] = f.readline().split(":")[1].lstrip().rstrip("\n")
    stats["TARGET"] = f.readline().split(":")[1].lstrip().rstrip("\n")
    stats["HEIGHT"] = f.readline().split(":")[1].lstrip().rstrip("\n")
    stats["RATIO"] = f.readline().split(":")[1].lstrip().rstrip("\n")
    stats["GLASSES"] = f.readline().split(":")[1].lstrip().rstrip("\n")
    stats["HAT"] = f.readline().split(":")[1].lstrip().rstrip("\n")
    stats["VANILLA"] = f.readline().split(":")[1].lstrip().rstrip("\n")
    stats["WARM"] = f.readline().split(":")[1].lstrip().rstrip("\n")
    stats["COLD"] = f.readline().split(":")[1].lstrip().rstrip("\n")
    stats["LOW"] = f.readline().split(":")[1].lstrip().rstrip("\n")
    stats["MED"] = f.readline().split(":")[1].lstrip().rstrip("\n")
    stats["HIGH"] = f.readline().split(":")[1].lstrip().rstrip("\n")
    stats["SHADOWS"] = f.readline().split(":")[1].lstrip().rstrip("\n")
    stats["PROFILES"] = f.readline().split(":")[1].lstrip().rstrip("\n")
    stats["ANGLED"] = f.readline().split(":")[1].lstrip().rstrip("\n")
    stats["CENTER"] = f.readline().split(":")[1].lstrip().rstrip("\n")
    # get rid of "video" line
    f.readline().lstrip().rstrip("\n")
    # empty line between sets
    f.readline().lstrip().rstrip("\n")
    # start new set

for key, value in stats.items():
	print("key: " + key + "\tvalue: " + value)
