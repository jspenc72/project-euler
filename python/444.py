#!/usr/bin/env python
import numpy as np
from utils import memoize, fact
# TODO: clean this up

N = 111
E = [0]*(N+1)
S = [0]*(N+1)
E[1] = S[1] = 1
for i in xrange(2, N+1):
    E[i] = 1 + 1./i * S[i-1]
    S[i] = S[i-1] + E[i]

#def S(n):
#    #return 1 + (n+1)*(np.log(n) - .5)
#    return 1 + (n+1)*sum(1./i for i in xrange(2,n+1))
#
#print 1 + 1./N * S(N-1)

gamma = 0.57721566490153286060651209008240243104215933593992

def EE(n):
    return np.log(n) + gamma + 1./(2*n) - 1./(12*n**2)

def T(n,k):
    if k==0:
        return 1
    else:
        ans = 1
        for j in xrange(k):
            ans *= (n+j)
        return ans / fact(k)
        #return sum(T(i,k-1) for i in xrange(1,n+1))

def SS(n,k):
    if k==0:
        if n > 1000:
            return EE(n)
        else:
            return E[n]
    else:
        return 1./k * ((n+1)*SS(n+1,k-1) - sum(T(n,j) for j in xrange(k+1)))

print SS(10,1)
print 11*(E[11]-1)
print sum(S[i] for i in xrange(1,11))
print SS(10,2)
def test(n):
    return abs(.5*((n+2)*S[n] - T(n,2)) - sum(S[i] for i in xrange(1,n+1))) < .00001

print test(10)
print test(50)
print test(100)

print .5*(11*S[11] - (1 + 10 + T(10,1)))
print SS(100,3)

print T(10,5), 10*11*12*13*14/120

print SS(10**14, 20)
