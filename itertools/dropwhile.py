
from itertools import dropwhile

a_list = [ 1, 3, 5, 3, 6, 7, 8, 1, 7 ]

print(*dropwhile(lambda x: x < 4, a_list))

def filt(x):
    return x < 4
    
print(*dropwhile(filt, a_list))

