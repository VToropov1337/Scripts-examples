package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

func main() {
	f, err := os.OpenFile("1.txt", os.O_APPEND|os.O_WRONLY, 0600)
	if err != nil {
		fmt.Println(err)
	}

	defer f.Close()

	if _, err = f.WriteString("some data to file\n"); err != nil {
		panic(err)
	}

	data, err := ioutil.ReadFile("1.txt")
	if err != nil {
		fmt.Println(err)
	}
	fmt.Print(string(data))
}
