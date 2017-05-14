
from itertools import starmap

for res in starmap(pow, [(2,3), (3,2), (10,3)]):
    print(res)

print()

[ i for i in starmap(print, [(2,3), (3,2), (10,3)]) ]

