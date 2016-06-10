import sqlite3
import json
import sys
import os


def load_data(p):
    '''
    Load data from some source, in this case data source
    is a local file which contains some mock data.
    '''
    with open(p) as d:
        return json.load(d)


def drop_table(cursor, db):
    '''
    Functionality to drop the table.
    '''
    cursor.execute('''DROP TABLE film''')
    db.commit()


def create_table(cursor, db):
    '''
    Create table using SQL sequence.
    '''
    cursor.execute('''CREATE TABLE film (
        id INTEGER PRIMARY KEY,
        asIso INTEGER,
        developer TEXT,
        dilution TEXT,
        film TEXT,
        temperature INTEGER,
        time INTEGER)''')
    db.commit()


def populate(cursor, db, data):
    '''
    Insert data into the database. It works, but there is a better
    way to do it. First, I don't know why autoincrementing doesn't
    work as expected. Second, this should be performed using
    .insertmany() function because of obvious reason.
    '''
    i = 1
    for d in data:
        t = (i, d["asIso"], d["developer"], d["dilution"], d["film"],
             d["temperature"], d["time"])
        cursor.execute(
            '''INSERT INTO film (id, asIso, developer, dilution, film, temperature, time) 
            VALUES (?, ?, ?, ?, ?, ?, ?)''', t)
        i += 1
    db.commit()
    print("Data inserted")


if __name__ == '__main__':
    # Find an absolute path of the data and load it.
    p = os.path.abspath('data.json')
    data = load_data(p)

    # Connect (or create and connect) to the database
    # and get a reference to a db cursor.
    db = sqlite3.connect('data.db')
    cursor = db.cursor()

    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        drop_table(cursor, db)
        print('Table dropped')
        sys.exit(0)
    else:
        # Ugly workaround for test. Create the table
        # if table already exists, do nothing.
        try:
            create_table(cursor, db)
            print('Table created')
        except sqlite3.OperationalError:
            print('Table exists')

    # Populate the data
    populate(cursor, db, data)

    # Close cursor after each operation with a database.
    cursor.close()
