package main

import "fmt"

func myTestFunc(a *string) {
	fmt.Println("--", a)
	*a += "da"
	fmt.Println(*a)
}

func main() {
	a := "hello"
	fmt.Println(&a, a)
	myTestFunc(&a)
	fmt.Println(a)
}
