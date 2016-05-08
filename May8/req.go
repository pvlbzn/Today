package main

import (
	"bufio"
	"fmt"
	"log"
	"net"
)

func GET() {
	addr, err := net.ResolveTCPAddr("tcp", "google.com:80")
	if err != nil {
		log.Fatal(err)
	}

	conn, err := net.DialTCP("tcp", nil, addr)
	if err != nil {
		log.Fatal(err)
	}
	defer conn.Close()

	fmt.Fprintf(conn, "GET / HTTP/1.0\r\n\r\n")

	buf := bufio.NewReader(conn)
	status, err := buf.ReadString('\n')
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Status:", status)
}

func main() {
	GET()
}
