####Streams

Sockets works with `InputStream` and `OutputStream`, so it is good to know what *streams* actually are.

**Streams**

Modern i/o is stream-based. A *stream* is a connection to a source of data or a destination for data, or both. An *input stream* may be associated with the keyboard, or with a some file.

```
input 	--->   	program		--->	output
```

There are a wide range of i/o sources, like web server, monitor, file, printer, etc.

If data flows **from a source into a program**, it is called an **input stream**. If data flows **from a program to a destination**, it is called an **output stream**. Fair enough.

Streams are part of `java.io` [package](http://orm-chimera-prod.s3.amazonaws.com/1234000001805/figs/lj4e_1201.png).

**Reading/Writing**:

```
open a stream
while more info
	read info
close the stream
```

-

There are two streams:

- Character Streams
- Byte Streams

**Character streams**:
`Reader` and `Writer` are the abstract superclasses for character streams in `java.io`. `Reader` and `Writer` provides API and partial impl for streams that read or write 16bit characters.

Subclasses of R/W implements specialized streams and are divided into two categories: read/write data; perform some sort of processing.


**Byte Streams**:
`InputStream` and `OutputStream` are 8bit bytes. These streams are typically used to r/w binary data. `Object[Input/Output]Stream` are used for object serialiation. I/O streams subclasses also have 2 categories: data sink streams; processing streams.
