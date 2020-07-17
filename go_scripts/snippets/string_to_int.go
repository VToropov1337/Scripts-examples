package main

import (
	"fmt"
	"strconv"
)

func main() {

	myAgeString := "26"
	fmt.Printf("My Age: %s\n", myAgeString)

	ageValue, err := strconv.Atoi(myAgeString)
	if err != nil {
		fmt.Println(err)
	}

	ageValue += 1
	fmt.Printf("New Age: %d\n", ageValue)

}
