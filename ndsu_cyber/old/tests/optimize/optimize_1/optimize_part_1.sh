#!/bin/bash
echo "sf and mn test script"

run_test () # run recognition testing
{
    echo -e "\ntests\n"
    for scalef2 in 1.5 1.4 1.3 1.2 1.1
    do
        echo "current sf: $scalef2"
        for minn2 in 5 4 3 2 1
        do
            echo "current mn: $minn2"
            for light2 in "a" "c" "w" "l" "m" "b"
            do
                if [ "$light2" == "a" ]
                then
                    echo "all lighting"
                    python3 new_faces.py -l 1 -m 1 -b 1 -s $scalef2 -n $minn2 -v 1 # all brightness test
                else
                    echo "light setting $light2"
                    python3 new_faces.py -$light2 1 -s $scalef2 -n $minn2 -v 1 # test
                fi
            done
        done
    done
    echo -e "\ntraining\n"
}

# training the recognizer with different settings
# train_sf, train_mn, and train lighting changing, res in different script
# res default (100)
for scalef in 1.5 1.4 1.3 1.2 1.1
do
    echo "current sf: $scalef"
    for minn in 5 4 3 2 1
    do
        echo "current mn: $minn"
        for light in "a" "c" "w" "d" "m" "b"
        do
            if [ "$light" == "a" ]
            then
                echo "all lighting"
                python3 new_faces_train.py -d 1 -m 1 -b 1 -s $scalef -n $minn \
                -v 1 -q 2 -a 1 -t 1 # all brightness training
                # options mean: vanilla, every lighting angle, angled positions
                # and central positions included
            else
                echo "light setting $light"
                python3 new_faces_train.py -$light 1 -s $scalef -n $minn -v 1 \
                -q 2 -a 1 -t 1 # training
                # options mean: vanilla, every lighting angle, angled positions
                # and central positions included
            fi
            run_test
        done
    done
done
