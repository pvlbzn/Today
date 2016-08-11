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


#### Dealing with JSON serialization
Well, `sql.NullType` solves problem with null handeling, but not with serialization. Serialized null type will produce data structure like:

```
"date_closed":{"String":"","Valid":false}
```

which is not ok.

Solution is to create a custom type and implement `json.Marshaler` interface on it.

```
type JsonNullString struct {
    sql.NullString
}

func (v JsonNullString) MarshalJSON() ([]byte, error) {
    if v.Valid {
        return json.Marshal(v.String)
    }
    return json.Marshal(nil)
}
```

So, instead of using `sql.NullString` this custom type may be used for proper JSON rendering.

