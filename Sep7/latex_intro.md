# LaTeX / TeX
TeX was developed by Donald Knuth. Motivation was to build a tool which allows construct math formulae which looks correct. LaTeX is an extensible system. By itself it is good for simple math formulas, for more advanced user should use additional packages.

LaTeX understands two *environments*

1. Text - text formalas are displayed inline
2. Displayed - fromulas displayed separately

## Syntax
Basically it feels like markdown with 'math' module, but nothing difficult at least with easy expressions. `n^{22}` means *n in power of 22*. However *continued fractions* looks a bit different:

```
\begin{equation}
    x = a_0 + \cfrac{1}{a_1
            + \cfrac{1}{a_2
            + \cfrac{1}{a_3 + \cfrac{1}{a_4} } } }
\end{equation}
```

Or a square root of a fraction:

```
\sqrt{\frac{a}{b}}
```

Or a matrice:

```
\[
    \begin{matrix}
     a & b & c \\
     d & e & f \\
     g & h & i
    \end{matrix}
\]
```

## Rendering
Unfortunately with a rendering situation is not that easy. Document can be compiled into PDF easily, but for web hosting/displaying some modules should be used. There is no simple way to display 'on the fly' LaTeX to formulas as you type in sublime text or vim for clear reasons.

There are some web services which accepts (via an iterface or a query string) LaTeX formula and they returns rendered image file which can be easily used everywhere.
