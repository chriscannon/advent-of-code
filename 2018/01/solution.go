package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Missing input filename.")
		return
	}

	file, err := os.Open(os.Args[1])
	defer file.Close()

	if err != nil {
		panic(err)
	}

	scanner := bufio.NewScanner(file)
	var currentFrequency int64
	var frequencyChanges []int64

	for scanner.Scan() {
		change, err := strconv.ParseInt(scanner.Text(), 10, 64)
		if err != nil {
			panic(err)
		}
		currentFrequency += change
		frequencyChanges = append(frequencyChanges, change)
	}
	fmt.Println("Part 1 resulting frequency: ", currentFrequency)

	currentFrequency = 0
	visited := make(map[int64]bool)
	visited[currentFrequency] = true

	for {
		for _, change := range frequencyChanges {
			currentFrequency += change

			if visited[currentFrequency] {
				fmt.Println("Part 2 first duplicated frequency: ", currentFrequency)
				return
			}

			visited[currentFrequency] = true
		}
	}
}