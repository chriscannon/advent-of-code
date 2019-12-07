#!/bin/bash
# Example command: ./start_day.sh 2019 1
set -e
if [ -z "$SESSION" ]
then
    echo "Set the \$SESSION environment variable."
    exit 1
fi

YEAR=$1
DAY=$2
DIR="$YEAR/$(printf "%02d" "$DAY")"

mkdir -p "$DIR"
sed -e "s/\$DAY/$DAY/g" -e "s/\$YEAR/$YEAR/g" template.go > "$DIR/main.go"
curl --fail "https://adventofcode.com/$YEAR/day/$DAY/input" --cookie "session=$SESSION" > "$DIR/input.txt"

echo "New day initialized under $DIR/"
