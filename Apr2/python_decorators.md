###[PEP 255](https://www.python.org/dev/peps/pep-0255/), generators, yield

> The yield statement may only be used inside functions.  A function that contains a yield statement is called a generator function.  A generator function is an ordinary function object in all respects, but has the new CO_GENERATOR flag set in the code object's co_flags member.



A decorator is a fucntion or a class that wraps (decorates) a function or a method. The 'decorated' function or method will replace the original 'undecorated' function or method.

```
def foo():
	# Do something.

def decorator(func):
	# Manipulate.
    return func

@decorator
def bar():
	# Do something.
	# bar() is decorated.
```

This mechanism is useful for separationg concerns and avoiding external unrelated logic polluting the core logic of the function or method. For example: Flask uses decorators heavily.