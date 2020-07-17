package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	data, err := ioutil.ReadFile("1.txt")
	if err != nil {
		fmt.Println(err)
	}

	fmt.Println(string(data))
}
