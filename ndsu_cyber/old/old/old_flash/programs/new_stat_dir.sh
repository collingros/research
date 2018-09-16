#!/bin/bash

# test using all variants of video
run_test ()
{
    for x in "abdul" "brett" "collin_gros" "isaac_burton" "marco_colasito" "michael_gibbons" "nick_snell" "william_clemons"
    do
        python3 c_faces2.py -t $x -c 1 -r "$1"
        python3 c_faces2.py -t $x -w 1 -r "$1"
        python3 c_faces2.py -t $x -l 1 -r "$1"
        python3 c_faces2.py -t $x -m 1 -r "$1"
        python3 c_faces2.py -t $x -b 1 -r "$1"
    done
}

echo "begin!"
date

# DOES WARMTH AFFECT RECOGNITION PERFORMANCE?

# train using vanilla, cold images, all lighting, no profiles,
# angles, and central positions
mkdir vanilla_cold
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 1 -q 2 -p 0 -a 1 -t 1 -r "vanilla_cold"
echo "phase 1 training finished"
run_test "vanilla_cold"
echo "phase 1 finished"
# train using vanilla, warm images, all lighting, no profiles,
# angles, and central positions
mkdir vanilla_warm
python3 c_faces_train2.py -e 0 -f 0 -v 1 -w 1 -q 2 -p 0 -a 1 -t 1 -r "vanilla_warm"
echo "phase 2 training finished"
run_test "vanilla_warm"
echo "phase 2 finished"
# train using vanilla, cold AND warm images, all lighting, no profiles,
# angles, and central positions
mkdir  vanilla_warmth
python3 c_faces_train2.py -e 0 -f 0 -v 1 -w 1 -q 2 -p 0 -a 1 -t 1 -r "vanilla_warmth"
echo "phase 3 training finished"
run_test "vanilla_warmth"
echo "phase 3 finished"
# DOES BRIGHTNESS AFFECT RECOGNITION PERFORMANCE?

# train using vanilla, low images, all lighting, no profiles,
# angles, and central positions
mkdir vanilla_low
python3 c_faces_train2.py -e 0 -f 0 -v 1 -d 1 -q 2 -p 0 -a 1 -t 1 -r "vanilla_low"
echo "phase 4 training finished"
run_test "vanilla_low"
echo "phase 4 finished"
# train using vanilla, medium images, all lighting, no profiles,
# angles, and central positions
mkdir vanilla_med
python3 c_faces_train2.py -e 0 -f 0 -v 1 -m 1 -q 2 -p 0 -a 1 -t 1 -r "vanilla_med"
echo "phase 5 training finished"
run_test
echo "phase 5 finished"
# train using vanilla, high images, all lighting, no profiles,
# angles, and central positions
mkdir vanilla_high
python3 c_faces_train2.py -e 0 -f 0 -v 1 -b 1 -q 2 -p 0 -a 1 -t 1 -r "vanilla_high"
echo "phase 6 training finished"
run_test "vanilla_high"
echo "phase 6 finished"
# train using vanilla, low, medium, and high images, all lighting,
# no profiles, angles, and central positions
mkdir vanilla_brightness
python3 c_faces_train2.py -e 0 -f 0 -v 1 -d 1 -m 1 -b 1 -q 2 -p 0 -a 1 -t 1 -r "vanilla_brightness"
echo "phase 7 training finished"
run_test "vanilla_brightness"
echo "phase 7 finished"
# train using vanilla, low, medium, and high images, warm, cold, all lighting,
# no profiles, angles, and central positions
mkdir vanilla_all
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 1 -w 1 -d 1 -m 1 -b 1 -q 2 -p 0 -a 1 -t 1 -r "vanilla_all"
echo "phase 7.5 training finished"
run_test "vanilla_all"
echo "phase 7.5 finished"

# DO COSMETICS AFFECT RECOGNITION PERFORMANCE?

# hat only, all brightness and warmth
mkdir hat
python3 c_faces_train2.py -e 0 -f 1 -v 0 -w 1 -c 1 -d 1 -m 1 -b 1 -q 2 -p 0 -a 1 -t 1 -r "hat"
echo "phase 8 training finished"
run_test "hat"
echo "phase 8 finished"
# glasses only, all brightness and warmth
mkdir glasses
python3 c_faces_train2.py -e 1 -f 0 -v 0 -w 1 -c 1 -d 1 -m 1 -b 1 -q 2 -p 0 -a 1 -t 1 -r "glasses"
echo "phase 9 training finished"
run_test "glasses"
echo "phase 9 finished"
# all hat, glasses, face, all brightness and warmth
mkdir "cosmetics_vanilla_warmth_brightness"
python3 c_faces_train2.py -e 1 -f 1 -v 1 -w 1 -c 1 -d 1 -m 1 -b 1 -q 2 -p 0 -a 1 -t 1 -r "cosmetics_vanilla_warmth_brightness"
echo "phase 10 training finished"
run_test "cosmetics_vanilla_warmth_brightness"
echo "phase 10 finished"

# DO VIEWING ANGLES AFFECT RECOGNITION PERFORMANCE?

# profiles, central, angles, all shadows, vanilla, cold, warm, all brightness
mkdir "all_pos"
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 1 -w 1 -d 1 -m 1 -b 1 -q 2 -p 1 -a 1 -t 1 -r "all_pos"
echo "phase 11 training finished"
run_test "all_pos"
echo "phase 11 finished"
# profiles, central, all shadows, vanilla, cold, warm, all brightness
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 1 -w 1 -d 1 -m 1 -b 1 -q 2 -p 1 -a 0 -t 1
echo "phase 12 training finished"
run_test
echo "phase 12 finished"
# central, angles, all shadows, vanilla, cold, warm, all brightness
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 1 -w 1 -d 1 -m 1 -b 1 -q 2 -p 0 -a 1 -t 1
echo "phase 13 training finished"
run_test
echo "phase 13 finished"
# central, all shadows, vanilla, cold, warm, all brightness
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 1 -w 1 -d 1 -m 1 -b 1 -q 2 -p 0 -a 0 -t 1
echo "phase 14 training finished"
run_test
echo "phase 14 finished"
# angles, all shadows, vanilla, cold, warm, all brightness
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 1 -w 1 -d 1 -m 1 -b 1 -q 2 -p 0 -a 1 -t 0
echo "phase 15 training finished"
run_test
echo "phase 15 finished"

# DO SHADOWS AFFECT RECOGNITION PERFORMANCE?

# central, all shadows, vanilla, cold, warm, all brightness
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 1 -w 1 -d 1 -m 1 -b 1 -q 2 -p 0 -a 1 -t 0
echo "phase 16 training finished"
run_test
echo "phase 16 finished"

echo "done!"
date

