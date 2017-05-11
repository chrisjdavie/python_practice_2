
from itertools import islice, count

counter = count()

for c in islice(counter, 5):
    print(c)

print()

for c in islice(counter, 5):
    print(c)

print()

for c in islice(count(), 2, 10):
    print(c)

print()

for c in islice(count(), 2, 10, 3):
    print(c)

