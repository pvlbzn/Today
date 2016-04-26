###Allocation primitives
Built-in functions `new` and `make`.

Source: [Effective Go](https://golang.org/doc/effective_go.html#allocation_new)

<br>

####new
Built-in function `new` allocates memory. It doesnt *initialize* the memory, it only *zeros* it. `new(T)` allocates zeroed storage for a new item of type `T` and returns its address, a value of type `*T`.

Pronounces like: "It returns a pointer to a newly allocated zero value of type `T`".

```
func NewFile(fd int, name string) *File {
    if fd < 0 {
        return nil
    }
    f := File{fd, name, nil, 0}
    return &f
}
```

It's ok to return the address of a local variable. Storage associated with the variable survives after the function returns.

The expressions `new(File)` and `&File{}` are equivalent.

<br>

####make
The built-in function `make(T, args)` server a purpose different from `new(T)`. It creates slices, maps, and channels only. It returns an initialized (not zeroed) value of type `T`, not `*T`.

The reason that slice, map and channel represents references, under the cover, to data structures that must be initialized before use.

A slice, is a three-item descriptor containing a pointer to the data, the length, and the capacity. Until those items are initialized, the slice is `nil`.

```
// Allocate an array of 100 ints and then create a slice structure
// with length 10 and a capacity of 100 pointing at the first 10 elements
// of the array.
make([]int, 10, 100)
```

In contrast, `new([]int)` returns a pointer to a newly allocated, zeroed slice structure. A pointer to a `nil` slice value.

```
// *p == nil
var p *[]int = new([]int)
// Slice v now refers to a new array of 100 ints
var v  []int = make([]int, 100)

// Unnecessarily complex:
var p *[]int = new([]int)
*p = make([]int, 100, 100)

// Idiomatic:
v := make([]int, 100)
```

####Conclusion
`make` applies only to maps, slices, channels, and doesn't return a pointer. To obtain an explicit pointer allocate with `new` or take the address of a variable explicitly.

