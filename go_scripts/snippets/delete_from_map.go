package main

import "fmt"

func main() {
	mymap := map[string]int{
		"Elliot": 25,
		"Fraser": 20,
		"Scott":  24,
	}

	fmt.Printf("%+v\n", mymap)

	delete(mymap, "Scott")

	fmt.Printf("%+v\n", mymap)

}
