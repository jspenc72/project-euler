#!/usr/bin/env python

N=2000

mem={}
def s(k):
    if k in mem: return mem[k]
    if k<=55: ret = (100003-200003*k+300007*k**3)%10**6 - 500000
    else: ret = (s(k-24)+s(k-55))%10**6 - 500000
    mem[k] = ret
    return ret

def maxs(arr):
    msf = meh = 0
    for t in arr:
        meh = max(t, meh+t)
        msf = max(msf, meh)
    return msf

tab = [[0]*N for i in xrange(N)]
for i in xrange(N):
    for j in xrange(N):
        tab[i][j] = s(i*N+j+1)

ans = 0
for i in xrange(N):
    ans = max(ans, maxs(tab[i]))
    gen = (tab[j][i] for j in xrange(N))
    ans = max(ans, maxs(gen))
    gen = (tab[j][j+i] for j in xrange(N-i))
    ans = max(ans, maxs(gen))
    gen = (tab[j][j-i] for j in xrange(i,N))
    ans = max(ans, maxs(gen))
    gen = (tab[j][N-j-1+i] for j in xrange(i,N))
    ans = max(ans, maxs(gen))
    gen = (tab[j][N-j-1-i] for j in xrange(N-i))
    ans = max(ans, maxs(gen))
print ans
