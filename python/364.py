#!/usr/bin/env python

# For stage 0, we have A X B X C cases to consider,
# where A, B, and C are each instances of
# particular subcases.

# Subcase A: whether the furthest left seat is at a boundary.
# There are 2 possibilities for this case

# Subcase B: whether the furthest right seat is at a boundary.
# There are 2 possibilities for this case

# Subcase C: whether the rightmost person is 1 seat or 2 seats
# away from the second-rightmost person.
# There are again 2 possibilities here.

N = 1000000
fact = [1]
M = 10**8 + 7

for i in xrange(1, N//2+1): # precompute factorials
    fact.append(fact[-1]*i%M)

def ch(n,k): # Calculating n choose k, mod M. Use Fermat's little thm.
    return fact[n]*pow(fact[k],M-2,M)%M*pow(fact[n-k],M-2,M)%M

ans = 0
for a in (False, True): # space not at end, space at end
    for b in (False, True): # space not at end, space at end
        for c in (False, True): # 1 seat away, 2 seats away from rightmost
            n = N - a - 2 - b - 1 - c
            x2 = n//2 - n%2
            x3 = n%2
            while x2 >= 0:
                n1 = x2 + x3 + 2 # number of participants in stage 0
                i1 = ch(x2+x3,x2) # number of interleavings for stage 0
                n2 = a + b + c + x3 # number of participants in stage 1
                p2 = n2 - a - b # number of empty adjacent pairs
                n3 = N-n1-n2 # number of participants in stage 2
                f1 = fact[n1]
                f2 = fact[n2]
                f3 = fact[n3]
                ans = (ans + f1*f2%M*pow(2,p2,M)*f3%M*i1%M)%M
                x2 -= 3
                x3 += 2
print ans
