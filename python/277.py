#!/usr/bin/env python

def modpow(a,n,m):
    ret=1
    while n:
        if n&1: ret=(ret*a)%m
        n>>=1
        a = (a*a)%m
    return ret

def check(a1):
    checkstr=''
    for i in xrange(len(moves)):
        if a1%3==0:
            checkstr+='D'
            a1/=3
        elif a1%3==1:
            checkstr+='U'
            a1 = (4*a1+2)/3
        else:
            checkstr+='d'
            a1 = (2*a1-1)/3
    return checkstr

moves='UDDDUdddDDUDDddDdDddDDUDDdUUD'
a=0
b=0
d=0

for m in moves:
    if m=='D': d += 1
    if m=='U':
        a+=2
        b*=4
        b+=2*3**d
        d+=1
    if m=='d':
        a+=1
        b*=2
        b-=3**d
        d+=1

# we may then use phi(3*3^d)==phi(3^30)==3^30-3^29 in order
# to find (2^21)^-1 (mod 3^30)
x = modpow(2**a,3**(d+1)-3**d-1,3**(d+1))*(2*3**d-b)%3**(d+1)

# x + k*3^30 > 10^15 ==> k == ceil((10^15-x)/3^30)
# assumes 10^15 - x is not evenly divisible by 3^30
print x + (10**15-x+3**30-1)/3**30 * 3**30
