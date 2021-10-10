import re

f = open("feed.txt", "r", encoding="utf8")

content = f.read()

res = re.findall(r'\w+', content)

print(len(res))

for word in res:
    print(word)