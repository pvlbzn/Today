####Aim

Main aim is to make a research and get myself familiar to "Unix-way". As a base I took a UNIX 03 standard. However, I won't cover in great details tools which are not implemented in Linux, which isn't UNIX nor POSIX(this one depends on distribution and may vary) on 100%. This may sound weird, because I can take a Linux Base Standard ([LSB 5.0.0](http://refspecs.linux-foundation.org/LSB_5.0.0/LSB-Core-generic/LSB-Core-generic/command.html#CMDUTIL)), but, for example, `at` utility is in the "Core" part of the LBS, but my lastest Ubuntu distro doesnt aware of it.

To be precise, main purpose is to take a close look at things such as tooling design, proper naming, unix-way, modularity.


####admin

```
$ man admin
> No manual entry for admin
```

Ok.

-

####alias

`alias` instructs the shell to replace one string with another.

```
alias [name=[command]]
```

Invoking `alias` without arguments prints all currently alased commands. Ouput is "shell-dependant". Bash will print aliases from .bash_aliases. Zsh will print another output.

-

####ar

`ar` - create, modify, and extract from archives.

Nowadays archiver used mostly to create and update static library files that the link editor or linker uses. It has been replaced by `tar` for purposes different from creation of static libs. This utility is here because this doc is about Unix, however in the Linux Standard Base `ar` has been deprecated.

-

####asa

`asa` - interpter carriage-control characters.

`man` pages on Linux 4.4.0 don't know about `asa`.

-

####at

`at` - queue, examine or delete jobs for later execution.

-

####awk

`awk` - pattern directed scamnning and processing language. `mawk` is an interpreter for the AWK PL. Alfred Aho, Peter Weinberger, Brian Kernighan is what AWK stands for.
