package common

// HeapPermutation
func HeapPermutation(a []int, size int) [][]int {
	var permutations [][]int
	if size == 1 {
		temp := make([]int, len(a))
		copy(temp, a)
		return [][]int{temp}
	}

	for i := 0; i < size; i++ {
		permutations = append(permutations, HeapPermutation(a, size-1)...)

		if size%2 == 1 {
			a[0], a[size-1] = a[size-1], a[0]
		} else {
			a[i], a[size-1] = a[size-1], a[i]
		}
	}

	return permutations
}
