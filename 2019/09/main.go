// Day 9 Advent of Code 2019
// https://adventofcode.com/2019/day/9
package main

import (
	"fmt"
	"log"
	"math"
	"strconv"

	"github.com/chriscannon/advent-of-code/common"
)

type paramMode int
type opCode int

const (
	position paramMode = iota
	immediate
	relative
)
const (
	add opCode = iota + 1
	multiply
	writeInput
	writeOutput
	jumpIfTrue
	jumpIfFalse
	lessThan
	equals
	increaseBase
)

func main() {
	instructions, err := common.ReadIntSlice(common.SplitAt(','))
	if err != nil {
		log.Fatalln("failed to read input: ", err)
	}

	input := make(chan int, 1)
	output := make(chan int, 1)
	go exec(instructions, input, output)
	input <- 1
	fmt.Println("Part 1: ", <-output)
	go exec(instructions, input, output)
	input <- 2
	fmt.Println("Part 2: ", <-output)
}

func exec(originalInstructions []int, input, output chan int) {
	instructions := make([]int, math.MaxInt32)
	copy(instructions, originalInstructions)

	var ip, base int
	for {
		n := len(strconv.Itoa(instructions[ip]))
		digits := common.GetDigits(instructions[ip], n)
		param1Mode, param2Mode, param3Mode := getParamModes(digits)

		switch getOpCode(digits) {
		case add:
			instructions[getWriteAddr(instructions, param3Mode, ip+3, base)] = getVal(instructions, param1Mode, ip+1, base) + getVal(instructions, param2Mode, ip+2, base)
			ip += 4
		case multiply:
			instructions[getWriteAddr(instructions, param3Mode, ip+3, base)] = getVal(instructions, param1Mode, ip+1, base) * getVal(instructions, param2Mode, ip+2, base)
			ip += 4
		case writeInput:
			instructions[getWriteAddr(instructions, param1Mode, ip+1, base)] = <-input
			ip += 2
		case writeOutput:
			output <- getVal(instructions, param1Mode, ip+1, base)
			ip += 2
		case jumpIfTrue:
			if getVal(instructions, param1Mode, ip+1, base) != 0 {
				ip = getVal(instructions, param2Mode, ip+2, base)
			} else {
				ip += 3
			}
		case jumpIfFalse:
			if getVal(instructions, param1Mode, ip+1, base) == 0 {
				ip = getVal(instructions, param2Mode, ip+2, base)
			} else {
				ip += 3
			}
		case lessThan:
			if getVal(instructions, param1Mode, ip+1, base) < getVal(instructions, param2Mode, ip+2, base) {
				instructions[getWriteAddr(instructions, param3Mode, ip+3, base)] = 1
			} else {
				instructions[getWriteAddr(instructions, param3Mode, ip+3, base)] = 0
			}
			ip += 4
		case equals:
			if getVal(instructions, param1Mode, ip+1, base) == getVal(instructions, param2Mode, ip+2, base) {
				instructions[getWriteAddr(instructions, param3Mode, ip+3, base)] = 1
			} else {
				instructions[getWriteAddr(instructions, param3Mode, ip+3, base)] = 0
			}
			ip += 4
		case increaseBase:
			base += getVal(instructions, param1Mode, ip+1, base)
			ip += 2
		case 99:
			return
		default:
			log.Fatalln("unknown command: ", instructions[ip])
		}
	}
}

func getVal(instructions []int, mode paramMode, ip, base int) int {
	switch mode {
	case immediate:
		return instructions[ip]
	case position:
		return instructions[instructions[ip]]
	case relative:
		return instructions[base+instructions[ip]]
	default:
		log.Fatal("unknown mode: ", mode)
	}
	return -1
}

func getWriteAddr(instructions []int, mode paramMode, ip, base int) int {
	switch mode {
	case position:
		return instructions[ip]
	case relative:
		return instructions[ip] + base
	default:
		log.Fatal("unknown mode: ", mode)
	}
	return -1
}

func getOpCode(digits []int) opCode {
	n := len(digits)
	code := digits[n-1]

	if len(digits) >= 2 {
		code = digits[n-2]*10 + code
	}

	return opCode(code)
}

func getParamModes(digits []int) (param1Mode, param2Mode, param3Mode paramMode) {
	n := len(digits)
	switch n {
	case 5:
		param3Mode = paramMode(digits[0])
		param2Mode = paramMode(digits[1])
		param1Mode = paramMode(digits[2])
	case 4:
		param2Mode = paramMode(digits[0])
		param1Mode = paramMode(digits[1])
	case 3:
		param1Mode = paramMode(digits[0])
	}

	if n > 5 {
		log.Fatalln("n is greater than 5: ", n)
	}

	return
}
