package main

import (
	"fmt"
	"strings"
)

func main() {
	originalString := "This is our original string"

	doesContain := strings.Contains(originalString, "our")
	fmt.Println(doesContain)

	doesNotContain := strings.Contains(originalString, "meh")
	fmt.Println(doesNotContain)
}
