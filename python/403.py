#!/usr/bin/env python

N=10**12
R=int(N**.5)
mod = 10**8

def s(r,h):
    return (h**3 + 3*h*r**2 + r**3 + (3*h**2 + 5)*r + 5*h + 6)//6%mod

def f(r,ph,qh):
    return (-4*(ph - qh - 1)*r**3 - ph**4 + 2*ph**3 - 11*ph**2 + \
            qh**4 - 6*(ph**2 - qh**2 - ph - qh)*r**2 + 2*qh**3 - 2*(2*ph**3 - 3*ph**2 - \
            2*qh**3 - 3*qh**2 + 11*ph - 11*qh - 10)*r + 11*qh**2 - 14*ph + 34*qh + 24)//24 % mod

total = (f(0,1,N) + f(-1,0,N-1))%mod
for r in xrange(1,R):
    total = (total + f(r,r+1,N//r))%mod
for r in xrange(-R,-1):
    total = (total + f(r, -r+1, N//abs(r)))%mod
    total = (total + s(r,-r)%mod)%mod
total = 2*total%mod
for r in xrange(0,R+1):
    total = (total + s(r,r)%mod)%mod
print total
