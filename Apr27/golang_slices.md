####Slices
A logical sequel of [this](https://github.com/pvlbzn/Today/blob/master/Apr25/golang_foundation.md) topic on Golang foundations.

How to grow slice beyond its capacity? No way. However this can be achieved an equivalent result by allocating a new array, copying the data over, and modifying the slice to describe the new array.

**Allocation**: `make(type, len, cap)`. 

```
slice := make([]int, 10, 15)
```

Allocate a new slice with a length 10 with a room for 5 more, with a capacity of 15.

Double the capacity:

```
s := make([]int, 10, 15)
newS := make([]int, len(s), 2*cap(s))
for i := range s {
    newS[i] = s[i]
}
s = newS
```

**Copy**: Go has a built-in function `copy`. Its argumets are two slices. It copies the data from right-hand argument to the left-hand argument.

```
newS := make([]int, len(s), 2*cap(s))
copy(newS, s)
```

**Append**:

Self-documenting code:

```
func Extend(slice []int, element int) []int {
    n := len(slice)
    if n == cap(slice) {
        // Slice is full; must grow.
        // We double its size and add 1, so if the size is zero we still grow.
        newSlice := make([]int, len(slice), 2*len(slice)+1)
        copy(newSlice, slice)
        slice = newSlice
    }
    slice = slice[0 : n+1]
    slice[n] = element
    return slice
}
```

```
// Append appends the elements to the slice.
// Efficient version.
func Append(slice []int, elements ...int) []int {
    n := len(slice)
    total := len(slice) + len(elements)
    if total > cap(slice) {
        // Reallocate. Grow to 1.5 times the new size, so we can still grow.
        newSize := total*3/2 + 1
        newSlice := make([]int, total, newSize)
        copy(newSlice, slice)
        slice = newSlice
    }
    slice = slice[:total]
    copy(slice[n:], elements)
    return slice
}
```

<br>

####The built-in function
>A weakness of Go is that any generic-type operations must be provided by the run-time. Some day that may change, but for now, to make working with slices easier, Go provides a built-in generic append function. It works the same as our int slice version, but for any slice type.

