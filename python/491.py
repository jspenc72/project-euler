#!/usr/bin/env python
from math import factorial as fact

# Notes: multiply by 10 <==> subtract from 11
# So each digit will be either "added" or "subtracted" from running sum
# We want to count number of ways to assign +/- s.t. 11 divides sum
# Problem: still need to worry about ordering of digits
# So we keep track of some additional info in DP:
# number of digit pairs that both have '+', call this p
# this means final amount is weighted by (10!/(2!)^p)^2
# observation: if p pairs cooccur with '+' label,
# then p pairs also cooccur with '-' label (this is why above weight is squared)

# analysis almost done. Another problem is that we cannot have
# any leading 0's. solution is to do above dp, but fix each
# i as leading digit, and keep track of whether i gets a + or -.
# w_i for i labeled +:
# (10!/(2!)^p) * (9!/(2!)^p)
# w_i for i labeled - (we are guaranteed to have at least 1 dup in this case):
# (10!/(2!)^p) * (9!/(2!)^(p-1))

# needs space prop. to [pos]*[modulus]*[dups]*[# + labels][i is + or minus] = 19*11*6*9*2
# need time prop. to 9*that

# EDIT: crap, it turns out that it's not necessary to jump through all those hoops;
# since placements of digits is equivalent modulo even/odd position, it suffices to
# calculate the number of unrestricted ways (leading 0's included) to place digits,
# then multiply this by 9/10 to compensate for leading digit. I don't really want
# to rewrite my disgusting dp code though so leaving it as it is.

F={}
def f(i,p,m,d,l,il):
    if p==-1:
        if m==0 and l==0 and d==0:
            return 1
        else:
            return 0
    if l-2*(p+1)>0 or l<0 or d<0:
        return 0
    h = (i,p,m,d,l,il)
    if h in F:
        return F[h]
    if p==i:
        # assign the label digit i has been preordained to get
        ans = f(i,p-1,(m+(p if il else -p))%11,d,l-il,il)
        F[h] = ans
        return ans
    # both get +, one gets + other gets -, both get -
    ans = f(i,p-1,(m+2*p)%11,d-1,l-2,il) + f(i,p-1,m,d,l-1,il) + f(i,p-1,(m-2*p)%11,d,l,il)
    F[h] = ans
    return ans

total=0L
for i in xrange(1,10):
    for ipos in (True,False):
        for dups in xrange(6):
            if dups==0 and not ipos:
                continue
            if dups==5 and ipos:
                continue
            ways = f(i,9,11-i,dups,10,ipos)
            if ipos:
                weight = fact(10)/2**dups * fact(9)/2**dups
            else:
                weight = fact(10)/2**dups * fact(9)/2**(dups-1)
            total += weight*ways
    print 9*total
    break # digits are equivalent modulo even/odd position, so I did more work than necessary
