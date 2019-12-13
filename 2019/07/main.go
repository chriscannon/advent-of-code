// Day 7 Advent of Code 2019
// https://adventofcode.com/2019/day/7
package main

import (
	"fmt"
	"log"
	"strconv"

	"github.com/chriscannon/advent-of-code/common"
	"github.com/dbyio/heappermutations"
)

func main() {
	instructions, err := common.ReadIntSlice(common.SplitAt(','))
	if err != nil {
		log.Fatalln("failed to read input: ", err)
	}

	permutations := heappermutations.Ints([]int{0, 1, 2, 3, 4})
	results := make(chan int, 1)
	for i := range permutations {
		runAmplifier(instructions, permutations[i], results, false)
	}

	var maxThrust, output int
	for range permutations {
		output = <-results
		if output > maxThrust {
			maxThrust = output
		}
	}

	fmt.Println("Part 1: ", maxThrust)

	permutations = heappermutations.Ints([]int{5, 6, 7, 8, 9})
	for i := range permutations {
		runAmplifier(instructions, permutations[i], results, true)
	}

	maxThrust = 0
	for range permutations {
		output = <-results
		if output > maxThrust {
			maxThrust = output
		}
	}

	fmt.Println("Part 2: ", maxThrust)
}

func runAmplifier(instructions, phasesSetting []int, results chan int, isFeedback bool) {
	// Amp 1
	amp1Input := make(chan int, 1)
	amp1Output := make(chan int, 1)
	go exec(instructions, phasesSetting[0], amp1Input, amp1Output, nil)

	// Amp 2
	amp2Output := make(chan int, 1)
	go exec(instructions, phasesSetting[1], amp1Output, amp2Output, nil)

	// Amp 3
	amp3Output := make(chan int, 1)
	go exec(instructions, phasesSetting[2], amp2Output, amp3Output, nil)

	// Amp 4
	amp4Output := make(chan int, 1)
	go exec(instructions, phasesSetting[3], amp3Output, amp4Output, nil)

	// Amp 5
	if isFeedback {
		go exec(instructions, phasesSetting[4], amp4Output, amp1Input, results)
	} else {
		go exec(instructions, phasesSetting[4], amp4Output, results, nil)
	}

	amp1Input <- 0
}

func exec(originalInstructions []int, phase int, input, output, final chan int) {
	instructions := make([]int, len(originalInstructions))
	copy(instructions, originalInstructions)

	var ip int
	var inputRead bool
	var finalOutput int
	for {
		n := len(strconv.Itoa(instructions[ip]))
		digits := common.GetDigits(instructions[ip], n)
		param1Mode, param2Mode := getParamModes(digits)

		switch getOpCode(digits) {
		case 1:
			instructions[instructions[ip+3]] = getVal(instructions, param1Mode, ip+1) + getVal(instructions, param2Mode, ip+2)
			ip += 4
		case 2:
			instructions[instructions[ip+3]] = getVal(instructions, param1Mode, ip+1) * getVal(instructions, param2Mode, ip+2)
			ip += 4
		case 3:
			if !inputRead {
				instructions[instructions[ip+1]] = phase
				inputRead = true
			} else {
				instructions[instructions[ip+1]] = <-input
			}
			ip += 2
		case 4:
			finalOutput = getVal(instructions, param1Mode, ip+1)
			output <- finalOutput
			ip += 2
		case 5:
			if getVal(instructions, param1Mode, ip+1) != 0 {
				ip = getVal(instructions, param2Mode, ip+2)
			} else {
				ip += 3
			}
		case 6:
			if getVal(instructions, param1Mode, ip+1) == 0 {
				ip = getVal(instructions, param2Mode, ip+2)
			} else {
				ip += 3
			}
		case 7:
			if getVal(instructions, param1Mode, ip+1) < getVal(instructions, param2Mode, ip+2) {
				instructions[instructions[ip+3]] = 1
			} else {
				instructions[instructions[ip+3]] = 0
			}
			ip += 4
		case 8:
			if getVal(instructions, param1Mode, ip+1) == getVal(instructions, param2Mode, ip+2) {
				instructions[instructions[ip+3]] = 1
			} else {
				instructions[instructions[ip+3]] = 0
			}
			ip += 4
		case 99:
			if final != nil {
				final <- finalOutput
			}
			return
		default:
			log.Fatalln("unknown command: ", instructions[ip])
		}
	}
}

func getVal(instructions []int, immediate bool, ip int) int {
	if immediate {
		return instructions[ip]
	}

	return instructions[instructions[ip]]
}

func getOpCode(digits []int) int {
	n := len(digits)
	opcode := digits[n-1]

	if len(digits) >= 2 {
		opcode = digits[n-2]*10 + opcode
	}

	return opcode
}

func getParamModes(digits []int) (param1Mode, param2Mode bool) {
	n := len(digits)
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

	return
}
