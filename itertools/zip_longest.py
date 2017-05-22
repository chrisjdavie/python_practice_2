
from itertools import zip_longest

for a, b in zip_longest([ 1, 2, 3 ], 'aaabbcdeefgh'):
    print(a,b)
print()
for a, b in zip_longest([ 1, 2, 3 ], 'aaabbcdeefgh', fillvalue='*'):
    print(a,b)

