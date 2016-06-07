## Three Whales of OOP

1. Encapsulation
2. **Inheritance**
3. **Polymorphism**

#### Inheritance: "is a"
The idea behind inheritance that new classes can extend existing ones. When you inherit from an existing class, you reuse its methods, fields, and you can write your own methods as well.

A standard example of inheritance: `Driver` or `Pilot` **is a** `Employee`.

This can be expressed in Java syntax as follows:

```
public class Pilot extends Employee {
	;
}
```

`Pilot` is a *subclass*, `Employee` is a *superclass*. More general stuff goes to `Employee` superclass, more specific stuff goes to `Employee` subclass(es).


#### Overriding
Some methods from superclass isn't works well on every subclass. `Pilot` may have a some sort of salary bonus for a saved fuel or whatever. This paramener must counts in superclass's method `getSalary()`. It is a right case of an *overriding* concept.

```
public double getSalary() {
	return super.getSalary() + bonus;
}
```

`super` is not a reference, `super` is a keyword which is directs the compiler to invoke the superclass's method.

##### Overriding Resolution
OR is a compiler process where the compiler choose a right method from *methods signatures*. Method `foo(int)` has the same name with method `foo(String)`, but the different *method signature*.

#### Constructor
Subclass constructor can use superclass constructor:

```
public Pilot(String name, double salary) {
	super(name, salary)
}
```

Because of an encapsulation subclass can not access superclass private fields, so it should initialize it using superclass constructor. If subclass constructed without `super` then no arguments constructor of the superclass will be invoked.

#### Polymorphism
Object variable can refer to multiple actual types.

```
// arr is an array of Drivers, Pilots and Employees
for (Employee empl : arr) {
	out.println(empl.getSalary());
}
```

It will work because of polymorphism. Each object will return their salary according to overloading features. Automatic selection of an approptiate method at the runtime is called *dynamic binding*.

In Java object variables are polymorphic.

```
Employee e;
e = new Pilot();
```

Superclass type variable can refer to superclass object or to any of subclass objects.
