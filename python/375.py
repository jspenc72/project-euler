#!/usr/bin/env python
from collections import deque

# probably an O(mod) solution, but O(N) is just fine
# just does the obvious thing, keeping track of M(i)
# at each index i.

N = 2*10**9
s = 290797
mod = 50515093
q = deque()
qsum = 0
runningsum = 0
ans = 0

q.appendleft((0,0))

for i in xrange(1,N+1):
    s = s**2 % mod
    while len(q) > 1 and q[0][0] > s:
        pop = q.popleft()
        qsum -= pop[0]
        runningsum -= (pop[1]-q[0][1])*pop[0]
    runningsum += (i-q[0][1])*s
    q.appendleft((s, i))
    ans += runningsum

print ans
