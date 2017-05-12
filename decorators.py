
from itertools import islice

# using a decorator to calculate and cache the nth prime
# this is of course not sensible - using the @ notation
# to change the inputs in a meaningful way is 
# unclear.
#
# IRL it'd be - 
# ith_prime = ith_value_cached_func_generator(generate_primes)
#
# I'm just checking that I remember the format and functionality
# of decorators properly

def ith_value_cached_func_generator(gen_fn, **kwargs):

    precalced = []
    values = gen_fn(**kwargs)

    def ith_fn(N):
        values_to_calc = N - len(precalced)

        for val in islice(values, max(0, values_to_calc)):
            precalced.append(val)

        return precalced[N-1]

    return ith_fn

@ith_value_cached_func_generator
def generate_primes(N=10**6):

    D = {}

    for q in range(2, N):
        if q not in D:
            yield q
            D[q*q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p+q,[]).append(p)
            del D[q]


print(generate_primes(4))
print(generate_primes(7))
print(generate_primes(3))



