# Monads
In FP monads are a way to build programs by joining simple components in predictable and robust way. A monad encapsulates values of a particular data type creating a new type associated with a specific computation. This computation followa s set of math axioms called monad laws.

In terms of OO programming a monad is an interface (mixin) parameterized by a type with a two methods: `return` and `bind` that describe:

- How to inject a value to get a monadic value of that injected value type
- How to use a function that makes a monadic value from a non-monadic one

The monad is similar to `IEnumerator` or `IIterator` in that it takes a type that itself takes a type. Main point of monad is being able to connect operations based on the interior type.


*Today I learned that monads topic is by far longer than 1 hour of learning*.
