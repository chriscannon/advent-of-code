// Day 2 Advent of Code 2019
// https://adventofcode.com/2019/day/2
package main

import (
	"fmt"
	"log"

	"github.com/chriscannon/advent-of-code/common"
)

const part2ExpectedOutput = 19690720

func main() {
	instructions, err := common.ReadUint64Slice(common.SplitAt(','))
	if err != nil {
		log.Fatalln("failed to read input: ", err)
	}

	part1 := exec(instructions, 12, 2)
	fmt.Println("Part 1: ", part1)
	base := exec(instructions, 0, 0)
	nounIncrease := exec(instructions, 1, 0) - base
	verbIncrease := exec(instructions, 0, 1) - base

	noun := (part2ExpectedOutput - base) / nounIncrease
	verb := (part2ExpectedOutput - base - (noun * nounIncrease)) / verbIncrease

	part2 := exec(instructions, noun, verb)
	if part2 != part2ExpectedOutput {
		log.Fatalf("Part 2 actual output %d does not match expected output %d\n", part2, part2ExpectedOutput)
	}
	fmt.Println("Part 2: ", 100*noun+verb)
}

func exec(originalInstructions []uint64, noun, verb uint64) uint64 {
	instructions := make([]uint64, len(originalInstructions))
	copy(instructions, originalInstructions)

	instructions[1] = noun
	instructions[2] = verb
loop:
	for i := 0; i < len(instructions); i += 4 {
		switch instructions[i] {
		case 1:
			instructions[instructions[i+3]] = instructions[instructions[i+1]] + instructions[instructions[i+2]]
		case 2:
			instructions[instructions[i+3]] = instructions[instructions[i+1]] * instructions[instructions[i+2]]
		case 99:
			break loop
		default:
			log.Fatalln("unknown command: ", instructions[i])
		}
	}
	return instructions[0]
}
