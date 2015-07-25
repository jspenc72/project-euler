#!/usr/bin/env python
import numpy as np

# Just implement the DP... dunno why the previous attempt failed.
# Maybe some more care should be taken with precision.

# More details:
#
# V[I] = E[I^2] - E[I]^2
#
# E[I] is easy to compute, the hard part is E[I^2]
#
# We can save some time by noting that:
#
# E[I^2] = E[(\sum_{k=1}^D i)^2]
#        = E[E[(\sum_{k=1}^D i)^2 | D]]
#        = E[E[D*E[i^2] - (D^2-D)*E[i]^2 | D]]
#
# Everything in the inner expectation is simple,
# so we just need a way to get P(D=d).
# This can be done by observing that
#
# P(D=d) = E[P(D=d | O)]
#
# and reasoning recursively the same way to get P(O=o).
# This results in a reasonably simple DP (see function 'f').
    
sides = [1,4,6,8,12]
P = [np.array([1.])]
for s in sides[1:]:
    P.append(np.zeros(s * len(P[-1])))

F={}
def f(i,j,k):
    if j==0 and k==0: return 1.
    if j>k: return 0.
    if sides[i]*j < k: return 0.
    if (i,j,k) in F: return F[i,j,k]
    ans = 0.
    for roll in xrange(1,min(k,sides[i])+1):
        ans += f(i,j-1,k-roll)/float(sides[i])
    F[i,j,k] = ans
    return ans

for i in xrange(1,len(sides)):
    for j in xrange(len(P[i-1])):
        for k in xrange(j,len(P[i])):
            P[i][k] += P[i-1][j] * f(i,j+1,k+1)

EI2 = 0.
ei = sum(xrange(1,21))/20.
ei2 = sum(i**2 for i in xrange(1,21))/20.

Ds = np.arange(1, len(P[-1])+1)
EI2 = np.sum(P[-1] * (Ds * ei2 + (Ds*Ds - Ds)*ei**2))

EI = 1.
for s in sides[1:] + [20]: # don't forget icosahedral dice
    EI *= (s+1)/2.

print EI2 - EI**2
