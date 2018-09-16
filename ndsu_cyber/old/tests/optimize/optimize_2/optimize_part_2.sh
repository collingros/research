#!/bin/bash
echo "res test script"

run_test () # run recognition testing
{
    echo -e "\ntests\n"
    for res2 in 75 100 150 200 300 500
    do
        echo "res setting $res2"
        for light2 in "a" "c" "w" "l" "m" "b"
        do
            if [ "$light2" == "a" ]
            then
                echo "all lighting"
                python3 new_faces.py -l 1 -m 1 -b 1 -p $res2 -v 1
                # all brightness test
                # options mean: vanilla, every lighting angle, angled positions
                # and central positions included
            else
                echo "light setting $light2"
                python3 new_faces.py -$light2 1 -p $res2 -v 1
                # options mean: vanilla, every lighting angle, angled positions
                # and central positions included
            fi
        done
    done
    echo -e "\ntraining\n"
}

# training the recognizer with different settings
# testing res against different lightings and positions
# res default (100)
for res in 75 100 150 200 300 500
do
    echo "res setting $res"
    for pos in "a" "p" "a" "t"
    do
        echo "pos setting $pos"
        for lpos in "0" "1" "2"
        do
            echo "lighting position $lpos"
            for light in "a" "c" "w" "d" "m" "b"
            do
                if [ "$light" == "a" ]
                then
                    echo "all lighting"
                    if [ "$pos" == "a" ]
                    then
                        echo "including all subj pos"
                        python3 new_faces_train.py -d 1 -m 1 -b 1 -l $res -a 1 \
                        -p 1 -t 1 -q $lpos -v 1
                    else
                        echo "subj pos setting $pos"
                        python3 new_faces_train.py -d 1 -m 1 -b 1 -l $res \
                        -$pos 1 -q $lpos -v 1 
                    fi
                    # all brightness training
                    # options mean: vanilla, every lighting angle, angled positions
                    # and central positions included
                else
                    echo "light setting $light"
                    if [ "$pos" == "a" ]
                    then
                        echo "including all subj pos"
                        python3 new_faces_train.py -$light 1 -l $res -a 1 -p 1 \
                        -t 1 -q $lpos -v 1 # training
                    else
                        echo "subj pos setting $pos"
                        python3 new_faces_train.py -$light 1 -l $res -$pos 1 \
                        -q $lpos -v 1 # training
                    fi
                    # options mean: vanilla, every lighting angle, angled positions
                    # and central positions included
                fi
                run_test
            done
        done
    done
done
