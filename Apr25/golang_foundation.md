###Quick Golang refreshers

####vars

```
var n1, n2, n3 type

var n4 tupe = value

var n5, n6, n7 := v1, v2, v3

// Blank is a special name
_, n8 := 45, 87
```

<br>

####consts
Constants are determined during compile time.

```
const Pi float32 = 3.1415926
const Pi = 3.1415926
```

<br>

####num types
Go has a `int` and `uint`. On 32bit host os they are 32bits, on 64bit host os they are 64bits. Also Go has more exact types: `int8, int16, int32, in64, uint8, uint16, uint32, uint64` and `rune, byte` where `rune` is an alias of `int32`, `byte` of `uint8`. Complex numbers: `complex128, complex64`.

```
func main() {
    var v1 int32 = 15
    var v2 int8 = 15
    fmt.Println(v1 + v2)
}

// -> invalid operation: v1 + v2 (mismatched types int32 and int8)
```

Go actually cares about types, and it do it in a right way:

```
func main() {
    var v1 int32 = 15
    var v2 int32 = 6
    fmt.Println(v1/v2)
}

// -> 2
```

Because `int32/int32 = int32`, not a `float32`.

<br>

####strings
Blog Golang [strings](https://blog.golang.org/strings).

<br>

####arrays
Blog Golang [arrays, slices, strings](http://blog.golang.org/slices).

Arrays not used often because the size of an array if part of its type.

```
// byte is an alias for uint8.
var buffer256 [256]byte
var buffer512 [512]byte
```

This buffer looks like this in memory, `buffer: byte byte ... 252/508 times more ... byte byte`. Elements can be accessed using common zero-index `buffer[255]`. Accessing `buffer[256]` will crash the program.

```
len(buffer256)

// -> 256
```

Most common arrays purpose in Go is to hold storage for a slice.

**UPD (April 27)**:

- Arrays are values. Assign one array to another copies all the elements.
- If you pass an array to a function, it will receive a cope of the array, not a pointer to it.
- The size of an array is part of its type.

[10]int in dictinct from [20]int.

####slices
>A slice is a data structure describing a contiguous section of an array stored separately from the slice variable itself. A slice is not an array. A slice describes a piece of an array.

```
var slice []byte = buffer256[100:150]

// Inside a function:
slice := buffer[100:150]
```

For now think of a slice as a little data structure:

```
// Illustration:
type sliceHeader struct {
    Length          int
    ZerothElement   *byte
}

slice := sliceHeader{Length: 50, ZerothElement: &buffer256[100],}
```

Slice a slice:

```
slice2 := slice[5:10]

// Illustration:
slice2 := sliceHeader{Length: 5, ZerothElement: &buffer256[105],}
```

Header still points to the same underlying array, stored in the `buffer256` variable.

```
slice = slice[5:10]

// Reslice: slice a slice:
slice = slice[1:len(slice)-1]

// Illustration:
slice := sliceHeader{Length: 4, ZerothElement: &buffer256[106],}
```

*Slice Header* is what's really stored in a slice variable.

**Passign slices to a func**:
Even though a slice contains a pointer, it is itself a value. Under the covers, it is a struct value holding a pointer and a length. It isnt a pointer to a struct. When you call a function that takes a slice as an argumenta, copy of the header is what gets passed to the function.

>Even though the slice header is passed by value, the header includes a pointer to elements of an array, so both the original slice header and the copy of the header passed to the function describe the same array. Therefore, when the function returns, the modified elements can be seen through the original slice variable.

**Pointers to slices**:

```
func PtrSubtractOneFromLength(slicePtr *[]byte) {
    slice := *slicePtr
    *slicePtr = slice[0 : len(slice)-1]
}

func main() {
    fmt.Println("Before: len(slice) =", len(slice))
    PtrSubtractOneFromLength(&slice)
    fmt.Println("After:  len(slice) =", len(slice))
}
```

Another exmpl:

```
package main

import (
    "fmt"
    "bytes"
    )

type path []byte

func (p *path) TruncateAtFinalSlash() {
    i := bytes.LastIndex(*p, []byte("/"))
    if i >= 0 {
        *p = (*p)[0:i]
    }
}

func main() {
    pathName := path("/usr/bin/tso") // Conversion from string to path.
    pathName.TruncateAtFinalSlash()
    fmt.Printf("%s\n", pathName)
}
```

If we'll pass a value rather than a pointer function wont work as intended because function will recieve a copy of the header, modify it and thats it. Original header will not be modified.

```
func (p path) TruncateAtFinalSlash() path {
    i := bytes.LastIndex(p, []byte("/"))
    if i >= 0 {
        p = (p)[0:i]
    }
    return p
}
```

Will return a new header, and this header will contain a pointer to expected array.

**Capacity**:
Third component of the slice header: capacity.

```
type sliceHeader struct {
    Lenght          int
    Capacity        int
    ZerothElement   *byte
}
```

>The Capacity field records how much space the underlying array actually has; it is the maximum value the Length can reach. Trying to grow the slice beyond its capacity will step beyond the limits of the array and will trigger a panic.


