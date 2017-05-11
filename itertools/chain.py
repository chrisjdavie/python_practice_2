
from itertools import chain

for el in chain([1, 2, 3], range(3), ['d', 'e', 'f']):
    print(el)

