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



# profiles
echo "PROFILE TESTS"

# profiles included with angles and central
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 1 -w 1 -q 2 -p 1 -a 1 -t 1 -l 100
echo "PROFILE PHASE 1 TRAINING FINISHED"
run_test 100
echo "PROFILE PHASE 1 FINISHED"

# profiles and angles, central angles excluded
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 1 -w 1 -q 2 -p 1 -a 1 -t 0 -l 100
echo "PROFILE PHASE 3 TRAINING FINISHED"
run_test 100
echo "PROFILE PHASE 3 FINISHED"

# profiles excluded from angles and central
# BASELINE 2: vanilla, cold and warm, no brightness, no profiles, all shadows
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 1 -w 1 -q 2 -p 0 -a 1 -t 1 -l 100
echo "PROFILE PHASE 4 TRAINING FINISHED"
run_test 100
echo "PROFILE PHASE 4 FINISHED"

# angles
echo "ANGLE TESTS"

# angles excluded, compare to BASELINE 2
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 1 -w 1 -q 2 -p 0 -a 0 -t 1 -l 100
echo "ANGLE PHASE 1 TRAINING FINISHED"
run_test 100
echo "ANGLE PHASE 1 FINISHED"

# only angles
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 1 -w 1 -q 2 -p 0 -a 1 -t 0 -l 100
echo "ANGLE PHASE 2 TRAINING FINISHED"
run_test 100
echo "ANGLE PHASE 2 FINISHED"

# beards
echo "BEARD TESTS"

# with beard people, testing with beard people
# for without beard people comparison - compare to BASELINE 2
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 1 -w 1 -q 2 -p 0 -a 1 -t 1 -l -z 1 100
echo "BEARD PHASE 1 TRAINING FINISHED"
run_beards 100
echo "BEARD PHASE 1 FINISHED"

# with beard people, testing without beard people
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 1 -w 1 -q 2 -p 0 -a 1 -t 1 -l -z 1 100
echo "BEARD PHASE 2 TRAINING FINISHED"
run_test 100
echo "BEARD PHASE 2 FINISHED"


# glasses
echo "GLASSES TESTS"

# BASELINE 1 but without Vanilla, and instead with Glasses
python3 c_faces_train2.py -e 1 -f 0 -v 0 -c 1 -w 1 -d 1 -m 1 -b 1 -q 2 -p 0 -a 1 -t 1 -l 100
echo "GLASSES PHASE 1 TRAINING FINISHED"
run_test 100
echo "GLASSES PHASE 1 FINISHED"

# BASELINE 2 but without Vanilla, and instead with Glasses
python3 c_faces_train2.py -e 1 -f 0 -v 0 -c 1 -w 1 -q 2 -p 0 -a 1 -t 1 -l 100
echo "GLASSES PHASE 2 TRAINING FINISHED"
run_test 100
echo "GLASSES PHASE 2 FINISHED"

# BASELINE 1 but with both Vanilla and Glasses
python3 c_faces_train2.py -e 1 -f 0 -v 1 -c 1 -w 1 -d 1 -m 1 -b 1 -q 2 -p 0 -a 1 -t 1 -l 100
echo "GLASSES PHASE 3 TRAINING FINISHED"
run_test 100
echo "GLASSES PHASE 3 FINISHED"

# BASELINE 2 but with both Vanilla and Glasses
python3 c_faces_train2.py -e 1 -f 0 -v 1 -c 1 -w 1 -q 2 -p 0 -a 1 -t 1 -l 100
echo "GLASSES PHASE 3 TRAINING FINISHED"
run_test 100
echo "GLASSES PHASE 3 FINISHED"

# BASELINE 1 but with both Vanilla and Glasses, excluding angles
python3 c_faces_train2.py -e 1 -f 0 -v 1 -c 1 -w 1 -d 1 -m 1 -b 1 -q 2 -p 0 -a 0 -t 1 -l 100
echo "GLASSES PHASE 4 TRAINING FINISHED"
run_test 100
echo "GLASSES PHASE 4 FINISHED"

# hat
echo "HAT TESTS"

# BASELINE 1 but without Vanilla, and instead with Hat
python3 c_faces_train2.py -e 0 -f 1 -v 0 -c 1 -w 1 -d 1 -m 1 -b 1 -q 2 -p 0 -a 1 -t 1 -l 100
echo "HAT PHASE 1 TRAINING FINISHED"
run_test 100
echo "HAT PHASE 1 FINISHED"

# BASELINE 2 but without Vanilla, and instead with Hat
python3 c_faces_train2.py -e 0 -f 1 -v 0 -c 1 -w 1 -q 2 -p 0 -a 1 -t 1 -l 100
echo "HAT PHASE 2 TRAINING FINISHED"
run_test 100
echo "HAT PHASE 2 FINISHED"

# BASELINE 1 but with both Vanilla and Hat
python3 c_faces_train2.py -e 0 -f 1 -v 1 -c 1 -w 1 -d 1 -m 1 -b 1 -q 2 -p 0 -a 1 -t 1 -l 100
echo "HAT PHASE 3 TRAINING FINISHED"
run_test 100
echo "HAT PHASE 3 FINISHED"

# BASELINE 2 but with both Vanilla and Hat
python3 c_faces_train2.py -e 0 -f 1 -v 1 -c 1 -w 1 -q 2 -p 0 -a 1 -t 1 -l 100
echo "HAT PHASE 3 TRAINING FINISHED"
run_test 100
echo "HAT PHASE 3 FINISHED"

# BASELINE 1 but with both Vanilla and Glasses, excluding angles
python3 c_faces_train2.py -e 0 -f 1 -v 1 -c 1 -w 1 -d 1 -m 1 -b 1 -q 2 -p 0 -a 0 -t 1 -l 100
echo "HAT PHASE 4 TRAINING FINISHED"
run_test 100
echo "HAT PHASE 4 FINISHED"

# BASELINE 1 but with Vanilla, Hat and Glasses
python3 c_faces_train2.py -e 1 -f 1 -v 1 -c 1 -w 1 -d 1 -m 1 -b 1 -q 2 -p 0 -a 1 -t 1 -l 100
echo "HAT PHASE 5 TRAINING FINISHED"
run_test 100
echo "HAT PHASE 5 FINISHED"

# BASELINE 2 but with Vanilla, Hat and Glasses
python3 c_faces_train2.py -e 1 -f 1 -v 1 -c 1 -w 1 -q 2 -p 0 -a 1 -t 1 -l 100
echo "HAT PHASE 6 TRAINING FINISHED"
run_test 100
echo "HAT PHASE 6 FINISHED"




echo "done!"
date

