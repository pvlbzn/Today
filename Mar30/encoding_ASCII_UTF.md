###Strings, encoding.

Well, I knew that strings is fairly complicated topic in programming, especially in low-level languages.

*Non-tech, historical remark*: in **non-networked** world were a lot of different encoding variations. It works kind of well when people was mostly typing and printing it out, or share their works to others, and those others were opening works on the same software. In the **networked** world, this thing become a problem. I personaly faced alot of issues, when I was a kid, with CP1251, CP1252, KOI8-R, ASCII. I've seen a lot of pages like "??? ??????? ??? ???? ?? ????? ??". People were forced to 'guess' an encoding type of a web page and switch it manually.



> There is a good read [The Absolute Minimum Every Software Developer Absolutely, Positively Musth Know About Unicode and Character Sets](http://www.joelonsoftware.com/articles/Unicode.html). This link I found on The Go Blog [Strings, bytes, runes and characters in Go](https://blog.golang.org/strings).



Answer is [**Unicode**](http://www.unicode.org/resources/utf8.html). Python docs about it: [Unicode HOWTO](https://docs.python.org/3/howto/unicode.html). 

There are few Unicodes, such as **UTF-8**, **UTF-16**, **UTF-32**. Thus, each character will take 1, 2 or 4 bytes.

| Encoding                   | G      | O      | O      | D      |
| -------------------------- | :----- | ------ | ------ | ------ |
| ASCII (decimal)            | 71     | 79     | 79     | 68     |
| UTF-8(Unicode code points) | U+0047 | U+004F | U+004F | U+0044 |



There can be a mess with *big-endian* and *little-endian* systems, because first will read **U+4E2D** as **4E 2D**, second as **2D 4E**. This problem solved by *Byte Order Mark* **U+FEFF** for UTF-16.



But there is still unsolveable issue - size. Solution is **UTF-8**.

For ASCII UTF-8 uses **1 byte per char**. Extended Latin characters takes **2 bytes**. Chinese chars takes **3 bytes**. Other rarely-used chars takes **4 bytes**.

Dissadvantage is that each character can take a different number of bytes, finding the char is an **O(N) operation**, thus the longer the string, the longer it takes to find a char.



