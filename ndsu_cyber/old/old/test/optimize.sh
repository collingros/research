#!/bin/bash
run_tests_norm ()
{
    echo "norm test"
    python3 new_faces.py -l 1 -m 1 -b 1 -p $1 -s $2 -n $3 # test on 'normal' lighting settings
}

run_tests_light ()
{
    echo "light tests"
    for i in "c" "w" "l" "m" "b"
    do
        echo "light setting is $i"
        python3 new_faces.py -$i 1 -p $1 -s $2 -n $3 # test on cold

    done
}

run_tests_res()
{
    echo "res tests"
    for i in 75 100 150 200 300 500 # different resolutions
    do
        echo "res is $i"
        run_tests_norm $i $1 $2
        run_tests_light $i $1 $2
    done
}

run_tests_sf()
{
    echo "scale factor tests"
    for i in 1.5 1.4 1.3 1.2 1.1
    do
        run_tests_res $i $1
    done
}

run_tests_mn()
{
    echo "min neighbors tests"
    for i in 5 4 3 2 1
    do
        run_tests_mn $i
    done
}

train_light ()
{
    echo "light train"
    for i in "c" "w" "l" "m" "b"
    do
        echo "light setting is $i"
        python3 c_faces_train2.py -$i 1 -p $1 -s $2 -n $3 # test on cold

    done
}

train_angle ()
{
    # for training options
}

train_pos ()
{
    # for training options
}

train_res ()
{
    echo "res train"
    for i in 75 100 150 200 300 500 # different resolutions
    do
        echo "res is $i"
        train_sf $i $1 $2
    done
}

train_sf ()
{
    echo "sf train"
    for i in 1.5 1.4 1.3 1.2 1.1 # different resolutions
    do
        echo "sf is $i"
        train_sf $i $1
    done
}

train_mn ()
{
    echo "mn train"
    for i in 5 4 3 2 1 # different resolutions
    do
        echo "mn is $i"
        train_sf $i
    done
}


# testing layout
#        python3 new_faces.py -w 1 -p $1 # test on warm
#        python3 new_faces.py -l 1 -p $1 # test on low
#        python3 new_faces.py -m 1 -p $1 # test on medium
#        python3 new_faces.py -b 1 -p $1 # test on high
# half trained half not trained
# use normal images
# get %identification %correct

