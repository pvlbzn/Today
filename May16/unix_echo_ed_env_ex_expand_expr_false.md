#### echo

`echo` - display a line of text.

Echo is one of tools, where less is more.

```
// Print all folders in pwd
echo */

// Print all folders with its content
echo */*

// Print allfiles of type .py
echo *.py

// Echo to
echo "text" >> text.txt
```

-

#### ed

`ed` - line-oriented text editor.

Originaly was written by Ken Thompson for the early Unix. Back in this time visual editors, such as vi, were impossible because of environments were the line-oriented paradigm only.

-

#### env

`env` - run a program in a modified environment.

Plain call `command env` prints out a list of all environment variables, such as GOPATH=[path] or SHELL=[path]. 

-

#### ex

`ex` - line-mode text editor of vi.

`ex` stands for extended, originally it was an extension of the `ed`. `ed` and `vi` points to one program but in different modes.

-

#### expand

`expand` - converts tabs to spaces.

```
echo "\t" > expand.txt
expand expand.txt > expand1.txt
cat -vet expand.txt
>^I$
cat -vet expand1.txt
>       $
```

-

#### expr

`expr` - evaluate expressions.

```
expr 5 \* 5
> 25
```

Can be used as a command-line calculator in case if machine has no some dynamic language interpreter such as Python, Ruby or whatever else.

-

#### false

`false` - do nothing, unsuccessfully.

Exit with a status code indicating failure.

-

#### Status
**admin, alias, ar, asa, at, awk, basename, batch, bc, bg, c99, cal, cat, cd, cflow, chgrp, chmod, chown, cksum, cmp, comm, command, compress, cp, crontab, csplit, ctags, cut, cxref, date, dd, delta, df, diff, dirname, du, echo, ed, env, ex, expand, expr, false**, fc, fg, file, find, fold, fort77, fuser, gencat, get, getconf, getopts, grep, hash, head, iconv, id, ipcrm, ipcs, jobs, join, kill, lex, link, ln, locale, localedef, logger, logname, lp, ls, m4, mailx, make, man, mesg, mkdir, mkfifo, more, mv, newgrp, nice, nl, nm, nohup, od, paste, patch, pathchk, pax, pr, printf, prs, ps, pwd, qalter, qdel, qhold, qmove, qmsg, qrerun, qrls, qselect, qsig, qstat, qsub, read, renice, rm, rmdel, rmdir, sact, sccs, sed, sh, sleep, sort, split, strings, strip, stty, tabs, tail, talk, tee, test, time, touch, tput, tr, true, tsort, tty, type, ulimit, umask, unalias, uname, uncompress, unexpand, unget, uniq, unlink, uucp, uudecode, uuencode, uustat, uux, val, vi, wait, wc, what, who, write, xargs, yacc, zcat
