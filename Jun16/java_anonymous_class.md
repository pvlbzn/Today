## Anonymous Class
More accurate name is anonymous inner classes, because anonymous class can not be top-level class. Thus, anonymous classes are declared inside another class.

```
public class Anonymous {

    public void addTwo(int i) {
        System.out.print(i+2);
    }

}


public class Overr {

    public static void main(String[] args) {
        Anonymous a1 = new Anonymous() {
            @Override
            public void addTwo(int i) {
                System.out.println(i+5);
            }
        };
        a1.addTwo(2);

        Anonymous a2 = new Anonymous();
        a2.addTwo(2);
    }

}
```

`a1` will print 7, `a2` will print 4. Idea is clear.

```
Anonymous a3 = new Anonymous() {
    // You can not call it because this is an anonymous
    // subclass of Anonymous and multiplyTwo isn't
    // defined in superclass. In other words, a3 reference
    // has no multiplyTwo method, but it has addTwo, which
    // is overriden, thus overriden method will be called.
    public void multiplyTwo(int i) {
        System.out.println(i*2+"\n");
    }

    @Override
    public void addTwo(int i) {
        System.out.println(i+5+"\n");
    }
};
```

`a3` can not call multiplyTwo. However this method can be called on object directly:

```
new Anonymous() {
    public void multiplyTwo(int i) {
        System.out.println(i*2+"\n");
    }

    @Override
    public void addTwo(int i) {
        System.out.println(i+5+"\n");
    }
}.multiplyTwo(5);
```

That means that in `a3` (as a class of the original `Anonumous`) **api** method **`multiplyTwo(int i)`** will not be present, however it will exist.

Using reflection against `a3` proves that actually `a3` object has `multiplyTwo(int i)` method:

```
System.out.println(a3.getClass().getMethods()[1].toString());
```

Prints:

```
public void main.java.com.pvlbzn.Lambda.Overr$2.multiplyTwo(int)
```


---

#### Decompiler

In decompiler original `Anonymous` class looks like:

```
class Anonymous {
    Anonymous() {
    }

    public void addTwo(int var1) {
        System.out.println(var1 + 2 + "\n");
    }
}
```

And construction with overriding looks like:

```
final class Overr$2 extends Anonymous {
    Overr$2() {
    }

    public void multiplyTwo(int var1) {
        System.out.println(var1 * 2 + "\n");
    }

    public void addTwo(int var1) {
        System.out.println(var1 + 5 + "\n");
    }
}
```

So, anonymous class *extends* base class.
