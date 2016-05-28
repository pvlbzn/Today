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



#### Disassembly

Consider the following code:

```
public static void main(String[] args) {
    int[] arr1 = new int[20];
    arr1[12] = 214;
    arr1(arr1);

    char[] arr2 = {'x', 'й'};
    arr2(arr2);

    System.out.println(arr1[12]);
    System.out.println(arr1[0]);

    System.out.println(arr2[0]);
}

public static void arr1(int[] arr) {
	arr[0] = 42;
}

public static void arr2(char[] arr) {
	arr[0] = 'a';
}
```

Use `javap -c`, meaningless code omited

```
// Push 20 onto operand stack.
0: bipush        20
// Create new int array [count, arrayref]. 20 popped off the operand stack.
2: newarray       int
// Store reference (I guess this arrayref) into lcoal variable.
4: astore_1
// Load reference from local variable.
5: aload_1
// Push 12 into operand stack.
6: bipush        12
// Push short. 
8: sipush        214
// Store into int array
11: iastore
// Load reference from local variable.
12: aload_1
// Call the method arr1.
13: invokestatic  #2                  // Method arr1:([I)V


// Push int constant, which is 2, which is the size of an array
16: iconst_2
// Create new char array. 2 popped off the operand stack.
17: newarray       char
// Duplicate the top operand stack value and push the duplicated
// value onto the operand stack. This, I guess, represent
// an arrayref for castore.
19: dup
// Push int constant, which is 0, which is the size of an array.
// This represent a index for castore.
20: iconst_0
// Push 120 onto operand stack. This represent a value for castore.
21: bipush        120
// Store into char array. The arrayref must be of type reference.
// The arrayref, index and value are popped from the operand stack.
23: castore
// arrayref
24: dup
// Index
25: iconst_1
// Value
26: sipush        1081
29: castore
30: astore_2
31: aload_2
32: invokestatic  #3                  // Method arr2:([C)V

// Print functions.

35: getstatic     #4                  // Field java/lang/System.out:Ljava/io/PrintStream;
38: aload_1
39: bipush        12
41: iaload
42: invokevirtual #5                  // Method java/io/PrintStream.println:(I)V
45: getstatic     #4                  // Field java/lang/System.out:Ljava/io/PrintStream;
48: aload_1
49: iconst_0
50: iaload
51: invokevirtual #5                  // Method java/io/PrintStream.println:(I)V
54: getstatic     #4                  // Field java/lang/System.out:Ljava/io/PrintStream;
57: aload_2
58: iconst_0
59: caload
60: invokevirtual #6                  // Method java/io/PrintStream.println:(C)V
63: return

public static void arr1(int[]);
Code:
0: aload_0
1: iconst_0
2: bipush        42
4: iastore
5: return

public static void arr2(char[]);
Code:
0: aload_0
1: iconst_0
2: bipush        97
4: castore
5: return
```


This is the exact reason why to mess with even such a simple topic is useful and meaningful. Lesson learned: the best source of information about Java from a low-level perspective is the Java Language Reference, and Java Virtual Machine Reference.

