#!/usr/bin/env python

N=3
p=10**9+7
def f(m,n):
    if m==1: return 0
    print pow(pow(2,n,p)-1,m-1,p)
    return (pow(pow(2,n,p)-1,m-1,p) - f(m-1,n))%p
print pow(pow(2,N,p)-1,N,p)
print (pow(pow(2,N,p)-1,N,p) - f(N,N))%p

t=0
for i in xrange(1,2**N):
    for j in xrange(1,2**N):
        for k in xrange(1,2**N):
            if i^j^k==0:
                t+=1
                print bin(2**N+i)[3:]
                print bin(2**N+j)[3:]
                print bin(2**N+k)[3:]
                print
print t
