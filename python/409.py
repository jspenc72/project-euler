#!/usr/bin/env python

def fact(n): return reduce(lambda x,y:x*y, xrange(2,n+1), 1)
def c(n,k): return fact(n)//fact(k)//fact(n-k)

M=10**9+7
N=10**7
P=pow(2,N,M)
pick = [1]
for i in xrange(1,N):
    pick.append(pick[-1]*(P-i)%M)
F=[-1]*(N+1)
def f(m):
    if m==1: return P-1
    if F[m]!=-1: return F[m]
    t = pick[m-1]
    ret = (g(m-1)*(P-m)%M + h(m-1)*(P-m)%M + (t-g(m-1)-h(m-1))*(P-m-1)%M)%M
    F[m] = ret
    return ret
G=[-1]*(N+1)
def g(m):
    if m==1: return P-1
    if G[m]!=-1: return G[m]
    ret = h(m-1)*(P-m)%M*m%M
    G[m]=ret
    return ret
H=[-1]*(N+1)
def h(m):
    if m==1: return 0
    if H[m]!=-1: return H[m]
    ret = (f(m-1)-g(m-1))%M
    H[m] = ret
    return ret
for i in xrange(2,N,20): f(i)
print f(N)
