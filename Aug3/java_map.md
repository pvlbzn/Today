## Java Collections Framework
JCF is a set of classes and interfaces that implement commonly reusable data structures. Although reffered to as a framework, it works like a library therefore further will be referenced as a library.


```
// Queue interface from collections

public interface Queue<E> extends Collection<E> {
    boolean add(E e);
    boolean offer(E e);

    // Retrieve and remove the head, throws an exception
    E remove();
    // Returns null if empty
    E poll();

    // Retrieve head but doesnt remove, throws an exception
    E element();
    // Returns null if empty
    E peek();
}
```

### Map
Map is not a subtype of the `Collection` interface, therefore it behaves a bit different from the `Collection` implementers. Map is an interface by itself with following implementations:

- HashMap
- HashTable
- EnumMap
- IdentityHashMap
- LinkedHashMap
- Properties
- TreeMap
- WeakHashMap

The most popular ones are `HashMap`, `TreeMap`. A hash map hashes the keys and a tree map uses an ordering on the keys to organize them in a search tree. The hash or comparison function is works only with the keys.

Keys must be unique. If the key is already present, `put()` method will replace an old key with a new one and *return* the old key.

```
Map<Integer, Point> coord = new HashMap<>();
Point x = new Point(15, 25);

// Store
// key/value
coord.put(15, x);

// Retrieve
coord.get(15);
```

If data doesn't need to be sorted then better to preffer `HashMap` because it is a little bit faster.
