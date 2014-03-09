#!/usr/bin/env python

N=10**7
prime = [True]*(N+1)
prime[0]=prime[1]=False
for i in xrange(int(N**.5)+2):
    if not prime[i] or i*i >= N+1: continue
    for j in xrange(i*i,N,i):
        prime[j]=False

plist=[]
for i in xrange(N):
    if prime[i]: plist.append(i)

demiprime=[]
for i in xrange(N+1):
    demiprime.append([i])

for p in plist:
    for q in xrange(p,N+1,p):
        if not demiprime[q]: continue
        if len(demiprime[q]) >= 3:
            demiprime[q] = False
        else: demiprime[q].append(p)

used = set([])
total = 0
for i in xrange(N,-1,-1):
    if not demiprime[i]: continue
    if len(demiprime[i]) == 3:
        test = (demiprime[i][1], demiprime[i][2])
        if test not in used:
            used.add(test)
            total += i
print total
