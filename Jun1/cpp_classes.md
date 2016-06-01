## cpp Classes

What's the point? Well:
>Actually I made up the term "object-oriented", and I can tell you I did not have C++ in mind. Alan Kay.

Classes are an expanded data structure concept. Data structure with a functions.

```
class Name {
    access:
        member;
    access:
        member;
} names;
```

Names is an optional list of names for objects of the class. Members can be a data or a function declaration. Access specifiers are optional. Access specifiers have 3 options: `private`, `public`, `protected`.

```
class Rectangle {
        int w, h;
    public:
        void set(int, int);
        int  area(void);
} rect;
```

`private` is the default access level. 

```
#include <iostream>
using namespace std;

class Rectangle {
        int w, h;
    public:
        void set(int, int);
        int  area() {
            return w * h;
        }
};

void Rectangle::set(int x, int y) {
    w = x;
    h = y;
}
```

`set(int, int)` is in `Rectangle` namespace. Function defined in class declaration is an inline member function.

```
#include <iostream>
using namespace std;

class Rectangle {
        int w, h;
    public:
        Rectangle (int, int);
        int  area() {
            return w * h;
        }
};

void Rectangle::Rectangle() {
    w = 10;
    h = 10;
}

void Rectangle::Rectangle(int x, int y) {
    w = x;
    h = y;
}

int main {
    Rectangle rect(5, 15);
    return 0;
}
```

Function called Classname::Classname is a constructor function. Constructor overloading is ok. `rect` is allocated on frame (I guess, memory management will be a next topic) and initialized with 5 and 15.

#### Initialization

```
// Functional form
Rectangle r1();

// Uniform initialization
Rectangle r2{15, 20};
Rectangle r3 = {25, 30};
```

Also, here is a constructor initialization:

```
Rectangle(int x, int y) : w(x), h(y) {}
```
