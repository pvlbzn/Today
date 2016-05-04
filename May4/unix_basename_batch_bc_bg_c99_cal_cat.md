####basename

`basename` - strip directory and suffix from filenames.

```
basename -s .md unix_admin_alias_ar_asa_at_awk.md
unix_admin_alias_ar_asa_at_awk

basename /usr/bin/explode
explode
```

-

####batch

`at, batch, atq, atrm` - queue, examine, delete jobs for later execution.

These commands doesn't present in lastest Linux versions.

-

####bc

`bc` - an arbitrary precision calculator language.

You can invoke an interactive calculator using `-i` agrument.

```
bc -i
5 > 2
1
5 < 1
0
```

More in `man bc`.

-

####bg

`bg` - shell builtin command.

-

####c99

'c99' - ANSI '99 compiler.

`c99` is substantially completely supported as of GCC 4.5 using `-std=c99`. On Linux `c99` is a shell-wrapper to the `cc`, which is a `gcc`.

-

####cal

`cal`, `ncal` - calendar

```
ncal
    May 2016          
Su  1  8 15 22 29   
Mo  2  9 16 23 30   
Tu  3 10 17 24 31   
We  4 11 18 25      
Th  5 12 19 26      
Fr  6 13 20 27      
Sa  7 14 21 28 
```

Argument `-y` will show a year-long calendar. `cal` with `-3` argument will print a current month, a previous and a next.

-

####cat

`cat` - concatenate files and pront on the stdout.

Wery simple, yet powerful tool.

```
$ touch {1..3}.txt
$ echo "one" > 1.txt && echo "two" > 2.txt
$ cat 1.txt; cat 2.txt;
one
two
$ cat 1.txt > 3.txt
$ echo "+" >> 3.txt
$ cat 2.txt >> 3.txt
$ cat 3.txt
one
+
two
```

```
bc -l | cat
```

`cat` is one of the most frequently used commands. It has three related functions with regard to text files: display; combine; create.

-

####Comments

I found a GNU [implementation](http://ftp.gnu.org/gnu/coreutils/?C=M;O=D) of the core utils, sources.

-

####Status

**admin, alias, ar, asa, at, awk, basename, batch, bc, bg, c99, cal, cat**, cd, cflow, chgrp, chmod, chown, cksum, cmp, comm, command, compress, cp, crontab, csplit, ctags, cut, cxref, date, dd, delta, df, diff, dirname, du, echo, ed, env, ex, expand, expr, false, fc, fg, file, find, fold, fort77, fuser, gencat, get, getconf, getopts, grep, hash, head, iconv, id, ipcrm, ipcs, jobs, join, kill, lex, link, ln, locale, localedef, logger, logname, lp, ls, m4, mailx, make, man, mesg, mkdir, mkfifo, more, mv, newgrp, nice, nl, nm, nohup, od, paste, patch, pathchk, pax, pr, printf, prs, ps, pwd, qalter, qdel, qhold, qmove, qmsg, qrerun, qrls, qselect, qsig, qstat, qsub, read, renice, rm, rmdel, rmdir, sact, sccs, sed, sh, sleep, sort, split, strings, strip, stty, tabs, tail, talk, tee, test, time, touch, tput, tr, true, tsort, tty, type, ulimit, umask, unalias, uname, uncompress, unexpand, unget, uniq, unlink, uucp, uudecode, uuencode, uustat, uux, val, vi, wait, wc, what, who, write, xargs, yacc, zcat
