###String, Python source, C

In Python (3) all strings are sequences of Unicode chars. **UTF-8 is a way of encoding characters as a sequence of bytes.** Characters are an abstraction. String is a sequence of those abstractions.



Since in P everything is an object:

```
a = 0.897234
b = 57
'{0:.1f} {1}'.format(a, b)
>> '0.9 57'

# Compound field names.
x = [13, 231, 3, 48]
'{0[1]}'.format(x)
>> '231'
```

[**Parsing rules**](https://www.python.org/dev/peps/pep-3101/) PEP 3101 for item key are: If it starts with a digit, then it is treated as a number; otherwise it is used as a string"

Wery useful reading in doc [Format Specification Mini-Language](https://docs.python.org/3.5/library/string.html#format-specification-mini-language).



```
# Yes, very original.
s = "kjhsdflkjahsdfjh asdjfh ashjdgf asdkjhfg as"
s.count("k")
>> 3
```



I was curious to look at implementation, how is `.count()` implemented, because it is O(n) function (as I understand it right, time to process a string grows with string?). Turns out these functions is in C, in [stringlib](https://github.com/python/cpython/tree/1fe0fd9feb6a4472a9a1b186502eb9c0b2366326/Objects/stringlib) and inside `.count()` uses the [`fastsearch`](https://github.com/python/cpython/blob/1fe0fd9feb6a4472a9a1b186502eb9c0b2366326/Objects/stringlib/fastsearch.h).

Also, all objects is [implemented](https://github.com/python/cpython/tree/1fe0fd9feb6a4472a9a1b186502eb9c0b2366326/Objects) in C.



Parse URL to dict:

```
link = 'http://www.amazon.com/gp/product/1449340377/ref=s9_simh_gw_g14_i3_r?ie=UTF8&fpl=fresh&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=desktop-1&pf_rd_r=0B7BTYWCYXZ4KPVPTKXX&pf_rd_t=36701&pf_rd_p=2437869742&pf_rd_i=desktop'

l = link.split('&')

# Described at the end.
ll = [v.split('=', 1) for v in l if '=' in v]

# Python can turn list-of-lists into a dictionary
ldic = dict(ll)
ldic
>> {'pf_rd_t': '36701',
'pf_rd_s': 'desktop-1',
'pf_rd_p': '2437869742',
'http://www.amazon.com/gp/product/1449340377/ref': 's9_simh_gw_g14_i3_r?ie=UTF8',
'pf_rd_i': 'desktop',
'pf_rd_r': '0B7BTYWCYXZ4KPVPTKXX',
'pf_rd_m': 'ATVPDKIKX0DER',
'fpl': 'fresh'}
```

About `str.split()`

```
help(str.split)
>> S.split(sep=None, maxsplit=-1) -> list of strings

s = 'Split,me,split!'
s.split()
>> ['Split,me,split!']
s.split(',')
>> ['Split', 'me', 'split!']
s.split(',', 1)
>> ['Split', 'me,split!']
```

Slicing stuff is also straighforward and logical:

```
s = 'Hello'
s[:]
>> Hello

s[1:]
>> ello

# This is interesting - step
s[::-1]
>> olleH
```



