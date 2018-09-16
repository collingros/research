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
    for pos2 in "x" "a" "o"
    do
        echo "testing pos is $pos2"
        python3 new_faces.py -$pos2 1 -w 1 -c 1 -l 1 -m 1 -b 1 -p $RES -s $SF -n $MN -v 1 # pos 1+5, 2+4, 3
    done
    echo -e "\ntraining\n"
}

for pos in "p" "a" "t"
do
    echo "training pos is $pos"
    python3 new_faces_train.py -$pos 1 -w 1 -c 1 -d 1 -m 1 -b 1 -l $RES -q 2 -v 1 -s $TRSF -n $TRMN # pos 1+5, 2+4, 3
    run_test
done

echo "training pos is p and a" 
python3 new_faces_train.py -a 1 -p 1 -w 1 -c 1 -d 1 -m 1 -b 1 -l $RES -q 2 -v 1 -s $TRSF -n $TRMN # pos 1+5, 2+4
run_test

echo "training pos is a and t" 
python3 new_faces_train.py -a 1 -t 1 -w 1 -c 1 -d 1 -m 1 -b 1 -l $RES -q 2 -v 1 -s $TRSF -n $TRMN # pos 2+4, 3
run_test

echo "training pos is p and t" 
python3 new_faces_train.py -p 1 -t 1 -w 1 -c 1 -d 1 -m 1 -b 1 -l $RES -q 2 -v 1 -s $TRSF -n $TRMN # pos 1+5, 3
run_test

echo "training pos is p, a and t" 
python3 new_faces_train.py -a 1 -p 1 -t 1 -w 1 -c 1 -d 1 -m 1 -b 1 -l $RES -q 2 -v 1 -s $TRSF -n $TRMN # pos 1+5, 2+4, 3
run_test














