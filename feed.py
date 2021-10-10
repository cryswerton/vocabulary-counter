import sqlite3
import re
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

# abre o arquivo
f = open(sys.argv[1], "r", encoding="utf8")

# pega o conteúdo do arquivo
content = f.read()

# extrai as palavras do conteúdo
res = re.findall(r'\w+', content)

# insere todas as palavras no banco de dados
for word in res:
    count = 0
    c.execute(f"SELECT 1 FROM words WHERE word='{word.lower()}'")
    data = c.fetchall()
    if data:
        count = count + 1
        print(f'Found word {data}: {count}')
    else:
        print('Not found.')
        c.execute(f"INSERT INTO words VALUES ('{word.lower()}', datetime('now'))")

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