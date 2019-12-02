// Day 2 Advent of Code 2019
// https://adventofcode.com/2019/day/2
package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

//Part2Output is the required output in register 0 for part 2
const Part2Output = 19690720

func main() {
	input := readInput()
	instructionsStr := strings.Split(input[0], ",")
	instructions := make([]int, len(instructionsStr))
	registers := make([]int, len(instructionsStr))
	for i := range instructionsStr {
		val, _ := strconv.Atoi(instructionsStr[i])
		instructions[i] = val
		registers[i] = val
	}

	part1 := exec(copySlice(instructions), copySlice(registers), 12, 2)
	fmt.Println("Part 1: ", part1)
	base := exec(copySlice(instructions), copySlice(registers), 0, 0)
	nounJump := exec(copySlice(instructions), copySlice(registers), 1, 0) - base
	verbJump := exec(copySlice(instructions), copySlice(registers), 0, 1) - base

	noun := (Part2Output - base) / nounJump
	verb := (Part2Output - base - (noun * nounJump)) / verbJump

	part2 := exec(copySlice(instructions), copySlice(registers), noun, verb)
	if part2 != Part2Output {
		log.Fatalf("Part 2 actual output %d does not match expected output %d\n", part2, Part2Output)
	}
	fmt.Println("Part 2: ", 100*noun+verb)
}

func copySlice(src []int) []int {
	return append([]int(nil), src...)
}

func exec(instructions []int, registers []int, input1, input2 int) int {
	registers[1] = input1
	registers[2] = input2
loop:
	for i := 0; i < len(instructions); i += 4 {
		switch instructions[i] {
		case 1:
			registers[instructions[i+3]] = registers[instructions[i+1]] + registers[instructions[i+2]]
		case 2:
			registers[instructions[i+3]] = registers[instructions[i+1]] * registers[instructions[i+2]]
		case 99:
			break loop
		default:
			log.Fatalln("unknown command: ", instructions[i])
		}
	}
	return registers[0]
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
