### In Essence
Java strings are implemented as sequence of `char` values. About `char` and `\u`: `public static void main(String\u005B\u005D args)` is perfectly fine. Unicode escape sequences are processed **before** the code is parsed.

### `char` and Unicode
I already made some study on Unicode [here](https://github.com/pvlbzn/Today/blob/ace6280d2d9e4ddb65af4e0a31219bc0be7348fd/Mar30/encoding_ASCII_UTF.md) and [here](https://github.com/pvlbzn/Today/blob/d0420e4d383855e827503097754f19f3a0474558/Apr2/encoding_corrections_on_unicode_research_skills.md), however that was about Unicode by itself and Python.

Java uses 16-bit unicode. The character in the basic multilingual plane are represented as 16-bit values, called **code units**. The supplementary characters are encoded as consecutive pairs of code units.

In Java `char` describes a code unit in the UTF-16 encoding. Thus, strongly recomended to not use the `char` type unless you are actually manipulating UTF-16 code units.

### Code Points and Code Units in the String
`length` method will return number of code units in the string. To get the true lenght, which is the number of code points call `.codePointCount()` method on the string object.

### Immutability
An instance of `String` class is immutable. What is immutability in Java? It means that there are no public API which allows to mutate a string. Native methods can, however this is another topic.