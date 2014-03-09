#!/usr/bin/env python

# just iterate through fibonacci numbers
# won't take long since they grow exponentially

total = 0
n, m = 1, 2
while m < 4*10**6:
    total += (not m&1)*m
    n, m = m, n+m
print total
