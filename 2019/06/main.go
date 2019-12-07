// Day 6 Advent of Code 2019
// https://adventofcode.com/2019/day/6
package main

import (
	"fmt"
	"log"

	"github.com/chriscannon/advent-of-code/common"
)

func main() {
	input, err := common.ReadStringSliceWithFields(")")
	if err != nil {
		log.Fatalln("failed to read input: ", err)
	}

	// Build a reverse tree to COM
	orbits := make(map[string][]string)
	for i := range input {
		orbits[input[i][1]] = append(orbits[input[i][1]], input[i][0])
	}

	var total int
	for object := range orbits {
		total += len(common.RunDFS(orbits, object)) - 1 // don't count the starting object
	}
	fmt.Println("Part 1: ", total)

	// Find all the parents of YOU
	youPath := common.RunDFS(orbits, "YOU")
	// Find all the parents of SAN
	sanPath := common.RunDFS(orbits, "SAN")

	fmt.Println("Part 2: ", shortestPath(youPath, sanPath))
}

// shortestPath finds the common parent of YOU and SAN then totals the steps taken to get there from YOU and SAN.
func shortestPath(youPath, sanPath []string) int {
	for i := range youPath {
		for j := range sanPath {
			if youPath[i] == sanPath[j] {
				return i + j - 2 // don't count the two starting paths
			}
		}
	}
	return -1
}
