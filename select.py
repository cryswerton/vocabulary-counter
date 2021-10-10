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
    if sys.argv[1] == 'amount':
        print(f'Words: {len(items)}')
else:
    for item in items:
        print(item)



# # commit a command
conn.commit()

# close the connecton
conn.close()