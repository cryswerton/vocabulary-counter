import sqlite3

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

c.execute("INSERT INTO words VALUES ('car', datetime('now'))")
c.execute("SELECT rowid, * FROM words")
# c.execute("SELECT * FROM customers WHERE first_name = 'Tim'")
# c.execute("SELECT * FROM customers WHERE first_name LIKE '%ohn%'")

items = c.fetchall()

for item in items:
    print(item)

# # commit a command
conn.commit()

# close the connecton
conn.close()