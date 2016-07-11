#!/usr/bin/env python

def F(a,b,c,n):
    x = (b-n+a)//a
    return n + 4*a*x - 3*c*x - c

def S_naive(a,b,c):
    return sum(F(a,b,c,n) for n in xrange(b+1))

def S(a,b,c):
    L = b//a
    ans = b*(b+1)//2 - (b+1)*c + a*(4*a - 3*c)*L*(L+1)//2
    weight = b - L*a + 1
    ans += weight * (4*a - 3*c) * (L+1)
    return ans

print S_naive(50, 2000, 40)
print S(50, 2000, 40)
print S(21**7, 7**21, 12**7) % 10**9
