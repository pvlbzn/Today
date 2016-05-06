####cd

`cd` - change the current working directory.

```
cd [option][directory]
```

Names can be expressed as local or absolute path. The current directory is represented by a single dot `.` and its parent directory is represented by `..`. Thus, it is possible to create a handy alias:

```
alias ..='cd ..'
alias ...='cd ../..'
```

-

####cflow

`cflow` - analyze a collection of source files (C PL) and output a graph charting dependencies between various functions.

```
cflow [path/to/code.c]
```

-

####chgrp

`chgrp` - change group

```
chgrp admin README.md
ls -l

-rw-r--r--  1   uname   admin   ...

chgrp staff README.md
ls -l

-rw-r--r--  1   uname   staff   ...
```

-

####chmod

`chmod` - change file modes or Access Control List.

The chmod utility modifies the file mode bits of the listed files.

Modes:

```
4000    set user ID on execution bit. Executables with this bit
        will run with effective uid set tot the uid of the file
        owner.

2000    set group id on execution bit.

1000    sticky bit.

0400    allow read by owner.

0200    allow write by owner.

0100    files: allow execution by owner.
        directories: allow group members to search in the dir.

0004    allow read by others.

0002    allow write by others.

0001    files: allow execution by others.
        directories: allow others to search in dir.
```

Modes may be absolute or symbolic. The absolute mode that permits:

- read
- write
- execute by the owner
- read and execute by a group
- read and execute by others

is **755**. Because: 400+200+100+040+010+004+001 = 755.

-

####chown

`chown` - change file owner and group.

```
chown [owner-user][file]
chown [owner-user:owner-group][file]
```

-

####cksum

`cksum` - display file checksum.

It outputs a CRC, the total number of octets, a file name into stdout. The checksum can be used to verify that files transferred by unreliable means arrived intact. It guards against accidental corruptions, however it isnt cryptographically secure.

CRC, a cyclic redurancy check, is an error-detecting code. Blocks of data entering these systems get a short check value attached, based on the remainder of a polunominal division of threir contents.

-

####Status

**admin, alias, ar, asa, at, awk, basename, batch, bc, bg, c99, cal, cat, cd, cflow, chgrp, chmod, chown, cksum**, cmp, comm, command, compress, cp, crontab, csplit, ctags, cut, cxref, date, dd, delta, df, diff, dirname, du, echo, ed, env, ex, expand, expr, false, fc, fg, file, find, fold, fort77, fuser, gencat, get, getconf, getopts, grep, hash, head, iconv, id, ipcrm, ipcs, jobs, join, kill, lex, link, ln, locale, localedef, logger, logname, lp, ls, m4, mailx, make, man, mesg, mkdir, mkfifo, more, mv, newgrp, nice, nl, nm, nohup, od, paste, patch, pathchk, pax, pr, printf, prs, ps, pwd, qalter, qdel, qhold, qmove, qmsg, qrerun, qrls, qselect, qsig, qstat, qsub, read, renice, rm, rmdel, rmdir, sact, sccs, sed, sh, sleep, sort, split, strings, strip, stty, tabs, tail, talk, tee, test, time, touch, tput, tr, true, tsort, tty, type, ulimit, umask, unalias, uname, uncompress, unexpand, unget, uniq, unlink, uucp, uudecode, uuencode, uustat, uux, val, vi, wait, wc, what, who, write, xargs, yacc, zcat
