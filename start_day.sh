#!/bin/bash
DAY=$1

mkdir $1
touch $1/sample.txt
cat template.py | sed "s/REPLACE/$DAY/g" > $1/solution.py

if [ -z "$SESSION" ]
then
    echo "\$SESSION environment variable is not set so the day's input will not be retrieved."
else
    curl --silent https://adventofcode.com/2018/day/$DAY/input --cookie "session=$SESSION" > $1/input.txt
fi

echo "New day initialized under $DAY/"
