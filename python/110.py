#!/usr/bin/env python

N = 4*10**6
M = 2*N-1
P = 15
#N = 1000
#M = 2*N-1
#P = 7

parr = []
factor = []
for i in xrange(300):
    factor.append({})

prime = [True]*300
prime[0]=prime[1]=False
p = -1
for i in xrange(300):
    if not prime[i]: continue
    p += 1
    factor[i][p] = 1
    for j in xrange(i<<1,300,i):
        k = 0
        t = j
        while t%i==0:
            t /= i
            k += 1
        prime[j] = False
        factor[j][p] = k

for i in xrange(300):
    if len(parr) >= P: break
    if prime[i]: parr.append(i)

def ways(arr):
    return reduce(lambda x,y : x*y, (2*i+1 for i in arr if i>0))

def last(arr):
    for i in xrange(len(arr)-1,-1,-1):
        if arr[i]>0: return i
    return -1

def number(arr):
    ret = 1
    for i in xrange(len(arr)):
        ret *= parr[i]**arr[i]
    return ret

a = [1]*P

while True:
    bigp = last(a)
    a[bigp] -= 1
    for i in xrange(2, parr[bigp]):
        f = factor[i]
        for j in f:
            a[j] += f[j]
        if ways(a) >= M:
            #print a, ways(a), i, factor[i], bigp, parr[bigp]
            break
        for j in f:
            a[j] -= f[j]
    else:
        a[bigp] += 1
        break

print number(a)
