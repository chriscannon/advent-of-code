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
	file := os.Stdin
	if len(os.Args) == 2 {
		var err error
		file, err = os.Open(os.Args[1])
		if err != nil {
			log.Panicln("error opening file: ", err)
		}
		defer func() {
			if err := file.Close(); err != nil {
				log.Panicln("error closing file: ", err)
			}
		}()
	}

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
