# NullPointerException

## Obvious Solution
Add null checks everywhere. This is usually done using *null coalescing operator* which is looks like `x ? x : y`, but Java has no this synatatic sugar.

## Java 8 Solution

```
class Inner {
    String str;
    String getStr() {
        return str;
    }
}


class Nested {
    Inner in;
    Inner getIn() {
        return in;
    }
}


class Outer {
    Nested nes;
    Nested get Nes() {
        return nes;
    }
}
```

Instead of classic check like `outer != null && outer.nested != null && outer.nested.inner != null` new Java 8 `Optional` type can be utilized.

```
Optional.of(new Outer())
    .map(Outer ::getNes)
    .map(Nested::getIn)
    .map(Inner ::getStr)
    .ifPresent(System.out::println);
```

The method `map` accepts a lambda expression of type `Function` and automatically wraps each function result into an `Optional`. Null checks are **automatically handled**.

Alternatively the same behaviour can be achieved:

```
public static <T> Optional<T> resolve(Supplier<T> resolver) {
    try {
        T result = resolver.get();
        return Optional.ofNullable(result);
    }
    catch (NullPointerException err) {
        return Optional.empty();
    }
}
```

## Optional
*Optional* is a simple container for a value which may be null or not-null.


```
Optional<String> opt = Optional.of("object");

opt.isPresent();                // true
opt.get();                      // "object"
opt.orElse("do something");     // "object"

opt.ifPresent((o) -> System.out.println(o));    // "object"
```

