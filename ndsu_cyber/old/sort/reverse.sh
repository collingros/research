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
