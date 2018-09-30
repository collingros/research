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
                rm -r out/opt_$dir_n
                mkdir out/opt_$dir_n

                python3 train.py -s $sf -n $mn -p $res -l 1 -v 1 -o 1 -i 1 \
                -z $casc -g 1 -a 1 -k out/opt_$dir_n \
            done
        done
    done
done
