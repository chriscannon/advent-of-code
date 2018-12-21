#!/bin/bash
if [ -z "$SESSION" ]
then
    echo "Set the \$SESSION environment variable."
    exit 1
fi

DAY=$1
YEAR=$(date +"%Y")

if [ $DAY -lt 10 ]; then
    DIR="$YEAR/0$DAY";
else
    DIR="$YEAR/$DAY";
fi

mkdir $DIR
touch $DIR/sample.txt
cat template.py | sed "s/REPLACE/$DAY/g" > $DIR/solution.py
curl --silent https://adventofcode.com/$YEAR/day/$DAY/input --cookie "session=$SESSION" > $DIR/input.txt

echo "New day initialized under $DIR/"
