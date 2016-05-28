## Array
An array is a container object which holds fixed number of values of a single type. Arrays are objects. Arrays are allocated in the `heap` using the `new` operator. In the `heap` array block of memory is made of all the elements together.

Variables contained in an array have no names but they are referenced by array access expressions - non-negative int values. These vars called *components*. All the *components* of an array have the same type. The element type of an array may be any any type, primitive or reference.

```
byte[] foo, bar, baz[]
// Is equivalent to:
byte foo[], bar[], baz[][]
```

`foo` holds a reference to an object. Declaration doesnt create an array object or allocate any space.

```
int[] a = new int[15];
int[] b = new int[25];
b = a;
```

`b` will point to `a` object on the heap. This is legit because length is not part of the type.

An array is created by an array creation expr or initializer. It specifies **the element type, the number of levels of nested arrays, and the length of the array**. The arrays length is available as a `final` instance variable `length`.

```
float f = 4f;
a[f];
```

Ligit. Because of the unary numeric promotion.

Array of `char`s is **not** a `String`.
