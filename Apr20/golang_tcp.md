###Go TCP server

For the sake of completeness I'll implement few things in Go which, recently, I did in Python and Java. There is two points:

- How the same things works in PL with different techical impl and their approach
- Interest in the Go

**Biased**: I found out that Go substitute Python in many fields. Especially if this field is about networking and concurrency. Python still shine in some categories, but for my purpose Go seems more interesting, and honestly - I love Go idioms, how it forces good coding style (fmt, no syntax highlighting, vim, documentation, code samples, open source, etc) and major point is how Go solves problems.

-

####Package `net`

>[Package](https://golang.org/pkg/net/) net provides a portable interface for network I/O, including TCP/IP, UDP, domain name resolution, and Unix domain sockets.


####TCP echo server

Look at `concurrent_echo.go`.

More fun is to make a Fibonacci service. Implementation is in `faas.go`.


