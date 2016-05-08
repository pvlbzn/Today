####DialTCP

Full code listening in : `./req.go`. Here code will skip all error handling and good practices.

```
1 addr, _ := net.ResolveTCPAddr("tcp", "google.com:80")
2 conn, _ := net.DialTCP("tcp", nil, addr)
3 
4 fmt.Fprintf(conn, "GET / HTTP1.0\r\n\r\n")
5 
6 buf := bufio.NewReader(conn)
7 status, _ := buf.ReadString('\n')
8 
9 fmt.Println("Status:", status)
```

Will print `Status: HTTP/1.0 302 Found`.

-

On 1 line `net.ResolveTCPAddr` parses addr as TCP address of the form "host:port" or "[ipv6-host%zone]:port" and resolves a pair of domain name and port name on the network, which must be unspecified "tcp" or "tcp4", "tcp6". `addr` variable is a \*TCPAddr type. 

-

`conn` is a \*TCPConn. `net.DialTCP(net string, laddr, raddr *TCPAddr)(*TCPConn, error)` connects to the remote address `raddr \*TCPAddr` on the network net (tcp, tcp4, tcp6). If laddr is not nil, it is used as the local address for the connection.

`DialTCP` (in implementation) returns `dialTCP(net, laddr, raddr, noDeadline, noCancel), where is `dialTCP` returnc `newTCPConn(fd)`.

```
// TCPConn is an implementation of the Conn interface for TCP network
// connections.
type TCPConn struct {
    conn
}

func newTCPConn(fd *netFD) *TCPConn {
    c := &TCPConn{conn{fd}}
    setNoDelay(c.fd, true)
    return c
}
```

-

`fmt.Fprintf(w io.Writer, format string, a ...interface{}) (n int, err error)` it formats according to a format specifier and writes to `w`, in this case writer is a `conn`.

-

`bufio.NewReader(rd io.Reader) \*Reader` returns a new Reader whose buffer has the default size. 

```
type Reader struct {
    buf          []byte
    rd           io.Reader // reader provided by the client
    r, w         int       // buf read and write positions
    err          error
    lastByte     int
    lastRuneSize int
}
```

`buf.ReadString('\n')` reads until the first occurrence of delim in the input, returning a string containing the data up to and including the delimeter.

```
func (b *Reader) ReadString(delim byte) (line string, err error) {
    bytes, err := b.ReadBytes(delim)
    line = string(bytes)
    return line, err
}
```

-

This code I took from golang source code:

```
// Copyright 2009 The Go Authors. All rights reserved.
```
