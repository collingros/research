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
python3 c_faces_train2.py -e 0 -f 0 -v 1 -w 1 -q 2 -p 0 -a 1 -t 1 #MISTAKE!!! DID NOT INCLUDE COLD!!!
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

echo "done!"
date

