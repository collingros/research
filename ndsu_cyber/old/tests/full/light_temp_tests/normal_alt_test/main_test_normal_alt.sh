#!/bin/bash
echo "main test script"
RES=100
TRSF=1.1
TRMN=4
SF=1.3
MN=4

run_test () # run recognition testing
{
    echo -e "\ntests\n"
    for cosmetic in "e" "f"
    do
        echo "cosmetic setting $cosmetic"
        for temp2 in "c" "w" "l" "m" "b"
        do
            echo "light setting $temp2"
            python3 new_faces.py -$temp2 1 -p $RES -s $SF -n $MN -$cosmetic 1
        done
    done
    echo -e "\ntraining\n"
}

for temp in "w" "c" "d" "m" "b"
do
    echo "training on $temp"
    python3 new_faces_train.py -$temp 1 -l $RES -a 1 -p 1 -t 1 -q 2 -v 1 -s $TRSF -n $TRMN #w c l m h
    run_test
done

echo "training on w+c"
python3 new_faces_train.py -w 1 -c 1 -l $RES -a 1 -p 1 -t 1 -q 2 -v 1 # w + c
run_test
echo "training on l+m+h"
python3 new_faces_train.py -d 1 -m 1 -b 1 -l $RES -a 1 -p 1 -t 1 -q 2 -v 1 -s $TRSF -n $TRMN # l + m + h
run_test






