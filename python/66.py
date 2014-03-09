#!/usr/bin/env python

from itertools import count

N=1000

di = {}

def convergent(arr,n):
    if n in di: return di[n]
    if n==0: return (arr[0][2], 1)
    if n==1: return (arr[1][2]*arr[0][2]+1, arr[1][2])
    t1 = convergent(arr,n-1)
    t2 = convergent(arr,n-2)
    bn = arr[1+(n-1)%(len(arr)-1)][2]
    con = (bn*t1[0]+t2[0], bn*t1[1]+t2[1])
    di[n] = con
    return con
    

def nextfrac(S,a0,m,d,a):
    m1 = d*a-m
    d1 = (S-m1*m1)/d
    a1 = (a0+m1)/d1
    return (m1,d1,a1)

def issquare(n):
    r = n**.5
    return abs(r-int(round(r))) < .001

maxx=0
maxd=0

for i in xrange(2, N+1):
    di = {}
    if issquare(i): continue
    s = set([])
    arr = []
    a0,m,d,a = int(i**.5),0,1,int(i**.5)
    t = (m,d,a)
    arr.append(t)
    for j in count(0):
        t = nextfrac(i,a0,*t)
        if t in s: break
        s.add(t)
        arr.append(t)
    for j in count(0):
        con = convergent(arr,j)
        x = con[0]
        if x**2-i*con[1]**2==1:
            if x>maxx:
                maxx=x
                maxd=i
            break
print maxd
