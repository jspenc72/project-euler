#!/usr/bin/env python
from itertools import count
from operator import mul

mem={}
def fact(n):
    if n in mem: return mem[n]
    if n<=1: return 1
    ret = reduce(mul, xrange(2,n+1))
    mem[n]=ret
    return ret

def c(n,k):
    return fact(n)/fact(k)/fact(n-k)

def window(i,n):
    if i==n-4: yield [i]
    else:
        for j in xrange(i+1,min(i+4,n-4)+1):
            for w in window(j,n):
                yield [i]+w

def win_weight(start):
    end = map(lambda x: x+4, start)
    d = 1
    prev = ei = si = 0
    while si<len(start) or ei<len(end):
        if si<len(start) and (ei >= len(end) or start[si] < end[ei]):
            d *= fact(start[si]-prev)
            prev = start[si]
            si += 1
        else:
            d *= fact(end[ei]-prev)
            prev = end[ei]
            ei += 1
    ret = fact(end[ei-1])//d//fact(len(start))
    if len(start)&1: return ret
    else: return -ret

def bitcount(n):
    ret = 0
    while n:
        n &= (n-1)
        ret += 1
    return ret

primes= [2,3,5,7,11,13,17,
         19,23,29,31,37,41,
         43,47,53,59,61,67,
         71,73,79,83,89,97]

def set_prod(s):
    p = 1
    i = 0
    while s:
        if s&1: p *= primes[i]
        i += 1
        s >>= 1
    return p

def prime(i):
    return primes[i]

memw={}
def wind(l,r,m):
    if m==0: return r==l
    ret = 0
    for i in xrange(4):
        if l<4-i or r<i: continue
        ret += c(l,4-i)*c(r,i)*wind(l,r+i,m-1)
    memw[l,r,m] = ret
    return ret

C={}
def cover(l,r,m,t):
    if m==t: return r==0
    if (l,r,m,t) in C: return C[l,r,m,t]
    ret = 0
    for i in xrange(5):
        if r<i or l<4-i: continue
        if i==0 and c(l,4)>m: ret += (c(l,4)-m)*cover(l,r,m+1,t)
        elif i>0: ret += c(l,4-i)*c(r,i)*cover(l+i,r-i,m+1,t)
    C[l,r,m,t] = ret
    return ret

T={}
def t(n):
    if n==4: return 1
    if n in T: return T[n]
    prev = t(n-1)
    a = (n-2)*(n-3)/2
    if prev<0: return a-prev
    return -prev-a

N = 10**16-1
#N = 1000-1
L = len(primes)
weight = [0]*(L+1)
#weight = map(lambda x:-x,[0, 0, 0, 0, -1, 10, -15, -140, 167, 588, 12405, 18040, -660825, -1491919L, 6540851L, 163231704L, 1047204165L, -7231126120L, -108538207191L, -380096664780L, 5390181262953L, 95286202048870L, 281549719657936L, -7312042598584976L, -103777130212078455L, -232673892541006534L])
ans = 0

coeff = [0]*(L+1)
coeff[4] = 1
for i in xrange(5,L+1):
    for k in count(1):
        if 2*k>i: break
        coeff[i] -= c(i,2*k)*coeff[i-k]

for i in xrange(4,L+1):
    #nz = False
#    for t in xrange(1,c(L,4)+1):
#        ways = cover(0,i,0,t)//fact(t)
#        if ways>0: nz = True
#        if nz and ways==0: break
#        if t&1: weight[i] += ways
#        else: weight[i] -= ways
#        #if not (t%1000): print t, weight[i]
    weight[i] = t(i)

#for i in xrange(4,L+1):
#    print i
#    for w in window(0,i):
#        weight[i] += win_weight(w)

for s in xrange(1<<L):
    if not (s%10000): print s, ans
    b = bitcount(s)
    if b<4: continue
    p = set_prod(s)
    #print b, (N//p), weight[b]
    ans += weight[b]*(N//p)
print ans
