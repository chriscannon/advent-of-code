// Day 5 Advent of Code 2019
// https://adventofcode.com/2019/day/5
package main

import (
	"fmt"
	"log"
	"strconv"

	"github.com/chriscannon/advent-of-code/common"
)

func main() {
	instructions, err := common.ReadIntSlice(common.SplitAt(','))
	if err != nil {
		log.Fatalln("failed to read input: ", err)
	}

	part1 := exec(instructions, 1)
	fmt.Println("Part 1: ", part1)
	part2 := exec(instructions, 5)
	fmt.Println("Part 2: ", part2)
}

func exec(originalInstructions []int, input int) int {
	instructions := make([]int, len(originalInstructions))
	copy(instructions, originalInstructions)

	var ip, output int
loop:
	for {
		n := len(strconv.Itoa(instructions[ip]))
		digits := common.GetDigits(instructions[ip], n)
		opcode := digits[n-1]

		if len(digits) >= 2 {
			opcode = (digits[n-2] * 10) + opcode
		}

		var param1Mode, param2Mode bool
		switch n {
		case 4:
			param2Mode = common.Itob(digits[0])
			param1Mode = common.Itob(digits[1])
		case 3:
			param1Mode = common.Itob(digits[0])
		}

		if n > 4 {
			log.Fatalln("n is greater than 4: ", n)
		}

		switch opcode {
		case 1:
			instructions[instructions[ip+3]] = getValueOrLiteral(instructions, param1Mode, ip+1) + getValueOrLiteral(instructions, param2Mode, ip+2)
			ip += 4
		case 2:
			instructions[instructions[ip+3]] = getValueOrLiteral(instructions, param1Mode, ip+1) * getValueOrLiteral(instructions, param2Mode, ip+2)
			ip += 4
		case 3:
			instructions[instructions[ip+1]] = input
			ip += 2
		case 4:
			output = getValueOrLiteral(instructions, param1Mode, ip+1)
			ip += 2
		case 5:
			if getValueOrLiteral(instructions, param1Mode, ip+1) != 0 {
				ip = getValueOrLiteral(instructions, param2Mode, ip+2)
			} else {
				ip += 3
			}
		case 6:
			if getValueOrLiteral(instructions, param1Mode, ip+1) == 0 {
				ip = getValueOrLiteral(instructions, param2Mode, ip+2)
			} else {
				ip += 3
			}
		case 7:
			if getValueOrLiteral(instructions, param1Mode, ip+1) < getValueOrLiteral(instructions, param2Mode, ip+2) {
				instructions[instructions[ip+3]] = 1
			} else {
				instructions[instructions[ip+3]] = 0
			}
			ip += 4
		case 8:
			if getValueOrLiteral(instructions, param1Mode, ip+1) == getValueOrLiteral(instructions, param2Mode, ip+2) {
				instructions[instructions[ip+3]] = 1
			} else {
				instructions[instructions[ip+3]] = 0
			}
			ip += 4
		case 99:
			break loop
		default:
			log.Fatalln("unknown command: ", instructions[ip])
		}
	}
	return output
}

func getValueOrLiteral(instructions []int, immediate bool, ip int) int {
	if immediate {
		return instructions[ip]
	}

	return instructions[instructions[ip]]
}
