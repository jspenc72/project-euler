#!/usr/bin/env python
from itertools import count
from utils import memoize

N=51

def squarefree(n,k,factor):
    fac = {}
    for i in xrange(2,n+1):
        for p in factor[i]:
            if p in fac: fac[p] += factor[i][p]
            else: fac[p] = factor[i][p]
    for i in xrange(2,k+1):
        for p in factor[i]:
            fac[p] -= factor[i][p]
    for i in xrange(2,n-k+1):
        for p in factor[i]:
            fac[p] -= factor[i][p]
    for f in fac:
        if fac[f] > 1: return False
    return True

@memoize
def fact(n):
    if n<=1: return 1
    return n*fact(n-1)

@memoize
def c(n,k):
    if k==0 or k==n: return 1
    if n<=1 and k<=1: return 1
    return c(n-1,k-1) + c(n-1,k)

#pascal = []
#for i in xrange(N): pascal.append([0]*52)
#pascal[0][1] = 1
#for i in xrange(1,N):
#    for j in xrange(1,i+1):
#        pascal[i][j] = pascal[i-1][j] + pascal[i-1][j-1]
prime = [True]*N
prime[0]=prime[1]=False
for i in count(2):
    if i*i>=N: break
    if not prime[i]: continue
    for j in xrange(i<<1,N,i):
        prime[j] = False
factor = [0]*N
for i in xrange(2,N):
    factor[i]={}
    for j in xrange(N):
        if not prime[j]: continue
        if not i%j: factor[i][j]=0
        num = i
        while not num%j:
            factor[i][j] += 1
            num /= j
done = set([])
total=1
squarefree(6,3,factor)
for row in xrange(2,N):
    for col in xrange(1,row/2+1):
        test = c(row,col)
        if test in done: continue
        done.add(test)
        if squarefree(row,col,factor):
            total += test
print total
