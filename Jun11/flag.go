package main

import (
	"flag"
	"fmt"
)

var (
	foo = flag.Bool("f", false, "foo bool")
	bar = flag.String("b", "", "bar string")
)

func main() {
	flag.Parse()

	if *foo {
		fmt.Println("true")
	} else {
		fmt.Println("false")
	}

	if *bar != "" {
		fmt.Println(*bar)
	}
}
