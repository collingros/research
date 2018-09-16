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

# DOES WARMTH AFFECT RECOGNITION PERFORMANCE?

# train using vanilla, cold images, all lighting, no profiles,
# angles, and central positions
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 1 -q 2 -p 0 -a 1 -t 1
echo "phase 1 training finished"
run_test
echo "phase 1 finished"
# train using vanilla, warm images, all lighting, no profiles,
# angles, and central positions
python3 c_faces_train2.py -e 0 -f 0 -v 1 -w 1 -q 2 -p 0 -a 1 -t 1
echo "phase 2 training finished"
run_test
echo "phase 2 finished"
# train using vanilla, cold AND warm images, all lighting, no profiles,
# angles, and central positions
python3 c_faces_train2.py -e 0 -f 0 -v 1 -w 1 -q 2 -p 0 -a 1 -t 1
echo "phase 3 training finished"
run_test
echo "phase 3 finished"
# DOES BRIGHTNESS AFFECT RECOGNITION PERFORMANCE?

# train using vanilla, low images, all lighting, no profiles,
# angles, and central positions
python3 c_faces_train2.py -e 0 -f 0 -v 1 -d 1 -q 2 -p 0 -a 1 -t 1
echo "phase 4 training finished"
run_test
echo "phase 4 finished"
# train using vanilla, medium images, all lighting, no profiles,
# angles, and central positions
python3 c_faces_train2.py -e 0 -f 0 -v 1 -m 1 -q 2 -p 0 -a 1 -t 1
echo "phase 5 training finished"
run_test
echo "phase 5 finished"
# train using vanilla, high images, all lighting, no profiles,
# angles, and central positions
python3 c_faces_train2.py -e 0 -f 0 -v 1 -b 1 -q 2 -p 0 -a 1 -t 1
echo "phase 6 training finished"
run_test
echo "phase 6 finished"
# train using vanilla, low, medium, and high images, all lighting,
# no profiles, angles, and central positions
python3 c_faces_train2.py -e 0 -f 0 -v 1 -d 1 -m 1 -b 1 -q 2 -p 0 -a 1 -t 1
echo "phase 7 training finished"
run_test
echo "phase 7 finished"
# train using vanilla, low, medium, and high images, warm, cold, all lighting,
# no profiles, angles, and central positions
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 1 -w 1 -d 1 -m 1 -b 1 -q 2 -p 0 -a 1 -t 1
echo "phase 7.5 training finished"
run_test
echo "phase 7.5 finished"

# DO COSMETICS AFFECT RECOGNITION PERFORMANCE?

# hat only, all brightness and warmth
python3 c_faces_train2.py -e 0 -f 1 -v 0 -w 1 -c 1 -d 1 -m 1 -b 1 -q 2 -p 0 -a 1 -t 1
echo "phase 8 training finished"
run_test
echo "phase 8 finished"
# glasses only, all brightness and warmth
python3 c_faces_train2.py -e 1 -f 0 -v 0 -w 1 -c 1 -d 1 -m 1 -b 1 -q 2 -p 0 -a 1 -t 1
echo "phase 9 training finished"
run_test
echo "phase 9 finished"
# all hat, glasses, face, all brightness and warmth
python3 c_faces_train2.py -e 1 -f 1 -v 1 -w 1 -c 1 -d 1 -m 1 -b 1 -q 2 -p 0 -a 1 -t 1
echo "phase 10 training finished"
run_test
echo "phase 10 finished"

# DO VIEWING ANGLES AFFECT RECOGNITION PERFORMANCE?

# profiles, central, angles, all shadows, vanilla, cold, warm, all brightness
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 1 -w 1 -d 1 -m 1 -b 1 -q 2 -p 1 -a 1 -t 1
echo "phase 11 training finished"
run_test
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
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 1 -w 1 -d 1 -m 1 -b 1 -q 2 -p 0 -a 0 -t 1
echo "phase 16 training finished"
run_test
echo "phase 16 finished"
# central, no shadows, vanilla, cold, warm, all brightness
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 1 -w 1 -d 1 -m 1 -b 1 -q 0 -p 0 -a 0 -t 1
echo "phase 17 training finished"
run_test
echo "phase 17 finished"
# central, only shadows, vanilla, cold, warm, all brightness
python3 c_faces_train2.py -e 0 -f 0 -v 1 -c 1 -w 1 -d 1 -m 1 -b 1 -q 1 -p 0 -a 0 -t 1
echo "phase 18 training finished"
run_test
echo "phase 18 finished"
echo "done!"
date

