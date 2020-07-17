package main

import "fmt"

func myTestFunc(a *int) {
	*a += 3
	fmt.Println(*a)
}

func main() {
	a := 2
	myTestFunc(&a)
	fmt.Println(a) // prints out 5
}
