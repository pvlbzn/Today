## Use of bytearray

This is based on Dave Beazley's [blog](http://dabeaz.blogspot.ru/2010/01/few-useful-bytearray-tricks.html) and a logical sequence to [Binary Sequence Type](https://github.com/pvlbzn/Today/blob/master/Jun5/python_binary_sequence_type.md) paper. 

```
s = bytearray(b'help')
s[:0] = b'Some '
> bytearray(b'Some help')

s[0]
> 83

s[0] = b'C'
> TypeError: an integer is required

s.append(ord('?'))
s
> bytearray(b'Some help?')
```

#### Assembly a message

```
msg = b''
# n: number of bytes being received over socket
while n > 0:
	chunk = s.recv(n) 		# Get data
	msg += chunk			# Add data
	n -= len(chunk)
```

The issue is that a `+=` horrible inefficient.

```
msg = bytearray()
while n > 0:
	chunk = s.recv(n) 		# Get data
	msg.extend(chunk) 		# Add data
	n -= len(chunk)
```

#### Binary Record Packing
Consider a problem:

```
import struct

# points = [(24, 35), ..., (122, 12)]
f = open('points.bin', 'wb')
f.write(struct.pack('I', len(points)))
for x, y in points:
	f.write(struct.pack('II', x, y))
f.close()
```

Better approach is:

```
import struct

f = open('points.bin', 'wb')
msg = bytearray()
msg.extend(struct.pack('I', len(points)))
for x, y in points:
	msg.extend(struct.pack('II', x, y))
f.write(msg)
f.close()
```

Second version runs much faster because it writes only once whole thing, not many times by small piece.


#### Simple XOR Cipher

```
key = 88
msg = bytearray(b'A simple cipher.')
enc = bytearray(char ^ key for char in msg)

> bytearray(b'\x19x+15(4=x;1(0=*v')

dec = bytearray(char ^ key for char in enc)

> bytearray(b'A simple cipher.')

```
