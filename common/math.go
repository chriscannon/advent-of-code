package common

import (
	"log"
)

// GetDigits takes an int (num) with length (n) as input and returns
// a slice of ints for each digit in the number.
func GetDigits(num, n int) []int {
	var digits []int
	for i := n - 1; i >= 0; i-- {
		denominator := Pow(10, i)
		digits = append(digits, (num/denominator)%10)
	}
	return digits
}

// Itob takes an int and converts it to a boolean
func Itob(i int) bool {
	if i != 0 && i != 1 {
		log.Fatalln("unknown integer to convert to boolean: ", i)
	}

	if i == 1 {
		return true
	}

	return false
}

// Pow computes a**b using binary powering algorithm.
// See Donald Knuth, The Art of Computer Programming, Volume 2, Section 4.6.3
// Source: https://groups.google.com/d/msg/golang-nuts/PnLnr4bc9Wo/z9ZGv2DYxXoJ
func Pow(a, b int) int {
	p := 1
	for b > 0 {
		if b&1 != 0 {
			p *= a
		}
		b >>= 1
		a *= a
	}
	return p
}
