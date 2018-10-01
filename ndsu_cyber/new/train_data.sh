#!/bin/bash

# optimize
# train on low
# test on low

dir_n=0
for casc in "lbph_frontal.xml" "haar_default.xml"
do
    for sf in 1.01 1.05 1.1 1.2 1.3 1.5
    do
        for mn in 1 3 5 7 10
        do
            for res in 150 480 960 1920 3456
            do
                ((dir_n++))
                rm -r out
                mkdir out
                mkdir out/opt_$dir_n

                python3 train.py -s $sf -n $mn -p $res -l 1 -v 1 -o 1 -i 1 \
                -z $casc -g 1 -a 1 -k out/opt_$dir_n \
                > ./out/opt_$dir_n/scriptstat.txt
            done
        done
    done
done
