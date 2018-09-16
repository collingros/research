#!/bin/bash

# BASELINE 1: vanilla, cold and warm, all brightness, no profiles, all shadows
# BASELINE 2: vanilla, cold and warm, no brightness, no profiles, all shadows
# test using all variants of video
run_test ()
{
    for x in "collin_gros" "isaac_burton" "marco_colasito" "nick_snell" "william_clemons" "demitrius"
    do
        python3 c_faces2.py -t $x -c 1 -p $1
        python3 c_faces2.py -t $x -w 1 -p $1
        python3 c_faces2.py -t $x -l 1 -p $1
        python3 c_faces2.py -t $x -m 1 -p $1
        python3 c_faces2.py -t $x -b 1 -p $1
    done
}

run_beards ()
{
    for x in "collin_gros" "isaac_burton" "marco_colasito" "nick_snell" "william_clemons" "demitrius" "abdul" "brett"
    do
        python3 c_faces2.py -t $x -c 1 -p $1
        python3 c_faces2.py -t $x -w 1 -p $1
        python3 c_faces2.py -t $x -l 1 -p $1
        python3 c_faces2.py -t $x -m 1 -p $1
        python3 c_faces2.py -t $x -b 1 -p $1
    done
}

echo "begin!"
date
# different resolutions

echo "RESOLUTION TESTS"
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 1 -w 1 -d 1 -m 1 -b 1 -q 2 -p 0 -a 1 -t 1 -l 50
echo "RESOLUTION PHASE 1 TRAINING FINISHED"
run_test 50
echo "RESOLUTION PHASE 1 FINISHED"

# BASELINE 1: vanilla, cold and warm, all brightness, no profiles, all shadows
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 1 -w 1 -d 1 -m 1 -b 1 -q 2 -p 0 -a 1 -t 1 -l 100
echo "RESOLUTION PHASE 2 TRAINING FINISHED"
run_test 100
echo "RESOLUTION PHASE 2 FINISHED"

python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 1 -w 1 -d 1 -m 1 -b 1 -q 2 -p 0 -a 1 -t 1 -l 200
echo "RESOLUTION PHASE 3 TRAINING FINISHED"
run_test 200
echo "RESOLUTION PHASE 3 FINISHED"

python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 1 -w 1 -d 1 -m 1 -b 1 -q 2 -p 0 -a 1 -t 1 -l 300
echo "RESOLUTION PHASE 4 TRAINING FINISHED"
run_test 300
echo "RESOLUTION PHASE 4 FINISHED"

python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 1 -w 1 -d 1 -m 1 -b 1 -q 2 -p 0 -a 1 -t 1 -l 600
echo "RESOLUTION PHASE 5 TRAINING FINISHED"
run_test 600
echo "RESOLUTION PHASE 5 FINISHED"


# shadows

# BASELINE 1 without Shadows
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 1 -w 1 -d 1 -m 1 -b 1 -q 0 -p 0 -a 1 -t 1 -l 100
echo "SHADOWS PHASE 1 TRAINING FINISHED"
run_test 100
echo "SHADOWS PHASE 1 FINISHED"

# BASELINE 1 with Shadows only
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 1 -w 1 -d 1 -m 1 -b 1 -q 1 -p 0 -a 1 -t 1 -l 100
echo "SHADOWS PHASE 2 TRAINING FINISHED"
run_test 100
echo "SHADOWS PHASE 2 FINISHED"

# warmth

# BASELINE 1 without Warm or Brightness
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 1 -w 0 -d 0 -m 0 -b 0 -q 2 -p 0 -a 1 -t 1 -l 100
echo "WARMTH PHASE 1 TRAINING FINISHED"
run_test 100
echo "WARMTH PHASE 1 FINISHED"

# BASELINE 1 without Cold or Brightness
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 0 -w 1 -d 0 -m 0 -b 0 -q 2 -p 0 -a 1 -t 1 -l 100
echo "WARMTH PHASE 2 TRAINING FINISHED"
run_test 100
echo "WARMTH PHASE 2 FINISHED"

# BASELINE 1 without Warmth and Low
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 0 -w 0 -d 1 -m 0 -b 0 -q 2 -p 0 -a 1 -t 1 -l 100
echo "WARMTH PHASE 3 TRAINING FINISHED"
run_test 100
echo "WARMTH PHASE 3 FINISHED"

# BASELINE 1 without Warmth and Med
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 0 -w 0 -d 0 -m 1 -b 0 -q 2 -p 0 -a 1 -t 1 -l 100
echo "WARMTH PHASE 4 TRAINING FINISHED"
run_test 100
echo "WARMTH PHASE 4 FINISHED"

# BASELINE 1 without Warmth and High
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 0 -w 0 -d 0 -m 0 -b 1 -q 2 -p 0 -a 1 -t 1 -l 100
echo "WARMTH PHASE 5 TRAINING FINISHED"
run_test 100
echo "WARMTH PHASE 5 FINISHED"

# BASELINE 1 without Warmth and all Brightness
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 0 -w 0 -d 1 -m 1 -b 1 -q 2 -p 0 -a 1 -t 1 -l 100
echo "WARMTH PHASE 6 TRAINING FINISHED"
run_test 100
echo "WARMTH PHASE 6 FINISHED"






echo "done!"
date

