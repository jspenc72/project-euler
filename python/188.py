#!/usr/bin/env python
from itertools import count
import sys
sys.setrecursionlimit(10000)

#N=16*10**6+1
#smallprime = [-1]*N
#for i in count(2):
#    if smallprime[i]!=-1: continue
#    if i*i >= N: break
#    for j in xrange(i,N,i):
#        if smallprime[j]!=-1: continue
#        smallprime[j]=i
#
#def totient(n):
#    if n==10**8: return 40*10**6
#    if n==40*10**6: return 16*10**6
#    ret=n
#    while n!=1:
#        p=smallprime[n]
#        while smallprime[n]==p: n/=p
#        ret = ret/p*(p-1)
#    return ret

def powermod(a,b,m):
    if b==0: return 1
    if b&1: return powermod(a,(b-1)/2,m)**2%m*a%m
    return powermod(a,b/2,m)**2%m

def uparrow(a,b,m):
    if b==1: return a%m
    return powermod(a,uparrow(a,b-1,m),m)

print uparrow(1777,1855,10**8)
#n=10**8
#while n!=1:
#    print n
#    n = totient(n)
