
import copy

from itertools import product

for prod in product( [ 1, 2, 3, 4 ], [ 'a', 'b', 'c' ] ):
    print(prod)
print()
for prod in product( [ 1, 2, 3 ], [ True, False ], repeat=3):
    print(prod)
print()
for prod in product( [ True, False ], repeat=3):
    print(prod)
print()

# this solution was me thinking about it as a tree
pool = [ True, False ]

result = [ [] ]

for _ in range(3):
    new_result = []
    for r in result:
        for p in pool:
            new_result.append(copy.copy(r))
            new_result[-1].append(p)
    result = new_result

for res in new_result:
    print(res)

print()
# this solution is the most direct one - 

# Initialise all with the zeroth value, update 
# right most entry until it rolls over, then look
# at next left. Reset all to the right on rollover. 

# it would serve as a solution with O(N) memory,
# and as a generator

# initialise with first element

output = []
i_output = []

for _ in range(3):
    output.append(pool[0])
    i_output.append(0)

# increment the right most element
# if it's a roll over, shift up one element

print(output)

while True:

    j_inc = 1
    while output[-j_inc] == pool[-1]:
        j_inc += 1
        if j_inc == len(output):
            break

    # on rollover, reset all values right        
    for j in range(1, j_inc):
        i_output[-j] = 0
        output[-j] = pool[0]
        
    i_output[-j_inc] += 1
    output[-j_inc] = pool[i_output[-j_inc]]

    print(output)
    if all([ op == pool[-1] for op in output]):
        break    


print()
# and for completenesses sake, the recursive solution
# this is very similar to the tree solution.

def product_rec(pool, r):
    if not r:
        return [[]]
        
    r -= 1
    output = []
    for p in pool:
        higher_solns = product_rec(pool, r)
        
        for soln in higher_solns:
            new_soln = copy.copy(soln)
            new_soln.append(p)
            output.append(new_soln)
    
    return output
    
for soln in product_rec(pool, 3):
    print(soln)

print()
# can I have the recursive solution yield?

def product_rec_gen(pool, r, lower_soln):
    if not r:
        yield lower_soln
    else:
        r -= 1
        for p in pool:
            new_soln = copy.copy(lower_soln)
            new_soln.append(p)
            yield from product_rec_gen(pool, r, new_soln)


for soln in product_rec_gen(pool, 3, []):
    print(soln)

print()

for res in product(['a', 'b'], [1, 2]):
    print(res)

print()

for res in product(['a', 'b'], [1, 2], repeat=2):
    print(res)

