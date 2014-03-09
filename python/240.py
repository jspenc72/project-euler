#!/usr/bin/env python

mem={}
def fact(n):
    if n<=1: return 1
    if n in mem: return mem[n]
    ret = n*fact(n-1)
    mem[n]=ret
    return ret

def parts(n,k,m):
    if k==1: yield [n]
    else:
        for i in xrange((n+1)/k,min(n-k+2,m+1)):
            for p in parts(n-i,k-1,i):
                yield [i] + p

def adj(arr):
    prev = arr[0]
    pcount = 0
    for i in xrange(1,len(arr)):
        if arr[i] != prev:
            yield i-pcount
            pcount = i
        prev = arr[i]
    yield len(arr)-pcount

total = 0
rolls = 20
sides = 12
top = 10
summit = 70
for p in parts(summit,top,sides):
    m = min(p)
    den = 1
    for d in adj(p):
        md = d
        den *= fact(d)
    den /= fact(md)
    for i in xrange(rolls-top+1):
        total += fact(rolls)/fact(top-i)/den/fact(md+i)*(m-1)**(rolls-top-i)
print total
