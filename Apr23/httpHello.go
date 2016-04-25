package main

import (
	"fmt"
	"io"
	"net/http"
)

func printInfo(r *http.Request) {
	fmt.Printf("Client: %s\n", r.UserAgent())
	fmt.Printf("Method: %s\n\n", r.Method)
}

func handler(w http.ResponseWriter, r *http.Request) {
	io.WriteString(w, "Hello")
	printInfo(r)
}

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":8080", nil)
}
