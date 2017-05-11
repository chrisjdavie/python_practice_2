
from itertools import cycle

for _, p in zip(range(15), cycle('abcd')):
    print(p)

