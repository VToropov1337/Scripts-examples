package main

import "fmt"

func main() {
	age := new(int)
	*age = 26
	// var age *int
	// age = new(int)
	// *age = 26

	fmt.Println(*age)
	fmt.Println(&age)
}
