package main

import (
	"./interf"
	"fmt"
)

func main() {
	// Also possible to defer defer.
	defer tryDefer(5)
	defer moreDefer()

	// Variardic
	variar(1, 2, 3, 4, 5)

	// Package
	rec := intertouch.Rect{"Blue", 7, 15}
	cir := intertouch.Circle{"Red", 16}

	// Use interface as type
	geoprinter(rec, cir)
}

func tryDefer(n int) {
	defer fmt.Println()
	for i := 0; i < n; i++ {
		defer fmt.Println(i)
	}
}

func moreDefer() {
	defer fmt.Println()
	defer fmt.Println("defer executes on function exit")
	fmt.Println("Message from the function")
}

func variar(n ...int) {
	fmt.Printf("There are %d parameters received.\n", len(n))
}

func geoprinter(g ...intertouch.GeoForm) {
	for _, obj := range g {
		fmt.Printf("perimeter is %f\n\n", obj.Perimeter())
	}
}
