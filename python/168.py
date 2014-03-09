#!/usr/bin/env python

def unique(n,d,orig_right):
    right=orig_right
    carry = 0
    s = 0
    place = 1
    for i in xrange(n-1):
        if place<10**5: s += right*place
        if place<10**5: place *= 10
        next_digit = d*right+carry
        right = next_digit%10
        carry = next_digit//10
    left = right*d + carry
    return (right!=0 and left == orig_right)*((right*place if place<10**5 else 0) + s)

ans=0
for n in xrange(2,101):
    for d in xrange(1,10):
        for right in xrange(1,10):
            ans = (ans+unique(n,d,right))%10**5
print ans
