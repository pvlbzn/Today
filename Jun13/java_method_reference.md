## Method Reference
Method reference gives a method reference, without executing this method. It is described using `::` syntax. It can be used to point to the following types:

- Static methods
- Instance methods
- Constructors using Class::new

#### Usage
```
List names = new ArrayList<>();
names.add("Jack");
names.add("James");
names.add("Jacob");
names.add("Jamal");

names.forEach(System.out::println);
```

This will print all the names.
