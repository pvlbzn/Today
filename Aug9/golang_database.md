## `sql` package
Package `sql` provides a generic interface around SQL databases. The `sql` package must be used in conjunction with a database driver.

```
db, err := sql.Open(driverName, dataSourceName)(*DB, error)
```

Learn by example:

```
var (
    id int
    name string
)

rows, err = db.Query("select id, name from users where id=$1", whateverID)
if err != nil {
    panic(err)
}
defer rows.Close()

for rows.Next() {
    err := rows.Scan(&id, &name)
    ir err != nil {
        log.Fatal(err)
    }
}

err = rows.Err()
ir err != nil {
    panic(err)
}
```

`Row` is the result of calling `QueryRow` and `Rows` is the result of a `Query`. Its cursor starts before the first row of the result set. `Close()` closes the `Rows` preventing further enumeration. If `Next` returns false, the `Rows` are closed automatically. `Close` does not affect the result of `Err`.

`func (rs *Rows) Scan(dest ...interface{}) error` copies the columns in the current row into the values pointed at by `dest`. The number of values in `dest` must be the same as the number of columns in `Rows`.

```
type User struct {
    id int
    login string
}

users = []User{}

for rows.Next() {
    var u User
    err = rows.Scan(&u.id, &u.login)
    if err != nil {
        panic(err)
    }
    users = append(users, u)
}
```

