#### date

`date` - display or set date and time.

```
date
> Thu May 12 20:13:15 MSK 2016
```

-

#### dd

`dd` - convert and copy a file.

It copies the standard input to the standard output. Input data is r/w in 512-byte blocks. `dd` uses not standard Unix syntax, instead of `command --option x` it uses a `command option=value`.

By default `dd` reads from stdin and writes to stdout. It can be changed by using the input file `if` and output file - `of`.

Thus, this tool is used to convert files and writes big sequences of the data to some media devices, sicne everything is a file.

Better to double check before press enter with any command with sudo.

-

#### delta

`delta` - saves editing changes in a SCCS file.

Not present on MacOS, which is really weird, since MacOS is one of the few Unix OSes.

-

#### df

`df` - display free disk space.

```
df -H

Filesystem      Size   Used  Avail Capacity  iused   ifree %iused  Mounted on
/dev/disk1      250G   219G    30G    88% 53570835 7410411   88%   /
```

`df` is a disk free.

-

#### diff

`diff` - compare files line by line.

It is a data comparison tool that calculates and displays the differences between two files. Typically, `diff` is used to show the changes between two versions of the same file. `diff` tool is *line-oriented*, not *character*.

-

#### dirname

`dirname` - return filename or directory portion of pathname.

-

#### du

`du` - display disk usage statistics.

`du` stands for disk usage.

-

#### Status
**admin, alias, ar, asa, at, awk, basename, batch, bc, bg, c99, cal, cat, cd, cflow, chgrp, chmod, chown, cksum, cmp, comm, command, compress, cp, crontab, csplit, ctags, cut, cxref, date, dd, delta, df, diff, dirname, du**, echo, ed, env, ex, expand, expr, false, fc, fg, file, find, fold, fort77, fuser, gencat, get, getconf, getopts, grep, hash, head, iconv, id, ipcrm, ipcs, jobs, join, kill, lex, link, ln, locale, localedef, logger, logname, lp, ls, m4, mailx, make, man, mesg, mkdir, mkfifo, more, mv, newgrp, nice, nl, nm, nohup, od, paste, patch, pathchk, pax, pr, printf, prs, ps, pwd, qalter, qdel, qhold, qmove, qmsg, qrerun, qrls, qselect, qsig, qstat, qsub, read, renice, rm, rmdel, rmdir, sact, sccs, sed, sh, sleep, sort, split, strings, strip, stty, tabs, tail, talk, tee, test, time, touch, tput, tr, true, tsort, tty, type, ulimit, umask, unalias, uname, uncompress, unexpand, unget, uniq, unlink, uucp, uudecode, uuencode, uustat, uux, val, vi, wait, wc, what, who, write, xargs, yacc, zcat
