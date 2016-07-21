## Arrays
Cpp has three types of arrays.

- C-style array
- std::array
- std::vector

Third option is *recommended* unless you know why you need other two.


### C-style

`type name [constant]`

C-style arrays are blocks of static memory whose size must be determined at compile time.

```
int foo[5] = {1, 2, 3};         // 4th and 5th member will initialized to a zero-value
int bar[]  = {1, 2, 3, 4, 5};   // equals to int bar[5];
int baz[] { 1, 2, 3 };          // ok
```

There are also *multidimensional arrays*:

```
int point[1][1];
int bad_idea[512][512][512];
```

Local arrays are created on the *stack* and have automatic storage duration, they destroyed when the function is done (since stack will be freed). Arrays created using `new` have dynamic storage duration and are stored on the *heap*.

```
int *foo = new int[10];
delete[] foo;
```


### `std::array`
C++11 standard introduced new 'kind' of arrays. This type is preferable to use over c-style arrays. It is a template class that encapsulate a statically-sized array, stored inside the object itself. If you instantiate the class on the stack, array itself will be on the stack. `std::array` can not grow or shrink.

```
#include <array>

std::array<int, 3> foo;                  // an int array with length 3
std::array<int, 3> bar = {1, 2, 3};      // initialization list
std::array<int, 3> baz {1 ,2 ,3};        // uniform initialization
```

Subscript operator doesnt perform any bounds-checking. `std::array` supports a second form of array element access that *does* bound checking:

```
std::array<int, 5> foo { 1, 2, 3, 4, 5 };
foo.at(3) = 10;         // Ok
foo.at(10) = 3;         // Error will be thrown

foo.size();             // 5
```

> Rule: always pass `std::array` by `const` reference.


### `std::vector`
It is a template class that encapsulate a dynamic array, stored in the heap, that grows and shrinks automatically if elements are added or removed. It provides a convinient and safe API to work with. If `std::array` closely follows the basic functionality of fixed arrays, `std::vector` comes with an additional API.

```
#include <vector>

std::vector<int> foo;               // initialized without size
std::vector<int> bar {1, 2, 3};     // uniform initialization

// Similarly to std::array vector has two methods to access element
bar[1] = 12;                        // no bound check
bar.at(3) = 13;                     // bound checked

foo = { 1, 2, 3, 4, 5 };            // ok, vector can grow
foo.resize(128);

foo = { 1 };                        // ok, vector can shrink
```

Self-cleanup prevents memory leaks

```
void fn(bool exit) {
    int *arr = new int[1]{ 1 };

    if (exit) return 0;

    // main functionality goes here

    delete[] arr;
}
```

If exit is true, memory will be leaked. This is not the case with `std::vector`, memory will be deallocated as soon as `arr` goes out of scope no matter `exit` or not.


### Conclusion
Every abstraction has its cost. However code safety should be preffered unless this abstraction is a bottle neck. `std::array` is more limited than `std::vector` but it's often more efficient since it is just a wraper around classic array. `std::array` and `std::vector` should be prefered over classic array in most cases.
