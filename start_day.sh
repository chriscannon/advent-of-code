#!/bin/bash
if [ -z "$SESSION" ]
then
    echo "Set the \$SESSION environment variable."
    exit 1
fi

YEAR=$1
DAY=$2

if [ $DAY -lt 10 ]; then
    DIR="$YEAR/0$DAY";
else
    DIR="$YEAR/$DAY";
fi

mkdir $DIR
touch $DIR/sample.txt
cat template.go | sed "s/REPLACE_DAY/$DAY/g" | sed "s/REPLACE_YEAR/$YEAR/g" > $DIR/main.go
curl --silent https://adventofcode.com/$YEAR/day/$DAY/input --cookie "session=$SESSION" > $DIR/input.txt

echo "New day initialized under $DIR/"
