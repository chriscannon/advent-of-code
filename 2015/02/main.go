// Day 2 Advent of Code 2015
// https://adventofcode.com/2015/day/2
// 1589036
package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	input := readInput()
	var totalWrapping, totalRibbon int
	for i := range input {
		sides := strings.Split(input[i], "x")
		l := convertDimension(sides[0])
		w := convertDimension(sides[1])
		h := convertDimension(sides[2])
		wrapping, ribbon := computeWrappingRibbonLength([]int{l, w, h})
		totalWrapping += wrapping
		totalRibbon += ribbon
	}
	fmt.Printf("Part 1 total square feet of wrapping paper: %d\n", totalWrapping)
	fmt.Printf("Part 2 total feet of ribbon: %d\n", totalRibbon)
}

func convertDimension(size string) int {
	dimension, err := strconv.Atoi(size)
	if err != nil {
		log.Fatalf("failed to convert string '%s' to int", size)
	}
	return dimension
}

func computeWrappingRibbonLength(d []int) (int, int) {
	wrapping := (2 * d[0] * d[1]) + (2 * d[1] * d[2]) + (2 * d[0] * d[2])
	sort.Ints(d)
	wrapping += d[0] * d[1]
	ribbon := (d[0] * 2) + (d[1] * 2) + (d[0] * d[1] * d[2])
	return wrapping, ribbon
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
