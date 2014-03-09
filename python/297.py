#!/usr/bin/env python

N=10**17
F=[1,2]
while True:
    n=F[-1]+F[-2]
    F.append(n)
    if n>=N: break

S={}
def s(n):
    if n==0: return 0
    if n in S: return S[n]
    total=0
    for i in xrange(len(F)):
        if F[i]>n: break
        total += min(F[i+1],n)-F[i] + s(min(F[i+1],n)-F[i])
    S[n]=total
    return total

print s(N)
