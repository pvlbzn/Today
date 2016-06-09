import sqlite3


def create_table(c, db):
    c.execute('''
        CREATE TABLE  users(id INTEGER PRIMARY KEY,
                            name TEXT, phone TEXT,
                            email TEXT unique,
                            password TEXT)
    ''')
    db.commit()


def drop_table(c, db):
    c.execute('''DROP TABLE users''')
    db.commit()


if __name__ == '__main__':
    db = sqlite3.connect('sample.db')
    cursor = db.cursor()
    # drop_table(cursor, db)
    create_table(cursor, db)
    cursor.close()
