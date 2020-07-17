package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	mydata := []byte("New data\n")

	err := ioutil.WriteFile("1.txt", mydata, 0777)

	if err != nil {
		fmt.Println(err)
	}
}
