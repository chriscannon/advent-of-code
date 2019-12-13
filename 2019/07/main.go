// Day 7 Advent of Code 2019
// https://adventofcode.com/2019/day/7
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

	// My permutation generator can't handle 0s so I increment the phase IDs
	// by 1 and then subtract by 1 when I execute the amplifier.
	phases := []int{1, 2, 3, 4, 5}
	permutations := common.HeapPermutation(phases, 5)
	results := make(chan int)

	for i := range permutations {
		runAmplifier(instructions, permutations[i], results, false)
	}

	maxThrust := 0
	for range permutations {
		output := <-results
		if output > maxThrust {
			maxThrust = output
		}
	}

	fmt.Println("Part 1: ", maxThrust)

	phases = []int{6, 7, 8, 9, 10}
	permutations = common.HeapPermutation(phases, 5)

	for i := range permutations {
		runAmplifier(instructions, permutations[i], results, true)
	}

	maxThrust = 0
	for range permutations {
		output := <-results
		if output > maxThrust {
			maxThrust = output
		}
	}

	fmt.Println("Part 2: ", maxThrust)
}

func runAmplifier(instructions, phasesSetting []int, results chan int, isFeedback bool) {
	// Amp 1
	amp1Input := make(chan int)
	amp1Output := make(chan int)
	go exec(instructions, 1, phasesSetting[0]-1, amp1Input, amp1Output, nil)

	// Amp 2
	amp2Output := make(chan int)
	go exec(instructions, 2, phasesSetting[1]-1, amp1Output, amp2Output, nil)

	// Amp 3
	amp3Output := make(chan int)
	go exec(instructions, 3, phasesSetting[2]-1, amp2Output, amp3Output, nil)

	// Amp 4
	amp4Output := make(chan int)
	go exec(instructions, 4, phasesSetting[3]-1, amp3Output, amp4Output, nil)

	// Amp 5
	if isFeedback {
		go exec(instructions, 5, phasesSetting[4]-1, amp4Output, amp1Input, results)
	} else {
		go exec(instructions, 5, phasesSetting[4]-1, amp4Output, results, nil)
	}

	amp1Input <- 0
}

func exec(originalInstructions []int, ampID, phase int, input, output, final chan int) {
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

			// Since we're using unbuffered channels Amp 1 needs to do
			// one last receive from Amp 5 in order for Amp 5 to get to
			// the halt command.
			if ampID == 1 {
				<-input
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
