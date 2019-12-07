package common

import (
	"log"
	"math"
)

// GetDigits takes an int (num) with length (n) as input and returns
// a slice of ints for each digit in the number.
func GetDigits(num, n int) []int {
	var digits []int
	for i := n - 1; i >= 0; i-- {
		denominator := int(math.Pow(10, float64(i)))
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
