### Importance of Testing

Today I learned about why testing is important. I mean, I know it is, but: **tests are important because they lead to better code design**. Bad code is nearly impossible to test well. Good code is easy to test. Of course it is 'in general', not in every case.

Consider following example:

```
def baz(n):
	# Do something with n
    return n

def bar(x, y, z):
	# Do comething with x, y, z and compute n
	return baz(n)

def foo():
	# Compute some values x, y, z
	bar(x, y, z)
```

Well, this example not worst possible, it is written without tests in mind. Yes, you can test it, but:

```
def baz(n):
	return n

def bar(x, y, z):
	return (x, y, z)
	
def foo():
	return (x, y, z)

# How to use it:
if __name__ == '__main__':
	x, y, z = foo()
    n = bar(x, y, z)
    r = baz(n)
    
```

This example doing the same job, but it is considerably more easy to test (in scale). However not only to scale, but it easier **to add** a new features, easier **to refactor** and it reduces **cognitive load** and your '**bus factor**' as a programmer.