// Day 4 Advent of Code 2019
// https://adventofcode.com/2019/day/4
package main

import (
	"fmt"
	"log"

	"github.com/chriscannon/advent-of-code/common"
)

func main() {
	input, err := common.ReadIntSlice(common.SplitAt('-'))
	if err != nil {
		log.Fatalln("failed to read input: ", err)
	}

	var atLeastTwoTotal, exactlyTwoTotal int
	for i := input[0]; i < input[1]+1; i++ {
		digitCount := make(map[int]int)
		var previousDigit int
		var notIncreasing bool
		for _, digit := range common.GetDigits(i, 6) {
			if digit < previousDigit {
				notIncreasing = true
				break
			}
			digitCount[digit] += 1
			previousDigit = digit
		}

		if notIncreasing {
			continue
		}

		var found, alreadyFoundTwo bool
		for _, count := range digitCount {
			if count == 2 && !alreadyFoundTwo {
				exactlyTwoTotal++
				alreadyFoundTwo = true
			}

			if count >= 2 {
				found = true
				if alreadyFoundTwo {
					break
				}
			}
		}

		if found {
			atLeastTwoTotal++
		}
	}
	fmt.Println("Part 1: ", atLeastTwoTotal)
	fmt.Println("Part 2: ", exactlyTwoTotal)
}
