#!/bin/bash

# optimize
# train on low
# test on low

# FIXME:
# ONLY TESTS ON SAME SETTING TRAINING SET
# ALL RESULTS WILL BE CORRECT

rm -r out2
mkdir out2

for train_dir in "151" "202" "17" "1" "172" "27"
do
    dir_n=0

    mkdir out2/data_$train_dir
    for casc in "lbph_frontal.xml" "haar_default.xml"
    do
        for sf in 1.01 1.05 1.1 1.2 1.3 1.5
        do
            for mn in 1 3 5 7 10
            do
                for res in 150 480 960 1920 3456
                do
                    ((dir_n++))
                    mkdir out2/data_$train_dir/opt_$dir_n

                    cur_dir=out2/data_$train_dir/opt_$dir_n
                    cp out/opt_$train_dir/train.yml $cur_dir/train.yml
                    cp out/opt_$train_dir/labels.pickle $cur_dir/labels.pickle

                    python3 test.py -s $sf -n $mn -p $res -l 1 -v 1 -o 1 -i 1 \
                    -z $casc -g 1 -a 1 -k $cur_dir \
                    > $cur_dir/scriptstat.txt
                done
            done
        done
    done
done
