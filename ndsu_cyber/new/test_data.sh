#!/bin/bash

# optimize
# train on low
# test on low

dir_n=0
for casc in "lbph_frontal.xml"
do
    for sf in 1.01
    do
        for mn in 1
        do
            for res in 150
            do
                ((dir_n++))
                rm -r test/opt_$dir_n
                mkdir test/opt_$dir_n

                cp out/opt_$dir_n/train.yml test/opt_$dir_n/train.yml
                cp out/opt_$dir_n/labels.pickle test/opt_$dir_n/labels.pickle

                python3 test.py -s $sf -n $mn -p $res -l 1 -v 1 -o 1 -i 1 \
                -z $casc -g 1 -a 1 -k test/opt_$dir_n \
                > ./test/opt_$dir_n/scriptstat.txt
            done
        done
    done
done
