#!/usr/bin/env python
from gmpy import mpq

N=45

psum=[0]*(N+2)
for i in xrange(N,0,-1):
    psum[i] = psum[i+1] + mpq(1)/mpq(i*i)

mem={}
def gao(i=2,t=mpq('1/2')):
    if t==0:
        print 'found'
        return 1
    if i==N+1 or t<0 or psum[i]<t: return 0
#    hsh=(i,t)
#    if hsh in mem: return mem[hsh]
    total = gao(i+1,t) + gao(i+1,t-mpq(1)/mpq(i*i))
#    mem[hsh]=total
    return total

print gao()
