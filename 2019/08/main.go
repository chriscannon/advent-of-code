// Day 8 Advent of Code 2019
// https://adventofcode.com/2019/day/8
package main

import (
	"fmt"
	"log"
	"math"

	"github.com/chriscannon/advent-of-code/common"
)

const (
	emptySpace  = "   "
	markedSpace = " X "
)

// Point is an X, Y coordinate
type Point struct {
	X, Y int
}

func main() {
	input, err := common.ReadDigitsIntSlice()
	if err != nil {
		log.Fatalln("failed to read input: ", err)
	}
	width, height := 25, 6
	layerDataCounts := make(map[int]map[int]int)
	stackedLayers := make(map[Point]int)

	var index int
	layerID := 1
	for i := 0; i < len(input); i += width * height {
		layerDataCounts[layerID] = make(map[int]int)
		for y := 0; y < height; y++ {
			for x := 0; x < width; x++ {
				data := input[index]
				layerDataCounts[layerID][data]++

				p := Point{X: x, Y: y}
				if _, ok := stackedLayers[p]; !ok && (data == 1 || data == 0) {
					stackedLayers[p] = data
				}
				index++
			}
		}
		layerID++
	}

	var onesTimesTwos int
	minZeros := math.MaxInt32

	for _, layer := range layerDataCounts {
		if layer[0] < minZeros {
			minZeros = layer[0]
			onesTimesTwos = layer[1] * layer[2]
		}
	}

	fmt.Println("Part 1: ", onesTimesTwos)
	fmt.Println("Part 2:")

	for y := 0; y < height; y++ {
		for x := 0; x < width; x++ {
			if data, ok := stackedLayers[Point{X: x, Y: y}]; ok {
				if data == 1 {
					fmt.Printf(markedSpace)
				} else {
					fmt.Printf(emptySpace)
				}
			} else {
				fmt.Printf(emptySpace)
			}
		}
		fmt.Println()
	}
}
