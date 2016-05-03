###Tool-a-Day

> Much of the power of the UNIX operating system comes from a style of program design that makes programs easy to use and, more important, easy to combine with other programs. This style has been called the use of software tools, and depends more on how the programs fit into the programming environment and how they can be used with other programs than on how they are designed internally. [...] This style was based on the use of tools: using programs separately or in combination to get a job done, rather than doing it by hand, by monolithic self-sufficient subsystems, or by special-purpose, one-time programs.

Thus, I want to study through every and each tools from the Unix Programming Environment.

I took [The Single UNIX Specification, Version 3](http://www.unix.org/version3/), this paper [InterfaceTables](http://www.unix.org/version3/inttables.pdf) in particular from page 28 to 31.

Technically, Unix programs expected to follow: "Do one thing and do it wel".

-

Utilities Interface Table

admin, alias, ar, asa, at, awk, basename, batch, bc, bg, c99, cal, cat, cd, cflow, chgrp, chmod, chown, cksum, cmp, comm, command, compress, cp, crontab, csplit, ctags, cut, cxref, date, dd, delta, df, diff, dirname, du, echo, ed, env, ex, expand, expr, false, fc, fg, file, find, fold, fort77, fuser, gencat, get, getconf, getopts, grep, hash, head, iconv, id, ipcrm, ipcs, jobs, join, kill, lex, link, ln, locale, localedef, logger, logname, lp, ls, m4, mailx, make, man, mesg, mkdir, mkfifo, more, mv, newgrp, nice, nl, nm, nohup, od, paste, patch, pathchk, pax, pr, printf, prs, ps, pwd, qalter, qdel, qhold, qmove, qmsg, qrerun, qrls, qselect, qsig, qstat, qsub, read, renice, rm, rmdel, rmdir, sact, sccs, sed, sh, sleep, sort, split, strings, strip, stty, tabs, tail, talk, tee, test, time, touch, tput, tr, true, tsort, tty, type, ulimit, umask, unalias, uname, uncompress, unexpand, unget, uniq, unlink, uucp, uudecode, uuencode, uustat, uux, val, vi, wait, wc, what, who, write, xargs, yacc, zcat

Thus, an average Unix tool name is 4 chars long (Well, 4.3, but I have no idea how to express .3 of the char).

<br>

####UPD

After I did a research on fist 6 tools, Linux 4.4 knew only about 2 of them. This is it. Linux isn't UNIX. Even not every Linux is POSIX. However, my mac machine perfectly aware about all tools, because it is registered product UNIX 03.
