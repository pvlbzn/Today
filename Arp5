###Unix File Descriptors

Each file has its own file descriptor, integer. So, file descriptor is an integer number that uniquely represents an opened file in OS.

When we open an existing file or create a new file, the kernel returns a file descriptor to the process. The kernel maintains a table of all file descriptors, which are in use.

*Recommend read: Advanced Programming in the UNIX Environment*

---

There are 3 standard POSIX file descriptors, corresponding to the three standard streams:

```
Value		<stdio.h> file stream
0			stdin
1			stdout
2			stderr
```

---

A **file descriptor is an non-negative integer** associated with an open file, but, that file can be a network connection, a FIFO, a pipe, a terminal, a real file, or whatever else. **Everything in Unix is a file**. Thus, when you want to communicate with another program over the Internet you going to do it through a file descriptor.

```
// Make a call using system routine. It returns the socket descriptor.
socket()
// Communicate through it using the socket calls.
send()
recv()
```

