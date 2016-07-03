## Database Normalization
Was studied [before](https://github.com/pvlbzn/Today/blob/d72d601d8350102f9e974d3b88c275ffcead7fa4/Jun29/cs_database_normalization.md).

## Database Aggregation
Database agregation is a function where the values of multiple rows are grouped together as input on certain criteria to form a single value of more significant meaning or measurement. Such functions are `count`, `avg`, `max`, `min`, `sum`.


## Database Joints
The basic idea behind joints is to get a full data from a normalized database. 

`join -> restriction -> aggregation`

## Key

### Primary Key

Primary key is a column that uniquely identify what each row in a table is about.

```
create table people (
    id serial primary key,
    name text,
    birthdate date
);

-- Or there can be two different primary key as one
create table postal_places (
    code text,
    country text,
    name text,
    -- Because code is not unique across all of the world,
    -- but it is unique to the each contry.
    primary key (code, country)
);
```

### Declaring Relationships

`references` provides referential integrity. Columns that are supposed to refere to each other are guaranteed to do so.

```
create table sales (
    sku text references products,
    sale_date date,
    count integer
);
```

### Foreign Key
Is a column or set of columns in one table, that uniquely identifies rows in another table.

```
create table students (
    id serial primary key,
    name text
);

create table courses (
    id text primary key,
    name text
);

create table grages (
    student integer references students(id),
    course text references courses(id),
    grade text
);
```

## Subqueries
Subquerie allows to select from the result of the previous select.

## Views
A *view* is a `select` query stored in the database in a way that lets you use it like a table.

## Operators
SQL supports common operators such as comparison oparators `=`, `>=`, etc.

```
select name from animals
where species = llama`
and birthdate >= date1
and birthdate <= date2;
```

## Python DB-API
Python has DB-API which is awesome idea to standartize all the modules for all databases. Generally it looks like:

```
import database_module as db

conn = db.connect('Connection', 'Name', 'User', 'Etc')
cursor = conn.cursor()
cursor.execute('SELECT QUERY')

results = cursor.fetchall()

conn.close()
```