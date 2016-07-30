## Enum
[PEP 435](https://www.python.org/dev/peps/pep-0435/) - adding an enum type to the Python standard library. Available since 3.4, backported to older versions as enum34.

The `enum` module defines an enum type with iteration and comparison capabilities.

```
from enum import Enum


class Animal1(Enum):
    cat = 1
    dog = 2
    goat = 3
    whale = 4
    alpaca = 5


for member in Animal1:
    print(member.name, member.value)
```

Will print `cat 1 dog 2 goat 3 whale 4 alpaca 5`.

Or, `enum` can be created programmatically

```
Animals2 = Enum(
    value='Animals', names=(
        'cat dog goat whale alpaca'))

for member in Animals2:
    print(member)
```

Will produce

```
Animals.cat
Animals.dog
Animals.goat
Animals.whale
Animals.alpaca
```

`enum` is an good implementation of its concept. 
