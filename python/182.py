#!/usr/bin/env python

p=1009
q=3643
phi=(p-1)*(q-1)
lam=611856
lamp=p-1
lamq=q-1

def gcd(a,b):
    while b!=0:
        a, b = b, a%b
    return a

total=0
for e in xrange(2,phi):
    if gcd(e,phi)>1 or (e-1)%lamp==0 or (e-1)%lamq==0: continue# or (e-1)%lam==0: continue
    total += e
print total
