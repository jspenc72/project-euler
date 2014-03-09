#!/usr/bin/env python

# Takes about 2 minutes on my machine
# Still fine imo, would be much faster in C

mem={}
def powermod(a,b,n):
    if (a,b) in mem: return mem[a,b]
    if b==0: return 1
    if b&1:
        ret = powermod(a,(b-1)/2,n)**2%n*a%n
        mem[a,b]=ret
        return ret
    ret = powermod(a,b/2,n)**2%n
    mem[a,b]=ret
    return ret

N=100000
prime = [True]*N
prime[0]=prime[1]=False
for i in xrange(2,N):
    if i*i>=N: break
    if not prime[i]: continue
    for j in xrange(i<<1,N,i):
        prime[j] = False

tot=10
for p in xrange(7,N):
    if not prime[p]: continue
    seen = [False]*p
    x = 10%p
    while True:
        if seen[x]:
            tot += p
            break
        seen[x]=True
        y=1
        for k in xrange(10):
            y = y*x%p
        x=y
        if x==1:
            #print p
            break
print tot
