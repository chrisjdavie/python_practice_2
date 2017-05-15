# what it doesn't do is copy, strictly, which is interesting
# and it does progress vals, so it shouldn't be used as a copy
# directly

from itertools import tee

vals = [ 4, 2, 7, 5 ]

vals_a, vals_b = tee(vals)

for a in vals_a:
    print(a)
print()
for b in vals_b:
    print(b)

