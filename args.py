import sys

print(sys.argv[1])

# for arg in sys.argv:
#     print(arg)

f = open(sys.argv[1], "r", encoding="utf8")

content = f.read()

print(content)