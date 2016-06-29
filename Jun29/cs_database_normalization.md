## Database Normalization
It is a process of organizing the columns and tables to minimize *data redurancy*. Data redurancy is the existence of data that is additional to the actual data and permits correction of errors in stored or transmited data.

Normalization involves decomposing a table into less redurant tables without losing information, and then linking the data back together by defining *foreign keys* in the onld table referencing the *primary keys* of the new ones.

**Primary key**, also known as a unique key is a set of zero or more attrubutes. The value of these attributes are required to be unique for each row in a relation.

**Foreign key** is a field in one table that uniquely identifies a row of another table.

## Normalization Process
- Specify the **key** of the relation
- Specify the **functional dependencies** of the relation
- Apply the definition of each normal form

There are around 7 normal forms exists, but most regular used (?) ones is first, second and third normal form. In essence these normalization forms is kind of benchmark how hard database is normalized. Normal forms are **cumulative in nature**, that means that 3NF is also 1NF and 2NF. Forms higher than 5NF sometimes aren't possible from practical point of view.

#### First Normal Form
A relation is in 1FN if and only if the domain of each attribute contains only indivisible values, and the value of each attribute contains only a single value from that domain.

1. No duplicate columns in single table
2. Each column has single value
3. Each row should be identified by a primary key

#### Second Normal Form
A table is in 2NF if it meets 1NF criteria and no non-prime attribute is dependent on any proper subset of any candidate key of the table.

1. Table should be in 1NF
2. There shouldnt be no partial dependency between non-key attributes and composite key. A partial dependency occurs when a non-key attribute is dependent on only a part of the composite key
3. There shouldnt be no subset of data that comes with multiple rows in a table
4. Define relationships among the new tables and the base table using foreign key

#### Third Normal Form
1. Table should be in 2NF
2. No non-key columns should depend on other non-key column or has no transitive functional depecndency