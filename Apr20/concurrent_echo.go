// Echo server.

package main

import (
	"bufio"
	"fmt"
	"net"
	"strconv"
)

const PORT = 25000

func clientCons(listner net.Listener) chan net.Conn {
	ch := make(chan net.Conn)
	i := 0
	go func() {
		for {
			client, err := listner.Accept()
			if client == nil {
				fmt.Errorf("Error: ", err)
				continue
			}
			i++
			fmt.Printf("%d: %v <-> %v\n", i, client.LocalAddr(), client.RemoteAddr())
			ch <- client
		}
	}()
	return ch
}

func handleCon(client net.Conn) {
	buf := bufio.NewReader(client)
	for {
		line, err := buf.ReadBytes('\n')
		if err != nil {
			break
		}
		client.Write(line)
	}
}

func main() {
	server, err := net.Listen("tcp", ":"+strconv.Itoa(PORT))
	if server == nil {
		fmt.Errorf("Error: ", err)
	}
	cons := clientCons(server)
	for {
		go handleCon(<-cons)
	}
}
