
import operator
from itertools import accumulate

vals = [ 1, 2, 3, 4, 5 ]

for acc in accumulate(vals):
    print(acc)
print()
for acc in accumulate(vals, func=operator.mul):
    print(acc)


