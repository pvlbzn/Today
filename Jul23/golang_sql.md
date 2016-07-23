## Golang and Database
[Here](https://golang.org/src/database/sql/doc.txt) is a statement about sql/driver packages. Package [sql](https://golang.org/pkg/database/sql/) provides a generic interface aroud SQL databases. 

```
// Connecting to a database
db, err := sql.Open(driver, name)

// To verify that a connection can be made before making a query
if err := db.Ping(); err != nil {
    log.Fatal(err)
}


// Executing queries
// Exec is ised where no rows are returned
res, err := db.Exec(
    "INSERT INTO users (name, age) VALUES ($1, $2)", name, age,
)

// Query is used for retrieval
rows, err := db.Query("SELECT * FROM users WHERE age=$1", age)
if err != nil {
    log.Fatal(err)
}
for rows.Next() {
    var name string
    if err := rows.Scan(&name); err != nil {
        log.Fatal(err)
    }
    // Do something with it
}
if err := rows.Err(); err != nil {
    log.Fatal(err)
}

// Query row is used where only a single row is expected
var age int64
row := db.QueryRow("SELECT age FROM users WHERE name = $1", name)
err := row.Scan(&age)

// Prepared statements!
age := 24
statement, err := db.Prepare("SELECT name FORM users WHERE age = $1")
if err != nil {
    log.Fatal(err)
}
// Exec, Query and QueryRow can be called on statements.
rows, err := statement.Query(age)
// Do smth
statement.Close()
```

