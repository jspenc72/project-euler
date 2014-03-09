#!/usr/bin/env python

# for i from 2 to 20
# compute prime factorization of i.
# use largest multiplicity in any
# prime factor seen thus far

def factorize(n):
    d = {}
    p=2
    while n>=p:
        while not n%p:
            n//=p
            d[p] = d.get(p,0)+1
        p+=1
    return d

facs = {}
for i in xrange(2,21):
    f = factorize(i)
    for j in f:
        facs[j] = max(facs.get(j,0),f[j])
print reduce(lambda x,y: x*y, (i**facs[i] for i in facs))
