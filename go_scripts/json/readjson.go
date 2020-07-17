package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

func main() {

	jsonFile, err := os.Open("users.json")
	defer jsonFile.Close()

	if err != nil {
		fmt.Println(err)
	}
	fmt.Println("Successfully Opened users.json")
	byteValue, _ := ioutil.ReadAll(jsonFile)
	fmt.Println(string(byteValue))

}
