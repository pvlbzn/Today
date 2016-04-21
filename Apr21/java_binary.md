###Binary things


Java **has no unsigned** types. Here is Gosling's answer:
>Gosling: For me as a language designer, which I don't really count myself as these days, what "simple" really ended up meaning was could I expect J. Random Developer to hold the spec in his head. That definition says that, for instance, Java isn't -- and in fact a lot of these languages end up with a lot of corner cases, things that nobody really understands. Quiz any C developer about unsigned, and pretty soon you discover that almost no C developers actually understand what goes on with unsigned, what unsigned arithmetic is. Things like that made C complex. The language part of Java is, I think, pretty simple. The libraries you have to look up.

*Well, in my opinion Java's bloat is much more a problem. Guess what? There is an API with helper methods like `divideUnsigned` and 3rd-party libs like Guava. This IS the problem.*

```
// 8-bit 'byte'

byte b1 = (byte)0b1111;
// Print: 15

byte b2 = (byte)0b11111111;
// 255, Right?
// Nope. -1
```

--

I spend 2 hours on this topic, to future me: use an API for everything in Java unless you want to be dissapointed.



