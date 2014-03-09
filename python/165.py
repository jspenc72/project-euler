#!/usr/bin/env python
from gmpy import mpq

mod=50515093
N=5000
p=[]
pts=set([])

def sgn(x):
    return (x>0)-(x<0)

def intersects(i, j):
    xi1,yi1,xi2,yi2=p[i][0],p[i][1],p[i][2],p[i][3]
    xj1,yj1,xj2,yj2=p[j][0],p[j][1],p[j][2],p[j][3]
    if sgn(sgn((xj1-xi1)*(yi2-yi1)-(xi2-xi1)*(yj1-yi1)) * sgn((xj2-xi1)*(yi2-yi1)-(xi2-xi1)*(yj2-yi1))) >= 0: return False
    if sgn(sgn((xi1-xj1)*(yj2-yj1)-(xj2-xj1)*(yi1-yj1)) * sgn((xi2-xj1)*(yj2-yj1)-(xj2-xj1)*(yi2-yj1))) >= 0: return False
    xp=None
    if xi2==xi1: xp=xi1
    else: mi=mpq(yi2-yi1)/mpq(xi2-xi1)
    if xj2==xj1: xp=xj1
    else: mj=mpq(yj2-yj1)/mpq(xj2-xj1)
    if xp==None: xp=mpq(yj1-yi1+mi*xi1-mj*xj1)/mpq(mi-mj)
    if xi1!=xi2: yp=mi*(xp-xi1)+yi1
    else: yp=mj*(xp-xj1)+yj1
    return (xp,yp)

total=0;
s=290797;
for i in xrange(N):
    t=[]
    for j in xrange(4):
        s=s*s%mod
        t.append(s%500)
    p.append(t)

for i in xrange(N):
    #print i
    for j in xrange(i):
        t=intersects(i,j)
        if t: pts.add(t)
print len(pts)
