### Static

Consider following: 

```
class SnS {
	
	class NonStaticInner {
	}

	static class StaticInner {
	}

	public List<Object> create() {
		return Arrays.asList(
			new NonStaticInner(),
			new StaticInner()
			);
	}
}
```

Compilation to bytecode, usign `javac`, produces `SnS.class`, `SnS$NonStaticInner.class`, `SnS$StaticInner.class`.

Lets take a look what these classes are:

```
$ javap -c SnS

...
0: iconst_2
1: anewarray     #2                  // class java/lang/Object
4: dup
5: iconst_0
6: new           #3                  // class SnS$NonStaticInner
9: dup
10: aload_0
11: invokespecial #4                  // Method SnS$NonStaticInner."<init>":(LSnS;)V
14: aastore
15: dup
16: iconst_1
17: new           #5                  // class SnS$StaticInner
20: dup
21: invokespecial #6                  // Method SnS$StaticInner."<init>":()V
24: aastore
25: invokestatic  #7                  // Method java/util/Arrays.asList:([Ljava/lang/Object;)Ljava/util/List;
28: areturn
...
```

Ok, without even knowing what these commands do, it is clear that `NonStaticInner` class doing more than `StaticInner`. Non-static class goes first. I tried to change source code, where I placed static class firs, result was the same - non-static class goes first.

`NonStaticInner` uses 7 commands, while `StaticInner` uses 4. 

#### NonStaticInner

```
new           #3                  // class SnS$NonStaticInner
dup
aload_0
invokespecial #4                  // Method SnS$NonStaticInner."<init>":(LSnS;)V
aastore
dup
iconst_1
```

`new` 			- create new object.
<br>
`dup`			- duplicate the top operand stack value and push the duplicated value onto the operand stack.
<br>
`aload_<n>` 	- load reference from local variable.
<br>
`invokespecial` - invoke instance method. Here this method is a constructor.
<br>
`aastore` 		- store into reference array.
<br>
`dup`			- duplicate the top operand stack value and push the duplicated value onto the operand stack.
<br>
`iconst_<n>`	- push the int constant `<i>` onto the operand stack.		

#### StaticInner

```
new           #5                  // class SnS$StaticInner
dup
invokespecial #6                  // Method SnS$StaticInner."<init>":()V
aastore
```

`new` 			- create new object.
<br>
`dup`			- duplicate the top operand stack value and push the duplicated value onto the operand stack.
<br>
`invokespecial` - invoke instance method. Here this method is a constructor.
<br>
`aastore` 		- store into reference array.

#### Difference
Static class doesnt load reference from local variable, doesnt duplicate top operand stack value after storing into reference array, doesnt push some `int` constant onto operand stack.

#### What The
As explained [here](http://stackoverflow.com/questions/3106912/why-does-android-prefer-static-classes?rq=1) (from this place I took an inspiration to do this research), the difference is that *non-static inner class* **does**  store an implicit reference to the enclosing object, while *static inner class* **does not**.

```
class SnS$NonStaticInner {
	private final SnS this$0;
	SnS$NonStaticInner(SnS enclosing) {
		this$0 = enclosing;
	}
}
class SnS$StaticInner {
	SnS$StaticInner(){}
}
```