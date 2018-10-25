#!/bin/bash


get_count ()
{
    count=0
    for i in *.JPG
    do
        ((count++))
    done
    echo $count
}


reverse ()
{
    for i in *.JPG
    do
        echo "flopping $i"
        convert $i -flop $i
    done

    x=1
    angle=7
    for i in *.JPG
        do
        echo "moving $i to angle_$angle"
        mv $i ./"angle_$angle"/$i
        if [ $(($x%5)) == 0 ]
        then
	        ((angle--))
        fi
        ((x++))
    done
}


reverse_all ()
{
    for j in *
    do
        cd $j
        for i in "vanilla" "hat" "glasses"
        do
            cd $i
            for l in "pos_0" "pos_1" "pos_2" "pos_3" "pos_4"
                do
                cd $l
                for x in "angle_1" "angle_2" "angle_3" "angle_4" "angle_5" "angle_6" "angle_7"
                    do
                        cd $x
                            reverse
                        cd ..
                    done
                cd ..
                done
            cd ..
        cd ..
    done
}

reverse_all







