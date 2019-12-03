// Day 1 Advent of Code 2019
// https://adventofcode.com/2019/day/1
package main

import (
	"fmt"
	"log"

	"github.com/chriscannon/advent-of-code/common"
)

func main() {
	input, err := common.ReadUint64Slice(nil)
	if err != nil {
		log.Fatalln("failed to read input: ", err)
	}

	var total, totalRecurse uint64
	for i := range input {
		totalRecurse += recurseFuel(input[i])
		total += calculateFuel(input[i])
	}
	fmt.Println("Part 1: ", total)
	fmt.Println("Part 2: ", totalRecurse)
}

func calculateFuel(mass uint64) uint64 {
	fuel := mass / 3

	if fuel < 2 {
		return 0
	}

	return fuel - 2
}

func recurseFuel(mass uint64) uint64 {
	fuel := calculateFuel(mass)
	if fuel == 0 {
		return 0
	}
	return fuel + recurseFuel(fuel)
}
