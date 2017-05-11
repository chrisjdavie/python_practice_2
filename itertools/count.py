from itertools import count

for c in count(15):
    print(c)
    if c > 30:
        break

print()

for c in count(15, 2):
    print(c)
    if c > 30:
        break

print()

for c in count():
    print(c)
    if c > 30:
        break

print()
print(dir(count()))
