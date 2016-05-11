####cmp

`cmp` - compare two files byte by byte

```
echo "1" > cmp1
echo "2" > cmp2

cmp cmp1 cmp2
> cmp1 cmp2 differ: byte 1, line 1

echo "1" > cmp2

cmp cmp1 cmp2
> (no output, means they are similar)
```

-

####comm

`comm` - compare two sorted files line by line

```
echo " comp" >> cmp1
echo " are" >> cmp2

comm cmp1 cmp2
>         1
>     are
> comp
```

-

####command

`command` - is a command.

Machine

```
uname -a
Linux name 4.4.0-22-generic #39-Ubuntu SMP Thu May 5 16:53:32 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux
```

Doesn't have manual entry for command. However command `command` exists. Using `zshell` tab interactive input feature, command will list all commands available on the current machine. Can be used:

```
command ls
```

-

####compress

`compress` - unix shell compression program based on the Lempel-Ziv-Welch algorithm.

LZW, compared to gzip and bzip2, performs faster with less memory usage. Produces significantly lower compression ratio. Usually has a `.z` extention. Not used much nowadays. Not present on Linux machine.

-

####cp

`cp` - copy files and directories.

One of the most frequent used tools.

```
cp from/what to/
```

Actually it has lots of features, more than 30, such as archive or backup.

-

####crontab

`crontab` - maintain crontab files for individual users.

I already described `cron` and `cronetab` is [here](https://github.com/pvlbzn/Today/blob/44832fe5470039d16ade208aa808d4b443bb5b99/Apr11/unix_cron.md). Each day, in this project (Today), `cron` triggers a python script which creates a folder for a current day.

-

####csplit

`csplit` - split a file into sectios determined by context lines.

In [this](http://www.sanfoundry.com/5-practical-csplit-command-usage-examples-in-linux/) post some kind of useful examples are shown.

-

####ctags

`ctags` - create tag files for source code.

Not present in Linux.

-

####cut

`cut` - remove sections from each line of files.

Usage [samples](http://www.computerhope.com/unix/ucut.htm).

-

####cxref

`cxref` - generate a clang program cross-reference table

This is a tool for producing documentaton on C language files (ANSI C).

-

####Status

**admin, alias, ar, asa, at, awk, basename, batch, bc, bg, c99, cal, cat, cd, cflow, chgrp, chmod, chown, cksum, cmp, comm, command, compress, cp, crontab, csplit, ctags, cut, cxref**, date, dd, delta, df, diff, dirname, du, echo, ed, env, ex, expand, expr, false, fc, fg, file, find, fold, fort77, fuser, gencat, get, getconf, getopts, grep, hash, head, iconv, id, ipcrm, ipcs, jobs, join, kill, lex, link, ln, locale, localedef, logger, logname, lp, ls, m4, mailx, make, man, mesg, mkdir, mkfifo, more, mv, newgrp, nice, nl, nm, nohup, od, paste, patch, pathchk, pax, pr, printf, prs, ps, pwd, qalter, qdel, qhold, qmove, qmsg, qrerun, qrls, qselect, qsig, qstat, qsub, read, renice, rm, rmdel, rmdir, sact, sccs, sed, sh, sleep, sort, split, strings, strip, stty, tabs, tail, talk, tee, test, time, touch, tput, tr, true, tsort, tty, type, ulimit, umask, unalias, uname, uncompress, unexpand, unget, uniq, unlink, uucp, uudecode, uuencode, uustat, uux, val, vi, wait, wc, what, who, write, xargs, yacc, zcat
