## Dealing With Nulls
Go `database/sql` package has `sql.NullString`, `sql.NullBool`, `sql.NullInt64`, `sql.NullFloat64`, use them when `null` is expected. For display use `type.Field.Value`.

```
type Sample struct {
    nonNull     string
    perhapsNull sql.NullString
}

func GetSample() []Sample {
    rows, _ := db.Query('select nonNull, perhapsNull from dataset;')
    defer rows.Close()

    samples := []Sample{}
    for rows.Next() {
        s := Sample{}
        rows.Scan(&m.nonNull, &m.perhapsNull)
        if s.Valid {
            // Ok
        } else {
            // Not ok
        }
        samples = append(samples, s)
    }
    return samples
}
```

