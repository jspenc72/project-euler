#!/usr/bin/env python

# sum of squares is n*(n+1)*(2n+1)/6
# square of sums is (n*(n+1)/2)^2

n = 100
print abs((n*(n+1)//2)**2 - n*(n+1)*(2*n+1)//6)
