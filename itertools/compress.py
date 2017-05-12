
from itertools import compress, cycle

for el in compress([ 1, 2, 3, 4, 5 ], [ True, False, True, False, True ]):
    print(el)

print()

for el in compress([ 1, 2, 3, 4, 5 ], cycle([1, 0])):
    print(el)



