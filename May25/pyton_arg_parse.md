## argparse
[`argparse`](https://docs.python.org/2/howto/argparse.html) is based on [`optparse`](https://docs.python.org/2/howto/argparse.html). `argparse` is "recommended" module to parse arguments.

#### Concepts
Different arguments options, an easy example:

```
1. $ ls
2. $ ls child_dir/
3. $ ls -al
4. $ ls --help
```

#### Framework
`argparse` behaves like a framework.

```
import argparse

p = argrapse.ApgumentParser()
p.parse_args()
```

If call this script with `-h` argument, it will already print meaningful help:

```
usage: script.py

optional argument:
	-h, --help  show this help message and exit
```

Example is here `./argvparser.py`.