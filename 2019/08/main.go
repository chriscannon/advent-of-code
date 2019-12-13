// Day 8 Advent of Code 2019
// https://adventofcode.com/2019/day/8
package main

import (
	"fmt"
	"log"
	"math"

	"github.com/chriscannon/advent-of-code/common"
)

func main() {
	input, err := common.ReadDigitsIntSlice()
	if err != nil {
		log.Fatalln("failed to read input: ", err)
	}
	width, height := 3, 2

	layers := make(map[int]common.Matrix)

	for i := 0; i < len(input); i += width * height {
		index := i
		for j := 0; j < width + height; j ++ {

		}
		for y := 0; y < height; y++ {
			for x := 0; x < width; x++ {
				layerID := i
				val := input[i+y+x]
				fmt.Println(val)
				if matrix, ok := layers[layerID]; !ok {
					m := common.NewMatrix()
					m.AddCoordinate(x, y, input[i+y+x], 0)
					layers[layerID] = m
				} else {
					matrix.AddCoordinate(x, y, input[i+y+x], 0)
				}
			}
		}
	}

	minZeros := math.MaxInt32
	var onesTimesTwos int
	for _, matrix := range layers {
		counts := make(map[int]int)
		for _, coord := range matrix.Data {
			for id := range coord.VisitedIDs {
				counts[id]++
			}
		}

		if counts[0] < minZeros {
			onesTimesTwos = counts[1] * counts[2]
			minZeros = counts[0]
		}
	}

	fmt.Println("Part 1: ", onesTimesTwos)
	// 100 too low
}
