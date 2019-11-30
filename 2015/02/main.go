// Day 2 Advent of Code 2015
// https://adventofcode.com/2015/day/2
package main

import (
	"bufio"
	"log"
	"os"
)

func main() {
	input := readInput(os.Args[1])
}

func readInput(fileName string) []string {
	inputFile, err := os.Open(fileName)
	if err != nil {
		log.Panicln("error opening file: ", err)
	}

	defer func(){
		if err := inputFile.Close(); err != nil {
			log.Panicln("error closing file: ", err)
		}
	}()

	var lines []string
	scanner := bufio.NewScanner(inputFile)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		log.Panicln("error reading file: ", err)
	}

	return lines
}
