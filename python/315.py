#!/usr/bin/env python

LL = 10**7
UL = 2*10**7

def bitcount(n):
    c = 0
    while n>0:
        c += 1
        n &= (n-1)
    return c

d = {}
naivedict = {}

clock = [0]*10
clock[0] = int('0b1110111',2)
clock[1] = int('0b0010010',2)
clock[2] = int('0b1011101',2)
clock[3] = int('0b1011011',2)
clock[4] = int('0b0111010',2)
clock[5] = int('0b1101011',2)
clock[6] = int('0b1101111',2)
clock[7] = int('0b1110010',2)
clock[8] = int('0b1111111',2)
clock[9] = int('0b1111011',2)

counts = [bitcount(c) for c in clock]

trans = []
for i in xrange(10):
    trans.append([0]*10)
for i in xrange(10):
    for j in xrange(i, 10):
        noverlap = bitcount(clock[i] ^ clock[j])
        trans[i][j] = noverlap
        trans[j][i] = noverlap

def dsum(n):
    return sum(int(digit) for digit in str(n))

def numtrans(n):
    if n in d: return d[n]
    sn = str(n)
    if len(sn) == 1: return counts[n]
    total = 0
    ds = dsum(n)
    sds = str(ds)
    l1 = len(sn)
    l2 = len(sds)
    for i in xrange(l1):
        c1 = int(sn[l1-i-1])
        if i < l2:
            c2 = int(sds[l2-i-1])
            total += trans[c1][c2]
        else: total += counts[c1]
    total += numtrans(ds)
    d[n] = total
    return total

def energy(n):
    total = 0
    for c in str(n):
        total += counts[int(c)]
    return total + numtrans(n)

def naive(n):
    if n in naivedict: return naivedict[n]
    sn = str(n)
    if len(sn) == 1: return 2*counts[n]
    total = 0
    for c in sn: total += 2*counts[int(c)]
    total += naive(dsum(n))
    naivedict[n] = total
    return total

prime = [True]*UL
prime[0]=prime[1]=False
for i in xrange(UL):
    if not prime[i]: continue
    for j in xrange(i<<1, UL, i): prime[j] = False

diff = 0
for i in xrange(LL, UL):
    if not prime[i]: continue
    diff += naive(i) - energy(i)
print diff
