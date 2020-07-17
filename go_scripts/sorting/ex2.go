package main

import (
	"fmt"
	"sort"
)

type Programmer struct {
	Age int
}

type byAge []Programmer

func (p byAge) Len() int {
	fmt.Println("len -->", len(p))
	return len(p)
}

func (p byAge) Swap(i, j int) {
	fmt.Println("swap -->", i, j)
	p[i], p[j] = p[j], p[i]
}

func (p byAge) Less(i, j int) bool {
	fmt.Println("less -->", p[i], p[j])
	return p[i].Age < p[j].Age
}

func main() {
	programmers := []Programmer{
		Programmer{Age: 30},
		Programmer{Age: 20},
		Programmer{Age: 50},
		Programmer{Age: 32},
		Programmer{Age: 42},
		Programmer{Age: 61},
		Programmer{Age: 19},
	}

	sort.Sort(byAge(programmers))

	fmt.Println(programmers)
}
