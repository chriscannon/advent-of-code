#!/bin/bash
DAY=$1

if [ $DAY -lt 10 ]; then
    DIR="0$DAY";
else
    DIR=$DAY;
fi

mkdir $DIR
touch $DIR/sample.txt
cat template.py | sed "s/REPLACE/$DAY/g" > $DIR/solution.py

if [ -z "$SESSION" ]
then
    echo "\$SESSION environment variable is not set so the day's input will not be retrieved."
else
    curl --silent https://adventofcode.com/2018/day/$DAY/input --cookie "session=$SESSION" > $DIR/input.txt
fi

echo "New day initialized under $DIR/"
