package main

import (
	"fmt"
	"net"
	"os"
)

func main() {
	addr, err := net.LookupIP(os.Args[1])
	if err != nil {
		fmt.Errorf("lookup ", err)
	}
	for _, a := range addr {
		fmt.Println(a)
	}
}
