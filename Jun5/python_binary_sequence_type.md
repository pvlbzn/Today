## Binary Sequence Type

`bytes`, `bytearray`, `memoryview`.

>The core built-in types for manipulating binary data are bytes and bytearray. They are supported by memoryview which uses the buffer protocol to access the memory of other binary objects without needing to make a copy.

Following is true for Python 3.5

#### `bytes`
Bytes objects are immutable sequence of single bytes. Bytes objects offer several methods that are only valid when working with ASCII data and are closely related to string objects in a variety of ways.

```
b`Same rules as "strings" have`
b'''3 single quotes'''
```

Only ASCII characters are permited in bytes literals. Any binary values over 127 must be entered into bytes literals using the '\' escape sequence.

Byte literals and representation are based on ASCII text, but bytes objects actually behave like **immutable sequences of integers, where is each value `0 <= x < 256`**.

```
# A zero-filled bytes object of a specified length
bytes(n)

# From iterable of integers
bytes(range(20))

# Via the buffer protocol
bytes(obj)
```

Since bytes objects are sequences of integers, for bytes `b`, `b[0]` will be an integer, while b[0:1] will be a bytes object of length 1.


#### 'bytearray'
Bytearray objects are a mutable counterpart to `bytes` objects. It is always created via constructor.

```
# Empty instance
bytearray()

# Zero-filled instance
bytearray(512)

# From iterable
bytearray(range(1024))

# Copying existing binary data via protocol buffer
bytearray(b'bytearray')
```

`bytearray` is mutable thus it support the [mutable sequence operations](https://docs.python.org/3.5/library/stdtypes.html?highlight=bytearray#typesseq-mutable) in addition to the common bytes and `bytearray` [operations](https://docs.python.org/3.5/library/stdtypes.html?highlight=bytearray#bytes-methods).


#### `memoryview`
Memory view objects allow Python code to access the internal data of an object that supports the [buffer protocol](https://docs.python.org/3.5/c-api/buffer.html#bufferobjects) without the copying.
