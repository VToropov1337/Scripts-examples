package main

import "fmt"

func main() {

	mymap := make(map[string]int)

	mymap["elliot"] = 25

	if _, ok := mymap["elliot"]; ok {
		fmt.Println(mymap["elliot"])
	}
}
