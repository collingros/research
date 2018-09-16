#!/bin/bash

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
