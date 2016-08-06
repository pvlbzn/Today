## Polymorphism
There are three main conceptions in OOP:

- Inheritance
- Encapsulation
- Polymorphism

First two are straightforward to understand. Third one, polymprphism, required some clarification.

Good real life analogy of polymorphism - *water*. It can be fluid, liquid, frozen, but it is always still a water in its nature.

## Polymorphism in Java
Java supports four kinds of the polymorphism:

1. Coercion
2. Overloading
3. Parametric
4. Subtype

#### Coercion
Coercion refers to a *type coercion* which is another name for an *implicit type cast*. *Type cast* is a way of changin an entity of one data type into another.

Each PL has its own rules about type casting. [Java casting conversions](https://docs.oracle.com/javase/specs/jls/se7/html/jls-5.html#jls-5.5).

```
int n1 = 15;
double n2 = 25.;

System.out.println(n1 + n2);        // 40.0
```

#### Overloading
For example operator overloading. Operator `+` can be used to add integers, to add floating point numbers, to concatenate string. Methods also can be overloaded. Android framework uses overloadings heavily.

```
class Parent {
    public void original() {
        System.out.println("1");
    }
}

class Child extends Parent {
    @Override
    public void original() {
        super.original();
        System.out.println("2");
    }
}
```

`original` method call on instance of the `Parent` class will print `1` while call on instance of the `Child` class will print both `1` and `2`.

