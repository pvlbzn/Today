###I/O streams

The `InputStream` has an `abstract int read()`. The `OutputStream` has an `abstract void write(int b)`. They both are abstract classes, which means that following classes will `extend` their functionality in more specific and narrowed way, here is an example:

```
public class ByteArrayOutputStream extends OutputStream {
	...
	public synchronised void write(int b) {
		// Implementation
	}
	...
}
```

And etc.

`[Input/Output]Stream` are byte-oriented streams, `Reader/Writer` are Unicode-oriented streams.

Both `read` and `write` method *block*. The `available` method lets check the number of bytes that are currently available for reading. After r/w close stream by calling a `close` method. Closing an output stream also *flushes* the buffer used for the output.

Java uses a **UTF-16**.
