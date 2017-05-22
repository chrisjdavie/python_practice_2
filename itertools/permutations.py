
from itertools import permutations

for perm in permutations([0, 1, 2, 3]):
    print(perm)
print()
for perm in permutations([ 0, 1, 2, 3 ], r = 3):
    print(perm)

