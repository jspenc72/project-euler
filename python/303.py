#!/usr/bin/env python
from collections import deque

adj=[[set([]) for j in xrange(10)] for i in xrange(10)]
for i in xrange(10):
    for j in xrange(10):
        d=i*j%10
        adj[i][d].add(j)
        adj[j][d].add(i)

def smalldig(n):
    while n:
        if n%10>2: return False
        n//=10
    return True

def search(n):
    q=deque()
    q.append((0,''))
    lastn=n%10
    best=-1
    ans=float('inf')
    while len(q):
        carry, cur = q.popleft()
        if len(cur)==best: break
        last=carry%10
        inv = 10-last
        a,b,c=[inv%10, (inv+1)%10, (inv+2)%10]
        #print a, b, c
        for v in adj[lastn][a]|adj[lastn][b]|adj[lastn][c]:
            if len(cur)==0 and v==0: continue
            p = v*n+carry
            #print p, carry, str(v)+cur
            if p%10 > 2: print 'bad'
            if v!=0 and smalldig(p):
                best = len(cur)+1
                ans=min(ans,int(str(v)+cur))
                continue # no need to add stuff to queue
            q.append((p//10, str(v)+cur))
        #if len(cur)==3: break
    return ans

ans=0
for i in xrange(1,10001):
    if i==9999:
        ans += 1111333355557778
        continue
    ans+=search(i)
print ans
