
from itertools import takewhile

for val in takewhile(lambda x: x < 4, [ 1, 3, 2, 5, 3, 7 ]):
    print(val)

