## SQLite
`SQLite` is a relational database contained in a `C` programming library. It isnt client-server database. `SQLite` is embedded into the end program. Its size is (version 3.13.0) 699KiB, and as far as I understand this size can be reduced via excluding some features.

`SQLite` has a great [documentation](https://www.sqlite.org/docs.html).

#### Limitations
It implements *most* of SQL-92 standard. `SQLite` supports an unlimited number of simultaneous readers, but it only allowe one writer at any instant tume.
#### Create

```
# Or without a db name
sqlite3 name.db
sqlite> ...
```

#### Pythons Perspective

```
import sqlite3
import json

data = json.load(open('data.json'))
# Create or open a file .db
conn = sqlite3.connecn('data.db')

# It is also possible to create db in RAM
db = sqlite3.connect(':memory:')
```

`SQLite` has bindings to a lot (really lot!) languages. Python just, as usual, okey of learn things, play with things.

```
# All manipulations should .close()
db.close()
```

Read code with comments `/manage_db.py`.