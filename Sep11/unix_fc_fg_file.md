#### fc

`fc` - lists, edits, reexecutes commands previously entered to a terminal.

On macos it opens vim with a last entered command.

-

#### fg

`fg` - continues a stopped job by running it in the foreground.

Typing `fg` will resume the most recently suspended or backgrounded job.

```
$ fg [job_id]
```

Use case: suspend & resume using `fg`.

```
➜  today git:(master) ✗ ping somepage.com

PING somepage.com 56 data bytes
Request timeout for icmp_seq 0

// Suspend via C+z
^Z
[1]  + 5420 suspended  ping somepage.com

➜  today git:(master) ✗ jobs -l
[1]  + 5420 suspended  ping somepage.com

➜  today git:(master) ✗ fg %1
[1]  + 5420 continued  ping somepage.com
Request timeout for icmp_seq 1
64 bytes from somepage.com icmp_seq=2 ttl=48 time=542.211 ms
64 bytes from somepage.com icmp_seq=3 ttl=48 time=942.658 ms
Request timeout for icmp_seq 4
64 bytes from somepage.com icmp_seq=5 ttl=46 time=333.893 ms

^Z
[1]  + 5420 suspended  ping somepage.com
```

-

#### file

`file` recongize the type of data contained in the file.

```
$ file unix_fc.md
unix_fc.md: UTF-8 Unicode English text, with very long lines

// Another example
05-Using Flask-Bootstrap.mp4: ISO Media, MPEG v4 system, version 1
```

-

Status

**admin, alias, ar, asa, at, awk, basename, batch, bc, bg, c99, cal, cat, cd, cflow, chgrp, chmod, chown, cksum, cmp, comm, command, compress, cp, crontab, csplit, ctags, cut, cxref, date, dd, delta, df, diff, dirname, du, echo, ed, env, ex, expand, expr, false, fc, fg, file**, find, fold, fort77, fuser, gencat, get, getconf, getopts, grep, hash, head, iconv, id, ipcrm, ipcs, jobs, join, kill, lex, link, ln, locale, localedef, logger, logname, lp, ls, m4, mailx, make, man, mesg, mkdir, mkfifo, more, mv, newgrp, nice, nl, nm, nohup, od, paste, patch, pathchk, pax, pr, printf, prs, ps, pwd, qalter, qdel, qhold, qmove, qmsg, qrerun, qrls, qselect, qsig, qstat, qsub, read, renice, rm, rmdel, rmdir, sact, sccs, sed, sh, sleep, sort, split, strings, strip, stty, tabs, tail, talk, tee, test, time, touch, tput, tr, true, tsort, tty, type, ulimit, umask, unalias, uname, uncompress, unexpand, unget, uniq, unlink, uucp, uudecode, uuencode, uustat, uux, val, vi, wait, wc, what, who, write, xargs, yacc, zcat