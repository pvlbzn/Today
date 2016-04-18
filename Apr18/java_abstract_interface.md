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

-

**UPD**:
One more 'real life example' about OO concepts:

>How about an analogy: when I was in the Air Force, I went to pilot training and became a USAF (US Air Force) pilot. At that point I wasn't qualified to fly anything, and had to attend aircraft type training. Once I qualified, I was a pilot (Abstract class) and a C-141 pilot (concrete class). At one of my assignments, I was given an additional duty: Safety Officer. Now I was still a pilot and a C-141 pilot, but I also performed Safety Officer duties (I implemented ISafetyOfficer, so to speak). A pilot wasn't required to be a safety officer, other people could have done it as well.

>All USAF pilots have to follow certain Air Force-wide regulations, and all C-141 (or F-16, or T-38) pilots 'are' USAF pilots. Anyone can be a safety officer. So, to summarize:

>Pilot: abstract class
C-141 Pilot: concrete class
ISafety Officer: interface
