#!/bin/bash

# optimize
# train on low
# test on low

# FIXME:
# ONLY TESTS ON SAME SETTING TRAINING SET
# ALL RESULTS WILL BE CORRECT

dir_n=""
for train_dir in "opt_151" "opt_202" "opt_17" "opt_1" "opt_172" "opt_27"
do
    for casc in "lbph_frontal.xml" "haar_default.xml"
    do
        for sf in 1.01 1.05 1.1 1.2 1.3 1.5
        do
            for mn in 1 3 5 7 10
            do
                for res in 150 480 960 1920 3456
                do
                    dir_n=$train_dir
                    rm -r out2
                    mkdir out2
                    mkdir out2/opt_$dir_n

                    cp out/opt_$dir_n/train.yml out2/opt_$dir_n/train.yml
                    cp out/opt_$dir_n/labels.pickle out2/opt_$dir_n/labels.pickle

                    python3 test.py -s $sf -n $mn -p $res -l 1 -v 1 -o 1 -i 1 \
                    -z $casc -g 1 -a 1 -k out2/opt_$dir_n \
                    > ./out2/opt_$dir_n/scriptstat.txt
                done
            done
        done
    done
done
