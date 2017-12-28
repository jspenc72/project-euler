#!/usr/bin/env python
from scipy.special import betainc, beta
from utils import c

N=3

def prob_lose_from_box_less(n, p, j):
    return 1. / p**p * sum(c(p-1, k) * float(p-j)**(p-1-k) for k in xrange(j,p))

def prob_lose_from_box_greater(n, p, j):
    asdf = 1. / (j-1)**p * (1. - n*c(n-1,p-1)*beta(p, n-p+1)*betainc(p, n-p+1, float(j-1)/j))
    #asdf = n*c(n-1, p-1) * 1. / (j-1)**p * (betainc(p,n-p+1,1.) - betainc(p, n-p+1, float(j-1)/j))
    #print 'n, p, j quantity:', n, p, j, asdf
    return c(n-1, p-1) * sum(1. / j**(p+k) * c(n-p, k) / c(n-1, p+k-1) for k in xrange(j-p, n-p+1)) + asdf

def prob_lose_from_box(n, p, j):
    if j<p:
        return p*prob_lose_from_box_less(n, p, j)
    elif j>p:
        return p*prob_lose_from_box_greater(n, p, j)
    elif j==p:
        return 0.
    else:
        raise Exception("impossible")

def prob_win(n, p):
    return 1. - sum(prob_lose_from_box(n, p, j) for j in xrange(1, n+1))

#def complicated(n, k, x):
#    return (1-k*x)**k*(1-(k+1)*x)**(n-k+1)*hyp2f1(1, n+1, k+1, (k+1)*(1-k*x))/k
#
#def residual(n, k, l=None, u=None):
#    if l is None:
#        l = 1./(k+1)
#    if u is None:
#        u = 1./k
#    return ((1-k*l)**n - (1-k*u)**n) / (k*n)
#
#def section(n, k):
#    u = 1./(k+1)
#    return residual(n, k, 0, u) - c(n-1,n-k)*(-complicated(n,k,0))

print prob_win(N, 1), 4./9
print prob_win(N, 2), 2./9
print prob_win(N, 3), 1./3
