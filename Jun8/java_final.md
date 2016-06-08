## final
`final` is the keyword which used in several differenc contexts. Usually `final` is tought to be constant variable, however in Java `final` means in a way more.

#### Application
The `final` keyword can be applied to

- field
- method
- class

#### Field
`final` field is final, it can not be changed after initialization.

#### Method
`final` keyword in method signature means that this method can't be overriden by subclasses. Programmer may declare all methods as `final` unless you have no good reason to want a polymorphism. 

#### Class
`final` class can not be subclassed.

---

C++ methods dont use a polymorphism unless programmer specifically request it. The good reason is a method resolution and as a consequence - performance, because it is AOT compiled language. Java is JIT and it can optimize stuff much better on runtime. But for sure, polymorphims is expensive.

Also, the `final` keyword plays its role with threading, which will be discussed later.