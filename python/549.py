#!/usr/bin/env python

N=10**8
smallprime = [-1]*(N+1)
for i in xrange(2,N+1):
    if i*i>N:
        if smallprime[i] == -1:
            smallprime[i] = i
        continue
    if smallprime[i] != -1:
        continue
    smallprime[i] = i
    for j in xrange(i*i,N+1,i):
        if smallprime[j] == -1:
            smallprime[j] = i

def factorize(n):
    while n>1:
        p = smallprime[n]
        mult = 0
        while smallprime[n] == p:
            mult += 1
            n //= p
        yield (p, mult)

def fact_mult(n,p):
    t = p
    ret = 0
    while n>=t:
        ret += n//t
        t *= p
    return ret

def get_smallest_for_p_and_mult(p, mult):
    lower = 0
    upper = mult
    while upper - lower > 1:
        mid = (lower + upper) // 2
        tmult = fact_mult(mid*p, p)
        if tmult >= mult:
            upper = mid
        else:
            lower = mid
    ret = (lower+1)*p
    return ret

ans = 0
for i in xrange(2,N+1):
    smallest = 0
    for p, mult in factorize(i):
        smallest = max(smallest, get_smallest_for_p_and_mult(p,mult))
    ans += smallest
print ans
