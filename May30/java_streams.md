## Streams
In the Java API, an object from which byte sequence can be readed is called an *input stream*. An object to which byte sequence can be written is called an *output stream*.

From input. To output.

Abstract `InputStream` and abstract `OutputStream` are about bytes. Abstract `Reader` and abstract `Writer` are about Unicode.

Methods `read` and `write` block until the byte is actually processed. If stream cant immediately be accessed, for example because of a network, the current thread block.

After use, `close` opened streams. Closing an `OutputStream` also flushes the buffer used for the output stream.

Java has more than 60 different stream types, so before use some stream better to check is this one is most suitable or not. Almost always, *in Java*, best way to do some task using API and better to do not touch low-level.

It's look like Java's interfaces have a naming convention about Stuff**able** suffix if interface has only one method, like in Golang with Stuff**er** suffix. It is not a statement, it is an assumption.

The way to use streams is to combine them:

```
FileInputStream fileIn = new FileInputStream("file");
DataInputStream dataIn = new DataInputStream(fileIn);
int n = dataIn.readInt();
```

Multiple capabilities can be achieved by nesting. By default streams are not buffered, which means that every call to `read` asks the OS to give out yet another byte. It's more efficient to request a block of data and put it into the buffer. 

```
DataInputStream dataIn = new DataInputStream(
		new BufferedInputStream(
				new FileInputStream("file")
		));
```

Thus, DataInputStream object will use buffered `read` method.

In need of capabilities of two streams, use two references:

```
DataInputStream dataIn = new DataInputStream(
		pushback = new PushbackInputStream(
				new BufferedInputStream(
						new FileInputStream("file)
				)));
```

TODO: [I/O](http://docs.oracle.com/javase/tutorial/essential/io/).
