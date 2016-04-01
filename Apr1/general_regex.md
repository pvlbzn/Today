###Regex

As wiki states:

> In [theoretical computer science](https://en.wikipedia.org/wiki/Theoretical_computer_science) and [formal language theory](https://en.wikipedia.org/wiki/Formal_language_theory), a **regular expression** (sometimes called a **rational expression**) is a sequence of [characters](https://en.wikipedia.org/wiki/Character_(computing)) that define a search pattern, mainly for use in [pattern matching](https://en.wikipedia.org/wiki/Pattern_matching) with [strings](https://en.wikipedia.org/wiki/String_(computer_science)), or [string matching](https://en.wikipedia.org/wiki/String_matching), i.e. "find and replace" - like operations.



Programming languages provide regexp built-in or via standard library.

There is a [RegExr](http://regexr.com/) page to play with regex live. For the moment I know only few regexp features as wildcard, or `touch day{1..29}.py` and actually I have no clue is it a regexp or a bash capabilities or regexp in bash?



```
s = '100 NORTH MAIN ROAD'
s.replace('ROAD', 'RD.')
>> '100 NORTH MAIN RD.'

s = '100 NORTH BROAD ROAD'
s.replace('ROAD', 'RD.')
# !
>> '100 NORTH BRD. RD.'
```

Now the same using a `re`

```
import re
re.sub('ROAD$', 'RD.', s)
'100 NORTH BROAD RD.'
```

`$` means the end of the string, `^` means the beginning of the string.

```
# No ROAD at the end.
s = '100 BROAD'
re.sub('ROAD$', 'RD.', s)
>> '100 BRD.'

re.sub('\\bROAD$', 'RD.', s)
>> '100 BROAD'

s = '100 BROAD ROAD APT. 3'
re.sub(r'\bROAD$', 'RD.', s)
>> '100 BROAD ROAD APT. 3'

re.sub(r'\bROAD\b', 'RD.', s)
>> '100 BROAD RD. APT 3'
```

`\b` means a word boundary must occur right here.

In Python a backslash plague is a thing. So prefix `r` means 'raw string', it tells to Python that nothing in this string should be escaped. `'\t'` is a tab, but `r'\t'` is what it is. So, always use a `r` prefix with regexp in Python, just in case.

`re.sub(r'\bROAD\b', 'RD.', s)` reads as "match 'ROAD' when it's a whole word by itself anywhere in the string."



REGEX:

```
# Character classes
[\s\S]		match any

\w			word
\W			not word

\d			digit
\D			

\s			whitespace
\S

[ABC]		character set
[^ABC]		negated set
[A-Z]		range


# Anchors
^			beginning
$			end
\b			word boundary
\B

# Escaped chars can be workarounded by r prefix.
```