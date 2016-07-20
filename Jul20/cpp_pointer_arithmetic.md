## Pointer Arithmetic
Pointer is a address's numeric value, therefore some arithmetic can be applied on these numbers. There are four arithmetic operators taht can be used on pointers:

- ++
- --
- +
- -

{@see ./arthm.cpp}

Function `void sample_one(int *ptr)` will produce

```
Address of arr[0] = 0x7fff58a886fc
Value of arr[0] = 1

Address of arr[1] = 0x7fff58a88700
Value of arr[1] = 2

Address of arr[2] = 0x7fff58a88704
Value of arr[2] = 3
```

Call to the `void sample_next(int *ptr)` will produce

```
Last member has 0x7fff58a88704 address
Value: 3
```
