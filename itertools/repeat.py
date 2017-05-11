
from itertools import repeat, islice

for elem in islice(repeat('A'), 10):
    print(elem)


print()

for elem in repeat('A', 10):
    print(elem)
