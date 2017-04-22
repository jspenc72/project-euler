#!/usr/bin/env python
import numpy as np

"""
Technically we don't need to construct the actual grid, but I'm lazy. It's a
random walk on a finite, connected, undirected graph. If the transition
probabilities were inversely proportional to degree, the steady state
distribution would have entries proportional to degree. (See e.g. Norris' book,
page 50). In fact this case can be generalized for the two transition matrices
given in the problem: for case 1 we can informally imagine inflating each
node's degree from d to d+1, and for case 2 we can informally imagine inflating
each node's degree from d to 2*d. It's easy to check that these informal
notions are equivalent to using the proper weights in the detailed balance
equations, allowing us to simplify the code somewhat.
"""

N=1000

pi1 = np.zeros((N,N))
pi2 = np.zeros((N,N))
pi1[:,:] = 5.
pi1[0,:] = pi1[N-1,:] = pi1[:,0] = pi1[:,N-1] = 4.
pi1[0,0] = pi1[0,N-1] = pi1[N-1,0] = pi1[N-1,N-1] = 3.
pi2[:,:] = 8.
pi2[0,:] = pi2[N-1,:] = pi2[:,0] = pi2[:,N-1] = 6.
pi2[0,0] = pi2[0,N-1] = pi2[N-1,0] = pi2[N-1,N-1] = 4.
pi1 /= np.sum(pi1)
pi2 /= np.sum(pi2)

ans = 0.
for s in xrange(N):
    sq = (s+1)**2
    i = (sq-1)//N
    j = (sq-1)%N
    ans += .5*(pi1[i,j] + pi2[i,j])

print '%.12f' % ans
