import sqlite3

# connect to database
conn = sqlite3.connect('database.db')

# create cursor
c = conn.cursor()

c.execute("DELETE FROM words")

# # commit a command
conn.commit()

# close the connecton
conn.close()