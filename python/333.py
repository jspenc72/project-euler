#!/usr/bin/env python

N=1000000
prime=[True]*N
prime[0]=prime[1]=False
for i in xrange(N):
    if i*i>=N: break
    if not prime[i]: continue
    for j in xrange(i*i,N,i): prime[j]=False

print 'got all the primes'

F={}
def f(n,x,y,p):
    if n==0: return 1
    if n<x or y==0: return 0
    if n<x*y:
        if p: return 0
        else: return f(n,x,y//3,False)
    if (n,x,y,p) in F: return F[n,x,y,p]
#    t = f(n-x*y,2*x,y//3)
#    if t: print n-x*y, 2*x, y//3
#    t = f(n,2*x,y)
#    if t: print n, 2*x, y
#    t = f(n,x,y//3)
#    if t: print n,x,y//3
    ff = f(n-x*y,2*x,y//3,False) + f(n,2*x,y,True)
    if not p: ff += f(n,x,y//3,False)
    F[n,x,y,p] = ff
    return ff

total=0
for i in xrange(2,N):
    if i%1000==0: print i
    if not prime[i]: continue
    q=1
    while q<=i: q*=3
    if f(i,1,q//3,False)==1:
        total+=i
print total
