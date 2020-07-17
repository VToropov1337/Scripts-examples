package main

import "fmt"

func main() {
	var code interface{}
	code = "hello"

	myString := code.(string)
	fmt.Println(myString)
}
