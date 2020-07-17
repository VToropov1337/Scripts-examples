package main

import (
	"fmt"
)

func bubbleSort(input []int) {
	n := len(input)
	if n < 2 {
		return
	}

	swapped := true

	for swapped {
		swapped = false
		for i := 1; i < n; i++ {
			if input[i-1] > input[i] {
				input[i], input[i-1] = input[i-1], input[i]
				swapped = true

			}

		}
	}

}

func main() {
	toBeSorted := []int{1, 3, 2, 2, 4, 8, 6, 7, 2, 3, 0}
	bubbleSort(toBeSorted)
	fmt.Println(toBeSorted)
}
