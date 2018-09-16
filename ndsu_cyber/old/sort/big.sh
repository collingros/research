get_count ()
{
    local x=0
    for i in *.JPG
    do
	    if [ $(($x%5)) == 0 ]
	    then
		    ((angle++))
	    fi
	    ((x++))
    done
    echo $x
}

make_dir ()
{
for i in "vanilla" "hat" "glasses"
do
    mkdir $i
    cd $i
    for l in "pos_0" "pos_1" "pos_2" "pos_3" "pos_4"
        do
        mkdir $l
        cd $l
        for x in "angle_1" "angle_2" "angle_3" "angle_4" "angle_5" "angle_6" "angle_7"
            do
                mkdir $x
            done
        cd ..
        done
    cd ..
done
}

sort_files ()
{
    local x=1
    local angle=1
    for i in *.JPG
    do
	    echo "moving $i to angle_$angle"
	    mv $i ./"angle_$angle"/$i
	    if [ $(($x%5)) == 0 ]
	    then
		    ((angle++))
	    fi
	    ((x++))
    done
}
reverse_files ()
{
    for i in *.JPG
    do
        echo "flopping $i"
        convert $i -flop $i
    done

    local x=1
    local angle=7
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

test=$(get_count)

if [ $test != 315 ]
then
    echo "count is not 315!"
    exit 1
fi
echo "total count is $test"

count=0
for i in *.JPG
do
    if [ $count -lt 105 ]
    then
        mv $i ./vanilla/$i

    elif [ $count -lt 210 ]
    then
        mv $i ./glasses/$i

    elif [ $count -le 315 ]
    then
        mv $i ./hat/$i
    fi
    ((count++))
done

test=0
for d in "glasses" "hat" "vanilla"
do
    count=0
    cd $d
    test=$(get_count)
    if [ $test != 105 ]
    then
        echo "count is not 105!"
        exit 1
    fi

    for i in *.JPG
    do
# ASSUMING THAT PICTURES ARE IN ORDER BY POSITION
        if [ $count -lt 35 ]
        then
            cp $i ./pos_0/$i
            mv $i ./pos_4/$i
        elif [ $count -lt 70 ]
        then
            cp $i ./pos_1/$i
            mv $i ./pos_3/$i

        elif [ $count -le 105 ]
        then
            mv $i ./pos_2/$i
        fi
        ((count++))
    done

    cd ./pos_0
    sort_files
    cd ../pos_1
    sort_files
    cd ../pos_2
    sort_files
    cd ../pos_3
    reverse_files
    cd ../pos_4
    reverse_files
    cd ..

    cd ..
done






