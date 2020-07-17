package main

import "fmt"

type Guitarist interface {
	PlayGuitar()
}

type BaseGuitarist struct {
	Name string
}

type AcousticGuitarist struct {
	Name string
}

func (b BaseGuitarist) PlayGuitar() {
	fmt.Printf("%s plays the Bass Guitar\n", b.Name)
}

func (b AcousticGuitarist) PlayGuitar() {
	fmt.Printf("%s plays the Acoustic Guitar\n", b.Name)
}

func main() {
	var player BaseGuitarist
	player.Name = "Paul"
	player.PlayGuitar()

	player2 := AcousticGuitarist{Name: "Ringo"}
	player2.PlayGuitar()

	var guitarists []Guitarist
	guitarists = append(guitarists, player)
	guitarists = append(guitarists, player2)

	for _, v := range guitarists {
		v.PlayGuitar()
	}

}
