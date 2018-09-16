#!/bin/bash

# test using all variants of video
run_test ()
{
    for x in "collin_gros" "isaac_burton" "marco_colasito" "nick_snell" "william_clemons"
    do
        python3 c_faces2.py -t $x -c 1
        python3 c_faces2.py -t $x -w 1
        python3 c_faces2.py -t $x -l 1
        python3 c_faces2.py -t $x -m 1
        python3 c_faces2.py -t $x -b 1
    done
}

echo "begin!"
date
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 1 -w 1 -q 2 -p 0 -a 1 -t 1 #MISTAKE!!! DID NOT INCLUDE COLD!!!
echo "phase 3 training finished"
run_test
echo "phase 3 finished"
echo "done!"
date

