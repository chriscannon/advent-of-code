// Day 3 Advent of Code 2019
// https://adventofcode.com/2019/day/3
package main

import (
	"fmt"
	"log"
	"math"
	"strconv"

	"github.com/chriscannon/advent-of-code/common"
)

func main() {
	input, err := common.ReadStringSliceWithFields(",")

	if err != nil {
		log.Fatalln("failed to read input: ", err)
	}

	matrix := common.NewMatrix()
	for i := range input {
		var x, y int
		matrix.AddCoordinate(0, 0, i)
		for j := range input[i] {
			var xDelta, yDelta int
			switch input[i][j][0] {
			case 'R':
				xDelta = 1
			case 'D':
				yDelta = -1
			case 'L':
				xDelta = -1
			case 'U':
				yDelta = 1
			default:
				log.Fatalln("unknown direction: ", input[i][j][0])
			}
			movement, _ := strconv.Atoi(input[i][j][1:])

			for movement != 0 {
				x += xDelta
				y += yDelta
				matrix.AddCoordinate(x, y, i)
				movement--
			}
		}
	}

	visited := matrix.VisitedNTimes(2)
	minManhattan := math.MaxInt32
	for i := range visited {
		manhattan := common.ComputeManhattanDistance(0, 0, visited[i].X, visited[i].Y)

		if manhattan < minManhattan {
			minManhattan = manhattan
		}
	}

	fmt.Println("Part 1:", minManhattan)
	// Too high 13418
}
