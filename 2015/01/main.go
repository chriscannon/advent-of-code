// Day 1 Advent of Code 2015
package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	input := readInput(os.Args[1])

	var floor, basementPosition int
	var foundBasement bool
	for i, r := range input[0] {
		switch r {
		case '(':
			floor++
		case ')':
			floor--
		}

		if !foundBasement && floor == -1 {
			basementPosition = i + 1
			foundBasement = true
		}
	}
	fmt.Printf("Part 1 floor: %d\n", floor)
	fmt.Printf("Part 2 first basement position: %d\n", basementPosition)
}

func readInput(fileName string) []string {
	file, fileErr := os.Open(fileName)
	if fileErr != nil {
		log.Panicln("error opening file: ", fileErr)
	}

	defer func() {
		if err := file.Close(); err != nil {
			log.Panicln("error closing file: ", err)
		}
	}()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		log.Panicln("error reading file: ", err)
	}

	return lines
}
