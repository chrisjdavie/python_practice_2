
from itertools import filterfalse

a_list = [ 1, 3, 7, 2, 5, 4, 9, 9 ]

print(*filterfalse(lambda x: x < 4, a_list))
print(*filterfalse(lambda x: x % 2, a_list))

