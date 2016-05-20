### Dependency Injection

>"Dependency Injection" is a 25-dollar term for a 5-cent concept. Dependency injection means giving an object its instance variables.

Dependency injection is basically providing the objects that an object needs(its actual dependencies) instead of having it construct them itself.

```
// Construct dependency
public Class() {
	obj = Factory.getObj();
}

// Inject dependency
public Class(Obj o) {
	this.obj = o;
}
```

Deps can be injected into objects by many means, such as constructor injection or setter injection or with help of DI frameworks, such as Spring.

TODO: [Read](http://martinfowler.com/articles/injection.html).