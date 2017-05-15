
from itertools import combinations_with_replacement

for val in combinations_with_replacement(range(4), 2):
    print(val)
print()
for val in combinations_with_replacement(range(4), 5):
    print(val)

