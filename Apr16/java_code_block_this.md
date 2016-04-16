####Execution Block

```
    public static void executionBlock() {
        System.out.println("Block will be executed?");
        {
            System.out.println(true);
        }
    }
```

Method call `executionBlock()` will print:

```
Block will be executed?
true
```

This is probably better to not use, but good to know how Java sees the world.

####This
Each *non-static* method runs in the context of an object. 

From [javadoc](https://docs.oracle.com/javase/tutorial/java/javaOO/thiskey.html):
>Within an instance method or a constructor, this is a reference to the current object — the object whose method or constructor is being called. You can refer to any member of the current object from within an instance method or a constructor by using this.

Programming language with OO paradigm usually have to make a choice how to pass a context. Java preffered implicit `this`. Python prefers explicit.

As states in 'Core Java', `this` is an implicit first parameter in a method.
