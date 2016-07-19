## SQLAlchemy
It is an open source SQL toolkit and object-relational mapper. Long story short: its an abstraction over SQL. Phylosophy behind SQLAlchemy is that databases behave less and less like object collections the more size and performance start to matter.


### Model

```
from sqlalchemy import create_engine

# echo logs generated SQL
engine = create_engine('sqlite:///:memory:', echo=True)
```

http://docs.sqlalchemy.org/en/latest/orm/tutorial.html