#!/usr/bin/env python
from itertools import count

n = 4
mod = 10**9

def ss(n):
    return n*(n+1)*(2*n+1)//6

ans, d = 0, 1
while d<=n:
    q = n//d
    last_d = n//q
    ans = (ans+q*(ss(last_d)-ss(d-1)))%mod
    d = last_d+1
print ans

#ans, p = 0, n+1
#for i in count(1):
#    if i>p: break
#    w = max(n//i,i)
#    ans = (ans + n//i*i**2 + (i-1)*(p*(p+1)*(2*p+1)//6 - w*(w+1)*(2*w+1)//6))%mod
#    p = w
#print ans
