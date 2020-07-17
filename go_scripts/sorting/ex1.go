package main

import (
	"fmt"
	"sort"
)

func main() {

	myInts := []int{1, 3, 2, 6, 3, 4}
	fmt.Println(myInts)

	// sort.Ints
	sort.Ints(myInts)
	fmt.Println(myInts)
}
