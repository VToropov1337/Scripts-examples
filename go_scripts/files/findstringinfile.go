package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func main() {
	data, err := ioutil.ReadFile("1.txt")
	if err != nil {
		fmt.Println(err)
	}

	if strings.Contains(string(data), "data") {
		fmt.Println("CATCH")
	}

}
