#!/bin/bash
# Example command: ./go_run.sh 2019 2
DIR="$1/$(printf "%02d" "$2")"
go run $DIR/main.go $DIR/input.txt
