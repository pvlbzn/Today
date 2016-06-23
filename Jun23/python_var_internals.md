## Call-by-What
Python is not call-by-value nor call-by-reference. In Python *object refereces are passed by value*. The parameter passed in is actually a reference to an object and this reference is passed by value.

#### Mutability
Some objects are mutable, some not. If you pass a mutable object into a method, reference, you can mutate the object.

#### So What?
Variables are about binding. They contain only a reference. They can mutate mutable objects accessing them by reference, but when variable is rebinded it has a new reference value in it. Actually the same this as in Java.
