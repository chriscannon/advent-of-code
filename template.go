// Day $DAY Advent of Code $YEAR
// https://adventofcode.com/$YEAR/day/$DAY
package main

import (
	"bufio"
	"log"
	"os"
)

func main() {
	input := readInput()
}

func readInput() []string {
	var inputFile *os.File
	if len(os.Args) == 2 {
		var openErr error
		inputFile, openErr = os.Open(os.Args[1])
		if openErr != nil {
			log.Panicln("error opening file: ", openErr)
		}
		defer func() {
			if err := inputFile.Close(); err != nil {
				log.Panicln("error closing file: ", err)
			}
		}()
	} else {
		inputFile = os.Stdin
	}

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
