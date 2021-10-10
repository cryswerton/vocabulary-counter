import sqlite3
import sys

# connect to database
conn = sqlite3.connect('database.db')

# create cursor
c = conn.cursor()

# create table
# c.execute(""" CREATE TABLE words (
#     word TEXT NOT NULL UNIQUE,
#     dateandtime TEXT
# )""")


# c.execute("schema words")

# c.execute("INSERT INTO words VALUES ('car', datetime('now'))")
# c.execute("SELECT name FROM sqlite_master WHERE type='table'")
# c.execute("SELECT * FROM words WHERE rowid=3")
# c.execute("SELECT * FROM customers WHERE first_name = 'Tim'")
# c.execute("SELECT * FROM customers WHERE first_name LIKE '%ohn%'")
c.execute("SELECT * FROM words")
items = c.fetchall()

if len(sys.argv) > 1:
    if sys.argv[1] == '-A':
        print(f'Words: {len(items)}')
    elif sys.argv[1].isnumeric():
        print('ID search:')
        c.execute(f"SELECT rowid, * FROM words WHERE rowid='{sys.argv[1]}'")
        items = c.fetchall()
        for item in items:
            print(item)
    else:
        print('Word search:')
        c.execute(f"SELECT rowid, * FROM words WHERE word='{sys.argv[1]}'")
        items = c.fetchall()
        for item in items:
            print(item)  
else:
    for item in items:
        print(item)

    



# # commit a command
conn.commit()

# close the connecton
conn.close()