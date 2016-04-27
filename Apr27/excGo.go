package main

import (
	"fmt"
)

func main() {
	// Also possible to defer defer.
	defer tryDefer(5)
	defer moreDefer()

	// Variardic
	variar(1, 2, 3, 4, 5)
}

func tryDefer(n int) {
	for i := 0; i < n; i++ {
		defer fmt.Println(i)
	}
}

func moreDefer() {
	defer fmt.Println("defer executes on function exit")
	fmt.Println("Message from the function")
}

func variar(n ...int) {
	fmt.Printf("There are %d parameters received.\n", len(n))
}
