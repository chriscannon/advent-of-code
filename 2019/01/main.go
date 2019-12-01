// Day 1 Advent of Code 2019
// https://adventofcode.com/2019/day/1
package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	input := readInput()
	var total, totalRecurse int
	for i := range input {
		mass, err := strconv.Atoi(input[i])

		if err != nil {
			log.Fatalf("failed to convert '%s' to int: %v", input[i], err)
		}

		totalRecurse += recurseFuel(mass)
		total += calculateFuel(mass)
	}
	fmt.Printf("Part 1 total fuel: %d\n", total)
	fmt.Printf("Part 2 total fuel recursive: %d\n", totalRecurse)
}

func calculateFuel(mass int) int {
	return (mass / 3) - 2
}

func recurseFuel(mass int) int {
	fuel := calculateFuel(mass)
	if fuel <= 0 {
		return 0
	}
	return fuel + recurseFuel(fuel)
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
