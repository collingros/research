import os
TRAIN_DIR = "database"

dir_train = os.listdir(TRAIN_DIR)

faces = []
labels = []
p = {}


dir_c = 0

skipped = 0
for dir_name in dir_train:

    label = dir_c
    p[dir_name] = dir_c

    p_types = TRAIN_DIR + "/" + dir_name #picture type directories, vanilla etc.
    p_type_names = os.listdir(p_types)

    for p_type in p_type_names:
        img_c = 0
        p_type_path = p_types + "/" + p_type

        pos_types = p_type_path
        pos_type_names = os.listdir(pos_types)

        for pos_type in pos_type_names:

            pos_type_path = pos_types + "/" + pos_type

            angle_types = pos_type_path
            angle_type_names = os.listdir(angle_types)

            for angle_type in angle_type_names:
                angle_type_path = angle_types + "/" + angle_type

                imgs = angle_type_path
                img_names = os.listdir(imgs)

                for img_name in img_names:
                    img_path = imgs + "/" + img_name

                    #print("directory: " + dir_name)
                    #print("img: " + img)
                    #print("p_type_path: " + img_path)

                    img_c += 1
        print("total imgs for " + dir_name + ": " + str(img_c))
        print(p_type)
    dir_c += 1

print("total people: " + str(dir_c))
print("total imgs: " + str(img_c))


