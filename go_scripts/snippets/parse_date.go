package main

import (
	"fmt"
	"time"
)

func main() {
	// the layout we want to use to parse our
	// date string
	layout := "2006-01-02T15:04:05.000Z"

	// the string we want to parse
	str := "2020-05-05T09:00:00.000Z"

	t, err := time.Parse(layout, str)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(t.Year())    // Year
	fmt.Println(t.Weekday()) // Tuesday
	fmt.Println(t.Day())     // 05
	fmt.Println(t.Month())   // May
}
