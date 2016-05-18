### .java

```
// Original java code

public class Some {
    public static void main(String[] args) {
        int x = 5;
        int y = 12;
        int j = x + y;
        System.out.print(j);
    }
}
```

### .class

```
// Compiled java bytecode

cafe babe 0000 0034 001b 0a00 0500 0e09
000f 0010 0a00 1100 1207 0013 0700 1401
0006 3c69 6e69 743e 0100 0328 2956 0100
0443 6f64 6501 000f 4c69 6e65 4e75 6d62
6572 5461 626c 6501 0004 6d61 696e 0100
1628 5b4c 6a61 7661 2f6c 616e 672f 5374
7269 6e67 3b29 5601 000a 536f 7572 6365
4669 6c65 0100 0953 6f6d 652e 6a61 7661
0c00 0600 0707 0015 0c00 1600 1707 0018
0c00 1900 1a01 0004 536f 6d65 0100 106a
6176 612f 6c61 6e67 2f4f 626a 6563 7401
0010 6a61 7661 2f6c 616e 672f 5379 7374
656d 0100 036f 7574 0100 154c 6a61 7661
2f69 6f2f 5072 696e 7453 7472 6561 6d3b
0100 136a 6176 612f 696f 2f50 7269 6e74
5374 7265 616d 0100 0570 7269 6e74 0100
0428 4929 5600 2100 0400 0500 0000 0000
0200 0100 0600 0700 0100 0800 0000 1d00
0100 0100 0000 052a b700 01b1 0000 0001
0009 0000 0006 0001 0000 0001 0009 000a
000b 0001 0008 0000 0039 0002 0004 0000
0011 083c 100c 3d1b 1c60 3eb2 0002 1db6
0003 b100 0000 0100 0900 0000 1600 0500
0000 0300 0200 0400 0500 0500 0900 0600
1000 0700 0100 0c00 0000 0200 0d
```

### .javap
`javap` - Java class file disassembler. `.class` file is like an assembly, but for a JVM.

```
$ javap Some

public class Some {
  public Some();
  public static void main(java.lang.String[]);
}
```

```
$ javap -c Some

public class Some {
  public Some();
    Code:
       0: aload_0
       1: invokespecial #1   // Method java/lang/Object."<init>":()V
       4: return

  public static void main(java.lang.String[]);
    Code:
       0: iconst_5
       1: istore_1
       2: bipush        12
       4: istore_2
       5: iload_1
       6: iload_2
       7: iadd
       8: istore_3
       9: getstatic     #2                  // Field java/lang/System.out:Ljava/io/PrintStream;
      12: iload_3
      13: invokevirtual #3                  // Method java/io/PrintStream.print:(I)V
      16: return
}
```

### Analyze
These instructions are [JVM Instructions](https://docs.oracle.com/javase/specs/jvms/se7/html/jvms-6.html). 

I'll try to understand whats going on:

`iconst_<i>` push the int constant `i` onto the operand stack.
`iconst_5 = 8 (0x8)`

`istore_<n>` stores int into local variable. `n` must be an index into the local variable array of the current frame.
`istore_1 = 60 (0x3C)`
`istore_2 = 61 (0x3D)`
`istore_3 = 62 (0x3e)`

`bipush` - push byte. 12?

`iload_<i>` - load int from local variable.
`iload_1 = 27 (0x1b)`
`iload_2 = 28 (0x1c)`
`iload_3 = 29 (0x1d)`

`iadd` - add int.

`getstatic` - get static field from class.

`invokevirtual` - invoke instance method, dispatch based on class.

Things are easy, despite I can not understand why `iconst_5` is 8. This code reads as:

Push int constant `i` onto the operand stack. 5 is pushed. Store `int` into local variable. 5 stored into the variable, which is represented by index from the *operand stack*. Push byte onto the operand stack. 12 is pushed. 12 is stored in operand stack. Load first and second value from operand stack. Add int. Store `int` into local variable. Get static field from class: `io/PrintStream`. Invoke instance method: `PrintStream.print:(I)V`. Return.




