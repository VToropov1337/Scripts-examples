package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {

	reader := bufio.NewReader(os.Stdin)
	fmt.Println("---------------------")

	for {
		fmt.Print("-> ")
		text, _ := reader.ReadString('\n')
		fmt.Println("===>", text)

		if strings.Contains(text, "hi") {
			fmt.Println("hello, Yourself")
		}

		// if strings.Compare("hi", text) == 0 {
		// fmt.Println("hello, Yourself")
		// }

	}

}
