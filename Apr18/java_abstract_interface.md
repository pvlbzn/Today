####Abstract Class/Method

**Class**:

- Abstract class cant be instantiated
- Abstract class can be subclassed
- It may include abstract methods

When an abstract class is subclassed, the subclass usually provides impl for all of the abstract methods in its superclass. If not, then the subclass must be also abstract.

**Method**:

- Abstract method declasred without an impl


The purpose of an abstract class is to function as a base for subclasses.

####Abstract stuff vs Interfaces

Interface is essentially a *type* that can be satisfied by any class that implements the interface. Any class that impl an interface:

- It must have `implements InterfaceName`
- It must actually implement an interface

Abstract classes are meant to be *inherited* from. Interfaces are meant to be *implemented*.

**Actual difference**: Subclass of an abstract class has a strong relationship between abstract class and itself. Idiotic examples with cars/animals/etc in OO: abstract class `Canine`, any deriving class *should* be an animal that belongs to the Canine family. On another hand - interface `Iterable`, it actually doesnt matter what will be `Iterable` dogs, worlds, ghosts.
