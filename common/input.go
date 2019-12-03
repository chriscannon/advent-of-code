package common

import (
	"bufio"
	"bytes"
	"fmt"
	"log"
	"os"
	"strconv"
)

func getInputFile() *os.File {
	file := os.Stdin
	if len(os.Args) == 2 {
		var err error
		file, err = os.Open(os.Args[1])
		if err != nil {
			log.Fatalln("failed to open file: ", err)
		}
	}
	return file
}

func closeFile(file *os.File) {
	if file == os.Stdin {
		return
	}

	if err := file.Close(); err != nil {
		log.Fatalln("failed to close file: ", err)
	}
}

// ReadUint64Slice scans the input file and parses it into a slice of uint64s.  If split is
// nil, each number is separated by a newline.  Otherwise, the input is split with that function.
func ReadUint64Slice(split bufio.SplitFunc) ([]uint64, error) {
	file := getInputFile()
	defer closeFile(file)
	scanner := bufio.NewScanner(file)

	if split != nil {
		scanner.Split(split)
	}

	var inputs []uint64
	for scanner.Scan() {
		value, err := strconv.ParseUint(scanner.Text(), 10, 64)
		if err != nil {
			return nil, fmt.Errorf("failed to convert value to uint64: %w", err)
		}

		inputs = append(inputs, value)
	}

	if err := scanner.Err(); err != nil {
		return nil, fmt.Errorf("failed to scan input: %w", err)
	}

	return inputs, nil
}

// SplitAt returns a bufio.SplitFunc closure, splitting at a substring
// scanner.Split(SplitAt(','))
// https://stackoverflow.com/a/51127669
// https://golang.org/src/bufio/scan.go#L345
func SplitAt(sep rune) func(data []byte, atEOF bool) (advance int, token []byte, err error) {
	return func(data []byte, atEOF bool) (advance int, token []byte, err error) {
		if atEOF && len(data) == 0 {
			return 0, nil, nil
		}

		if i := bytes.IndexByte(data, byte(sep)); i >= 0 {
			return i + 1, dropNewline(data[0:i]), nil
		}

		if atEOF {
			return len(data), dropNewline(data), nil
		}

		return
	}
}

// If specifying a custom split we can assume that the split is not
// a newline character and can remove the trailing newline character
// https://golang.org/src/bufio/scan.go#L332
func dropNewline(data []byte) []byte {
	if len(data) > 0 && data[len(data)-1] == '\n' {
		return data[0 : len(data)-1]
	}
	return data
}
