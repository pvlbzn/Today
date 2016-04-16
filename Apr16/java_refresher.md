###Java Refreshers
Perhaps, I'm going to write a **Java Refreshers series** for a few days, because:

- I found that I having some miss understandings with reading well-written Java code.
- I want to write kind of 'idiomatic' Java code, at least do my best.

The most difficult part of learning (properly, not syntax) various languages is to teach yourself to think in this language, **be idiomatic**. This point is important in every PL, however, I think that you have to put even more intentions to be 'idiomatic' in bloated / extremely bloated PL like Java.

####Primitives, Objects, Pass-by-What
Here is a lot of things going on, these topics are related, better I'll write some examples:

Find code in `/Refreshing.java` 

```
Integer n1 = new Integer(5);
Integer n2 = new Integer(5);

n1 == n2 			// False
```

Because here is comparasion between two values which holds addresses.

Java is pass-by-**value**:

- For *primitive* arguments (int, float, ..) the pass-by-value is the **actual value** of the primitive.
- For *object*, the pass-by-value is the **value of the reference** to the object.

An old example of these statements is:

```
public static void main( String[] args ){
    Dog aDog = new Dog("Max");
    foo(aDog);

    if (aDog.getName().equals("Max")) { //true
        System.out.println( "Java passes by value." );

    } else if (aDog.getName().equals("Fifi")) {
        System.out.println( "Java passes by reference." );
    }
}

public static void foo(Dog d) {
    d.getName().equals("Max"); // true

    d = new Dog("Fifi");
    d.getName().equals("Fifi"); // true
}
```

####Primitive Versus Class

Lesson: prefer primitives to boxed primitives, and watch out for unintentional autoboxing.

Joshua Bloch's example:

```
// Hideously slow program! Can you spot the object creation?
public static void main(String[] args) {
    Long sum = 0L;
    for (long i = 0; i < Integer.MAX_VALUE; i++) {
         sum += i;
    }
    System.out.println(sum);
}
```

>If you will replace “Long” with “long” - you will improve performance from 43 sec to 6.8 sec.
