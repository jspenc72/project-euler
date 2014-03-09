#!/usr/bin/env python
import sys

# dp where we need to keep track of:
# - remaining units of each type (25x75)
#
# From here, it's just a matter of counting
# how many ways to color 1 of each type with N colors
#
# See function N

A = [[1,2,5], [0,4,6], [0,3,5], [2,4], [1,3,6], [0,2,6], [1,4,5]]
B = [[1,2,5], [0,4], [0,3,5], [2,4], [1,3,6], [0,2,6], [4,5]]
mod = 10**8

def check(G, H, i, color):
    for j in xrange(i):
        if j in G[i] and H[j]==color: return True
    return False

def N(G, H, i, c):
    if i==len(G): return 1
    total = 0
    color = -1
    for j in xrange(i):
        # if we've already seen H[j], either
        # it was bad or we will have already
        # tried it. because we only assign new colors
        # monotonically increasing, this is valid.
        if H[j]<=color: continue
        color = max(color, H[j])
        if check(G, H, i, H[j]): continue
        H[i] = H[j]
        total += N(G, H, i+1, c)
    color += 1
    H[i] = color
    total += (c-color)*N(G, H, i+1, c)
    return total

def main():
    if len(sys.argv) < 4:
        a, b, c = 25, 75, 1984
    else:
        a, b, c = map(int, sys.argv[1:])
    H=[0]*len(A)
    startA = N(A, H, 0, c)
    startB = N(B, H, 0, c)
    H[1] = 1
    appA = N(A, H, 2, c)
    appB = N(B, H, 2, c)

    F={}
    def f(a,b):
        if a<0 or b<0: return 0
        if a==0 and b==0: return 1
        if (a,b) in F: return F[a,b]
        F[a,b] = (appA*f(a-1,b)%mod + appB*f(a,b-1)%mod)%mod
        return F[a,b]
    
    print (startA*f(a-1, b)%mod + startB*f(a, b-1)%mod)%mod

if __name__=='__main__':
    main()
