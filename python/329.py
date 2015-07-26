#!/usr/bin/env python
import numpy as np
from fractions import Fraction

N=500
seq = 'PPPPNNPPPNPPNPN'
seq = map(lambda x: True if x=='P' else False, seq)

# we can actually get away with using a table with only
# two rows since computation of the next row only
# requires the previous row, but I am lazy
mem = np.zeros((len(seq), N), dtype=Fraction)

prime = np.ones(N+1,dtype=bool)

prime[0]=prime[1]=False
for i in xrange(N+1):
    if not prime[i]: continue
    if i*i > N: break
    for j in xrange(i*i,N+1,i):
        prime[j] = False

prime = prime[1:]

for i in xrange(len(seq)):
    for j in xrange(N):
        
        if i>0:
            fac = Fraction(0,1)
            if j>0:
                fac += mem[i-1][j-1] * (Fraction(1,2) if j-1>0 else 1)
            if j<N-1:
                fac += mem[i-1][j+1] * (Fraction(1,2) if j+1<N-1 else 1)
        else:
            # can probably be factored out at the end, but we
            # do this here to be safe
            fac = Fraction(1,N)

        if prime[j] == seq[i]:
            fac *= Fraction(2,3)
        else:
            fac *= Fraction(1,3)

        mem[i][j] = fac

print np.sum(mem[-1])
