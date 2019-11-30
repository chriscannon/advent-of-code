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
		l, _ := strconv.Atoi(sides[0])
		w, _ := strconv.Atoi(sides[1])
		h, _ := strconv.Atoi(sides[2])
		wrapping, ribbon := computeArea([]int{l, w, h})
		totalWrapping += wrapping
		totalRibbon += ribbon
	}
	fmt.Printf("Part 1 total square feet of wrapping paper: %d\n", totalWrapping)
	fmt.Printf("Part 2 total feet of ribbon: %d\n", totalRibbon)
}

func computeArea(d []int) (int, int) {
	wrapping := (2 * d[0] * d[1]) + (2 * d[1] * d[2]) + (2 * d[0] * d[2])
	sort.Ints(d)
	wrapping += d[0] * d[1]
	ribbon := (d[0] * 2) + (d[1] * 2) + (d[0] * d[1] * d[2])
	return wrapping, ribbon
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
