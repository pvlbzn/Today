## Compound Assignment Operators
In most of emperial languages compound operators are present, such as `+=`, `*=`, etc.

Consider following code:

```
class Cast {
	
	public static void main(String []args) {
		int i  = 8;
		i += 12.9;
		System.out.println(i);
	}

}
```

It will print 20, not 20.9 nor 21.

### Why
Who need a [specs](http://docs.oracle.com/javase/specs/jls/se8/html/jls-15.html#jls-15.26.2) while you have a **disassembler**?

```
// Dropped everything meaningless for case study

0: bipush        8
2: istore_1
3: iload_1
4: i2d
5: ldc2_w        #2                  // double 12.9d
8: dadd
9: d2i
10: istore_1

```

Againg, using [JVM Instruction Set](https://docs.oracle.com/javase/specs/jvms/se8/html/jvms-6.html) lets find out whats going on.

```
bipush		- push the byte. The immediate byte is sign-extedede
			  to an int value. That value is pushed onto the
			  operand stack.

istore_<n>	- store int into local valiable. n must be an 
			  index into the local variable array of the
			  current frame. The value on top of the operand
			  stack must be of type int.

iload_<n>	- load int from local variable. n must be an index
			  into the local varibale array of the current frame.
			  Must be an int. The value at n is pushed onto the
			  operand stack.

i2d			- convert int to double. Value on the top of the
			  operand stack must be int. Value converted to a
			  double result, result is pushed onto the operand
			  stack.

ldc2_w		- push long or double from run-time constant pool, wide
			  index.

dadd		- add double.  Both v1 and v2 must be of type double. 

d2i			- convert double to int.
```

So, what is going on:

8 `int` pushed onto operand stack, stored into a local variable. `int` loaded from local variable and pushed onto the operand stack, converted to `double` and result pushed onto the operand stack. 12.9d pushed to the operand stack from run-time constant pool. `v1` and `v2` added, result converted to `int` and stored in the original local variable of the type `int`.

Thus, the `i += 12.9` basically equals to `i = (int)((double)i + 12.9)`. Similar thing actually written in specs:

>A compound assignment expression of the form E1 op= E2 is equivalent to E1 = (T) ((E1) op (E2)), where T is the type of E1, except that E1 is evaluated only once.