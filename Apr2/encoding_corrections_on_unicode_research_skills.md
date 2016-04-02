### Correction on encoding topic, research skill.

**Research**: Always check information twice, it isn't that hard, much harder is to come up to **wrong** understanding and later fix it. Also, general experience, **read** *programmers* blogs, **not** *techical writers* blogs. There is a big difference. Thus, when you reading about some topic which is bigger than one stackoverflow post, check info twice.



####Unicode

Unicode is **not** equal to UTF-(Amount of bits). UTF-8 is **not** UTF-16 twice. Unicode was a first and unsuccesfull attempt to solve encoding problem. UTF-8, among others, is prefferable and a right way to encode your strings nowadays.

UTF-8 size:

```
U+0000 - U+007F					Bytes: 1	Bits of code points: 7
U+0080 - U+07FF					Bytes: 2	Bits of code points: 11
U+0800 - U+FFFF					Bytes: 3	Bits of code points: 16
U+10000 - U+1FFFFF				Bytes: 4	Bits of code points: 21
U+200000 - U+3FFFFFF			Bytes: 5	Bits of code points: 26
U+4000000 - U+7FFFFFFF			Bytes: 6	Bits of code points: 31
```

Each code-point start with a some bits that essentially say "You have to read N bytes".

Good spec is [here](https://en.wikipedia.org/wiki/UTF-8).