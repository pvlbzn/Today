// Echo server.

package main

import (
	"bufio"
	//"bytes"
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
		line, _, err := buf.ReadLine()
		if err != nil {
			break
		}
		n, _ := strconv.ParseInt(string(line[:]), 0, 64)
		f := fib(n)
		ans := strconv.FormatInt(f, 10)
		ans += "\n"
		client.Write([]byte(ans))
	}
}

func fib(n int64) int64 {
	if n == 0 || n == 1 {
		return n
	}
	return fib(n-2) + fib(n-1)
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
