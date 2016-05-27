# Errors

- User Input Errors
- Device Errors
- Phycisal Limitations
- Network Errors
- Code Errors

And each of this types has much more specific errors like i/o exception, array out of bound exception, etc.


### Throws

Java allows every method an alternative exit path if something went wrong and normal task flow is unavailable. In this case method doesnt return value - it **throws** an object that incapsulates error information.

While *throws* method exits and doesnt return anything, execution falls into exception handling mechanism which searches for an exception handler that can deal with this particular issue.

### Classification
An exception object is always an instance of `Throwable`. Sure you can create custom exceptions.

```
		Throwable
			|
	+-------+-------+
	|				|
  Error			Exception
```

`Error` is about Java runtime, dont mess with it.

There are different (many-many) `Exception`s are present. Each exception wrapped in their package. For example `java.io` has `IOException` which derives from `Exception` from `java.lang` package, which, as already said, derives from `Throwable`.

`RuntimeException` almost always means that you did something wrong.

### Checked, Unchecked
The JLS calls exceptions of the class (and subclasses of course) `Error` and of the class `RuntimeException` as **unchecked exception** All others are **checked exceptions**.

Method which *throws* telling to Java Compiler what it return and what can go wrong. 

```

```