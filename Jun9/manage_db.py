import sys
import sqlite3


def create_table(c, db):
    c.execute(
        '''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT unique, password TEXT)''')
    db.commit()


def drop_table(c, db):
    c.execute('''DROP TABLE users''')
    db.commit()


def insert(c, db):
    # Data to insert
    n = 'Someone'
    p = '+347834221182'
    e = 'some@one.com'
    s = '1q2w3e4r5t'
    c.execute('''INSERT INTO users(name, phone, email, password)
                 VALUES(?,?,?,?)''', (n, p, e, s))
    print('User inserted')
    db.commit()


if __name__ == '__main__':
    db = sqlite3.connect('sample.db')
    cursor = db.cursor()

    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        drop_table(cursor, db)
        print('Table dropped')
        sys.exit()
    else:
        # Ugly workaround for test. Create the table
        # if table already exists, do nothing.
        try:
            create_table(cursor, db)
            print('Table created')
        except sqlite3.OperationalError:
            print('Table exists')

    # Insert the data
    insert(cursor, db)

    cursor.close()
