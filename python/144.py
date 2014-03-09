#!/usr/bin/env python

def xnext(m1,b):
    rad = ((2*m1*b)**2-4*(m1**2+4)*(b**2-100))**.5
    xp1 = ((-2*m1*b)+rad)/(2*(m1**2+4))
    xp2 = ((-2*m1*b)-rad)/(2*(m1**2+4))
    return (xp1,xp2)

eps = 0.000001
count = 0

m0 = (-9.6-10.1)/1.4
b0 = 10.1
x0 = xnext(m0,b0)[0]
y0 = m0*x0+b0

while abs(x0) > 0.01 or abs(y0-10.0) > 1.0:
    count += 1 #Add the 'bounce' for the previous iteration
    mp = -4.0*x0/y0
    m1 = (m0*mp*mp+2.0*mp-m0)/(1.0+2.0*m0*mp-mp*mp)
    b1 = y0 - m1*x0
    t = xnext(m1,b1)
    x1 = t[0]
    if abs(x1-x0) < eps: x1 = t[1]
    x0 = x1
    m0 = m1
    b0 = b1
    y0 = m0*x0+b0

print count
