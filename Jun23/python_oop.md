## OOP

From the documentation:
> Python classes provide all the standard features of Object Oriented Programming: the class inheritance mechanism allows multiple base classes, a derived class can override any methods of its base class or classes, and a method can call the method of a base class with the same name. Objects can contain arbitrary amounts and kinds of data. As is true for modules, classes partake of the dynamic nature of Python: they are created at runtime, and can be modified further after creation.

By default members are public, all members functions are *virtual* (can be overriden). Everything is an object, as well as classes are.

```
# A new class definition looks like:

class ClassName(object):
    '''
    Docstring
    '''
    
    # Note, explicit self parameter
    def __init__(self, p1, p2):
        '''
        Docstring
        '''
        self.p1 = p1
        self.p2 = p2

    def method(self, n):
        pass
```

Python uses explicit `self`, rather than implicit like Java do. `self` is a reference to the object.

#### Class, Static Methods

```
# Static method is method without self
class Math(object):
    ...
    @staticmethod
    def square(n):
        return n**2

# Class method:
class Vehicle(object):
    ...
    @classmethod
    def is_motorcycle(cls):
        return cls.wheels == 2
```

#### Inheritance
Imagine abstract class Vehicle and two object which are Vehicle: Car, Truck. The syntaxis of the inheritance is for a parent `class Vehicle(object)` and `class Car(Vehicle)` for a child.

