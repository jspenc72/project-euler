#!/usr/bin/env python
#import sys

#r=int(sys.argv[1])
#mod=int(sys.argv[2])
#
#row=[1]
#for i in xrange(r):
#    row = [1] + [(row[i]+row[i+1])%mod for i in xrange(len(row)-1)] + [1]
#    for v in row:
#        if v: print v,
#        else: print '*',
#    #print [v for v in row], sum(not v for v in row)
#    print sum(not v for v in row)

#See Lucas' Theorem

def sumupto(digits, p):
    if not digits: return 1
    n=digits[0]
    l=len(digits)-1
    return (n*(n+1)/2)*(p*(p+1)/2)**l + (n+1)*sumupto(digits[1:], p)

N=10**9-1
p=7
digits=[]
while N>0:
    digits.append(N%p)
    N/=p
digits.reverse()
print sumupto(digits, 7)
