###Strings and Bytes

String is an immutable sequence of Unicode characters. Bytes object is an immutable sequence of numbers 0-255.



[String and Bytes literals](https://docs.python.org/3/reference/lexical_analysis.html#strings).

```
b = b'a'
b[0]
>> 97

c = RB'bca'
c[2]
>> 97

d = rB'Ц'
>> SyntaxError: bytes can only contain ASCII literal characters.
```

SyntaxError because, bytes is … bytes. 0 - 255. Byte.



