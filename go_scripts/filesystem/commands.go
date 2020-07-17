package main

import (
	"fmt"
	"os/exec"
	"runtime"
)

func execute() {

	out, err := exec.Command("ls").Output()
	// out, err := exec.Command("ls", "-ltr").Output()
	if err != nil {
		fmt.Printf("%s", err)
	}

	fmt.Println("ls command successfully executed")
	output := string(out[:])
	fmt.Println(output)

	// let's try the pwd command herer
	out, err = exec.Command("pwd").Output()
	if err != nil {
		fmt.Printf("%s", err)
	}
	fmt.Println("pwd command successfully executed")
	output = string(out[:])
	fmt.Println(output)
}

func main() {
	if runtime.GOOS == "windows" {
		fmt.Println("Dont work on your machine")
	} else {
		execute()
	}
}
