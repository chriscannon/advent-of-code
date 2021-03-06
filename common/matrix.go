package common

import (
	"fmt"
	"strconv"
	"strings"
)

// XY
type XY struct {
	X, Y int
}

// Coordinate
type Coordinate struct {
	X, Y       int
	VisitedIDs map[int]bool
}

func newCoordinate(x, y, id int) Coordinate {
	visited := make(map[int]bool)
	visited[id] = true

	return Coordinate{
		X:          x,
		Y:          y,
		VisitedIDs: visited,
	}
}

// Matrix
type Matrix struct {
	Data                   map[XY]Coordinate
	MaxX, MinX, MaxY, MinY int
	Steps                  map[XY]map[int]int
}

// NewMatrix
func NewMatrix() Matrix {
	return Matrix{Data: make(map[XY]Coordinate), Steps: make(map[XY]map[int]int)}
}

// Print
func (m *Matrix) Print() {
	for y := m.MaxY + 1; y > m.MinY-1; y-- {
		var line []string
		for x := m.MinX - 1; x < m.MaxX+1; x++ {
			if x == 0 && y == 0 {
				line = append(line, "C")
				continue
			}
			xy := XY{X: x, Y: y}
			val, ok := m.Data[xy]
			if !ok {
				line = append(line, ".")
			} else if len(val.VisitedIDs) == 1 {
				for k := range val.VisitedIDs {
					line = append(line, strconv.Itoa(k))
				}
			} else {
				line = append(line, "X")
			}
		}
		fmt.Println(strings.Join(line, ""))
	}
}

func (m *Matrix) AddCoordinate(x, y, id, step int) {
	xy := XY{X: x, Y: y}
	val, ok := m.Data[xy]
	if !ok {
		m.Data[xy] = newCoordinate(x, y, id)
	} else {
		val.VisitedIDs[id] = true
	}

	ids, ok := m.Steps[xy]
	if !ok {
		// If we haven't seen this coordinate before add the ID's steps
		steps := make(map[int]int)
		steps[id] = step
		m.Steps[xy] = steps
	} else if _, ok := ids[id]; !ok {
		// Only add the steps for this ID if we haven't seen it before.
		// We don't add the steps after the first observation because we know those steps
		// will be greater than the previous step and we are only interested in the minimum amount of steps.
		ids[id] = step
	}

	if x > m.MaxX {
		m.MaxX = x
	}

	if y > m.MaxY {
		m.MaxY = y
	}

	if x < m.MinX {
		m.MinX = x
	}

	if y < m.MinY {
		m.MinY = y
	}
}

func (m *Matrix) VisitedNTimes(n int) []XY {
	var visited []XY
	for xy, coordinate := range m.Data {
		if len(coordinate.VisitedIDs) == n {
			// Ignore the starting position
			if xy.X == 0 && xy.Y == 0 {
				continue
			}
			visited = append(visited, xy)
		}
	}
	return visited
}

func ComputeManhattanDistance(x1, y1, x2, y2 int) int {
	return Abs(x1-x2) + Abs(y1-y2)
}

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
