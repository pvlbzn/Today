## Preprocessor Derectives

#### include

There are two include derectives:

- `#include <>`
- `#include ""`

`""` - the preprocessor searches in the same dir as the file containing derictive, like developer defined headers.

`<>` - the preprocessor searches in an implementation dependent manners, normally used for std stuff.

In theory. In practice: its depends on implementation.


#### define

`#define` - define preprocessor macros.

Syntax: `#define identifier replacement`. What it does: when the preprocessor encouners defined identifier it replaces it with a replacement. Replacement can be an expression, a statement, a block.

```
// An expression
15 * 7
x > y

// A statement
int x;
x = 25;

// A block
{
	;
}
```

An example:

```
#include <iostream>

#define get_max(x, y) (x>y?x:y)

int main() {
	int x = 15;
	int y = 25;
	std::cout << get_max(x, y) << std::endl;
}
```

```
$ gcc directive.cpp -o direct -lstdc++
$ ./direct
> 25
```