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

const (
	position paramMode = iota
	immediate
	relative
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

	var ip, relativeBase int
	for {
		n := len(strconv.Itoa(instructions[ip]))
		digits := common.GetDigits(instructions[ip], n)
		param1Mode, param2Mode, param3Mode := getParamModes(digits)

		switch getOpCode(digits) {
		case 1:
			instructions[getWriteAddr(instructions, param3Mode, ip+3, relativeBase)] = getVal(instructions, param1Mode, ip+1, relativeBase) + getVal(instructions, param2Mode, ip+2, relativeBase)
			ip += 4
		case 2:
			instructions[getWriteAddr(instructions, param3Mode, ip+3, relativeBase)] = getVal(instructions, param1Mode, ip+1, relativeBase) * getVal(instructions, param2Mode, ip+2, relativeBase)
			ip += 4
		case 3:
			instructions[getWriteAddr(instructions, param1Mode, ip+1, relativeBase)] = <-input
			ip += 2
		case 4:
			output <- getVal(instructions, param1Mode, ip+1, relativeBase)
			ip += 2
		case 5:
			if getVal(instructions, param1Mode, ip+1, relativeBase) != 0 {
				ip = getVal(instructions, param2Mode, ip+2, relativeBase)
			} else {
				ip += 3
			}
		case 6:
			if getVal(instructions, param1Mode, ip+1, relativeBase) == 0 {
				ip = getVal(instructions, param2Mode, ip+2, relativeBase)
			} else {
				ip += 3
			}
		case 7:
			if getVal(instructions, param1Mode, ip+1, relativeBase) < getVal(instructions, param2Mode, ip+2, relativeBase) {
				instructions[getWriteAddr(instructions, param3Mode, ip+3, relativeBase)] = 1
			} else {
				instructions[getWriteAddr(instructions, param3Mode, ip+3, relativeBase)] = 0
			}
			ip += 4
		case 8:
			if getVal(instructions, param1Mode, ip+1, relativeBase) == getVal(instructions, param2Mode, ip+2, relativeBase) {
				instructions[getWriteAddr(instructions, param3Mode, ip+3, relativeBase)] = 1
			} else {
				instructions[getWriteAddr(instructions, param3Mode, ip+3, relativeBase)] = 0
			}
			ip += 4
		case 9:
			relativeBase += getVal(instructions, param1Mode, ip+1, relativeBase)
			ip += 2
		case 99:
			return
		default:
			log.Fatalln("unknown command: ", instructions[ip])
		}
	}
}

func getVal(instructions []int, mode paramMode, ip, relativeBase int) int {
	switch mode {
	case immediate:
		return instructions[ip]
	case position:
		return instructions[instructions[ip]]
	case relative:
		return instructions[relativeBase+instructions[ip]]
	default:
		log.Fatal("unknown mode: ", mode)
	}
	return -1
}

func getWriteAddr(instructions []int, mode paramMode, ip, relativeBase int) int {
	switch mode {
	case position:
		return instructions[ip]
	case relative:
		return instructions[ip] + relativeBase
	default:
		log.Fatal("unknown mode: ", mode)
	}
	return -1
}

func getOpCode(digits []int) int {
	n := len(digits)
	opCode := digits[n-1]

	if len(digits) >= 2 {
		opCode = digits[n-2]*10 + opCode
	}

	return opCode
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
